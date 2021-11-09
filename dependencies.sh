#!/bin/bash

for var in pyrealsense2 opencv-python argparse DateTime numpy pyserial
do
yes | pip install $var
done
