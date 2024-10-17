#!/usr/bin/env python3
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, MJPEGEncoder, Encoder
from picamera2.outputs import FileOutput, FfmpegOutput
from libcamera import controls
import time
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (1920, 1080)}, encode="main")
picam2.configure(config)

picam2.set_controls({"FrameRate": 30, "AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0})

h264_encoder = H264Encoder()
h264_output = f"recording_{time.strftime('%Y-%m-%d_%H-%M-%S')}.h264"

picam2.start_recording(h264_encoder, h264_output)

while True:
    pass

lores_encoder.stop()
picam2.stop_recording()
