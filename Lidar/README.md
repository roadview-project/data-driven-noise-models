The lidar noise model is based on the calculation of the vanishing distance.  


To use the template, simply retrieve the file *lidarDataDrivenNoiseModel.py*  and use it as shown in the example below. 

*import pandas as pd
import lidarDataDrivenNoiseModel as lidarDataDrivenNoiseModel
weatherClass = "Fog" #"Rain" or "Snow"
lddnm = lidarDataDrivenNoiseModel.lidarDataDrivenNoiseModel()
weatherIntensity = 150
dfClearWeather = pd.read_csv('someLidarPointCloud.csv')
dfWithWeatherSimul = lddnm.applyLidarModelToDataframeRadius(dfClearWeather, 'dist', 'intensity', weatherIntensity)*