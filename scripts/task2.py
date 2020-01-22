#!/usr/bin/env python

# make sure to execute the following lines at the terminal before running this py file
# source ~/catkin_ws/devel/setup.bash
# chmod +x catkin_ws/src/cs169_prog_assign_1/scripts/task2.py

# IMPORTANT: Basically the code is the same as task1.py
# The reason why I made a separate file is that the because of erros message with transformation compressed image,
# Users cannot see the input pop-up asking (task 2 needs to be inputted as 1)
# Therefore, I manually inputted constant 1.0 value for the distance to be travelled

import rospy
import math
from geometry_msgs.msg import Twist, PoseStamped

# define Rosbot class containing publisher and subscriber in task1 node
class Rosbot:
    def __init__(self):
        self.publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.subscriber = rospy.Subscriber("/pose",PoseStamped, self.pose_callback)
        self.rate = rospy.Rate(5)
        self.initial_pose = None
        self.pose = PoseStamped()

    def distance_traveller(self, dist_input):
        vel_msg = Twist()
        vel_msg.angular.z = 0

        while not rospy.is_shutdown():
            # if the distance travelled is less than the user input, robot keeps going as per velocity 2m/s
            # I made the velocity linear x command as 2m/s constant no matter what we input values
            if abs(self.pose.pose.position.x - self.initial_pose) < dist_input:
                vel_msg.linear.x = dist_input / abs(dist_input * 5) # making rosbot's velocty as 2 m/s
                print "Current distance", abs(self.pose.pose.position.x - self.initial_pose)
                self.publisher.publish(vel_msg)
                self.rate.sleep()

            # if the distacne travelled reaches the user's input, it sends stop signal as linear.x= 0
            # and I killed the node by signal shutdown source: http://wiki.ros.org/rospy/Overview/Initialization%20and%20Shutdown
            else:
                print("Distance reached!")
                vel_msg.linear.x = 0
                self.publisher.publish(vel_msg)
                self.rate.sleep()
                rospy.signal_shutdown("Stopped!")

    def pose_callback(self, msg):
        self.pose = msg

    def update_pose_msg(self):
        update_pose_msg = rospy.wait_for_message("/pose", PoseStamped)
        self.initial_pose = update_pose_msg.pose.position.x


def main():
    # distance to be travelled as 1.0 meter according to the task 2
    dist_input = 1.0
    Rosbot2 = Rosbot()

   # initial position subscriber by rospy.wait_for_message
    Rosbot2.update_pose_msg()
    Rosbot2.distance_traveller(dist_input)

if __name__ =="__main__":
    rospy.init_node("task2")
    main()
