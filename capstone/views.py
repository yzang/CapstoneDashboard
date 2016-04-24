from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from capstone import dao


def home(request):
    return render(request, 'crash_report.html', {})


def upload(request):
    return render(request, 'uploader.html', {})


def getMajorFatal(request):
    crashes = dao.getMajFatalCrash();
    list = []
    for crash in crashes:
        data = {}
        data['lat'] = crash.lat
        data['lng'] = crash.lng
        data['crn'] = crash.crn
        list.append(data)
    return HttpResponse(json.dumps(list))


def getCrashByCollisionType(request):
    crashes, fatal_crashes = dao.getCrashByCollisionType()
    labels = []
    label_dict = {}
    total_data = []
    json_data = {}
    series = []
    for crash in crashes:
        label = crash['collision_type']
        label_dict[label] = len(labels)
        labels.append(label)
        total_data.append(crash['collision_type__count'])
    fatal_data = [0 for i in range(len(total_data))]
    for fatal in fatal_crashes:
        label = fatal['collision_type']
        index = label_dict.get(label)
        fatal_data[index] = fatal['collision_type__count']
    series.append(buildSerie('Total Count',total_data))
    series.append(buildSerie('Fatal Count',fatal_data))
    json_data['labels'] = labels
    json_data['series'] = series
    return HttpResponse(json.dumps(json_data))

# build the second chart
def getCrashByIntersectionType(request):
    json_data={}
    labels=[]
    series=[]
    all_data={}
    dataset=dao.getSeverityAndInterception()
    for key in dataset.keys():
        label_filled=len(labels)>0
        items=dataset.get(key)
        for item in items:
            if not label_filled:
                labels.append(item['intersect_type'])
            if not all_data.has_key(key):
                all_data[key]=[]
            all_data[key].append(item[key+'__sum'])
    for key in all_data.keys():
        series.append(buildSerie(key.replace('_',' '),all_data.get(key)))
        series.sort(key=lambda x:x.get('max'),reverse=True)
    json_data['labels']=labels
    json_data['series']=series
    return HttpResponse(json.dumps(json_data))

def getCrashSeverityByMonth(request):
    json_data={}
    labels=[]
    series=[]
    crn_data=[]
    ped_data=[]
    motor_data=[]
    bicycle_data=[]
    dataset=dao.getMonthlySeverity()
    for item in dataset:
        labels.append(str(item['year'])+'/'+str(item['month']))
        crn_data.append(item['crn__count'])
        ped_data.append(item['ped_death_count__sum'])
        motor_data.append(item['mcycle_death_count__sum'])
        bicycle_data.append(item['bicycle_death_count__sum'])
    series.append(buildSerie('total crash',crn_data))
    series.append(buildSerie('pedestrian death',ped_data))
    series.append(buildSerie('motorcycle death',motor_data))
    series.append(buildSerie('bicycle death',bicycle_data))
    json_data['labels']=labels
    json_data['series']=series
    return HttpResponse(json.dumps(json_data))


def buildSerie(legend, data):
    serie = {'legend': legend,
             'max': max(data),
             'data': data}
    return serie

