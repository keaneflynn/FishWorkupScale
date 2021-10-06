import cv2
import numpy as np

class WeightDetector:
    def __init__(self):
        self.weightConfidence = 0.01
        self.weightNMS = 0.2
        
        self.weightClass_names = []
        with open("classNames4Numbers.txt","r") as f: #add proper files
            self.weightClass_names = [cname.strip() for cname in f.readlines()]
            
        weightNet = cv2.dnn.readNet("numberFile.weights","numberConfigurationFile.cfg") #add proper files
        self.weightModel = cv2.dnn_DetectionModel(weightNet)
        self.weightModel.setInputParams(size=(256, 256), scale=1 / 255, swapRB=True)
        
        self.numberCentroid = []
        self.numberHeight = []
        self.numberWidth = []
        self.numberClass = []

    def weightDetection(self, color_frame):
        #run standard detection method for numbers on the scale
        self.classes, self.scores, self.boxes = self.weightModel.detect(color_frame, self.weightConfidence, self.weightNMS)
        self.numberDetection_count = len(self.classes)    
        
        for i in range(self.numberDetection_count):
            #Loop over detections and create an array with all of the important info for each detection
            self.numberWidth.append(self.boxes[i, 2])
            #self.numberHeight.append(self.boxes[i, 3])
            self.numberX_coordinate = ((self.box_width[i] // 2) + self.boxes[i, 0],
                                       #(self.box_height[i] // 2) + self.boxes[i, 1])
            self.numberClass.append(self.classes[i])
            
        return self.numberCentroid, self.numberClass

    def numArrangement(self):
        fishWeight_array = []
        #take in classes output and organize them by left to right screen position (increasing x-coordinate value) and create single floating point value for weight value
        # ex) [(5,400),(3, 370),(7,355),(4,385)] -> needs to be read out in the following order [(7,355),(3, 370),(4,385),(5,400)] which will be a weigt of 734.5 grams

        return fishWeight_array

    
            
