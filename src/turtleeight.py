#!/usr/bin/env python

from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
import math
import rospy
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)




def moveTurtle():
    rate = rospy.Rate(70.0)    	#can change to give better resultion
    
    T = 5 			#time for 1 revolution; can change
    
    t0 = rospy.get_time()	#initial time
    
    while not rospy.is_shutdown():
        
        t = rospy.get_time() - t0	#gives t=0 every time so turtle starts at same spot
    

        vX = (12 * math.pi * math.cos(4 * math.pi * t / T)) / T
        vY = (6 * math.pi * math.cos(2 * math.pi * t / T)) / T
        
        aX = (-48 * math.pi * math.pi * math.sin(4 * math.pi * t / T)) / (T * T)
        aY = (-12 * math.pi * math.pi * math.sin(2 * math.pi * t / T)) / (T * T)
        
        v = math.sqrt(vX * vX + vY * vY)

        omega = (vX * aY - vY * aX) / (vX * vX + vY * vY)

        command = Twist()    
        command.linear.x = v
        command.linear.y = 0
        command.linear.z = 0
        command.angular.x = 0
        command.angular.y = 0
        command.angular.z = omega

        pub.publish(command)
        rate.sleep()



if __name__ == '__main__':
    try:
        rospy.wait_for_service('turtle1/teleport_absolute')
        turtle_sp = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        turtle_sp = (20,5,0)
        rospy.init_node('steering_turtle', anonymous=True)
        moveTurtle()
    except rospy.ROSInterruptException: pass
