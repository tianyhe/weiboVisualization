from datetime import datetime, timedelta

from dateutil import relativedelta
import plotly.graph_objects as go
from plotly.graph_objs import Bar
from plotly import offline

from wb_data import Weibo

file_path = 'weibo/科勒United/readable_wb_data.json'
base_url = 'https://weibo.com/1676455960/'

wb = Weibo(file_path, base_url)

# # Testing the dictionary
# for i in range(0, 10):
#     print(f"pb_times: {wb.data['pb_times'][i]}")
#     print(f"wb_links: {wb.data['wb_links'][i]}")
#     print(f"up_nums: {wb.data['up_nums'][i]}")
#     print(f"retweet_nums: {wb.data['retweet_nums'][i]}")
#     print(f"comments_nums: {wb.data['comment_nums'][i]}")
#     print(f"labels: {wb.data['labels'][i]}\n")

# # Testing the graph function.
# start_date = datetime.strptime('2020-05-01', '%Y-%m-%d')
# end_date = datetime.strptime('2020-06-01', '%Y-%m-%d')
# wb.visual(start_date, end_date, "January, 2020")
# print(wb.start_index)
# print(wb.pb_times[wb.start_index])
# print(wb.labels[wb.start_index])
# print(wb.end_index)
# print(wb.pb_times[wb.end_index])
# print(wb.labels[wb.end_index])

# # Draw daily tweets up_nums, retweet_nums, comment_nums by month.
# monthabb = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "Octorber",
#     11: "November",
#     12: "December",
#     }

# start_date = datetime.strptime('2019-12-01', '%Y-%m-%d')
# end_date = start_date + relativedelta.relativedelta(months=1)
# title_name = f"{monthabb[12]}, 2019"
# wb.visual(start_date, end_date, title_name)

# for i in range(1,6):
#     end_date = start_date + relativedelta.relativedelta(months=1)
#     wb.visual(start_date, end_date, f"{monthabb[i]}, 2020")
#     print(start_date, end_date)
#     start_date = end_date

# Drawing the Monthly Engagement Index for 2019
title_name = '2019'
start_date = datetime.strptime('2019-01-01', '%Y-%m-%d')
x_axis, up_nums_m, retweet_nums_m, comment_nums_m, labels_m = [], [], [], [], []
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
links = [
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_1.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_2.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_3.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_4.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_5.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_6.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_7.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_8.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_9.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_10.html',
    '/Users/tianyaohe/GitHub/python/python_project/weibospider/html/2019/2019_11.html',
    None
]


for i in range(0, 12):
    end_date = start_date + relativedelta.relativedelta(months=1)
    x_val = f"<a href='{links[i]}'>{months[i]}</a>"
    up_nums = wb.retrieve_data(start_date, end_date, 'up_nums')
    retweet_nums = wb.retrieve_data(start_date, end_date, 'retweet_nums')
    comment_nums = wb.retrieve_data(start_date, end_date, 'comment_nums')
    labels = f"Period: {str(start_date)} ~ {str(end_date)}<br>"
    labels += f"Engagement Index: {sum(up_nums) + sum(retweet_nums) + sum(comment_nums)}"
    x_axis.append(x_val)
    up_nums_m.append(sum(up_nums))
    retweet_nums_m.append(sum(retweet_nums))
    comment_nums_m.append(sum(comment_nums))
    labels_m.append(labels)
    start_date = end_date

data = [
    {
        'type': 'bar',
        'name': 'up_nums',
        'x': x_axis,
        'y': up_nums_m,
        'hovertext': labels_m,
        'marker': {
            'color': 'rgb(235, 91, 52)',
            'line': {'width': 1.5, 'color': 'rgb(235, 91, 52)'}
        },
        'opacity': 0.6,
    },
    {
        'type': 'bar',
        'name': 'retweet_nums',
        'x': x_axis,
        'y': retweet_nums_m,
        'hovertext': labels_m,
        'marker': {
            'color': 'rgb(77, 232, 121)',
            'line': {'width': 1.5, 'color': 'rgb(77, 232, 121)'}
        },
        'opacity': 0.6,
    },
    {
        'type': 'bar',
        'name': 'comment_nums',
        'x': x_axis,
        'y': comment_nums_m,
        'hovertext': labels_m,
        'marker': {
            'color': 'rgb(7, 140, 242)',
            'line': {'width': 1.5, 'color': 'rgb(7, 140, 242)'}
        },
        'opacity': 0.6,
    },
]

my_layout = {
    'title': f"Tweets from @KohlerUnited - 2019",
    'titlefont': {'size': 28},
    'xaxis': {
        'type' : 'category',
        'title': 'Published Time',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        'tickangle': 0,
    },
    'yaxis': {
        'title': 'Engagement Index',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'barmode': 'stack',
}

fig = {'data': data, 'layout': my_layout}
fig = go.Figure(fig)
offline.plot(fig, filename=f"html/2019.html")
