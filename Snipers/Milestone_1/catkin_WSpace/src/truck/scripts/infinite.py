#!/usr/bin/env python3 


import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion


global pub_steer , pub_vel , pup_brake
pub_steer=rospy.Publisher('/SteeringAngle',Float64,queue_size=10)
pub_vel=rospy.Publisher('/cmd_vel',Float64,queue_size=10)
pub_brake=rospy.Publisher('/brakes',Float64,queue_size=10)

global leftt , rightt , straight2 , straight1 , x

leftt  = False  
rightt = False 
straight2=False
#starting straight by default  
straight1=True

### all prints in this code used to ensure the coditions is run will or not  
def  c_straight_path(data) : 
    global pub_steer , pub_vel 
    global leftt , rightt , straight2 , straight1 , x 
    position_y =  ( data.pose.pose.position.y)
    position_x =  ( data.pose.pose.position.x)
    ori = data.pose.pose.orientation 
    orientation = [ori.x,ori.y,ori.z,ori.w]
    (roll,pitch,yaw) = euler_from_quaternion(orientation)
    theta = yaw *100
    print (theta)

    
    ## moving straight (forward)
    if straight1==True and position_y < -60.0 :
            vel= 0.08
            angle = 0
            pub_steer.publish(angle)
            pub_vel.publish( vel)
            print ('forward ')

            x=x+1 ## to calculate the distance car moved in one line for reusing it in the x shape 

            if -61.0 <= position_y <= -60.0 :
                leftt = True
                straight1=False
                print ('turn left')
            
    ## rotate left  in circle with 6 meter radius
    if leftt  == True : 
            vel= 0.08
            angle=20.714
            pub_vel.publish(vel)
            pub_steer.publish(angle)   
            print ('lefttt  ')

            if  -200.0 < theta < -180.0 :       
                leftt  = False  
                straight2=True
                print ('forward again x shape')

    if  straight2 == True   : 
            vel= 0.08
            angle = 0
            pub_vel.publish(vel)
            pub_steer.publish(angle)
            print ('againnn')

            x=x-1                       ##### 

            if  -5.0 < x <= 2 :       
                straight2=False
                rightt  = True
                print ('turn right')

    if rightt  == True :
            vel= 0.08
            angle= -20.714
            pub_vel.publish(vel)
            pub_steer.publish(angle)   
            print ('rightttt ')

            if  -5 < theta < 5 :
                 straight1=True
                 rightt  = False
 



def pose():
    rospy.init_node('infinite', anonymous=True)
    sub=rospy.Subscriber('/odom',Odometry,c_straight_path)  
    rate=rospy.Rate(1000)
    rospy.spin()

if __name__ =="__main__":
    x=0
    try:
       pose()
    except rospy.ROSInterruptException:
        pass