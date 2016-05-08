import csv
import json
import os, sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneDashboard.settings'

def import_vehicle_csv(file):
    application = get_wsgi_application()
    from capstone.models import Vehicle
    file_name = os.path.join("data_processing/vehicle/", file)
    with open(file_name, "rb") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        vehicle_list = []
        for row in reader:
            if not row or len(row) < 3:
                continue
            crn, year, type = row
            vehicle=Vehicle(crn=crn,year=year,type=type)
            vehicle_list.append(vehicle)
            print row
        Vehicle.objects.bulk_create(vehicle_list)
    print "Load data complete"
