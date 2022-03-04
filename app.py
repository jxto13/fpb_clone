from flask import Flask, render_template
from datetime import datetime, timedelta
import requests, json 

app = Flask(__name__)

def split_data(data):
    title = data['profile']['l10n'][0]['title']
    slug = data['profile']['l10n'][0]['slug']
    image = data['profile']['l10n'][0]['image']['baseUrl'] + '/' + data['profile']['l10n'][0]['image']['file']
    date = data['date']['publish']
    date = date[:-6]
    date = datetime.strptime(date,'%Y/%m/%d %H:%M:%S')
    date += timedelta(minutes=10)
    fase = data['playlists']['data'][0]['l10n'][0]['name']
    embedLink = data['embedLink']
    return [title,slug,image,date,fase,embedLink]


baseURL = "https://sky-video-api.global.ssl.fastly.net/1/channel/"
endURL = "lives?iso=pt&page=1&order=asc&order_by=position&ids=playlists,labels,profile,playlists,channels"

token = "token=1638670429_f7d796eafca3b84a9f2d5ebb81c9e08980fcc3b7_IGW1Ar7TbRE1UtQa_zlf7zt9xgeinydl7"
apikey = "apikey=IGW1Ar7TbRE1UtQa&apitoken=zlf7zt9xgeinydl7"

ligas = [["54","Liga Betclic"],
        ["50","Liga Betclic Feminina"],
        ["70","FIBA Europe Cup"],
        ["49","Pro Liga"],
        ["52","CN1 Masculina"],
        ["56","CN2 Masculina"]
        ]

for i in ligas:
    url = baseURL+i[0]+"/"+endURL+"&"+token+"&"+apikey
    response = requests.get(url)
    data = json.loads(response.text)
    data = data['data']

    tmp = []
    size = 0
    for j in data:
        tmp.append(split_data(j))
        size += 1
    i.append(size)
    i.append(tmp)

@app.route('/<some_place>')
def some_place_page(some_place):
    for i in ligas:
        for j in i[3]:
            if(j[1] == some_place):
                return render_template('video-page.html', data = i[3][0])

    
@app.route("/")
def hello_world():
    return render_template('template.html', data = ligas)