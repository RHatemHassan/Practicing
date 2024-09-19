#!/usr/bin/env python

import rospy 
from geometry_msgs.msg import Pose2D
import matplotlib.pyplot as plt
import numpy as np

def robot_pos(data):
    rospy.loginfo(' The new theta is : %s', format((data.theta*180/np.pi)) ) 
    plt.plot(data.x,data.y,marker=(3,0,(data.theta*180/np.pi)-90),markerSize=10,color='m')
    plt.axis('equal')
    plt.draw()
    plt.pause(0.01)

def listener_2 (): 
    rospy.init_node('position_control',anonymous=True)
    rospy.Subscriber('pioneer_location', Pose2D ,robot_pos)

    rospy.spin()


if __name__ == '__main__' : 
    listener_2 ()







