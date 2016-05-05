# put all the queries here
from capstone.models import *
from django.db.models import Q, Sum, Count



def getFilteredCrash(params):
    crash = Crash.objects
    if params is None:
        return crash
    if params.get('year_from') and params.get('year_to'):
        crash = crash.filter(year__gte=params.get('year_from')[0], year__lte=params.get('year_to')[0])
    if params.get('month_from') and params.get('month_to'):
        crash = crash.filter(month__gte=params.get('month_from')[0], month__lte=params.get('month_to')[0])
    if params.get('day_from') and params.get('day_to'):
        crash = crash.filter(day__gte=params.get('day_from')[0], day__lte=params.get('day_to')[0])
    if params.get('hour_from') and params.get('hour_to'):
        crash = crash.filter(hour__gte=params.get('hour_from')[0], hour__lte=params.get('hour_to')[0])
    if params.get('injury_options[]') and params.get('injury_options[]')[0]:
        crash = crash.filter(max_severity_level__in=params.get('injury_options[]'))
    if params.get('collision_options[]') and params.get('collision_options[]')[0]:
        crash = crash.filter(collision_type__in=params.get('collision_options[]'))
    return crash


def getMajFatalCrash(params=None):
    crash_data=getFilteredCrash(params)
    return crash_data


## 1st chart - collision type
def getCrashByCollisionType(params=None):
    crash_data=getFilteredCrash(params)
    dataset = crash_data.values('collision_type').\
        order_by('collision_type').annotate(crash_count=Count('crn'),
                                            severe=Sum('sev_inj_count'),
                                            automobile=Sum('fatal_count')-Sum('mcycle_death_count')-Sum('bicycle_death_count')-Sum('ped_death_count'),
                                            pedestrian=Sum('ped_death_count'),
                                            motorcycle=Sum('mcycle_death_count'),
                                            bicycle=Sum('bicycle_death_count'))
    return dataset


##  2nd - severity level, intercept_type view
def getSeverityAndInterception(params=None):
    crash_data=getFilteredCrash(params)
    dataset= crash_data.values('intersect_type').annotate(crash_count=Count('crn'),
                                                              severe=Sum('sev_inj_count'),
                                                              automobile=Sum('fatal_count')-Sum('mcycle_death_count')-Sum('bicycle_death_count')-Sum('ped_death_count'),
                                                              pedestrian=Sum('ped_death_count'),
                                                              motorcycle=Sum('mcycle_death_count'),
                                                              bicycle=Sum('bicycle_death_count'))
    return dataset


##  4 th chart from Gokul - monthly view
def getMonthlySeverity(params=None):
    crash_data=getFilteredCrash(params)
    crash_list = crash_data.values('year', 'month').order_by().annotate(crash_count=Count('crn'),
                                                                        severe=Sum('sev_inj_count'),
                                                                        automobile=Sum('fatal_count')-Sum('mcycle_death_count')-Sum('bicycle_death_count')-Sum('ped_death_count'),
                                                                        motorcycle=Sum('mcycle_death_count'),
                                                                        bicycle=Sum('bicycle_death_count'),
                                                                        pedestrian=Sum('ped_death_count'))
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
    years.sort()
    return years

def getAllPersonTypes():
    person_type_data=Person.objects.values('person_type').distinct().order_by()
    person_types=map(lambda x:x['person_type'],person_type_data)
    return person_types

def getAllCollisionTypes():
    collision_types=Crash.objects.values('collision_type').distinct().order_by()
    collision_types=map(lambda x:x['collision_type'],collision_types)
    return collision_types