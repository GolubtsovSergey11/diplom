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

TOKEN = '92109221aca3be40097356391136dfb27b712e35561537bc4ffbd5b6349b0d1921a43be2abc63c52c3f8e'

#Получаем список групп
id_user = int(input('Введите id пользователя: '))
params_groups = {'user_id': id_user, 'access_token': TOKEN, 'extended': 1, 'v': 5.89}
response = requests.get('https://api.vk.com/method/groups.get', params_groups)
#print(response.json())
response = response.json()['response']
print(response)
groups_id = []
for ids in response['items']:
    string = 'https://vk.com/'
    groups_id.append(ids['id'])
    print(ids)

without_friends = []

for ids in groups_id:
    time.sleep(0.4)
    Params = {'group_id': ids, 'access_token': TOKEN, 'filter': 'friends', 'v': 5.89}
    res = requests.get('https://api.vk.com/method/groups.getMembers', Params)
    res = res.json()
    #print(res)
    try:
        if res['response']['count'] == 0:
            print(res)
            print(ids)
            without_friends.append(ids)
        else:
            continue
    except KeyError as KE:
        print(KE)
output_dict = []
without_friends = set(without_friends)
for i in response['items']:
    if i['id'] in without_friends:
        output_dict_1 = {}
        output_dict_1['name_group'] = i['name']
        output_dict_1['id_group'] = i['id']
        output_dict.append(output_dict_1)

with open('test.json', 'w', encoding='utf-8') as file:
    json.dump(output_dict, file, ensure_ascii=False, indent=2)