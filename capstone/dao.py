#put all the queries here
from capstone.models import Crash


def getCrashByYear(year):
    crash_list=Crash.objects.filter(year=year)
    return crash_list

def getCrashByYearRange(year_from,year_to):
    crash_list=Crash.objects.filter(year__gte=year_from,year__lte=year_to)
    return crash_list