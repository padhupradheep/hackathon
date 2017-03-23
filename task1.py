#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


def left_right(message):
    print message
    msg=Twist()
    msg1=String()
    rospy.init_node('leftright')
    dire=message.data.lower()
    if dire=="l":
        moving(-0.2,msg,msg1)
	
    elif dire=="r":
        moving(0.2,msg,msg1)
	   
def moving(vel,msg,msg1):
    nt=0
    distance = input("Enter distance ")
    time=distance/0.2
    ct=rospy.get_time()                

    while (nt-ct<=time):
        msg.linear.y=vel
        lr_pub.publish(msg)
        nt=rospy.get_time()
        msg.linear.y=0
        lr_pub.publish(msg)
    msg1.data='success'    
    a.publish(msg1)
        
def trigger_callback(message):
    execute = message.data.lower()    
    
def main():
    global lr_pub
    global a
    rospy.init_node('leftright')
    rospy.Subscriber('/input', String, left_right)    
    rospy.Subscriber('/event_in', String, trigger_callback)
    a=rospy.Publisher('/event_out', String, queue_size=10)
    rospy.Subscriber('/event_out',String,left_right)
    lr_pub=rospy.Publisher('/cmd_vel', Twist,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
       rate.sleep()
    pass
    
if __name__ == '__main__':
   main()
