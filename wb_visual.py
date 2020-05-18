import plotly.graph_objects as go
from plotly.graph_objs import Bar
from plotly import offline

# Make Visualization

data = [
{
    'type': 'bar',
    'name': 'up_nums',
    'x': wb_links[:166],
    'y': up_nums[:166],
    'hovertext': labels[:166],
    'marker': {
        'color': 'rgb(235, 91, 52)',
        'line': {'width': 1.5, 'color': 'rgb(235, 91, 52)'}
    },
    'opacity': 0.6,
},
{
    'type': 'bar',
    'name': 'retweet_nums',
    'x': wb_links[:166],
    'y': retweet_nums[:166],
    'hovertext': labels[:166],
    'marker': {
        'color': 'rgb(77, 232, 121)',
        'line': {'width': 1.5, 'color': 'rgb(77, 232, 121)'}
    },
    'opacity': 0.6,
},
{
    'type': 'bar',
    'name': 'comment_nums',
    'x': wb_links[:166],
    'y': comment_nums[:166],
    'hovertext': labels[:166],
    'marker': {
        'color': 'rgb(7, 140, 242)',
        'line': {'width': 1.5, 'color': 'rgb(7, 140, 242)'}
    },
    'opacity': 0.6,
},
]

my_layout = {
    'title': 'Most-Popular Tweet from @KohlerUnited',
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
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()
offline.plot(fig, filename='output/wb_data.html')