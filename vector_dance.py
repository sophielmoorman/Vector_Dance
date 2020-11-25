# python3 vector_dance.py 005060e3

# imports to control vector
import anki_vector
from anki_vector.events import Events
from anki_vector import annotate
from anki_vector.util import degrees, distance_mm, speed_mmps

# import to pass in arguments in command line
import sys

def cube(robot):
    # try to connect to cube 
    robot.world.connect_cube()
    
    # get cube (if connection worked)
    if robot.world.connected_light_cube:
        # cube should light up
        robot.behavior.pickup_object(robot.world.connected_light_cube, use_pre_dock_pose=True, num_retries=3)

def sing(robot):
    robot.behavior.say_text("Ah. Ah. Ah. Ah. Staying alive!")
    robot.behavior.say_text("Ah. Ah. Ah. Ah. Staying alive!")

def dance(robot):
    # some arm action
    robot.behavior.set_lift_height(0, max_speed=3, duration=3)
    robot.behavior.set_lift_height(1.0, max_speed=3, duration=3)
    # turn in place
    robot.behavior.turn_in_place(degrees(180))
    robot.behavior.turn_in_place(degrees(-180))
    # some arm action
    robot.behavior.set_lift_height(0, max_speed=3, duration=3)
    robot.behavior.set_lift_height(1.0, max_speed=3, duration=3)
    # turn in place
    robot.behavior.turn_in_place(degrees(180))
    robot.behavior.turn_in_place(degrees(-180))

def nod(robot):
    robot.behavior.set_head_angle(degrees(0))
    robot.behavior.set_head_angle(degrees(20))
    robot.behavior.set_head_angle(degrees(0))
    robot.behavior.set_head_angle(degrees(20))

def main():

    # pass in arguments from command line (python3 vector_dance.py 005060e3)
    arg = sys.argv[1]    

    # open robot like you open a file
    with anki_vector.Robot(serial=arg,show_viewer=True) as robot:

        # sing
        robot.behavior.say_text("I like to sing!")
        sing()
        
        # nod along to the beat
        robot.behavior.say_text("Sick beat!")
        nod()
        
        # dance 
        robot.behavior.say_text("I will dance now!")
        dance()

        # light up cube
        robot.behavior.say_text("Where is my cube?")
        cube()
        
if __name__ == "__main__":
    main()