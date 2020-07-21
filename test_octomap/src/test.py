#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from octomap_msgs.msg import Octomap

def callback(data):
    print('received msg')
    print(type(data.data))
    l = list(data.data)
    print(len(l))

    # data is of type uint8 check
    # https://github.com/OctoMap/octomap_msgs/blob/melodic-devel/msg/Octomap.msg
    # So it takes 8 bits, 1 byte
    size_in_MBytes = float(len(l)) / 10E6
    print('size_in_MBytes = ' + str(size_in_MBytes))

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/octomap_full', Octomap, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
