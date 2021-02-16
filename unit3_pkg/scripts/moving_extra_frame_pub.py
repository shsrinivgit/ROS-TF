#!/usr/bin/env python
import rospy
import tf
import math
roll = 0
pitch = 0
if __name__ == '__main__':
    rospy.init_node('my_moving_carrot_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(5.0)
    turning_speed_rate = 2
    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec()
        print(t)
        yaw = t % (2*math.pi) - math.pi
        print('yaw',yaw)
        quaternion = tf.transformations.quaternion_from_euler(roll,pitch,yaw)
        br.sendTransform((1.0,0.0, 0.0),
                         quaternion,
                         rospy.Time.now(),
                         "moving_carrot",
                         "coke_can")
        rospy.sleep(1)