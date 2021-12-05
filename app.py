from flask import Flask, render_template
from string import Template
import requests, json 
app = Flask(__name__)

url = "https://sky-video-api.global.ssl.fastly.net/1/channel/54/lives?iso=pt&order=asc&order_by=position&ids=playlists,labels,profile,playlists,channels&token=1638670429_f7d796eafca3b84a9f2d5ebb81c9e08980fcc3b7_IGW1Ar7TbRE1UtQa_zlf7zt9xgeinydl7&apikey=IGW1Ar7TbRE1UtQa&apitoken=zlf7zt9xgeinydl7"

response = requests.get(url)
data = json.loads(response.text)
data = data['data']

def split_data(data):
    title = data['profile']['l10n'][0]['title']
    slug = data['profile']['l10n'][0]['slug']
    image = data['profile']['l10n'][0]['image']['baseUrl'] + '/' + data['profile']['l10n'][0]['image']['file']
    date = data['date']['begin']
    date = date[:-5]
    fase = data['playlists']['data'][0]['l10n'][0]['name']
    embedLink = data['embedLink']
    return [title,slug,image,date,fase,embedLink]

liga= []
for i in data:
    liga.append(split_data(i))

# liga feminina
url = "https://sky-video-api.global.ssl.fastly.net/1/channel/50/lives?iso=pt&page=1&per_page=15&order=asc&order_by=position&ids=playlists,labels,profile,playlists,channels&token=1638680261_6dcd05776d5e66a81b31eed83a5b1eac06cd6f65_IGW1Ar7TbRE1UtQa_zlf7zt9xgeinydl7&apikey=IGW1Ar7TbRE1UtQa&apitoken=zlf7zt9xgeinydl7"
response = requests.get(url)
data = json.loads(response.text)
data = data['data']

liga_feminina= []
for i in data:
    liga_feminina.append(split_data(i))

# cn2 mas
url = "https://sky-video-api.global.ssl.fastly.net/1/channel/56/lives?iso=pt&page=1&per_page=15&order=asc&order_by=position&ids=playlists,labels,profile,playlists,channels&token=1638680064_c9842f687430dd50aa2e17f4d32fa886e1afb341_IGW1Ar7TbRE1UtQa_zlf7zt9xgeinydl7&apikey=IGW1Ar7TbRE1UtQa&apitoken=zlf7zt9xgeinydl7"

response = requests.get(url)
data = json.loads(response.text)
data = data['data']

cn2_masc= []
for i in data:
    cn2_masc.append(split_data(i))


@app.route('/<some_place>')
def some_place_page(some_place):
    for i in liga:
        if(i[1] == some_place):
            return render_template('video-page.html', data = i)
    for i in liga_feminina:
        if(i[1] == some_place):
            return render_template('video-page.html', data = i)
    for i in cn2_masc:
        if(i[1] == some_place):
            return render_template('video-page.html', data = i)

@app.route("/")
def hello_world():
    return render_template('template.html', data_liga = liga, data_liga_feminina = liga_feminina, data_cn2_masc = cn2_masc)