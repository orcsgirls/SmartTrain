import time
from intelino.trainlib import TrainScanner, Train
from intelino.trainlib.enums import SnapColorValue as C
from intelino.trainlib.messages import (
    TrainMsgEventFrontColorChanged,
    TrainMsgEventSnapCommandDetected,
)

def main():

    class train_pass():
        def __init__(self, id, snap):
            self.id = id
            self.snap = snap
            self.used_by = None
            self.trains_waiting = []
            
    class train_passes():
        def __init__(self, count=1):
            names = ['RED pass', 'BLUE pass', 'GREEN pass']
            colors = [C.RED, C.BLUE, C.GREEN]
            self.passes=[]
            for i in range(count):
                self.passes.append(train_pass(names[i],colors[i]))

        def pass_free(self, color):
            return (self.passes[self._color_pass(color)].used_by is None)
        
        def pass_occupied(self, color, train):
            self.passes[self._color_pass(color)].used_by = train
        
        def pass_waiting(self, color, train):
            self.passes[self._color_pass(color)].trains_waiting.append(train)
            
        def pass_left(self, train):
            index = self._train_pass(train)
            if index!=-1:
                self.passes[index].used_by = None
            return index
            
        def pass_id(self, color):
            return self.passes[self._color_pass(color)].id
        
        def pass_release_waiting_trains(self, index):
            waiting_train = None
            color = self.passes[index].snap
            waiting_trains = self.passes[index].trains_waiting
            if len(waiting_trains)>0:
                waiting_train = self.passes[index].trains_waiting.pop(0)
            return waiting_train, color
        
        def pass_info(self):
            for p in self.passes:
                print(f">> {p.snap}: Occupied by {p.used_by} - Waiting {p.trains_waiting}")
            
        def _color_pass (self, color):
            for i, p in enumerate(self.passes):
                if p.snap == color:
                    return i
            return -1
        
        def _train_pass (self, train):
            for i, p in enumerate(self.passes):
                if p.used_by == train:
                    return i
            return -1
                
    def enter_pass(train: Train, color):        
        if passes.pass_free(color):
            train.drive_at_speed(30)
            passes.pass_occupied(color, train)
            print(train.alias, "entered the ", passes.pass_id(color))
        else:
            train.stop_driving()
            passes.pass_waiting(color, train)
            print(train.alias, "waits for the ", passes.pass_id(color)," to be free")
        passes.pass_info()

    def leave_pass(train: Train):
        pass_index = passes.pass_left(train)
        print(train.alias, "left pass", pass_index)
        if pass_index>=0:
            print("Releasing waiting trains ..")
            release_waiting_trains(pass_index)
        passes.pass_info()

    def handle_snap_commands(train: Train, msg: TrainMsgEventSnapCommandDetected):
        if msg.colors == (C.WHITE, C.MAGENTA, C.RED, C.BLACK):
            enter_pass(train, C.RED)
        if msg.colors == (C.WHITE, C.MAGENTA, C.BLUE, C.BLACK):
            enter_pass(train, C.BLUE)

    def handle_colors(train: Train, msg: TrainMsgEventFrontColorChanged):
        if msg.color == C.YELLOW:
            leave_pass(train)
                   
    def release_waiting_trains(pass_index):
        train_waiting, color = passes.pass_release_waiting_trains(pass_index)
        print(f"Releasing {train_waiting} from {color} pass")
        if train_waiting:
            enter_pass(train_waiting, color)
        passes.pass_info()
        
    #=======================================================================================
       
    trains = TrainScanner().get_trains(max_count=3)
    passes = train_passes(count=2)
    
    # identify our trains
    trains[0].alias = "RED Train"
    trains[0].set_headlight_color(front=(255, 0, 0), back=(255, 0, 0))
    if len(trains)>1:
        trains[1].alias = "BLUE Train"
        trains[1].set_headlight_color(front=(0, 0, 255), back=(0, 0, 255))
    if len(trains)>2:
        trains[2].alias = "GREEN Train"
        trains[2].set_headlight_color(front=(0, 255, 0), back=(0, 255, 0))

    # setup event listeners
    for train in trains:
        train.clear_custom_snap_commands()
        train.add_snap_command_detection_listener(handle_snap_commands)
        train.add_front_color_change_listener(handle_colors)

    # start driving
    for train in trains:
        train.drive_at_speed(30)

    # running until exception or keyboard interrupt
    try:
        input("Press enter to stop ..")
    except KeyboardInterrupt:
        print("Aborted by user")
    finally:
        print("Disconnecting ..")
        for train in trains:
            train.stop_driving()
            train.set_headlight_color()
            train.remove_snap_command_detection_listener(handle_snap_commands)
            train.remove_front_color_change_listener(handle_colors)
            train.disconnect()


if __name__ == "__main__":
    main()
