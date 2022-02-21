
from __future__ import print_function
import os
from pymavlink import mavutil
from argparse import ArgumentParser
parser = ArgumentParser(description=__doc__)

## Please note UID2 requires you are using Mavlink 2

# os.environ["MAVLINK20"] = "1"
# export MAVLINK20=1

parser.add_argument("--baudrate", type=int,
                  help="master port baud rate", default=115200)
parser.add_argument("--device", default='tcp:127.0.0.1:5762',help="SITL")
parser.add_argument("--source-system", dest='SOURCE_SYSTEM', type=int,
                  default=1, help='MAVLink source system for this GCS')
args = parser.parse_args()


master = mavutil.mavlink_connection(args.device, baud=args.baudrate, source_system=args.SOURCE_SYSTEM)

## TODO: Actual code to get Public Key
with open('upload_tests/mavlink_upload.json', 'rb') as f:
    payload = f.read()
    # print("Supports ftp for file transfers: %s" % master.capabilities.ftp)
    master.mav.file_transfer_protocol_send(0,master.target_system, master.target_component, payload)
master.close()