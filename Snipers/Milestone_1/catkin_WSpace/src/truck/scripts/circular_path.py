#!/usr/bin/env python3 


import rospy
from std_msgs.msg import Float64

def  circular_path() : 
    ## creating puplisher for steer angle and velocity  control (the topic name must be same as in copplia_code)
    pub_steer=rospy.Publisher('/SteeringAngle',Float64,queue_size=10) 
    pub_vel=rospy.Publisher('/cmd_vel',Float64,queue_size=10)         
    # creating the node 
    rospy.init_node('cicular', anonymous=True)
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        angle=20.714
        velocity= 0.08
        pub_steer.publish(angle)
        pub_vel.publish(velocity)

        rate.sleep()



if __name__ =="__main__":
    try:
       circular_path()
    except rospy.ROSInterruptException:
        pass