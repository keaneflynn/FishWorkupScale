# Automated fish workup scale

Hello! Welcome to yet another of my neural network fisheries contraptions. In this git repo, we will be capturing fish images through an intel RealSense camera which will then be used for object detection and length measurements. The computer will also be connected to the serial port of an Ohaus Ranger series scale via usb to obtain weight values. It currently only works with Windows operating system due intel's lack of support to other OS, however I am going to try to get it working with macOS as well as linux.

## To download and setup program
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

## Program info and output
Upon launching this program, it will begin a loop process that will be hung until you press the "Print" button on the scale, or whatever button is used to issue a readout on your scale (untested for other scale models). Upon pressing this button, your scale will send the immediate weight value through your COM port to your computer where it will be stored. THe loop then continues to capture an image from the Intel RealSense camera where the object in question will be detected and the length of the object (horizontal distance) will be stored. All of these storage data will be printed out to a .json file in the output directory after each press of the "Print" button on your scale. These files can easily be converted to whatever desired format later through packages such as JQ from your terminal.

### Program background, inspiration, and funding sources
