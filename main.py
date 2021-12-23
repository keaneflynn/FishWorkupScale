import cv2
from argparse import ArgumentParser
from fishDetectYolo import *
from json_output import *
from realsense import *
from weightGrab import ScaleGrab


def main():
    parser = ArgumentParser(description='measure detected objects using YOLO')
    parser.add_argument('samplename', type=str, help='unique name or identifier for the sample of data you are collecting')
    args = parser.parse_args()

    rs = RealSense()
    sg = ScaleGrab()

    while True:
        fd = FishDetections()
        
        weight_g = sg.readout()
        _, depth_frame, color_frame = rs.grab_frame() 
        fd.detection(color_frame)
        fd.object_distance(depth_frame)
        fd.object_length()
        fd.object_height()
        fd.draw_output(color_frame, weight_g)
        main_dataVector, class_list = fd.json_data()

        fo = FileOutput(args.samplename, main_dataVector, weight_g)
        fo.to_json(class_list)

        cv2.imshow("color frame", color_frame)
        cv2.waitKey(1)
        
    rs.release_frame()
    cv2.destroyAllWindows()
    exit(0)

if __name__ == '__main__':
    main()
