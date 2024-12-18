#!/usr/bin/env python3

from cartesian_interface.pyci_all import *

ci = pyci.CartesianInterfaceRos()
tcp_1 = ci.getTask('tcp')

waypoints = [
    Affine3(pos=[0.45, -0.30, 0.10], rot=[0, 1, 1, 0]),
    Affine3(pos=[0.45,  0.30, 0.10], rot=[0, 1, 1, 0]),
    Affine3(pos=[0.45, -0.30, 0.60], rot=[0, 1, 1, 0]),
    Affine3(pos=[0.45,  0.30, 0.60], rot=[0, 1, 1, 0]),
]

wp_time = 1.5

while True:
    for w in waypoints:
        tcp_1.setPoseTarget(w, wp_time)
        tcp_1.waitReachCompleted(10.0)
