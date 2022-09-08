#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Bicycle():
    def __init__(self):
        rospy.init_node('front_steering')
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/turtle1/pose', Pose, callback=self.pose_upgrade)
        self.rate = rospy.Rate(10)
        
        self.time = 0

    def pose_upgrade(self, msg: Pose):
        self.pose = msg

    def move(self, time_of_motion, vel, delta):
        self.lr = rospy.get_param("/lr")
        self.lf = rospy.get_param("/lf")
        self.vel = vel
        self.delta = delta

        while self.time < time_of_motion:
            self.beta = np.arctan((self.lr * np.tan(self.delta)) / (self.lr + self.lf))
            vel =  Twist()

            vel.linear.x = self.vel * np.cos(self.pose.theta + self.beta)
            vel.linear.y = self.vel * np.sin(self.pose.theta + self.beta)
            vel.linear.z = 0

            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = ((self.vel * np.cos(self.beta) * np.tan(self.delta)) / (self.lr + self.lf))
            
            self.pub.publish(vel)

            self.rate.sleep()
            self.time += 0.1
            self.delta -= 0.01

        vel.linear.x = 0
        vel.linear.y = 0
        vel.angular.z = 0
        
        self.pub.publish(vel)
        print('Time Finished')

        rospy.spin()


model = Bicycle()

time_of_motion = float(input('Enter time of motion value: '))
vel = float(input('Enter velocity value: '))
str_angle = float(input('Enter steering angle value: '))

model.move(time_of_motion, vel, str_angle)