#!/usr/bin/env python3 


import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion


global pub_steer , pub_vel , pub_brake ,left ,straight ,right
pub_steer=rospy.Publisher('/SteeringAngle',Float64,queue_size=10)
pub_vel=rospy.Publisher('/cmd_vel',Float64,queue_size=10)
pub_brake=rospy.Publisher('/brakes',Float64,queue_size=10)


def  c_straight_path(data) : 
    global pub_steer , pub_vel  ,pub_brake ,left ,straight,right

    ## getting the position and orientation from odom 
    position_y =  ( data.pose.pose.position.y)
    position_x =  ( data.pose.pose.position.x)
    ori = data.pose.pose.orientation 
    orientation = [ori.x,ori.y,ori.z,ori.w]
    (roll,pitch,yaw) = euler_from_quaternion(orientation)
    ## the yaw theta is the angle around z_axis 
    theta = int(yaw *100)
    print (yaw *100)

    ## moving with high velocity in the begining (to reach in minumum time )
    if position_y < -30:
     vel = .2
     angle = 0
     pub_steer.publish(angle)
     pub_vel.publish( vel)

    ## decreasing velocity to avoid car slipping while rotation
    if   -20 < position_y < -5:
     vel = .06
     angle = 0
     pub_steer.publish(angle)
     pub_vel.publish( vel)
    
    ## start rotation for left from the position 0 in y_axis until the car reach angle 90 
    if 0 <= position_y  and theta <= 90  and left == True : ##### 
         
            vel = .040
            angle = 25
            pub_vel.publish(vel)
            pub_steer.publish(angle) 
            
            ## changing parameters to avoid runing this condition again and to go right
            if   85 <= theta  <= 90  :
                left = False
                right = True 
                print ('go right')  

    if  left == False  and 0 < theta <= 90  and right == True  :
            vel = .040
            angle = -25
            pub_vel.publish(vel)
            pub_steer.publish(angle)

            if 0 <= theta <= 6  : 
             straight = True                
             right = False 
             print ('straight again')       



    if straight == True :
     vel = .04
     angle = 0
     pub_steer.publish(angle)
     pub_vel.publish( vel)


    if straight == True and position_y > 10:
     vel = .08
     angle = 0
     pub_steer.publish(angle)
     pub_vel.publish( vel)

    if position_y >= 74:
           brake_equ = .5
           vel = 0
           pub_brake.publish(brake_equ)
           pub_vel.publish(vel)

def pose():
    rospy.init_node('position_y', anonymous=True)
    sub=rospy.Subscriber('/odom',Odometry,c_straight_path)  
    rate=rospy.Rate(100)
    rospy.spin()

if __name__ =="__main__":
    left = True
    straight = False
    right = False


    try:
       pose()
    except rospy.ROSInterruptException:
        pass




