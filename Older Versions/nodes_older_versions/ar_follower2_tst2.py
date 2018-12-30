#!/usr/bin/env python

"""
    ar_follower.py - Version 1.0 2013-08-25
    
    Follow an AR tag published on the /ar_pose_marker topic.  The /ar_pose_marker topic
    is published by the ar_track_alvar package
    
    Created for the Pi Robot Project: http://www.pirobot.org
    Copyright (c) 2013 Patrick Goebel.  All rights reserved.
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details at:
    
    http://www.gnu.org/licenses/gpl.html
"""
import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Twist
from math import copysign
import time
import tf

class ARFollower():
    #global counter
    def __init__(self):
        rospy.init_node("ar_follower")
                        
        # Set the shutdown function (stop the robot)
        rospy.on_shutdown(self.shutdown)
        
        # How often should we update the robot's motion?
        self.rate = rospy.get_param("~rate", 15)
        r = rospy.Rate(self.rate) 
        
        # The maximum rotation speed in radians per second
        self.max_angular_speed = rospy.get_param("~max_angular_speed", 0.9)
        
        # The minimum rotation speed in radians per second
        self.min_angular_speed = rospy.get_param("~min_angular_speed", 0.1)
        
        # The maximum distance a target can be from the robot for us to track
        self.max_x = rospy.get_param("~max_x", 20.0)
        
        # The goal distance (in meters) to keep between the robot and the marker
        self.goal_x = rospy.get_param("~goal_x", 0.0001)
        
        # How far away from the goal distance (in meters) before the robot reacts
        self.x_threshold = rospy.get_param("~x_threshold", 0.01)
        
        # How far away from being centered (y displacement) on the AR marker
        # before the robot reacts (units are meters)
        self.y_threshold = rospy.get_param("~y_threshold", 0.05) #0.05 0.2
        
        # How much do we weight the goal distance (x) when making a movement
        self.x_scale = rospy.get_param("~x_scale", 0.5)

        # How much do we weight y-displacement when making a movement        
        self.y_scale = rospy.get_param("~y_scale", 0.5)
        
        # The max linear speed in meters per second
        self.max_linear_speed = rospy.get_param("~max_linear_speed", 0.3)
        
        # The minimum linear speed in meters per second
        self.min_linear_speed = rospy.get_param("~min_linear_speed", 0.1)

        #intialize frame counter
        self.TargetFlag = rospy.get_param("~TargetFlag", False)
        # Publisher to control the robot's movement
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=5)
        
        # Intialize the movement command
        self.move_cmd = Twist()
        

        # Set flag to indicate when the AR marker is visible
        self.target_visible = False
        self.TargetFlag	 = False;
       
        # Wait for the ar_pose_marker topic to become available
        rospy.loginfo("Waiting for ar_pose_marker topic...")
        rospy.wait_for_message('ar_pose_marker', AlvarMarkers)
        
        # Subscribe to the ar_pose_marker topic to get the image width and height
        rospy.Subscriber('ar_pose_marker', AlvarMarkers, self.set_cmd_vel)
        rospy.Subscriber('ar_pose_marker', AlvarMarkers, self.initial_spin)        

        rospy.loginfo("Marker messages detected. Starting follower...")
        
        # Begin the cmd_vel publishing loop
        while not rospy.is_shutdown():
            # Send the Twist command to the robot
            self.cmd_vel_pub.publish(self.move_cmd)
            
            # Sleep for 1/self.rate seconds
            r.sleep()

    def initial_spin(self, msg):
    # TAG OF THE PREVIOUS TEAM
        MappingFlag = True
        

        # Pick off the first marker (in case there is more than one)
        #if (( self.target_visible == False) and (MappingFlag==True)):
        #self.move_cmd.angular.z = 1.1
        #if(self.target_visible == True)
         # self.move_cmd.angular.z =0
        #break

    def set_cmd_vel(self, msg):
        global TargetFlag
        #counter = 0
        try:
            marker = msg.markers[0]
	    
           
            # rospy.loginfo("the Roll is: %d",roll)
            # rospy.loginfo("the Pitch is: %d",pitch)
            # rospy.loginfo("the Roll is: %d",yaw)
            if not self.target_visible:
                rospy.loginfo("FOLLOWER is Tracking Target!")
                # quaternion = (
                #                 marker.pose.orientation.x,
                #                 marker.pose.orientation.y,
                #                 marker.pose.orientation.z,
                #                 marker.pose.orientation.w)
                # euler = tf.transformations.euler_from_quaternion(quaternion)
                # roll = euler[0]
                # pitch = euler[1]
                # yaw = euler[2]

                #counter+=1
                #rospy.loginfo("the frame count is : %f", counter)
                #print ("Number of succesfully tracked frames so far: %i",counter)
                self.move_cmd.angular.z = 0.0
                self.target_visible = True
                #rospy.sleep(0.09) nice response
        except:
            # If target is lost, stop the robot by slowing it incrementally
            self.move_cmd.linear.x /= 1.9
            if(self.TargetFlag is not True):
               self.move_cmd.angular.z = 0.9 #1.08
            else:
	       self.move_cmd.linear.y = 0.0
               self.move_cmd.linear.z = 0.0
	       self.move_cmd.linear.x = 0.0
            
            if self.target_visible:
                rospy.loginfo("FOLLOWER LOST Target!")
                self.target_visible = False
                #counter+=1
            return
                    
        
        #rospy.loginfo("the frame count is : %f", counter)

        quaternion = (
                        marker.pose.pose.orientation.x,
                        marker.pose.pose.orientation.y,
                        marker.pose.pose.orientation.z,
                        marker.pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        roll = euler[0]
        pitch = euler[1]
        yaw = euler[2]
        
        rospy.loginfo("the Roll is: %f",roll)
        rospy.loginfo("the Pitch is: %f",pitch)
        rospy.loginfo("the yaw is: %f",yaw)


    
        # Get the displacement of the marker relative to the base
        target_offset_y = marker.pose.pose.position.y
        
        # Get the distance of the marker from the base
        target_offset_x = marker.pose.pose.position.x
        
        # Get the distance of the marker from the base
        target_offset_z = marker.pose.pose.position.z

        rospy.loginfo("the target_offset_x is: %f",target_offset_x)
        rospy.loginfo("the target_offset_y is: %f",target_offset_y)
        rospy.loginfo("the target_offset_z is: %f",target_offset_z)

        # Rotate the robot only if the displacement of the target exceeds the threshold
        if ((abs(target_offset_y) > (self.y_threshold)) and (self.TargetFlag is not True)):
            # Set the rotation speed proportional to the displacement of the target
            speed = (target_offset_y * self.y_scale)
            self.move_cmd.angular.z = copysign(max(self.min_angular_speed,
                                        min(self.max_angular_speed, abs(speed))), speed)
        else:
            self.move_cmd.angular.z = 0.0
            #self.counter = 121;
 
        # Now get the linear speed
        if (target_offset_x - self.goal_x) > self.x_threshold:
            speed =  abs((self.goal_x - (target_offset_x + 0.2))) * self.x_scale
            if speed > 0:
                speed *= 1.5
            self.move_cmd.linear.x = copysign(min(self.max_linear_speed, max(self.min_linear_speed, abs(speed))), speed)
        else:
            self.move_cmd.linear.x /= 1.9
            cspeed =  self.move_cmd.linear.x
            rospy.loginfo("the current speed is : %f",cspeed)
            if((target_offset_x <= 0.8 ) and (target_offset_x >= 0.30) and (cspeed <= 0.1)):#0.8 0.05 0.1, respectively
                self.move_cmd.linear.x = 0.3  # 0.4 worked
                rospy.loginfo("increasing Speed \n")
            else:
                self.move_cmd.linear.x /= 1.01
                self.move_cmd.linear.y = 0.0
                self.move_cmd.linear.z = 0.0
                self.TargetFlag = True;
		rospy.loginfo("the frame count is : %r", self.TargetFlag)
                rospy.loginfo("target achieved\n")

    def shutdown(self):
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)     

if __name__ == '__main__':
    
    try:

        ARFollower()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("AR follower node terminated.")
