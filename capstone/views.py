from django.http import HttpResponse, QueryDict
from django.shortcuts import render
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from capstone import dao


def home(request):
    return render(request, 'crash_report.html', {})


def upload(request):
    return render(request, 'uploader.html', {})


@csrf_exempt
def getMajorFatal(request):
    query_dict = request.POST
    params = dict(query_dict.iterlists())
    crashes = dao.getMajFatalCrash(params);
    list = []
    for crash in crashes:
        data = {}
        data['lat'] = crash.lat
        data['lng'] = crash.lng
        data['crn'] = crash.crn
        list.append(data)
    return HttpResponse(json.dumps(list))


@csrf_exempt
def getCrashByCollisionType(request):
    query_dict = request.POST
    params = dict(query_dict.iterlists())
    dataset = dao.getCrashByCollisionType(params)
    labels = []
    total_crash = []
    json_data = {}
    series = []
    severe=[]
    automobile=[]
    pedestrian=[]
    motorcycle=[]
    bicycle=[]
    for item in dataset:
        labels.append(item['collision_type'])
        total_crash.append(item.get('crash_count',0))
        severe.append(item.get('severe',0))
        automobile.append(item.get('automobile',0))
        pedestrian.append(item.get('pedestrian',0))
        motorcycle.append(item.get('motorcycle',0))
        bicycle.append(item.get('bicycle',0))
    series.append(buildSerie('crash', total_crash))
    series.append(buildSerie('severe', severe))
    series.append(buildSerie('automobile', automobile))
    series.append(buildSerie('pedestrian', pedestrian))
    series.append(buildSerie('motorcycle', motorcycle))
    series.append(buildSerie('bicycle', bicycle))
    json_data['labels'] = labels
    json_data['series'] = series
    return HttpResponse(json.dumps(json_data))


@csrf_exempt
def getCrashByIntersectionType(request):
    query_dict = request.POST
    params = dict(query_dict.iterlists())
    dataset = dao.getSeverityAndInterception(params)
    labels = []
    total_crash = []
    json_data = {}
    series = []
    severe=[]
    automobile=[]
    pedestrian=[]
    motorcycle=[]
    bicycle=[]
    for item in dataset:
        labels.append(item['intersect_type'])
        total_crash.append(item.get('crash_count',0))
        severe.append(item.get('severe',0))
        automobile.append(item.get('automobile',0))
        pedestrian.append(item.get('pedestrian',0))
        motorcycle.append(item.get('motorcycle',0))
        bicycle.append(item.get('bicycle',0))
    series.append(buildSerie('crash', total_crash))
    series.append(buildSerie('severe', severe))
    series.append(buildSerie('automobile', automobile))
    series.append(buildSerie('pedestrian', pedestrian))
    series.append(buildSerie('motorcycle', motorcycle))
    series.append(buildSerie('bicycle', bicycle))
    json_data['labels'] = labels
    json_data['series'] = series
    return HttpResponse(json.dumps(json_data))


@csrf_exempt
def getCrashSeverityByMonth(request):
    json_data = {}
    labels = []
    series = []
    crn_data = []
    ped_data = []
    motor_data = []
    bicycle_data = []
    query_dict = request.POST
    params = dict(query_dict.iterlists())
    dataset = dao.getMonthlySeverity(params)
    for item in dataset:
        labels.append(str(item['year']) + '/' + str(item['month']))
        crn_data.append(item['crn__count'])
        ped_data.append(item['ped_death_count__sum'])
        motor_data.append(item['mcycle_death_count__sum'])
        bicycle_data.append(item['bicycle_death_count__sum'])
    series.append(buildSerie('total crash', crn_data))
    series.append(buildSerie('pedestrian death', ped_data))
    series.append(buildSerie('motorcycle death', motor_data))
    series.append(buildSerie('bicycle death', bicycle_data))
    json_data['labels'] = labels
    json_data['series'] = series
    return HttpResponse(json.dumps(json_data))


def getCrashByVehicleAndAge(request):
    json_data = {}
    years = dao.getAllYears()
    total_age_data = dao.getPersonAge()
    total_vehicle_data = getVehicleType()
    age_ranges = total_age_data.keys()
    age_ranges.sort(key=lambda x: x[0])
    person_types = dao.getAllPersonTypes()
    max1, max2 = 0, 0
    # put series for each year
    for year in years:
        series = []
        age_data = dao.getPersonAge(year)
        vehicle_data = getVehicleType(year)
        for person_type in person_types:
            data = []
            for age_range in age_ranges:
                count = age_data.get(age_range, {}).get(person_type, 0)
                max1 = max(max1, count)
                data.append({"name": age_range, "value": count})
            series.append({'data': data})
        series.append({'data': vehicle_data})
        json_data[year] = series
    total_series = []
    # put series for total crash
    for person_type in person_types:
        data = []
        for age_range in age_ranges:
            count = total_age_data.get(age_range, {}).get(person_type, 0)
            max2 = max(max2, count)
            data.append({"name": age_range, "value": count})
        total_series.append({'data': data})
    total_series.append({'data': total_vehicle_data})
    # build into final json data
    json_data['years'] = years
    json_data['age_ranges'] = age_ranges
    json_data['person_types'] = person_types
    json_data['max'] = [max1, max2]
    json_data['total'] = total_series
    return HttpResponse(json.dumps(json_data))


def getVehicleType(year=-1):
    dataset = dao.getVehicleType(year)
    data = []
    total = 0.0
    for item in dataset:
        total += item['type__count']
    other_total = 0
    for item in dataset:
        count = item['type__count']
        type = item['type']
        if count / total < 0.01:
            other_total += count
        else:
            vehicle = {}
            vehicle['name'] = type
            vehicle['value'] = count
            data.append(vehicle)
    data.append({'name': 'others', 'value': other_total})
    return data


def buildSerie(legend, data):
    if not data:
        return {
            'legend': legend,
            'max': 0,
            'data': []
        }
    return {'legend': legend,
            'max': max(data),
            'data': data}
