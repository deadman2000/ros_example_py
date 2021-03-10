#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image


def img_callback(img):
    rospy.loginfo('%d x %d    size: %d', img.width, img.height, len(img.data))


def example():
    rospy.init_node('example', anonymous=True)
    rospy.Subscriber('/drone_camera_264_main/image_raw', Image, img_callback, queue_size=5)
    rospy.spin()


if __name__ == '__main__':
    try:
        example()
    except rospy.ROSInterruptException:
        pass
