import argparse

from vision import detect_video, detect_camera, detect_img, online_client, rtsp
from settings import *

FLAGS = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments, press Ctrl+C to stop.'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str, required=False, default='',
        help="Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default='',
        help="[Optional] Video output path"
    )

    parser.add_argument(
        '--cam', nargs='?', required=False,
        help="[Optional] Using camera,by default using built-in camera of laptop,press Esc to stop."
    )

    parser.add_argument(
        '--web', nargs='?', required=False,
        help="[Optional] Using web server,press Ctrl+C to stop."
    )

    parser.add_argument(
        '--online', nargs='?', required=False,
        help="[Optional] Using a C/S structure system, will start a video stream detecting client. Please run "
             "remote.py on the device with a camera and configure ip and port in settings.py first. Press Esc to stop."
    )
    parser.add_argument(
        '--rtsp', nargs='?', required=False,
        help="[Optional] Detect video stream from an IP camera or something else. Need rtsp address as argument."
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
#        if "input" in FLAGS:
#            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img()
    elif "cam" in FLAGS:
        detect_camera(CAM_NUMBER)
    elif "online" in FLAGS:
        online_client()
    elif "rtsp" in FLAGS:
        rtsp(FLAGS.rtsp)
    elif "web" in FLAGS:
        from web_server import server_start
        server_start()
    elif "input" in FLAGS:
        detect_video(FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
