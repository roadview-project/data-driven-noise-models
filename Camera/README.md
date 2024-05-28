The camera noise model is based on the well-known CycleGAN algorithm. The version available by following this link was used: 

https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

During our development work, we have chosen the pytorch version, with the pip installation. 


Once the standard installation has been carried out, you can test our trained models by issuing the following command:

*python test.py --dataroot ./datasets --name models/weather_wanted --model cycle_gan*

To do this, you can specify the location of your data in place of *./datasets*
 and choose the weather you wish (*weather_wanted*) to simulate from the following list: *fog_light, fog_medium, fog_heavy, rain_floor_wet, rain_light, rain_heavy, snow_light, snow_heavy.*




