#!/usr/bin/env python
import rospy
import roslib;

from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def sonar_callback():
    
	
	scan = LaserScan()
	rospy.init_node('task2')  
	scan_pub = rospy.Publisher('scan', LaserScan, queue_size=50)
	num_readings = 100
	laser_frequency = 40
	ranges[num_readings]=0
	intensities[num_readings]=0

	count = 0
	r = rospy.Rate(1.0)
	for i in range (0,num_readings):
		ranges[i]=count;
		intensities[i]=100+count;

	current_time = rospy.Time.now()
	

	scan.header.stamp = current_time
	scan.header.frame_id = 'laser_frame'
	scan.angle_min = -1.57
	scan.angle_max = 1.57
	scan.angle_increment = 3.14 / num_readings
	scan.time_increment = (1.0 / laser_frequency) / (num_readings)
	scan.range_min = 0.0
	scan.range_max = 100.0
	scan.ranges = []
	scan.intensities = []
	for i in range(0, num_readings):
		scan.ranges.append(1.0 * count)  # fake data
		scan.intensities.append(1)  # fake data

	scan_pub.publish(scan)
	count += 1
	r.sleep()


	    
	    
	    
	   
	    

if __name__ == '__main__':
	sonar_callback()
