#! /usr/bin/env python

import rospy
import time
import sys
from nav_msgs.msg import OccupancyGrid
yo=rospy.get_param("initial_pose")

def dothis(data):
	temp=data
	temp.info.origin.position.x=temp.info.origin.position.x-yo.get("tx")
	temp.info.origin.position.y=temp.info.origin.position.y-yo.get("ty")
	print(temp)
	pub.publish(temp)
rospy.init_node("this_map")
sub=rospy.Subscriber("map",OccupancyGrid,dothis)
pub=rospy.Publisher("this_map",OccupancyGrid,queue_size=10)
rospy.spin()
	
