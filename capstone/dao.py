# put all the queries here
from capstone.models import *
from django.db.models import Q, Sum, Count



def getFilteredCrash(year_range, month_range, day_range, hour_range, injuries, collision_types):
    crash = Crash.objects
    if year_range:
        crash = crash.filter(year__gte=year_range[0], year__lte=year_range[1])
    if month_range:
        crash = crash.filter(month__gte=month_range[0], month__lte=month_range[1])
    if day_range:
        crash = crash.filter(day__gte=day_range[0], day__lte=day_range[1])
    if hour_range:
        crash = crash.filter(hour__gte=hour_range[0], hour__lte=hour_range[1])
    if injuries:
        crash = crash.filter(max_severity_level__in=injuries)
    if collision_types:
        crash = crash.filter(collision_type__in=collision_types)
    return crash


def getCrashByYearRange(year_from, year_to):
    crash_list = Crash.objects.filter(year__gte=year_from, year__lte=year_to)
    return crash_list


def getMajFatalCrash():
    crash_list = Crash.objects.filter(max_severity_level__in=['Killed', 'Major injury', 'Minor injury'])
    return crash_list


## 1st chart - collision type
def getCrashByCollisionType():
    crashes = Crash.objects
    crash_list = crashes.values('collision_type').annotate(Count('collision_type'))
    fatal_list = crashes.filter(max_severity_level__in=['Killed', 'Major injury']).values('collision_type').annotate(
        Count('collision_type'))
    return crash_list, fatal_list


##  2nd - severity level, intercept_type view
def getSeverityAndInterception():
    fatal_count_list = Crash.objects.values('intersect_type').annotate(Sum('fatal_count'))
    mcycle_death_count_list = Crash.objects.values('intersect_type').annotate(Sum('mcycle_death_count'))
    bicycle_death_count_list = Crash.objects.values('intersect_type').annotate(Sum('bicycle_death_count'))
    ped_death_count_list = Crash.objects.values('intersect_type').annotate(Sum('ped_death_count'))
    intersection = {'fatal_count': fatal_count_list, 'mcycle_death_count': mcycle_death_count_list,
                    'bicycle_death_count': bicycle_death_count_list, 'ped_death_count': ped_death_count_list}
    return intersection


##  4 th chart from Gokul - monthly view
def getMonthlySeverity():
    crash_list = Crash.objects.values('year', 'month').order_by().annotate(Sum('mcycle_death_count'),
                                                                           Sum('bicycle_death_count'),
                                                                           Sum('ped_death_count'),
                                                                           Count('crn'))
    return crash_list


def getVehicleType(year=-1):
    vehicles=Vehicle.objects
    if year>0:
        vehicles=vehicles.filter(year=year)
    vehicle_list = vehicles.values('type').order_by().annotate(Count('type'))
    return vehicle_list


def getPersonAge(year=-1):
    person_objects=Person.objects
    if year>0:
        person_objects=person_objects.filter(year=year)
    person_list={}
    step=10
    for i in range(0,60,step):
        if i!=0:
            start=i+1
        else:
            start=i
        end=i+step
        items=person_objects.filter(age__gte=start,age__lte=end).values('person_type').order_by().annotate(Count('person_type'))
        entry={}
        for item in items:
            entry[item['person_type']]=item['person_type__count']
        person_list[str(start)+'-'+str(end)]=entry
    entry={}
    items=person_objects.filter(age__gte=61).values('person_type').order_by().annotate(Count('person_type'))
    for item in items:
        entry[item['person_type']]=item['person_type__count']
    person_list['>60']=entry
    return person_list

def getAllYears():
    years_data=Crash.objects.values('year').distinct()
    years=map(lambda x:x['year'],years_data)
    return years

def getAllPersonTypes():
    person_type_data=Person.objects.values('person_type').distinct().order_by()
    person_types=map(lambda x:x['person_type'],person_type_data)
    return person_types
