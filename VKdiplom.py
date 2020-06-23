import requests
from urllib.parse import urlencode
import time
import json

OAUTH = 'https://oauth.vk.com/authorize'
params_dict = {
    'client_id': 7516850,
    'display_page': 'page',
    'scope': 'friends, groups',
    'response_type': 'token',
    'v' : 5.89}

URL_to_get_token = ('?'.join((OAUTH, urlencode(params_dict))))
print(URL_to_get_token)

TOKEN = '8979bcdfa9dff35611eb3adc56a2ddc371e9c83134b509b498c120a16e2378ebc4d7de68bd6e15f9f4acb'

#Получаем список групп
params_groups = {'user_id': 19451240, 'access_token': TOKEN, 'extended': 1, 'v': 5.89}
response = requests.get('https://api.vk.com/method/groups.get', params_groups)
print(response.json()['response']['items'])
response = response.json()['response']
print(response)
groups_id = []
for ids in response['items']:
    string = 'https://vk.com/'
    groups_id.append(ids['id'])
print(groups_id)

output_dict = {}

for ids in groups_id:
    time.sleep(0.4)
    Params = {'group_id': ids, 'access_token': TOKEN, 'filter': 'friends', 'v': 5.89}
    res = requests.get('https://api.vk.com/method/groups.getMembers', Params)
    res = res.json()
    try:
        if res['response']['count'] != 0:
            #print(ids)
            print(res)
            for name in response['items']:
                output_dict['name_group'] = name['name']
                output_dict['id_group'] = name['id']
                output_dict['members_count'] = res['response']['count']

        else:
            continue
    except KeyError as KE:
        print(KE)

print(output_dict)

with open('test.json', 'w', encoding='utf-8') as file:
    json.dump(output_dict, file, ensure_ascii=False, indent=2)
