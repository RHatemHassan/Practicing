#!/usr/bin/env python3 


import rospy
from std_msgs.msg import Float64
def pub_steer():
    pub=rospy.Publisher('/SteeringAngle',Float64,queue_size=10)
    rospy.init_node('steer_ang', anonymous=True)
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        angle=0
        
        pub.publish(angle)
        rate.sleep()


if __name__ =="__main__":
    try:
        pub_steer()
    except rospy.ROSInterruptException:
        pass