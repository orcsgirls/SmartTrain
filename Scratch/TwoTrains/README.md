These examples require two Intelino trains and show train teamwork 🙂

### `CollisionAvoidanceOnePass.sb3`

Pass refers to a sectio of the track both trains need to share. At the entrance of the pass a white magenta 
snaps work like a traffic light to allow the train to continue if the pass is empty and to stop otherwise.
Yellow snaps indicate that a train has left the pass. Setup the track as shown below. Note we use snap actions
to move one train on the outer loop and the otehr on the inner loop so the code does not have to worry about
that.

<img src="https://github.com/orcsgirls/SmartTrain/blob/master/Scratch/TwoTrains/CollisionAvoidanceOnePass.png?raw=true" width="600">

Trains start as shown on the image facing opposite directions. Click the green flag in Scratch and the trains will
start and (hopefully) not collide. Space or the Stop sprite will stop both trains. Clicking on each train 
sprite will stop or start just that train. The diagram on the screen indicates which train is where (in the pass or its home track).

### `CollisionAvoidanceTwoPass.sb3`

Same concept as above just with two double loops and the switch sections on each side are the Since there are two, different
color sequences mark the entry to each pass. Here is the track layout

<img src="https://github.com/orcsgirls/SmartTrain/blob/master/Scratch/TwoTrains/CollisionAvoidanceTwoPass.png?raw=true" width="600">

### `WagonExchange.sb3`

Here two trains exchange a wagon. This exampele is adaptec from the 
[Intelino Python examples](https://github.com/intelino-code/intelino-trainlib-py-examples/tree/master/examples). The code is similar to the
single train version except on completing the drop, the code signals the otehr train to pick it up. Here is the track
layout to run the example.

<img src="https://github.com/orcsgirls/SmartTrain/blob/master/Scratch/TwoTrains/WagonExchange.png?raw=true" width="600">
