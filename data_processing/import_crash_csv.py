import csv
import json
import os, sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneDashboard.settings'


def import_crash_csv(dir,file):
    application = get_wsgi_application()
    from capstone.models import Crash
    file_name = os.path.join(dir, file)
    with open(file_name, "rU") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        crash_list = []
        for row in reader:
            if not row or len(row) < 20:
                continue
            crn, year, month, day, hour, intersect_type, collision_type, \
            fatal_count, injury_count, sev_inj_count,maj_inj_count, \
            mcycle_death_count, mcycle_sev_inj_count, \
            bicycle_death_count, bicycle_sev_inj_count, ped_death_count, \
            ignore, max_severity_level, lat, lng = row
            crash = Crash(crn=crn, year=year, month=month, day=day, hour=hour, intersect_type=intersect_type,
                          collision_type=collision_type, fatal_count=fatal_count, injury_count=injury_count,
                          sev_inj_count=sev_inj_count,maj_inj_count=maj_inj_count, mcycle_death_count=mcycle_death_count,
                          mcycle_sev_inj_count=mcycle_sev_inj_count,bicycle_death_count=bicycle_death_count, bicycle_sev_inj_count=bicycle_sev_inj_count,
                          ped_death_count=ped_death_count, max_severity_level=max_severity_level, lat=lat, lng=lng)
            crash_list.append(crash)
            print row
        Crash.objects.bulk_create(crash_list)
    print "Load data complete"

if __name__=='__main__':
    import_crash_csv('crash/','crash_clean.csv')