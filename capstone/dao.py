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


def getVehicleType():
    vehicle_list = Vehicle.objects.values('type').order_by().annotate(Count('type'))
    return vehicle_list


##  5th chart from Gokul - age
def getPersonAge():
    teen = Person.objects.filter(age__gte=0, age__lte=18).values('person_type').order_by().annotate(
            Count('person_type'))
    yong = Person.objects.filter(age__gte=19, age__lte=40).values('person_type').order_by().annotate(
            Count('person_type'))
    middle = Person.objects.filter(age__gte=41, age__lte=60).values('person_type').order_by().annotate(
            Count('person_type'))
    old = Person.objects.filter(age__gte=61, age__lte=99).values('person_type').order_by().annotate(
            Count('person_type'))
    person_list = [('teen', teen), ('yong', yong), ('middle', middle), ('old', old)]
    return person_list


'''
#Q poster. where are crash with major severity happens?
def getMajCrash(year):
    crash_list=Crash.objects.filter(year=year,maj_inj_count>0)
    return crash_list

#Q1.Where are pedestrians being hit?    
def getPedestrianHit(year):
    crash_list=Crash.objects.filter(year=year,ped_count>0)
    return crash_list
    
#Q2.Where are pedestrians being killed?
def getPedestrianKilled(year):
    crash_list=Crash.objects.filter(year=year,ped_death_count>0)
    return crash_list

#Q3.Where are bicyclists being hit?
def getBicyclistHit(year):
    crash_list=Crash.objects.filter(year=year,bicycle_count>0)
    return crash_list

#Q4.Where are bicyclists being killed?
def getBicyclistKilled(year):
    crash_list=Crash.objects.filter(year=year,bicycle_death_count>0)
    return crash_list
    
#Q5.How many [cars, bikes, motorcyles, pedestrians] crashed on this particular segment in a particular year?
def getBicyclistKilled(year):
    crash_list[0]=Crash.objects.filter(year=year,intersect_type=0).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[1]=Crash.objects.filter(year=year,intersect_type=1).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[2]=Crash.objects.filter(year=year,intersect_type=2).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[3]=Crash.objects.filter(year=year,intersect_type=3).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[4]=Crash.objects.filter(year=year,intersect_type=4).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[5]=Crash.objects.filter(year=year,intersect_type=5).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[6]=Crash.objects.filter(year=year,intersect_type=6).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[7]=Crash.objects.filter(year=year,intersect_type=7).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[8]=Crash.objects.filter(year=year,intersect_type=8).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))
    crash_list[9]=Crash.objects.filter(year=year,intersect_type=9).aggregate(Sum(automobile_count),Sum(bicycle_count),Sum(motorcycle_count),Sum(ped_count))

    return crash_list

#Q6 district data not loaded 

#Q7 What are the top 10 street segments for total crashes, pedestrian crashes, bicyclist crashes, and fatalities for each year?

#8 What are the ages of those involved in crashes?
def getCrashByAge(year):
    crash_list[0]=Crash.objects.filter(year=year,person_type=1).aggregate(Driver_age=Avg(age))
    crash_list[1]=Crash.objects.filter(year=year,person_type=2).aggregate(passenge_age=Avg(age))
    crash_list[3]=Crash.objects.filter(year=year,person_type=7).aggregate(pedestrian_age=Avg(age))
    return crash_list
#9 How many bicycle crashes happen on street segments with trolley tracks? NO shapefile for streets data

#10 What types of crashes are occurring along this particular segment? 
def getCrashByIntersect(year):
    crash_list[0]=Crash.objects.filter(year=year,intersect_type=0).aggregate(mid_block=Avg(age))
    crash_list[1]=Crash.objects.filter(year=year,intersect_type=1).aggregate(four_way=Avg(age))
    crash_list[2]=Crash.objects.filter(year=year,intersect_type=2).aggregate(t_intersection=Avg(age))
    crash_list[3]=Crash.objects.filter(year=year,intersect_type=3).aggregate(y_intersection=Avg(age))
    crash_list[4]=Crash.objects.filter(year=year,intersect_type=4).aggregate(traffic_circle=Avg(age))
    crash_list[5]=Crash.objects.filter(year=year,intersect_type=5).aggregate(multiple_leg=Avg(age))
    crash_list[6]=Crash.objects.filter(year=year,intersect_type=6).aggregate(on_ramp=Avg(age))
    crash_list[7]=Crash.objects.filter(year=year,intersect_type=7).aggregate(off_ramp=Avg(age))
    crash_list[8]=Crash.objects.filter(year=year,intersect_type=8).aggregate(cross_over=Avg(age))
    crash_list[9]=Crash.objects.filter(year=year,intersect_type=9).aggregate(railroad=Avg(age))
    return crash_list
'''
