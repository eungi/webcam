#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2
import numpy as np

bridge = CvBridge()

def main() :
	pub = rospy.Publisher('camera/rgb/image_raw', Image, queue_size=1)
	rospy.init_node('camera', anonymous=True)
	rate = rospy.Rate(10)

	cap = cv2.VideoCapture(1)
	if (cap.isOpened() == False): 
		print("Unable to read camera feed")
	frame_width = int(cap.get(3))
	frame_height = int(cap.get(4))
	print(frame_width, frame_height)

	while not rospy.is_shutdown():
		ret, frame = cap.read()
		if ret == True: 
			frame_ = bridge.cv2_to_imgmsg(frame, "bgr8")
			pub.publish(frame_)
		rate.sleep()

if __name__ == '__main__':
	try :
		main()
	except rospy.ROSInterruptException:
		pass
