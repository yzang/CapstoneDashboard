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


def getCrashByVehicleAndAge(request):
    json_data={}
    years=dao.getAllYears()
    print years
    total_age_data=dao.getPersonAge()
    total_vehicle_data=getVehicleType()
    age_ranges=total_age_data.keys()
    age_ranges.sort(key=lambda x:x[0])
    person_types=dao.getAllPersonTypes()
    max1,max2=0,0
    # put series for each year
    print person_types
    print total_age_data
    for year in years:
        series=[]
        age_data=dao.getPersonAge(year)
        vehicle_data=getVehicleType(year)
        for person_type in person_types:
            data=[]
            for age_range in age_ranges:
                count=age_data.get(age_range,{}).get(person_type,0)
                max1=max(max1,count)
                data.append({"name":age_range,"value":count})
            series.append({'data':data})
        series.append({'data':vehicle_data})
        json_data[year]=series
    total_series=[]
    # put series for total crash
    for person_type in person_types:
        data=[]
        for age_range in age_ranges:
            count=total_age_data.get(age_range,{}).get(person_type,0)
            max2=max(max2,count)
            data.append({"name":age_range,"value":count})
        total_series.append({'data':data})
    total_series.append({'data':total_vehicle_data})
    # build into final json data
    json_data['years']=years
    json_data['age_ranges']=age_ranges
    json_data['person_types']=person_types
    json_data['max']=[max1,max2]
    json_data['total']=total_series
    return HttpResponse(json.dumps(json_data))



def getVehicleType(year=-1):
    dataset=dao.getVehicleType(year)
    data=[]
    total=0.0
    for item in dataset:
        total+=item['type__count']
    other_total=0
    for item in dataset:
        count=item['type__count']
        type=item['type']
        if count/total<0.01:
            other_total+=count
        else:
            vehicle={}
            vehicle['name']=type
            vehicle['value']=count
            data.append(vehicle)
    data.append({'name':'others','value':other_total})
    return data



def buildSerie(legend, data):
    serie = {'legend': legend,
             'max': max(data),
             'data': data}
    return serie

