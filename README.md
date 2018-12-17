# Visual-Servoing-ROS
## Main Contributors: MIKHAILOV Ivan, BOTROS Karim
Contributor: Some guy named Hussain, not sure though

## Table of Content:

[Project Description](https://github.com/Kivo0/Visual-Servoing-ROS#i-Project-Description)


I. Project Description
    ___________________

here is the description

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

