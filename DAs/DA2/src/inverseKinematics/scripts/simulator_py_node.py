#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
import numpy as np # import the numpy library
import random # import the random library


'''
These is my publisher function where I publish the pose2d
'''

def publisher():
	pub2 = rospy.Publisher('pose',Pose, queue_size = 10) #create a publisher for pose using pose2d
	rospy.init_node('pose_publisher', anonymous=True) #initialise the node
	rate = rospy.Rate(2) #2hz
	while not rospy.is_shutdown():  #checks if the program has not been terminated
		p = Pose2D() # create variable for the pose2d function
		p.x =  random.uniform(1, 1000) # input random float value into the x for the pose2d
		p.y  =  random.uniform(1,1000) # input random float value into the y for the pose2d
		p.theta  = (np.pi)/2.0 # calculate the theta with the numpy library
		pub2.publish(p) # it will publish the x,y and theta values from the pose2d
		rate.sleep() # put it to sleep amount of time	


def diffdrive(msg):
	v_l = msg.linear.y # gets the left velocity from the driver
	v_r = msg.linear.x # gets the right velocity from the driver
	p = Pose2D() # create variable for the pose2d function

	t = 3

	#straight Line
	if(v_l == v_r):
		theta_n = p.theta 
		x_n = p.x + v_l * t * np.cos(p.theta )
		y_n = p.y + v_l * t * np.sin(p.theta )
		rospy.loginfo("x_n: %f y_n: %f theta_n: %f" % (x_n,y_n,theta_n))
	#circular motion
	else:
		#calculate the radius
		R = 1/2.0 * ((v_l + v_r) / (v_r - v_l))
		#computing center of curvature
		ICC_x = p.x - R * np.sin(p.theta )
		ICC_y = p.y + R * np.cos(p.theta )
		#compute the angular velocity
		omega = (v_r - v_l) / 1
		#computing angle change
		dtheta = omega * t
		#forward kinematics for differential drive
		x_n = np.cos(dtheta)*(p.x-ICC_x) - np.sin(dtheta)*(p.y-ICC_y) + ICC_x
		y_n = np.sin(dtheta)*(p.x-ICC_x) - np.cos(dtheta)*(p.y-ICC_y) + ICC_y
		theta_n = p.theta  + dtheta
		rospy.loginfo("x_n: %f y_n: %f theta_n: %f" % (x_n,y_n,theta_n))

def simulator():
	
	rospy.init_node('simulator', anonymous=True) #initialise the node
	rospy.Subscriber("cmd_vel", Twist, diffdrive) #create a subscriber for cmd_vel using twist, call it back in the diffdrive
	rospy.spin() # put it to sleep amount of time



if __name__ == '__main__':
	
	#simulator() # calls the simulator function

