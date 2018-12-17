# Visual-Servoing-ROS
## Main Contributors: MIKHAILOV Ivan, BOTROS Karim
Contributor: Some guy named Hussain, not sure though

## Table of Content:

[Project Description](https://github.com/Kivo0/Visual-Servoing-ROS#i-Project-Description)
[Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#ii-Turtlebot-Navigation)
[Basic Commands for Launch](




I. Project Description
   -------------------
we are addressing the problem of visual servoing of a mobile robot "turtlebot 2" our beloved turlte. the problem is the localization of an indoor mobile robot is never accurate. so in order to achieve an accuracy of few centimeters or even milimeter scale. we need to do visual servoing to reach the target with minimum distance. so in easy words. our robot goes from outside the room to the center of the room using [Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#Turtlebot-Navigation)


II. Turtlebot Navigation
   ---------------------

the some other guy should write here !!!!!!!! not on microsoft Word!!!!!



   Basic Commands
   --------------

### Create 4 SSH: ###

ssh turtlebot@192.168.0.100

### MINIMAL (on robot): ###

roslaunch turtlebot_bringup minimal.launch

### Kinect launch(robot or PC):###

roslaunch freenect_launch freenect.launch publish_tf:=false

### Launch file for marker parameters to be detected (size, error etc.) - (robot or PC):###

roslaunch rbx2_ar_tags ar_large_markers_kinect.launch

### Modified Follower Code:###

roslaunch rbx2_ar_tags ar_follower.launch

###COMPILE THE CODE (not literally):###

scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags/nodes/ar_follower2.py turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags/nodes

### Update launch file ###

scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags/launch/ar_large_markers_kinect.launch turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags/launch

### Update all nodes (the whole nodes folder) ###

scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags/nodes turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags

### Update the whole launch file folder ###

scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags/launch turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags

### UPDATE MAPS ###

scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags/map turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags


### Update the whole project folder ###
scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/

### Launch amcl with pre-created map ###
1. roslaunch turtlebot_navigation amcl_demo.launch map_file:=/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags/map/test_map22.yaml

### See stuff in rviz and select destinations ###
2. roslaunch turtlebot_rviz_launchers view_navigation.launch --screen 


### Navigation launch ###
1. roslaunch rbx2_ar_tags navi_1.launch
2. roslaunch rbx2_ar_tags navi_2.launch

