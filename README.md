# Automated fish workup scale

Hello! Welcome to yet another of my neural network fisheries contraptions. In this git repo, we will be capturing fish images through an intel RealSense camera which will then be used for object detection and length measurements. The computer will also be connected to the serial port of an Ohaus Ranger series scale via usb to obtain weight values. It currently only works with Windows operating system due intel's lack of support to other OS, however I am going to try to get it working with macOS as well as linux.

## To download and setup program
After moving into the desired local directory to download the repository, sssue the following command in your terminal to download this repository:
```
git clone https://github.com/keaneflynn/FishWorkupScale.git && cd FishWorkupScale/
```
Then to install the necessary dependencies to run this script, issue the following commands in your terminal to run the bash script:
```
chmod 755 dependencies.sh
./dependencies.sh
```
