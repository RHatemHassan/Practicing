#!/usr/bin/env python3

# This node ( will receive a string message )

import rospy                     
from std_msgs.msg import String  

def call_back(mssg) :  #interrupt 
    rospy.loginfo(' I heard to : %s', mssg.data ) 

def listener_func ():
    rospy.init_node('listener_1',anonymous=True)
    rospy.Subscriber('my_topi', String ,call_back)

    rospy.spin()

if __name__ == '__main__' :
    try : 
        listener_func ()
    except rospy.ROSInterruptException :
        pass 

