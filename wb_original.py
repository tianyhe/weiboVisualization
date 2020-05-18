import json
from datetime import datetime

import plotly.graph_objects as go
from plotly.graph_objs import Bar
from plotly import offline

def main(start_year, start_month, end_year, end_month, monthabb):
    """Store all required data for visualization."""
    # Store all the data in Json file to a dictionary.
    file_path = 'weibo/科勒United/readable_wb_data.json'
    wb_dicts = []
    with open(file_path) as fhand:
        data = json.loads(fhand.read())
        wb_dicts = data['weibo']

    base_url = 'https://weibo.com/1676455960/'
    pb_titles, pb_times, wb_links, up_nums, retweet_nums, comment_nums, labels = [], [], [], [], [], [], []

    for wb_dict in wb_dicts:
        # x_aixs
        pb_time = wb_dict['publish_time']
        pb_time = datetime.strptime(pb_time, '%Y-%m-%d %H:%M')
        pb_title = pb_time.strftime("%m-%d")
        wb_url = base_url + wb_dict['id']
        wb_link = f"<a href='{wb_url}'>{pb_time}</a>"
        pb_titles.append(pb_title)
        pb_times.append(pb_time)
        wb_links.append(wb_link)
        # y_aixs
        up_num = wb_dict['up_num']
        retweet_num = wb_dict['retweet_num']
        comment_num = wb_dict['comment_num']
        up_nums.append(up_num)
        retweet_nums.append(retweet_num)
        comment_nums.append(comment_num)
        # hover_text
        wb_id = wb_dict['id']
        content = wb_dict['content']
        label = f"Content: {content[:50]}..."
        labels.append(label)

    # Store all the data in a dictionary and reverse the order of each list.
    data = {}
    data['pb_titles'] = pb_titles
    data['pb_times'] = pb_times
    data['wb_links'] = wb_links
    data['up_nums'] = up_nums
    data['retweet_nums'] = retweet_nums
    data['comment_nums'] = comment_nums
    data['labels'] = labels

    for k, v in data.items():
        k = v.reverse()

    # # The index of "2018-08-06 16:16".
    # start_time = datetime.strptime("2018-08-06 16:16", '%Y-%m-%d %H:%M')
    # for index, ele in enumerate(pb_times):
    #     if ele == start_time:
    #         start_index = index
    # print(start_index)

    # # The index of "2018-12-31 21:30".
    # end_time = datetime.strptime("2019-01-31 20:00", '%Y-%m-%d %H:%M')
    # for index, ele in enumerate(pb_times):
    #     if ele == end_time:
    #         end_index = index + 1
    # print(end_index)

    # # Find the first date in 2018 and return its index.
    # for index, ele in enumerate(pb_times):
    #     if ele.year == 2018:
    #         start_index = index
    #         print(start_index)
    #         break

    # # Find the first date after 2018 and return its index.
    # for index, ele in enumerate(pb_times):
    #     if ele.year == 2019:
    #         end_index = index
    #         print(end_index)
    #         break

    # Find the index of the start_date.
    try:
        for index, ele in enumerate(pb_times):
            if ele.year == start_year and ele.month == start_month:
                start_index = index
                #print(start_index)
                print(ele)
                break
    except:
        print("Missing the current month data.")
        quit()

    # Find the index of the end_date.
    for index, ele in enumerate(pb_times):
        if ele.year == end_year and ele.month == end_month:
            end_index = index
            #print(end_index)
            print(ele)
            break

    # Testing
    # print(f"pb_titles: {pb_titles[start_index:end_index]}")
    # print(f"pb_time: {pb_times[start_index:end_index]}")
    # print(f"wb_link: {wb_links[i]}")
    # print(f"up_num: {up_nums[i]}")
    # print(f"retweet_num: {retweet_nums[i]}")
    # print(f"comment_num: {comment_nums[i]}")
    # print(f"label: {labels[i]}\n")

    # Make Visualization
    data = [
    {
        'type': 'bar',
        'name': 'up_nums',
        'x': wb_links[start_index:end_index],
        'y': up_nums[start_index:end_index],
        'hovertext': labels[start_index:end_index],
        'marker': {
            'color': 'rgb(235, 91, 52)',
            'line': {'width': 1.5, 'color': 'rgb(235, 91, 52)'}
        },
        'opacity': 0.6,
    },
    {
        'type': 'bar',
        'name': 'retweet_nums',
        'x': wb_links[start_index:end_index],
        'y': retweet_nums[start_index:end_index],
        'hovertext': labels[start_index:end_index],
        'marker': {
            'color': 'rgb(77, 232, 121)',
            'line': {'width': 1.5, 'color': 'rgb(77, 232, 121)'}
        },
        'opacity': 0.6,
    },
    {
        'type': 'bar',
        'name': 'comment_nums',
        'x': wb_links[start_index:end_index],
        'y': comment_nums[start_index:end_index],
        'hovertext': labels[start_index:end_index],
        'marker': {
            'color': 'rgb(7, 140, 242)',
            'line': {'width': 1.5, 'color': 'rgb(7, 140, 242)'}
        },
        'opacity': 0.6,
    },
    ]

    my_layout = {
        'title': f"Tweets from @KohlerUnited - {monthabb}, {start_year}",
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Published Time',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
            'tickangle': 45,
            'tickformat': '%d %B %Y',
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
    # fig.update_layout(
    #     xaxis=dict(
    #         rangeselector=dict(
    #             buttons=list([
    #                 dict(count=1,
    #                     label="1m",
    #                     step="month",
    #                     stepmode="backward"),
    #                 dict(count=6,
    #                     label="6m",
    #                     step="month",
    #                     stepmode="backward"),
    #                 dict(count=1,
    #                     label="YTD",
    #                     step="year",
    #                     stepmode="todate"),
    #                 dict(count=1,
    #                     label="1y",
    #                     step="year",
    #                     stepmode="backward"),
    #                 dict(step="all")
    #             ])
    #         ),
    #         rangeslider=dict(
    #             visible=True
    #         ),
    #         type="date"
    #     )
    # )

    #fig.show()
    offline.plot(fig, filename=f"output/2020/{start_year}_{start_month}.html")

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
monthabb = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "Octorber",
    11: "November",
    12: "December",
    }

for i in month[:6]:
    if i == 12:
        main(2020, i, 2021, 1, monthabb[i])
    elif i < 12:
        for k in range(1,3):
            try:    
                main(2020, i, 2020, i + k, monthabb[i])
                break
            except UnboundLocalError:
                print(f"Missing the following month data.")
            else:
                break
