from get_location_metres import *
from get_distance_metres import *
from vehicle import *
from arm_and_takeoff import *
from goto_position_target_body_ned import *
from goto_position_target_body_offset_ned import *
from goto_position_target_local_offset_ned import *
from goto_position_target_local_ned import *
import time
from dronekit import VehicleMode

arm_and_takeoff(10)
#vehicle.play_tune("AAAA")


aLocation1 = LocationGlobalRelative(-35.36317521, 149.16524649)
aLocation2 = LocationGlobalRelative(-35.36326500, 149.16524715)
a = get_distance_metres(aLocation1, aLocation2)
print(a)