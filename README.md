# cs169_prog_assign_1

This git repository is made for Dartmouth Robotics CS 69/169 Robotics perception course' programming assignment.
Works are coded by Mingi Jeong, 1st year Ph.D. Students in Robotics/Computer Science at Dartmouth.
This program was conducted on ROS kinetic and Linux Ubuntu 18.04

I am pleased to take this class taught by Prof.Alberto Quattrini Li.

# How to download and install necessary packages
1) git clone to your catkin_ws folder
2) Make sure you have "rosbot_webui" package in your catkin_ws git clone https://github.com/husarion/rosbot_webui.git
3) Make sure you have "husarion_ros" package in your catkin_ws git clone https://github.com/husarion/husarion_ros.git
4) catkin_make
5) After you connect(ssh) to the Rosbot 2.0, source ~/catkin_ws/devel/setup.bash
6) run command to make your python scripts executable e.g (chmod +x ~/catkin_ws/src/cs169_prog_assign_1/scripts/task1.py)

# Execute
For each task given by this assignment, I made it modular.
In other words, you have only to execute each launch file as per task.
e.g. "roslaunch cs169_prog_assign_1 task1.launch"
1) For task1, you need to input the value of the distance to be traveled on the command line
2) For task2, you don't have to input the value. The robot will proceed 1 meter and it will record Rosbag file
3) For task3, it is executing teleop node. You can control the robot on keyboard and see visualization by making marker visible on your Rviz.
