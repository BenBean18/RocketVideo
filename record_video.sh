#!/bin/bash
# Note: stream.ts should be a named pipe, run `mkfifo stream.ts` to create it
cd /home/rocket/RocketVideo
#sudo nohup ./rpidatv/bin/rpidatv -i stream.ts -s 600 -c 1/2 -m RF -f 423 -p 7 > /dev/null 2>&1 &
nohup python3 record_only.py > /dev/null 2>&1 &
