import math
import numpy as np

class lidarDataDrivenNoiseModel():
    def __init__(self, weather, coeffLidar=1):
        """
        :param weather:  'Rain', 'Fog', or 'Snow'
        :param coeffLidar : offset coefficient according to the Lidar model. 1.0 for Velodyne VLP16, 0.9 for Ouster OS1
        """
        self.weather = weather
        self.coeffLidar = coeffLidar
        if self.weather == "Rain":
            self.slopeNormal = 0.22530445
            self.slopeLowReflectivity = 0.15688675
        if self.weather == "Fog":
            self.slopeNormal = 0.34634364
            self.slopeLowReflectivity = 0.30286536
        if self.weather == "Snow":
            self.slopeNormal = 0.32685039
            self.slopeLowReflectivity = 0.32685039

    def cartesian_to_spherical(self, x, y, z):
        """Converts a cartesian coordinate (x, y, z) into a spherical one (radius, theta, phi)."""
        radius = math.sqrt(x*x + y*y + z*z)
        theta = math.atan2(math.sqrt(x * x + y * y), z)
        phi = math.atan2(y, x)
        return [radius, theta, phi]

    def spherical_to_cartesian(self, radius, theta, phi):
        """Converts a spherical coordinate (radius, theta, phi) into a cartesian one (x, y, z)."""
        x = radius * math.cos(phi) * math.sin(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(theta)
        return [x, y, z]

    def weatherIntensityToEquivalentMor(self, weatherIntensity):
        """
        This function takes the weather intensity as input and proposes the equivalent MOR as output.
        :param weatherIntensity: rainfall rate in mm/h for rain, MOR in m for fog, equivalent MOR in m for snow.
        :return: weatherEquivalentMor : the equivalent MOR (m) MOR = Meteorological Optical Range
        """
        weatherEquivalentMor = 0
        if self.weather == "Rain":
            weatherEquivalentMor = -0.8308 * weatherIntensity + 159.16
        if self.weather == "Fog":
            weatherEquivalentMor = weatherIntensity
        if self.weather == "Snow":
            weatherEquivalentMor = weatherIntensity
        return weatherEquivalentMor

    def applyLidarModelToDataframePoint(self, df, xCol, yCol, zCol, pointIntensityCol, weatherIntensity):
        """
        This function is used to apply the noise model to a dataframe containing lidar points in Cartesian coordinates.
        :param df: a Dataframe contaning a lidar point cloud, with (x, y and z) columns and a lidar reflectivity column. Each row is a point.
        :param xCol: the name of the x column into the dataframe.
        :param yCol: the name of the y column into the dataframe.
        :param zCol: the name of the z column into the dataframe.
        :param pointIntensityCol: the name of the lidar reflectivity/intensity column into the dataframe.
        :param weatherIntensity: the weather intensity : rainfall rate in mm/h for rain, MOR in m for fog, equivalent MOR in m for snow.
        :return: df the dataframe with the new point cloud, as if it was into the weather of weather intensity.
        """
        df['radius'] = np.sqrt(df[xCol]*df[xCol] + df[yCol]*df[yCol] + df[zCol]*df[zCol])
        df['theta'] = np.arctan2(np.sqrt(df[xCol] * df[xCol] + df[yCol] * df[yCol]), df[zCol])
        df['phi'] = np.arctan2(df[yCol], df[xCol])

        df = self.applyLidarModelToDataframeRadius(df, 'radius', pointIntensityCol, weatherIntensity)

        df[xCol] = df['radius'] * np.cos(df['phi']) * np.sin(df['theta'])
        df[yCol] = df['radius'] * np.sin(df['phi']) * np.sin(df['theta'])
        df[zCol] = df['radius'] * np.cos(df['theta'])

        df.drop(columns=['radius', 'theta', 'phi'], inplace=True)
        return df

    def applyLidarModelToDataframeRadius(self, df, radiusCol, pointIntensityCol, weatherIntensity):
        """
        This function is used to apply the noise model to a dataframe containing lidar points in polar coordinates.
        :param df: a Dataframe contaning a lidar point cloud, with (x, y and z) columns and a lidar reflectivity column. Each row is a point.
        :param radiusCol: the name of the radius column into the dataframe.
        :param pointIntensityCol: the name of the lidar reflectivity/intensity column into the dataframe.
        :param weatherIntensity: the weather intensity : rainfall rate in mm/h for rain, MOR in m for fog, equivalent MOR in m for snow.
        :return: df the dataframe with the new point cloud, as if it was into the weather of weather intensity.
        """
        weatherEquivalentMor = self.weatherIntensityToEquivalentMor(weatherIntensity)
        disappearingDistanceNormal = weatherEquivalentMor * self.slopeNormal * self.coeffLidar
        disappearingDistanceLowReflectivity  = weatherEquivalentMor * self.slopeLowReflectivity * self.coeffLidar
        df = df[
            (df[radiusCol]<disappearingDistanceNormal) &
            ( (df[radiusCol]<disappearingDistanceLowReflectivity) & df[pointIntensityCol]<10 )
        ]
        return df
