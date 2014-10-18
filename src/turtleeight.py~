#!/usr/bin/env python

#running turtle in a figure 8
#Andrew Turchina
#ME495
#HW1

from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist	#twist geometry as given from turtlesim wiki subscriber
import math		#need to import modules
import rospy		#need to import modules
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)




def moveTurtle():
    rate = rospy.Rate(75.0)    	#can change to give better resultion
    T = input('\n Insert value for T:') 			#time for 1 revolution; can change
    #T = 5
    t0 = rospy.get_time()	#initial time
    
    while not rospy.is_shutdown():
        
        t = rospy.get_time() - t0	#gives t=0 every time so turtle starts at same spot
    

        vX = (12 * math.pi * math.cos(4 * math.pi * t / T)) / T #derivative of x = v*cos(theta)
        vY = (6 * math.pi * math.cos(2 * math.pi * t / T)) / T	#derivative of y = v*sin(theta)
        
        aX = (-48 * math.pi * math.pi * math.sin(4 * math.pi * t / T)) / (T * T) #2nd derivative of x
        aY = (-12 * math.pi * math.pi * math.sin(2 * math.pi * t / T)) / (T * T) #2nd derivative of y
        
        v = math.sqrt(vX * vX + vY * vY) #triangle properties a^2+b^2=c^2 to get linear velocity

        omega = (vX * aY - vY * aX) / (vX * vX + vY * vY)	#derivative of theta=tan(y'/x')^-1 (mathematica)

        command = Twist()    		#we see that the turtlesim_node subscribes to cmd_vel for the linear and angular command velocity
        command.linear.x = v		#velocity in x direction of turtle is important	
        command.linear.y = 0
        command.linear.z = 0
        command.angular.x = 0
        command.angular.y = 0
        command.angular.z = omega	#angular velocity around the z-axis of turtle is important

        pub.publish(command)
        rate.sleep()



if __name__ == '__main__':
    try:
        rospy.wait_for_service('turtle1/teleport_absolute')
        turtle_sp = (0,0,0)  			#try to center so doesn't hit walls
        turtle_sp = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)	#used in combo with above, not sure why doesn't work alone
        rospy.init_node('steering_turtle', anonymous=True)
        moveTurtle()
    except rospy.ROSInterruptException: pass
