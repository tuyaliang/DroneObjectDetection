# Visual Object Detect System
Visual Object Detect System is a project based on Tensorflow, Keras, YOLOv3, also compiling some interesting stuffs such as detecting image on web page and a C/S remote monitor system.
> Note:This is also my project to participate in the Wuliangchun Cup Competition in Electronics and Information Engineering School of Sichuan University.Thanks to Professor Lei for providing necessary assistance.

> Due to the inability to understand the algorithm hidden in YOLOv3, code files in /vision/yolo3 completely come from keras-yolo3.


--------
## Installation Instrction
### Test Environment
	
Windows 10 1803 + NVIDIA GTX1060 6GB

Anaconda 4.3.0

Python 3.5.2

TensorFlow-GPU 1.8.0 (Due to the limit of CPU compute capibility, single image would take 1.5 seconds or so to draw, it's hard to used to process a video.)

Keras 2.2.0

CUDA 9.0.176 (https://developer.nvidia.com/cuda-90-download-archive)

cuDNN 7.3.1.20 (https://developer.nvidia.com/cudnn)

To get the source code, run:
	
    git pull https://github.com/MrZilinXiao/VisualObjectDetection.git
    
Before run main.py, please run:

    pip install -r main.py.packages.txt
	
to install necessary dependencies.

then run 

    python main.py --help

to see what functions main.py have.

--------
## Functions Introduction
    python main.py --help
    
    usage: main.py [-h] [--image] [--input [INPUT]] [--output [OUTPUT]]
                   [--cam [CAM]] [--web [WEB]] [--online [ONLINE]] [--rtsp [RTSP]]
    
    optional arguments:
      -h, --help         show this help message and exit
      --image            Image detection mode, will ignore all positional
                         arguments, press Ctrl+C to stop.
      --input [INPUT]    [Optional] Video input path
      --output [OUTPUT]  [Optional] Video output path
      --cam [CAM]        [Optional] Using camera,by default using built-in camera
                         of laptop,press Esc to stop.
      --web [WEB]        [Optional] Using web server,press Ctrl+C to stop.
      --online [ONLINE]  [Optional] Using a C/S structure system, will start a
                         video stream detecting client. Please run remote.py on
                         the device with a camera and configure ip and port in
                         settings.py first. Press Esc to stop.
      --rtsp [RTSP]      [Optional] Detect video stream from an IP camera or
                         something else. Need rtsp address as an argument.
            
remote_server.py can start an online streaming server which sends local camera's video stream to client.
remote_server_2.py is only for Python2.7 to avoid unnecessary configuration.                        

##Trainning Your Own DataSet

VisualObjectDetection can train over PASCAL VOC format dataset without pre-trained model.
Files needed for training are in tool folder.To be specific

## Performance Test


