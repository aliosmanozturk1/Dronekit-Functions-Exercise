from vehicle import *
from pymavlink import mavutil
import time


def goto_position_target_global_int(aLocation):
    """
    Send SET_POSITION_TARGET_GLOBAL_INT command to request the vehicle fly to a specified location.
    """
    msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,  # time_boot_ms (not used)
        0, 0,  # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,  # frame
        0b0000111111111000,  # type_mask (only speeds enabled)
        aLocation.lat * 1e7,  # lat_int - X Position in WGS84 frame in 1e7 * meters
        aLocation.lon * 1e7,  # lon_int - Y Position in WGS84 frame in 1e7 * meters
        aLocation.alt,
        # alt - Altitude in meters in AMSL altitude, not WGS84 if absolute or relative, above terrain if GLOBAL_TERRAIN_ALT_INT
        0,  # X velocity in NED frame in m/s
        0,  # Y velocity in NED frame in m/s
        0,  # Z velocity in NED frame in m/s
        0, 0, 0,  # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    # send command to vehicle
    vehicle.send_mavlink(msg)
