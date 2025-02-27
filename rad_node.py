#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32

rospy.init_node('rad_node')
pub = rospy.Publisher('orientation', Float32, queue_size=10)


def callback (imu_tipe):
    rad=imu_tipe
    rad_tipe = Float32()
    rospy.loginfo(rad)
    rad_tipe.data = rad
    pub.publish(rad_tipe)


rospy.Subscriber('imu', Imu, callback, queue_size=10)
rospy.spin()