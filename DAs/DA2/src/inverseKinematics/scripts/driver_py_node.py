#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist
import random #random library
import numpy as np # import the numpy library


'''
These is my driver function where I publish the cmd_vel for left and right
'''

def driver():
	rospy.init_node('driver', anonymous=True) #initialise the node
	pub = rospy.Publisher('goal_pose', Pose, queue_size=10) #create a publisher for cmd_vel using pose2d
	goal_pose = Pose2D() # create variable for the pose2d function
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown(): #checks if the program has not been terminated
		goal_pose.x =  random.uniform(1, 1000) # input random float value into the x for the pose2d
		goal_pose.y  =  random.uniform(1,1000) # input random float value into the y for the pose2d	
		goal_pose.theta  = (np.pi)/2.0 # calculate the theta with the numpy library
		rospy.loginfo("x = %f y = %f theta = %f " % (goal_pose.x,goal_pose.y,goal_pose.theta)) # print the left and right velocity in the terminal
		pub.publish(goal_pose) # it will publish the x and y values from the twist
		rate.sleep() # put it to sleep amount of time			

def getDistance():
	gpose = Pose2D()
	current_pose = Pose2D()
	return np.sqrt(np.power(current_pose.x- gpose.x,2) + np.power(current_pose.y- gpose.y,2))

def getAngle():
	gpose = Pose2D()
	current_pose = Pose2D()
	return ((np.arctan2(gpose.y - current_pose.y, gpose.x - current_pose.x)) - current_pose.theta)

def moveGoal(distance_tolerance):
	#current_pose = Pose2D()
	velocity_publisher = Publisher('cmd_vel', Twist, queue_size = 10)
	vel_msg = Twist()
	e_theta = 0.00
	integral_theta = 0.00
	diff_theta = 0.00
	e_dist = 0.00
	integral_dist = 0.00
	diff_dist = 0.00
	#rate = rospy.Rate(10)

	e_theta = getAngle()
	e_dist = getDistance()
	k1 = 7.5
	k2 = 0.00001
	k3 = 0.01
	#linear velocity
	vel_msg.linear.x = (k1 * e_dist / 20.0) + (k2*integral_dist) + (k3*diff_dist)
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	#angular velocity
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = (k1*e_theta) + (k2*integral_theta) + (k3*diff_theta)
	e_theta = getAngle()
	e_dist = getDistance()

	integral_theta = integral_theta + e_theta
	integral_dist = integral_dist + e_dist

	diff_dist = e_dist - diff_dist
	diff_theta = e_theta - diff_theta

	velocity_publisher.publish(vel_msg)
	rospy.spin()
	rate.sleep()

	while(e_dist > distance_tolerance):
		print("end move goal")
		vel_msg.linear.x = 0
		vel_msg.linear.z = 0
		velocity_publisher.publish(vel_msg)






if __name__ == '__main__':
	
	moveGoal(1) # calls the driver function


	

