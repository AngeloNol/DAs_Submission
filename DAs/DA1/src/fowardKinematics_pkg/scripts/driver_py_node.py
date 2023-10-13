#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist 
import random #random library

'''
These is my driver function where I publish the cmd_vel for left and right
'''
def driver():
	rospy.init_node('driver', anonymous=True) #initialise the node
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10) #create a publisher for cmd_vel using twist
	vel_msg = Twist() # create variable for the twist function
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown(): #checks if the program has not been terminated
		vel_msg.linear.x = random.uniform(1,1000) # input random float value into the x for the twist
		vel_msg.linear.y = random.uniform(1,1000) # input random float value into the y for the twist
		rospy.loginfo("right = %f left = %f " % (vel_msg.linear.x,vel_msg.linear.y)) # print the left and right velocity in the terminal
		pub.publish(vel_msg) # it will publish the x and y values from the twist
		rate.sleep() # put it to sleep amount of time		


if __name__ == '__main__':
	try:
		driver(); # calls the driver function
	except rospy.ROSInterruptException: # this catches exception
		pass

	

