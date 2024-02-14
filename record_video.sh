#!/bin/bash
# Note: stream.ts should be a named pipe, run `mkfifo stream.ts` to create it
cd /home/rocket/RocketVideo
sudo nohup ./rpidatv/bin/rpidatv -i stream.ts -s 1000 -c 1/2 -m RF -f 423 -p 7 -l > /dev/null 2>&1 &
sudo nohup python3 video_recorder.py > /dev/null 2>&1 &
