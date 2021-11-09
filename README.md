# Automated fish workup scale

Hello! Welcome to yet another of my neural network fisheries contraptions. In this git repo, we will be capturing fish images through an intel RealSense camera which will then be used for object detection and length measurements. The computer will also be connected to the serial port of an Ohaus Ranger series scale via usb to obtain weight values. It currently only works with Windows operating system due intel's lack of support to other OS, however I am going to try to get it working with macOS as well as linux.


## Download and setup program
After moving into the desired local directory to download the repository, sssue the following command in your terminal to download this repository:
```
git clone https://github.com/keaneflynn/FishWorkupScale.git && cd FishWorkupScale/
```
Then to install the necessary dependencies to run this script, issue the following command in your terminal to run the bash script:
```
./dependencies.sh
```

## Running the program
Once the above steps are completed, issue the following command in your terminal to run the program that will enter you into a data capture loop:
```
python main.py <samplename>
```
\*Note that there is a positional argument of 'samplename' needed for the process to function as this information will be passed to the .json output files.

## Program info and output
Upon launching this program, it will begin a loop process that will be hung until you press the "Print" button on the scale, or whatever button is used to issue a readout on your scale (untested for other scale models). Upon pressing this button, your scale will send the immediate weight value through your COM port to your computer where it will be stored. The loop then continues to capture an image from the Intel RealSense camera where the object in question will be detected and the length of the object (horizontal distance) will be stored. All of these stored data will be printed out to a .json file along with the sample name and the current date and time in ISO format in the output directory after each press of the "Print" button on your scale. These files can easily be converted to whatever desired format later through packages such as [JQ](https://stedolan.github.io/jq/) from your terminal.

![sample image](https://github.com/keaneflynn/FishWorkupScale/blob/master/media/sample_image.png)
*Above is an output window of the data written to each .json file for visualization purposes, this function can easily be commented out if so desired.*

### Program background, inspiration, and funding sources
This project was created with the hope to improve data collection for fisheries research in the Mekong Delta watershed. Sampling fishes at their field sites can be arduous and time consuming and I hope that this can imporove throughput. The Mekong Delta is currently experiencing drastic impacts from land and water use changes and it is imperative that the fishery is monitored to sustain this resource and, consequently, the local peoples livelihood and culture.   
I would like to thank the Global Water Center of UNR (Aaron Koning, Dr. Zeb Hogan, and Dr. Sudeep Chandra) for funding the equipment necessary to test this hardware/software combination out to create this program. I hope that someone can use this somehow to improve their workflow for whatever they are working on. As always, shoot me a message if you have any questions or recommendations for features to add.  
"Peace, love, and taco grease" - Guy Fieri

