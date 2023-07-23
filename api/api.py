import time
import requests
import json
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/get-col-data')
def get_colombia_data():
    response_api = requests.get('https://api.hungermapdata.org/v1/foodsecurity/country/COL/region?date_start=2023-06-01&date_end=2023-07-01')
    print("Response api code: ", response_api.status_code)
    api_data = response_api.text
    json_data = json.loads(api_data)

    # for data in json_data['data']['memes']:
    #     id.append(data['id'])
    #     names.append(data['name'])
    #     urls.append(data['url'])
         
    print("json_data: ", json_data)
    return json_data

@app.route('/get-bfa-metric-a')
def get_burkinafaso_metric_a():    
    response_api = requests.get('https://api.hungermapdata.org/v1/foodsecurity/country/BFA/region?date_start=2022-06-01&date_end=2023-07-01')

    print("Response api code: ", response_api.status_code)
    api_data = response_api.text
    json_data = json.loads(api_data)

    response_data = [{}]

    for item in json_data:
        # average monthly for region
        dateTimeObj = datetime.strptime(item['date'], "%Y-%m-%d")
        print ("dateTimeObj", dateTimeObj)
        if item['region']['id'] in response_data_item:
            response_data_item = {}
            response_data_item['region']['id']=item['region']['id']
            response_data_item['region']['name']=item['region']['name']
            response_data_item['year']=dateTimeObj.year
            response_data_item['month']=dateTimeObj.month
            response_data_item['average_fcs_people']=(response_data_item['average_fcs_people']+item['metrics']['fcs']['people'])/2
            response_data_item['average_fcs_prevalence']=(response_data_item['average_fcs_prevalence']+item['metrics']['fcs']['prevalence'])/2
        else:
            response_data_item = {}
            response_data_item['region']['id']=item['region']['id']
            response_data_item['region']['name']=item['region']['name']
            response_data_item['year']=dateTimeObj.year
            response_data_item['month']=dateTimeObj.month
            response_data_item['average_fcs_people']=item['metrics']['fcs']['people']
            response_data_item['average_fcs_prevalence']=item['metrics']['fcs']['prevalence']

        response_data.append(response_data_item)

    return json.dumps(response_data)

@app.route('/get-col-metric-a')
def get_colombia_metric_a():
    response_api = requests.get('https://api.hungermapdata.org/v1/foodsecurity/country/COL/region?date_start=2022-06-01&date_end=2023-07-01')

    print("Response api code: ", response_api.status_code)
    api_data = response_api.text
    json_data = json.loads(api_data)

    response_data = [{}]

    for item in json_data:
        # average monthly for region
        dateTimeObj = datetime.strptime(item['date'], "%Y-%m-%d")
        print ("dateTimeObj", dateTimeObj)
        if item['region']['id'] in response_data_item:
            response_data_item = {}
            response_data_item['region']['id']=item['region']['id']
            response_data_item['region']['name']=item['region']['name']
            response_data_item['year']=dateTimeObj.year
            response_data_item['month']=dateTimeObj.month
            response_data_item['average_fcs_people']=(response_data_item['average_fcs_people']+item['metrics']['fcs']['people'])/2
            response_data_item['average_fcs_prevalence']=(response_data_item['average_fcs_prevalence']+item['metrics']['fcs']['prevalence'])/2
        else:
            response_data_item = {}
            response_data_item['region']['id']=item['region']['id']
            response_data_item['region']['name']=item['region']['name']
            response_data_item['year']=dateTimeObj.year
            response_data_item['month']=dateTimeObj.month
            response_data_item['average_fcs_people']=item['metrics']['fcs']['people']
            response_data_item['average_fcs_prevalence']=item['metrics']['fcs']['prevalence']

        response_data.append(response_data_item)

    return json.dumps(response_data)