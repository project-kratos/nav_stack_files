#! /usr/bin/env python

import rospy 
from tf.msg import tfMessage
from geometry_msgs.msg import Transform,Pose,Vector3,Quaternion
from nav_stack_files.srv import Initial_pose,Initial_poseResponse

temp_tf_msg=tfMessage()
temp_transform_msg=Transform()
temp_transform_msg.translation=Vector3(0,0,0)
temp_transform_msg.rotation=Quaternion(0,0,0,0)
temp_tf_msg.transforms.append(temp_transform_msg)
data1=Pose()

def doThis(data):
	global temp_tf_msg
#	print(temp_tf_msg)
#	print(data.transforms[0])
	if data.transforms[0].child_frame_id=="base_footprint":
#		if (temp_tf_msg.transforms[0].translation!=data.transforms[0].transform.translation or temp_tf_msg.transforms[0].rotation!=data.transforms[0].transform.rotation):
			temp_tf_msg=data 
			data1.position=temp_tf_msg.transforms[0].transform.translation
			data1.orientation=temp_tf_msg.transforms[0].transform.rotation
			rospy.set_param("initial_pose",{'tx':data1.position.x,'ty':data1.position.y,'tz':data1.position.z,'qx':data1.orientation.x,'qy':data1.orientation.y,'qz':data1.orientation.z})
#			rospy.dump_param("this.yaml")
	
def doThat(request):
	if request:
		return data1

rospy.init_node("initial_pose_srv")
sub=rospy.Subscriber("tf",tfMessage,doThis)
server=rospy.Service("initial_pose",Initial_pose,doThat)
rospy.spin()



