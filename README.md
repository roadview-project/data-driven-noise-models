# Library of validated statistical noise models
## Summary
### Objectives
The objective of this deliverable is to share the data-driven weather noise model library published as part of ROADVIEW D3.3 (https://roadview-project.eu/). It covers fog, rain, and snow conditions and Light Detection And Ranging (LiDAR), camera and RAdio Detection And Ranging (RADAR) sensors.
### Methodology and implementation
The data-driven noise models are based on the following principle: natural data with and without degraded weather is used to determine the noise added by the weather using a machine learning method. The decision was made to treat the case of camera, LiDAR and RADAR independently, as the input data is very different. For cameras, a Cycle-GAN method was used to process the images in their entirety. For LiDAR and RADAR, a point-by-point classification method based on the notion of vanishing distance was created. The training data used are public images collected by CE in the case of the cameras, and data acquired by CE on the Puy-de-Dôme (PDD) site (France) during the 2022-2023 and 2023-2024 winters (created as part of T3.2).
### Outcomes
Concerning cameras, the Cycle-GAN method was implemented for the different weather conditions, with the possibility of giving intensity classes. Some of the results show the relevance of data-driven models, which in the case of snow make it possible to simulate all the associated effects. This is a counter point to just simulating the snow falling from the sky. For example, this method allows the removal of leaves from trees, snow on the ground including vehicle tracks. Concerning LiDARs, the point-by-point method based on the vanishing distance makes it possible to reproduce the three weather conditions, by specifying the exact desired intensity of the weather. Finally, this report shows that RADAR is insensitive to weather for the tested adverse weather intensities.
### Next steps
The next step is to validate the models developed during T3.4. This validation will be carried out on data from the REHEARSE database (created as part of T3.2). This work will be promoted through the publication of scientific articles on the various models developed. Finally, some data and camera models prepared in Task 3.3 will be reused in Task 5.2 on camera-based measurement of weather conditions.

## Repo organisation
This repository is organised as follows. The camera and lidar noise models are provided and described in their respective folders. The radar does not have a noise model, as it has been shown to be insensitive to weather.

## Reference
If you use the noise models proposed here, please cite the following report: 
P. Duthon, H. Ouattara, S. Liandrat, Y. Poledna, ROADVIEW D3.3 - Library of validated statistical noise models. 2024.

## Acknowledgement
Funded by the European Union (grant no. 101069576). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Climate, Infrastructure and Environment Executive Agency (CINEA). Neither the European Union nor the granting authority can be held responsible for them. UK and Swiss participants in this project are supported by Innovate UK (contract no. 10045139) and the Swiss State Secretariat for Education, Research and Innovation (contract no. 22.00123) respectively.
