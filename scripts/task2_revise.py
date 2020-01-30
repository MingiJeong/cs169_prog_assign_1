#!/usr/bin/env python

# make sure to execute the following lines at the terminal before running this py file
# source ~/catkin_ws/devel/setup.bash
# chmod +x catkin_ws/src/cs169_prog_assign_1/scripts/task1.py


import rospy
import math
from geometry_msgs.msg import Twist, PoseStamped
from timeit import default_timer as timer

# define Rosbot class containing publisher and subscriber in task1 node
class Rosbot:
    def __init__(self):
        self.publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.rate = rospy.Rate(5)
        self.initial_time = None

    def distance_traveller(self):
        vel_msg = Twist()
        vel_msg.angular.z = 0

        while not rospy.is_shutdown():
            # if the distance travelled is less than the user input, robot keeps going as per velocity 2m/s
            # I made the velocity linear x command as 2m/s constant no matter what we input values
            if self.initial_time == None:
                self.initial_time = timer()
            else:
                vel_msg.linear.x = 0.2 # making rosbot's velocty as 0.2 m/s
                print("going (current time)", timer()-self.initial_time)
                self.publisher.publish(vel_msg)
                self.rate.sleep()
                if timer() - self.initial_time >= 5:
                    print("Distance reached!")
                    vel_msg.linear.x = 0
                    self.publisher.publish(vel_msg)
                    self.rate.sleep()
                    rospy.signal_shutdown("Stopped!")


def main():
    # user input of distance to be travelled on the screen and convert it into float type
    # dist_input = float(input("Distance for Rosbot to travel? (unit: meters):"))
    Rosbot2 = Rosbot()
    # initial position subscriber by rospy.wait_for_message
    #Rosbot2.update_pose_msg()
    Rosbot2.distance_traveller()

if __name__ =="__main__":
    rospy.init_node("task1")
    main()
