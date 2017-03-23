#!/usr/bin/env python
import rospy


from geometry_msgs.msg import Twist



def left_right():
	global velocity_publisher
	twist = Twist()
	rospy.init_node('leftright')    
  
    	velocity_publisher = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
	
	
	st1=raw_input("Enter the string")
	if st1=="left":
		twist.linear.x=0.1
		twist.linear.y = 0.0
		print "left"

	elif st1=="right":
		twist.linear.x=-0.1
		twist.linear.y=0.0
		print "rigt"
	
	velocity_publisher.publish(twist)
	


    
    
  


if __name__ == '__main__':
   left_right()
