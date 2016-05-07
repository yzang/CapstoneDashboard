import csv
import json
import os, sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneDashboard.settings'

def import_person_csv(file):
    application = get_wsgi_application()
    from capstone.models import Person
    file_name = os.path.join("data_processing/person/", file)
    with open(file_name, "rb") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        person_list=[]
        for row in reader:
            if not row:
                continue
            crn,year,sex,age,person_type,helmet=row
            person=Person(crn=crn,year=year,sex=sex,age=age,person_type=person_type,restraint_helmet=helmet)
            person_list.append(person)
            print row
        Person.objects.bulk_create(person_list)
    print "Load data complete"
