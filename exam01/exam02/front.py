
import os
import requests
import json

temp = {
  'receiver'  : '팀장' ,
  'purpose'   : '프로젝트 수행에 일정에 문제가 없는지 확인' , 
  'tone'      : '친절하고 젠틀함' , 
  'more_info' : '프로젝트가 언제 끝날지 확인해 주기 바래' 
}

url = 'http://localhost:5000/api/text'

headers = {'Content-Type':'application/json; charset=utf-8'}

print('body : ' , temp)

datas = json.dumps(temp)

response = requests.post(url, headers=headers, data=datas)

if response.status_code == 200 :
    print(json.loads(response.text))
else :
    print(json.loads(response.text))
