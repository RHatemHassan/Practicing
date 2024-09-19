#!/usr/bin/env python3 


import rospy
from std_msgs.msg import Float64
def pub_cmdvel():
    pub=rospy.Publisher('/cmd_vel',Float64,queue_size=10)
    rospy.init_node('gas_on', anonymous=True)
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        gas=1
        pub.publish(gas)
        rate.sleep()


if __name__ =="__main__":
    try:
        pub_cmdvel()
    except rospy.ROSInterruptException:
        pass