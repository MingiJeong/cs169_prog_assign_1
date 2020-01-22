#!/usr/bin/env python

# make sure to execute the following lines at the terminal before running this py file
# source ~/catkin_ws/devel/setup.bash
# chmod +x catkin_ws/src/cs169_prog_assign_1/scripts/task3.py


import rospy
import math
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist, PoseStamped, Vector3, Quaternion
from visualization_msgs.msg import Marker

def plotter_callback(msg):
    current_pose = msg
    vis_marker = Marker()
    vis_marker.header.seq =current_pose.header.seq # header seq same as subscribed msg
    vis_marker.header.frame_id = current_pose.header.frame_id # frame id same as subscribed msg
    vis_marker.header.stamp = rospy.Time.now()
    vis_marker.type = 0 # marker type as arrow
    vis_marker.action = Marker.ADD

    # not only for marker's x,y position, I also considered orientation of the pose.
    # Therefore, on Rviz, I can see the heading direction of the robot.
    vis_marker.pose.position.x = current_pose.pose.position.x
    vis_marker.pose.position.y = current_pose.pose.position.y
    vis_marker.pose.position.z = 0
    vis_marker.pose.orientation.x = current_pose.pose.orientation.x
    vis_marker.pose.orientation.y = current_pose.pose.orientation.y
    vis_marker.pose.orientation.z = current_pose.pose.orientation.z
    vis_marker.pose.orientation.w = current_pose.pose.orientation.w
    vis_marker.scale.x = 1
    vis_marker.scale.y = 0.1
    vis_marker.scale.z = 0.1
    vis_marker.color.a =1.0
    vis_marker.color.r = 0.0
    vis_marker.color.g = 1.0
    vis_marker.color.b = 0.0
    # publisher helper fuction which publishes Visual marker
    publisher_helper(vis_marker)

    print ("subscribing", vis_marker.pose.position.x, "///", vis_marker.pose.position.y)

def publisher_helper(marker):
    # Through the "/custom_marker" topic, I am sending Marker message which contains the above data
    marker_publisher = rospy.Publisher("/custom_marker", Marker, queue_size=10)
    marker_publisher.publish(marker)
    rate = rospy.Rate(10)
    rate.sleep()
    print ("publishing", marker.pose.position.x, "///", marker.pose.position.y)

def main():
    # in node task3 I made a pose subscriber having a plotter callback function
    pose_subscriber = rospy.Subscriber("/pose", PoseStamped, plotter_callback)
    rospy.spin()

if __name__ =="__main__":
    rospy.init_node("task3")
    main()
