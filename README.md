# Crash analysis dashboard
Crash data dashboard developed by Carnegie Melon University

## Data model

### Person
- crn/Integer
- year/Integer
- sex/Character(30)
- age/Integer
- person\_type/Character(30)
- restraint\_helmet/Character(30)

### Vehicle
- crn/Integer
- year/Integer
- type/Character(30)

### Crash
- crn/Integer
- year/Integer
- month/Integer
- day/Integer
- hour/Integer
- intersect\_type/Character(30)
- collision\_type/Character(30)
- automobile\_count/Integer
- motorcycle\_count/Integer
- bus\_count/Integer
- small\_truck\_count/Integer
- heavy\_truck\_count/Integer
- suv\_count/Integer
- van\_count/Integer
- bicycle\_count/Integer
- fatal\_count/Integer
- injury\_count/Integer
- maj\_inj\_count/Integer
- sev\_inj\_count/Integer
- mcycle\_death\_count/Integer
- mcycle\_maj\_inj\_count/Integer
- mcycle\_sev\_inj\_count/Integer
- bicycle\_death\_count/Integer
- bicycle\_maj\_inj\_count/Integer
- bicycle\_sev\_inj\_count/Integer
- ped\_count/Integer
- ped\_death\_count/Integer
- ped\_maj\_inj\_count/Integer
- ped\_sev\_inj\_count/Integer
- comm\_veh\_count/Integer
- max\_severity\_level/Char(max\_length=30)
- has\_intersection/CharField(max\_length=10)
- lat/Float
- lng/Float

## Data upload/clear history

![screenshot](http://i.imgur.com/3pZFAff.png)

From home page, click on Data Management - upload crash or upload vehicle or upload person, choose csv file then click on upload, data will be appended, and front end will be refreshed.

If for any reason, user would like to clear history data and reload all data, one can choose clear history, all data loaded before will be cleared.

## Deployment Plan

### Infrastructure

Launch an EC2 instance with Ubuntu 14.04.

Instance Type: any type

Storage: at least 10 GB

Allow port 80/433 for security groups

### Environment

Install apache2:

`sudo apt-get install apache2`

Install pip:

`sudo apt-get install pip`

Install django:

`pip install Django==1.9.6`

### Code Deployment

Download or clone the code from github: <https://github.com/zym242/CapstoneDashboard>

Configure the apache server for django:

[*https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/modwsgi/*](https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/modwsgi/)

## Development

To run this app locally with Python 3:

```
git clone https://github.com/CityOfPhiladelphia/crash-analysis-dashboard
cd crash-analysis-dashboard
python -m venv venv
source ./env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Running `runserver` will create an empty SQLite database in the same directory called `db.sqlite3`. Stop the server and create all tables with `python manage.py migrate`.

Next, you'll need to populate the database. There are three CSV files in `data_processing/` which you can use for testing:

* crash_clean.csv
* person_clean.csv
* vehicle_clean.csv

Start the server again, navigate to `http://localhost:8000`, and load the data using the import tools in the main menu.
