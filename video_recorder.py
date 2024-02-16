#!/usr/bin/env python3
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, MJPEGEncoder, Encoder
from picamera2.outputs import FileOutput, FfmpegOutput
from libcamera import controls
import time
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (1536, 864)}, lores={"size": (640, 360)}, encode="main")
picam2.configure(config)

picam2.set_controls({"FrameRate": 20, "AfMode": controls.AfModeEnum.Continuous})

h264_encoder = H264Encoder()
h264_output = f"recording_{time.strftime('%Y-%m-%d_%H-%M-%S')}.h264"

lores_encoder = H264Encoder()
lores_encoder.size = config["lores"]["size"]
lores_encoder.format = config["lores"]["format"]
lores_encoder.bitrate = 800000
lores_encoder.output = FfmpegOutput("-f mpegts -minrate 700k -maxrate 900k -bufsize 10000 -muxrate 921568 stream.ts")
lores_encoder.repeat = True
lores_encoder.iperiod = 10
lores_encoder.start()

picam2.start_recording(h264_encoder, h264_output)

lores_stream = picam2.stream_map["lores"]

start = time.time()
while True:
    request = picam2.capture_request()
    lores_encoder.encode(lores_stream, request)
    request.release()

lores_encoder.stop()
picam2.stop_recording()
