#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
global pub_brakee , pub_vel
pub_brakee = rospy.Publisher('/brakes',Float64,queue_size=10)
pub_vel=rospy.Publisher('/cmd_vel',Float64,queue_size=10)



def brake (data):
    global pub_brakee, pub_vel
    position = int (data.pose.pose.position.y)
    rospy.loginfo(position)

    pub_vel.publish(.4)


    while position >= -20 :
            brake_equ = 1
            vel = 0
            pub_brakee.publish(brake_equ)
            pub_vel.publish(vel)


    
    
def pub_brake():
    rospy.init_node('position', anonymous=True)
    sub=rospy.Subscriber('/odom',Odometry,brake)
    rate=rospy.Rate(10)
    rospy.spin()




if __name__ =="__main__":
    try:
       pub_brake()
    except rospy.ROSInterruptException:
        pass