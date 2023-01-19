These examples use a single Intelino train. 

### `RainbowRemote.sb`

This example allows to start and stop the train by clicking on the train sprite. 
The top light on the train cycles through the color wheel as the train moves along the track.

### `ColorSensorChange.sb3`

Train control by clicking the train sprite as before. This time the costume (color) of the train 
will change matching the color of the last snap the train drove over.

### `StationAnnouncement.sb3`

Train control by clicking the train sprite as before. The sprite of the track will move according to the speed of the train. 
When the train encounters a white magenta green color sequence it will stop and make a station annoucement using the
text-to-speech extension before departing again. Make sure the computer sound is up.

### `WagonDrop.sb3`

This uses a double loop and the train will trip the cart and pick it up again. The train layout should be like this

<img src="https://github.com/orcsgirls/SmartTrain/blob/master/Scratch/OneTrain/WagonDrop.png?raw=true" width="600">

The white magenta snaps mark the drop off location for the wagon. White magenta blue triggers reversing when picking up
the wagon and white magenta red marks the home location for the train.

For questions or to show off your train layouts, contact thomas@orcsgirls.org. 
