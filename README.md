# Visual-Servoing-ROS

## Team Members:

[![botros karim](https://s.gravatar.com/avatar/5149755ee69696f33d24c159cf243363?s=100)](https://github.com/Kivo0) | [![Ivan Mikhalov ](https://s.gravatar.com/avatar/6681bbc8ebfffa4946bfd93fa1efa4c3?s=100)](https://github.com/Ivan-Mikhailov) | [![hassan Saeed ](https://avatars0.githubusercontent.com/u/22390315?s=1)](https://github.com/hassansrs) 
 ---|---|---
 [Karim Botros](https://github.com/Kivo0) | [Ivan MIKHAILOV](https://github.com/Ivan-Mikhailov) | [Hassan](https://github.com/hassansrs)  


## Table of Content:

I. [Project Description](https://github.com/Kivo0/Visual-Servoing-ROS#i-Project-Description)

II. [Hardware components](https://github.com/Kivo0/Visual-Servoing-ROS#ii-Hardware-contraints)

III. [Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#iii-Turtlebot-Navigation)
     
   * [Ros Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#Ros-Navigation)
     
   * [Map Creation and Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#Map-Creation-and-Navigation)
   


IV.[Visual Servoing](https://github.com/Kivo0/Visual-Servoing-ROS#iv-Visual-Servoing)
   * [Markers!](https://github.com/Kivo0/Visual-Servoing-ROS#markers)
     
   * [Searching for Target!](https://github.com/Kivo0/Visual-Servoing-ROS#Searching-for-Target!)
    
   * [Attacking the Target](https://github.com/Kivo0/Visual-Servoing-ROS#Attacking-the-Target)
   
   * [Parking "Centering the robot to the center of the marker" ](https://github.com/Kivo0/Visual-Servoing-ROS#parking-centering-the-robot-to-the-center-of-the-marker)
   

V. [Speed Control!](https://github.com/Kivo0/Visual-Servoing-ROS#v-speed-control)


VI. [Basic Commands for Launch](https://github.com/Kivo0/Visual-Servoing-ROS#vi-Basic-Commands)


I. Project Description
   -------------------
we are addressing the problem of visual servoing of a mobile robot "turtlebot 2" our beloved turlte. the problem is the localization of an indoor mobile robot is never accurate. so in order to achieve an accuracy of few centimeters or even milimeter scale. we need to do visual servoing to reach the target with minimum distance. so in easy words. our robot goes from outside the room to the center of the room using [Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#Turtlebot-Navigation)

II. Hardware components
   -------------------
The project is based on **ROS** (Robot Operating System) environment running the eighth ROS distribution release named **indigo** and a **TurtleBot2** as a robot. Turtlebot2 includes YUJIN Kobuki base, a 2200 mAh battery pack, a **KinectV1** sensor, and an Asus 1215N laptop with a dual core processor. The system is run through a stationary PC, connected to the TurtleBot, and running  **Ubuntu 14.04 LTS**.

III. Turtlebot Navigation
   ---------------------
#### Ros Navigation
 Navigation Stack takes in current location of the robot, the goal pose, the Odometry data of Robot (wheel encoders etc) and data from a sensor as an input, and outputs the necessary velocity commands and forward them to the mobile base in order to move the robot to the designated goal:

<p align="center"><img src = "https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/images/overview_tf.png" width="800" ></p>

 #### Map Creation and Navigation
 
 A map is generated following the tutorial presetented on ROS WIKI page: http://wiki.ros.org/turtlebot_navigation/Tutorials/Build%20a%20map%20with%20SLAM
 
 Following map generation of the enviornment, initial(starting and goal position) are extracted. Please refer to the repository for detials on how to proceed with this: https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/Turtlebot_navigation.pdf
 
 After we have initial and goal position of turtlebot we can proceed with next steps, i.e are connection with turtlebot and than controlling it via publishing initial and goal position.
 
 To control our turtlebot which is the netbook(Asus) via the workstation(Dell).
 `$ ssh turtlebot@192.168.0.100`
 
 Then once connection with turtlebot is established, in the same terminal proceed with:
  `$ roslaunch turtlebot_bringup minimal.launch`
  
 In the new terminal we launch:
  `$ roslaunch turtlebot_navigation amcl_demo.launch map_file:=/home/turtlebot/ros/indigo/catkin_ws/src/rbx2_ar_tags/map/test_map22.yaml`
  
 In the new terminal, while making sure turtlebot is placed on its original initial position please publish on initial position topic:
  `$ rostopic pub -1 /initialpose geometry_msgs/PoseWithCovarianceStamped '{header: {stamp: now, frame_id: "map"}, pose: {position: {x: -4.96073627472, y: 1.06203043461 , z: 0.0}, orientation: {x: 0.0, y: 0.0, z: -0.371774223976, w: 0.928323179926}}}'`
 
 To proceed to the goal position copy in terminal following command:
  `$ rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 0.318982511759, y: -0.757121920586 , z: 0.0}, orientation: {x: 0.0, y: 0.0, z: -0.360750805748, w: 0.932662241196}}}'`  
  
While navigating problems incurred were related to collision with the edge of the room while turtlebot moves towards its goal, also sometimes due to speed turtlebot was not able to keep up on its original planned trajectory due to which it will stop moving. These problems can be solved by tuning parameters in navigation package. For details, on tuning turtlebot navigation package, please refer to this document: http://kaiyuzheng.me/documents/navguide.pdf

Results of navigation can be observed in a video on a YouTube channel, created specifically for this project:
[![](http://img.youtube.com/vi/Kis-Ex1mv2Y/0.jpg)](http://www.youtube.com/watch?v=Kis-Ex1mv2Y "")
  
IV. Visual Servoing
   ----------------
   #### Markers!
   
   For the purpose of Fine Positioning we used Alvar for ROS as our main library (http://wiki.ros.org/ar_track_alvar). The reasons why Alvar was chosen are mentioned in the ROS survey written by our team and included in this repository. Nevertheless, the main idea is to use AR tags as an artificial marking on the target, which needs to be approached by a robot.
   
   In the project we used several set ups, each of which provides certain advantages and disadvantages. Each set up is characterized by the size and the amount of tags:
- Bigger tags are generally better detected from a higher distance, but the precision drops on smaller distance up to inability to detect the tag when being too close, which is exactly the often encountered case for fine positioning. 
- Smaller tags are better detected from up close, on bigger distances the tag is lost very often, resulting in some issues from unsteady motion to no detection at all.

Example of the AR tag and also the tag we used for the Fine Positioning (#5) can be observed on the figure below:
<p align="center"><img src="https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/images/MarkerData_5.png" width="170"></p>

Considering the aforementioned properties, we tried several solitary (one-tag) set ups, including:
- one big tag of *15x15 cm*
- one average tag of *10x10 cm*
- one small tag of *7x7 cm*
- one tiny tag of *5x5 cm*

During the usage of one-tag set ups, we devised a new approach, which will involve the usage of a smaller tag, forming a pair of to tags, to counter the various issues, when the tobot approaches the target withing the distance of several centimeters. Generally, at that point the bigger tag doesn't fit in the field of view of Kinect, therefore we needed a smaller tag, but at the same time the approach should have still handled good distances. For this reason, Our Team was decided to use **both tags at the same time - bigger and smaller.**

The sizes can depend on the distance, but the general idea is that the small tag handles the closest possible positioning of the robot, while the bigger one everything else. Several multiple-tag set ups used by our team are listed below:
- two tags: *15x15 cm* + *10x10 cm*
- two tags: *15x15 cm* + *7x7 cm*
- **two tags: *15x15 cm* + *5x5 cm***
- two tags: *10x10 cm* + *7x7 cm*
- two tags: *10x10 cm* + *5x5 cm*
- two tags: *7x7 cm* + *5x5 cm*

At the moment, we are using *15x15 cm* + *5x5 cm* set. One might wonder, how the multiple tag detection is handled. For this purpose **ar_large_markers_kinect.launch** file can be accessed and the parameters there, corresponding to the parameters of the tags, can be observed. We found out, that true multiple tag handling doesn't need to be implemented i.e. positioning of each tag in respect to each other are not necessary for our purpose. Therefore, only the biggest tag size is put in the aforementioned .launch file. In addition, both tags are exactly the same, not considering the size. So when the robot approaches the target and starts to lose the bigger tag from time to time, the smaller one compensates for these losses until the biggest one is lost completely or appears to be detected very rarely, and the small one is detected constantly due to it's smaller size.

This solution drastically improves **precision and detection uptime** (uptime is the time in which the kinect detects the target in this case it changed from alternating to steady continious signal), making it nearly flawless. It is advised to use two tags at all times, when up-close fine positioning is required. If the task requires the robot to be very close to the marker in range of 20 cm* to 5 cm* then only the smaller tag is needed.

The final set up used in the approach can be seen below and is available for printing in the original size:
<p align="center"><img src="https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/images/MarkerData_5_15_and_5.png" width="250"></p>
   
   #### Searching for Target!
   first part of the alogrithm after the robot arrives near the ***"marker"*** the search phase begins which is the first phase of our algorithm, its completed directly after the **first mapping and localization phase ends** = "letting the turtlebot localize itself and go near to the loading marker to load the goods". the search is done by rotating the robot continously more than 360&deg; untill it detects our marker then it attacks the marker and kills it! please see our failed trials >>>link here<<<<<<< 
   
   #### Attacking the Target
   
   there is many ways to do to arrive at the target **"All roads leads to Maker" by Botros, Karim .. myself!**,  initially the alvar library can't center the robot or align it perpendicular to the target if the robot was already near at the begining of the servoing algorithm to the marker so we thought of using **yaw** a component of Quaternions number system which indicates the perpendicularity of the marker plane with the kinect plane. there are other components in Quaternions but we are only interested in yaw for now, after many attempts and experiments recordings we achieved our task of making the robot perpindcular to the surface of the marker
   
   #### Parking "Centering the robot to the center of the marker"
   

Results of visual servoing can be observed in a video on a YouTube channel, created specifically for this project:
[![](http://img.youtube.com/vi/l2s1D08dkuQ/0.jpg)](http://www.youtube.com/watch?v=l2s1D08dkuQ "") 

V. Speed Control!
------------------

it is hard task to achieve the same gap distance between the robot and the marker! that is because the robot increases its speed linearly to achieve the target therefore if the initial distance is close to the target distance the initial speed will be low and the robot will not be close to the target at the end. and also if the robot is far away the initial speed will be high and the robot might hit the marker. therefore we had to apply control to this linear model. **note: "this model can be modeled with the non linearities such as the friction of the kabuki base wheels with the ground and weight changes on the robot and many other factors but we neglected these factors to make the system linear"**. so we get the current speed of the robot and apply the control equation and feed the new speed to the motors. Feedback PID speed Control.
     


VI. Basic Commands
------------------
In this chapter you can find useful commands, which will help you to launch the project part by part i.e. seperately use navigation and fine positioning parts of the project. This commands directly run the launch files, which take care of everything else.

To run Visual servoing for Fine Positioning, please, follow these steps:
- First, two SSH connections to your tutlebot should be created. In our case, the command was: **ssh turtlebot@192.168.0.100**
- Secondly, we launch the base and the corresponding features: **roslaunch turtlebot_bringup minimal.launch**
- Thirdly, the kinect is launched using: **roslaunch freenect_launch freenect.launch publish_tf:=false**
- Next, parameters of the markers are initialized using: **roslaunch rbx2_ar_tags ar_large_markers_kinect.launch**
- Finally, the preparations are finished, and the robot starts to perform his routine **roslaunch rbx2_ar_tags ar_follower.launch**
It is important to mention, that **ar_large_markers_kinect.launch** and **ar_follower.launch** are run on the PC, while the **minimal.launch** and **freenect.launch** are run on turtlebot.

To run Mapping & Localisation for Navigation, please, follow these steps:
- First, run **roslaunch rbx2_ar_tags navi_1.launch**, which, in turn, brings up the minimal and loads the map of the area, which should be replaced, since you will probably use the robot in a different unknown to him environment.
- Second, run **roslaunch rbx2_ar_tags navi_2.launch**, which will set the parameters for the start and the finish of the pre-chosen path for the turtlebot, which you should adjust to fit to your map. Then it will launch rviz to observe your robot's movement and response from the sensors.

Please, notice, that the first launch file **navi_1.launch** should be run on the turtlebot, while **navi_2.launch** contains the command, which launches rviz, which can drastically decrease the performance of the turtlebot, so it is advised to run it on the PC.

In case you want to introduce some changes, there are some useful commands, which will allow you to have a more or less "compilation" abilities in regards to your code, which will greatly enhance the speed with which you can work. Basically, it gives you an ability to copy with replacement the files you have on your system to the turtlebot. So, when some changes are made, whis commands can be used as a "compilation method" to transfer files fast to the robot and be able to try them straight away.

For this purpose it is easy enough to update the whole project folder as followed:
**scp -r /home/mscv/ros/indigo/catkin_ws/src/rbx2_ar_tags turtlebot@192.168.0.100:/home/turtlebot/ros/indigo/catkin_ws/src/**
Please, note, that the paths used above should be changed to your own, depending on your system paths.


## LICENSE

[![MIT LICENSE](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/LICENSE)

