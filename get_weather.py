#!/usr/bin/env python

import requests


# example:
# http://api.wunderground.com/api/455e4a0034eb74d2/conditions/q/WA/Seattle.json



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
    result = {}
    result['current_temp'] = data['current_observation']['temperature_string']
    result['weather'] = data['current_observation']['weather']
    result['city'] = data['current_observation']['display_location']['city']
    result['state'] = data['current_observation']['display_location']['state']
    result['icon'] = data['current_observation']['icon']
    return result


if __name__ == "__main__":
    data = get_weather("WA", "Seattle")

    #print()
    #print('Seattle current weather:')
    print(get_current_conditions())
