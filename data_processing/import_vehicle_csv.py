import csv
import json
import os, sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneDashboard.settings'

if __name__ == '__main__':
    application = get_wsgi_application()
    from capstone.models import *
    with open("./vehicle.csv", "rb") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        vehicle_list = []
        for row in reader:
            if not row or len(row) < 5:
                continue
            crn, year, type, x, y = row
            vehicle=Vehicle(crn=crn,year=year,type=type,X=x,Y=y)
            vehicle_list.append(vehicle)
            print row
        Vehicle.objects.bulk_create(vehicle_list)
    print "Load data complete"
