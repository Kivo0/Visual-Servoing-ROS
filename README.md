# Visual-Servoing-ROS
## Main Contributors: MIKHAILOV Ivan, BOTROS Karim, SAEED Hassan


## Table of Content:

I. [Project Description](https://github.com/Kivo0/Visual-Servoing-ROS#i-Project-Description)

II. [Hardware components](https://github.com/Kivo0/Visual-Servoing-ROS#ii-Hardware-contraints)

III. [Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#iii-Turtlebot-Navigation)
     
   * [Ros Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#Ros-Navigation)
     
   * [Move_base node](https://github.com/Kivo0/Visual-Servoing-ROS#Move_base-node)
   
   * [Global Planner](https://github.com/Kivo0/Visual-Servoing-ROS#Global-Planner)
   
   * [Costmap](https://github.com/Kivo0/Visual-Servoing-ROS#Costmap)
   
   * [Global Costmap](https://github.com/Kivo0/Visual-Servoing-ROS#Global-Costmap)
   
   * [Local Planner](https://github.com/Kivo0/Visual-Servoing-ROS#Local-Planner)
   
   * [Local costmap](https://github.com/Kivo0/Visual-Servoing-ROS#Local-costmap)

IV.[Visual Servoing](https://github.com/Kivo0/Visual-Servoing-ROS#iv-Visual-Servoing)
     
   * [Searching for Target!](https://github.com/Kivo0/Visual-Servoing-ROS#Searching-for-Target!)
    
   * [Attacking the Target](https://github.com/Kivo0/Visual-Servoing-ROS#Attacking-the-Target)
   
   * [Parking "Centering the robot to the center of the marker" ](https://github.com/Kivo0/Visual-Servoing-ROS#parking-centering-the-robot-to-the-center-of-the-marker)
   
   * [Markers!](https://github.com/Kivo0/Visual-Servoing-ROS#markers)
   

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
 ![alt text](https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/images/overview_tf.png)
 
•	Odometry source: This gives robot position with respect to its initial position eg via wheel encoders. The odom publishes to the Navigation stack, with message type nav_msgs/ Odometry.

•	Sensor source: In navigation sensors are used for localizing the robot in the map (via kinect) and also to detect the obstacles in the path of the robot.

•	 Sensor transforms/tf: Data captured by the various sensors must be referenced to a common frame of reference (usually the base_link) for comparison with data coming from different sensors. The robot should publish the relationship between the main robot coordinate frame and the different sensors' frames using ROS transforms.

•	Base_controller: It is to convert the output of the Navigation stack, which is a Twist (geometry_msgs/Twist) message, into corresponding motor velocities for the robot.

#### Move_base node
Function of this node from navigation stack is to move a robot from its present position to a designated (goal) position. This node is responsible for linking the global planner and the local planner for path planning, connecting to rotate recovery package if the robot is stuck in some obstacle, and connecting global costmap and local costmap for getting the map of obstacles of the environment. 
![alt text](https://github.com/Kivo0/Visual-Servoing-ROS/blob/master/images/move_base_diagram.png)
#### Global Planner
When a new goal is received by the move_base node, this goal is immediately sent to the global planner. Then, the global planner is in charge of calculating a safe path in order to arrive at that goal pose. This path is calculated before the robot start moving, so it will not take into account the readings that the robot sensors are acquiring while moving. For calculating the path the global planner uses the costmap.

#### Costmap
A costmap is a map that represents places that are safe for the robot to be in a grid of cells. Usually, the values in the costmap are binary, representing either free space or places where the robot would be in collision. Each cell in a costmap has an integer value in the range (0-255). There exist two types of costmaps: global costmap and local costmap.
The globlal costmap is created from the static map. (The map generated using the gmapping package) .The local costmap is created from the robot’s sensor readings. So the global planner uses the global costmap in order to calculate the path to follow.

#### Global Costmap:
The global costmap is created from a user-generated static map. In this case the costmap is initialized to match the width, height, and obstacle information provided by the static map. This configuration is normally used in conjunction with a localization system, such as amcl.

#### Local Planner
After global planner has calculated the path to follow, this path is sent to local planner. The local planner, then, will execute each segment of the global plan. So given a plan to follow and a map, the local planner will deliver velocity commands to move the robot. Contradictory to the global planner, the local planner monitors the odometer and the laser data, and chooses a collision-free local plan for the robot.

#### Local costmap
Local planner uses the local costmap in order to calculate the local plans. Unlike the global costmap, the local costmap is created directly via robot’s sensor readings.

IV. Visual Servoing
   ----------------
   #### Markers!
   For the purpose of Fine Positioning we used Alvar for ROS as our main library (http://wiki.ros.org/ar_track_alvar). The reasons why Alvar was chosen are mentioned in the ROS survey written by our team and included in this repository. Nevertheless, the main idea is to use AR tags as an artificial marking on the target, which needs to be approached by a robot.
   In the project we attempted at usage of several 
   
   
   #### Searching for Target!
   first part of the alogrithm after the robot arrives near the ***"marker"*** the search phase begins which is the first phase of our algorithm, its completed directly after the **first mapping and localization phase ends** = "letting the turtlebot localize itself and go near to the loading marker to load the goods". the search is done by rotating the robot continously more than 360&deg; untill it detects our marker then it attacks the marker and kills it! please see our failed trials >>>link here<<<<<<< 
   
   #### Attacking the Target
   
   there is many ways to do to arrive at the target **"All roads leads to Maker" by Botros, Karim .. myself!**,  initially the alvar library can't center the robot or align it perpendicular to the target if the robot was already near at the begining of the servoing algorithm to the marker so we thought of using **yaw** a component of Quaternions number system which indicates the perpendicularity of the marker plane with the kinect plane. there are other components in Quaternions but we are only interested in yaw for now, after many attempts and experiments recordings we achieved our task of making the robot perpindcular to the surface of the marker
   
   #### Parking "Centering the robot to the center of the marker"
   
   

 

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

