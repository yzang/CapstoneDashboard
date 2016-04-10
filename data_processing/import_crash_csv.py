import csv
import json
import os, sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
Input: standard input with json format
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneDashboard.settings'

if __name__ == '__main__':
    application = get_wsgi_application()
    from capstone.models import *

    with open("CrashClean_final.csv", "rb") as infile:
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

            person = Person(crn=crn, year=year, sex=sex, age=age, person_type=person_type, restraint_helmet=helmet)
            crash_list.append(crash)
            print row
        Person.objects.bulk_create(person_list)
    print ":oad data complete"
