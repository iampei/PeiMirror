#!/usr/bin/env python

import requests


# example:
# http://api.wunderground.com/api/455e4a0034eb74d2/conditions/q/WA/Seattle.json

key = "da30a9e85a98e5d8"

url_template = "http://api.wunderground.com/api/{key}/conditions/q/{state}/{city}.json"


def get_weather(state, city):
    url = url_template.format(key=key, state=state, city=city)
    r = requests.get(url)
    # print(r.headers['content-type'])
    data = r.json()
    # print(data)
    return data


def get_current_conditions():
    data = get_weather("WA", "Seattle")
    result = 'Current Temp: ' + data['current_observation']['temperature_string']+ '\nWeather: ' + data['current_observation']['weather']
    #result = {}
    # result['current_temp'] = data['current_observation']['temperature_string']
    # result['wind_speed'] = data['current_observation']['wind_mph']
    # result['weather'] = data['current_observation']['weather']
    return result


if __name__ == "__main__":
    data = get_weather("WA", "Seattle")

    #print()
    #print('Seattle current weather:')
    #print(get_current_conditions())