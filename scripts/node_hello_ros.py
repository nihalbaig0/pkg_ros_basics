#!/usr/bin/env python3

import rospy

def main():
    # Make the scripta ROS Node
    rospy.init_node('node_hello_ros', anonymous=True)

    #Print info on the console
    rospy.loginfo("Hello World")

    # Keep the node alive till it is killed by the user.
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass