import cv2
from argparse import ArgumentParser
from fishDetectYolo import *
from json_output import *
from realsense import *
from weightDetectYolo import *

def main():
    parser = ArgumentParser(description='measure detected objects using YOLO')
    parser.add_argument('--samplename', type=str, help='unique name or identifier for the sample of data you are collecting')
    args = parser.parse_args()

    while True:

        rs = RealSense()
        wd = WeightDetector()
        fd = FishDetections()

        input('press enter to begin capture loop . . .')

        _, depth_frame, color_frame = rs.grab_frame() 
        fd.detection(color_frame)
        fd.object_distance(depth_frame)
        fd.object_length()
        fd.object_height()
        fd.draw_output(color_frame)
        main_dataVector, class_list = yd.json_data()

        fo = FileOutput(args.samplename, main_dataVector)
        fo.to_json(class_list)

        cv2.imshow("color frame", color_frame)
        cv2.waitKey(1)
        
    rs.release_frame()
    cv2.destroyAllWindows()
    exit(1)

if __name__ == '__main__':
    main()
