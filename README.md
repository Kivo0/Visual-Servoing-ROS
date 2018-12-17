# Visual-Servoing-ROS
## Main Contributors: MIKHAILOV Ivan, BOTROS Karim
Contributor: Some guy named Hussain, not sure though

## Table of Content:

I. [Project Description](https://github.com/Kivo0/Visual-Servoing-ROS#i-Project-Description)

II. [Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#ii-Turtlebot-Navigation)

  * [Basic Commands for Launch](https://github.com/Kivo0/Visual-Servoing-ROS#Basic-Commands)




I. Project Description
   -------------------
we are addressing the problem of visual servoing of a mobile robot "turtlebot 2" our beloved turlte. the problem is the localization of an indoor mobile robot is never accurate. so in order to achieve an accuracy of few centimeters or even milimeter scale. we need to do visual servoing to reach the target with minimum distance. so in easy words. our robot goes from outside the room to the center of the room using [Turtlebot Navigation](https://github.com/Kivo0/Visual-Servoing-ROS#Turtlebot-Navigation)

II. Hardware contraints
   -------------------
The project is based on **ROS** (Robot Operating System) environment running the eighth ROS distribution release named **indigo** and a **TurtleBot2** as a robot. Turtlebot2 includes YUJIN Kobuki base, a 2200 mAh battery pack, a **KinectV1** sensor, and an Asus 1215N laptop with a dual core processor. The system is run through a stationary PC, connected to the TurtleBot, and running  **Ubuntu 14.04 LTS**.

III. Turtlebot Navigation
   ---------------------

the some other guy should write here !!!!!!!! not on microsoft Word!!!!!

Are you talking about that Goosesain guy? Not sure I saw him today!


#### Basic Commands
    ------------------
In this chapter you can find useful commands, which will help you to launch the project part by part i.e. seperately use navigation and fine positioning parts of the project. This commands directly run the launch files, which take care of everything else.

To run Visual servoing for Fine Positioning, please, follow these steps:
- First, 2 SSH connections to your tutlebot should be created. In our case, the command was: **ssh turtlebot@192.168.0.100**
- Secondly, we launch the base adn the corresponding features: **roslaunch turtlebot_bringup minimal.launch**
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

