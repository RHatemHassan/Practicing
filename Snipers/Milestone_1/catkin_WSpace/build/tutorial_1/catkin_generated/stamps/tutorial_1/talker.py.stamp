#!/usr/bin/env python

# This node ( will publish a string message )

import rospy                     #add rospy library  
from std_msgs.msg import String  #define string variable 

def talker_func ():
    pub = rospy.Publisher('my_topi',String, queue_size=10) # creating publisher 
    rospy.init_node('talker_1', anonymous=True)            #creating node 
    rate = rospy.Rate(2)            # 3 hz (3msg_1sec)
    while not rospy.is_shutdown():  # while the node didn't kill
        sent_msg = 'Hello world >_< %s' % rospy.get_time()  
        rospy.loginfo(sent_msg)     # = print(sent_msg) 
        pub.publish(sent_msg)
        rate.sleep()

if __name__ == '__main__' :
    try : 
        talker_func ()
    except rospy.ROSInterruptException :
        pass 

