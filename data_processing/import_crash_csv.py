import csv
import json
import os, sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneDashboard.settings'

def import_crash_csv(file):
    application = get_wsgi_application()
    from capstone.models import Crash
    file_name = os.path.join("data_processing/crash/",file)
    with open(file_name, "rU") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        crash_list = []
        for row in reader:
            if not row or len(row) < 34:
                continue
            crn, year, month, day, hour, intersect_type, collision_type, \
            automobile_count, motorcycle_count, bus_count, small_truck_count, \
            heavy_truck_count, suv_count, van_count, bicycle_count, fatal_count, \
            injury_count, maj_inj_count, sev_inj_count, mcycle_death_count, \
            mcycle_maj_inj_count, mcycle_sev_inj_count, bicycle_death_count, \
            bicycle_maj_inj_count, bicycle_sev_inj_count, ped_count, ped_death_count, \
            ped_maj_inj_count, ped_sev_inj_count, comm_veh_count, \
            max_severity_level, intersection, lat, lng = row
            crash=Crash(crn=crn,year=year,month=month,day=day,hour=hour,intersect_type=intersect_type,
                        collision_type=collision_type,automobile_count=automobile_count,motorcycle_count=motorcycle_count,
                        bus_count=bus_count,small_truck_count=small_truck_count,heavy_truck_count=heavy_truck_count,
                        suv_count=suv_count,van_count=van_count,bicycle_count=bicycle_count,fatal_count=fatal_count,
                        injury_count=injury_count,maj_inj_count=maj_inj_count,sev_inj_count=sev_inj_count,
                        mcycle_death_count=mcycle_death_count,mcycle_maj_inj_count=mcycle_maj_inj_count,
                        mcycle_sev_inj_count=mcycle_sev_inj_count,bicycle_death_count=bicycle_death_count,
                        bicycle_maj_inj_count=bicycle_maj_inj_count,bicycle_sev_inj_count=bicycle_sev_inj_count,
                        ped_count=ped_count,ped_death_count=ped_death_count,ped_maj_inj_count=ped_maj_inj_count,
                        ped_sev_inj_count=ped_sev_inj_count,comm_veh_count=comm_veh_count,
                        max_severity_level=max_severity_level,has_intersection=intersection,lat=lat,lng=lng)
            crash_list.append(crash)
            print row
        Crash.objects.bulk_create(crash_list)
    print "Load data complete"
