from operator import itemgetter
import requests
from plotly.graph_objs import Bar 
from plotly import offline

#Создание вызова API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r= requests.get(url)
print(f"Status code: {r.status_code}")

#Обработка информации о кажой статье
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #Создание отдельного вызова API для каждой статьи 
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus code: {r.status_code}")
    response_dict = r.json()

    #Построение словаря для каждой статьи.
    try:
            comment = int(response_dict['descendants'])
    except KeyError:
            comment = 0
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"<a href='http://news.ycombinator.com/item?id={submission_id}'></a>",
        'comments': comment,
    }
    submission_dicts.append(submission_dict)

#submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
#                reverse=True)

links = [submission_dict['hn_link'] for submission_dict in submission_dicts]
comments = [submission_dict['comments'] for submission_dict in submission_dicts]
titles = [submission_dict['title'] for submission_dict in submission_dicts]
#Визуализация
data = [{
    'type': 'bar',
    'x':  titles,
    'y': comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Hacker News Top',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'titles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}, 
    },
    'yaxis': {
        'title': 'comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='C:/Users/Kceni/Desktop/personal_projects/math/api/hacker_news_top.html')