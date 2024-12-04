from vehicle import *
from pymavlink import mavutil


def set_roi(location):
    """
    Send MAV_CMD_DO_SET_ROI message to point camera gimbal at a
    specified region of interest (LocationGlobal).
    The vehicle may also turn to face the ROI.

    For more information see:
    http://copter.ardupilot.com/common-mavlink-mission-command-messages-mav_cmd/#mav_cmd_do_set_roi
    """
    # create the MAV_CMD_DO_SET_ROI command
    msg = vehicle.message_factory.command_long_encode(
        0, 0,  # target system, target component
        mavutil.mavlink.MAV_CMD_DO_SET_ROI,  # command
        0,  # confirmation
        0, 0, 0, 0,  # params 1-4
        location.lat,
        location.lon,
        location.alt
    )
    # send command to vehicle
    vehicle.send_mavlink(msg)
