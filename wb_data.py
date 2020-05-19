import json
from datetime import datetime

import plotly.graph_objects as go
from plotly.graph_objs import Bar
from plotly import offline

class Weibo():
    """A class to prepare data for visualization."""

    def __init__(self, file_path, base_url):
        """Initialize all the attributes."""
        self.file_path = file_path
        self.base_url = base_url
        self._storing()
        self._extracting()
        self._filing()

    def _storing(self):
        """Store all the data in json to a dictionary structure."""
        wb_dicts = []
        with open(self.file_path) as fhand:
            data = json.loads(fhand.read())
            wb_dicts = data['weibo']
        self.wb_dicts = wb_dicts

    def _extracting(self):
        """Extract required data to different lists."""
        pb_times, wb_links, up_nums, retweet_nums, comment_nums, labels = [], [], [], [], [], []

        for wb_dict in self.wb_dicts:
            # x_aixs
            pb_time = wb_dict['publish_time']
            pb_time = datetime.strptime(pb_time, '%Y-%m-%d %H:%M')
            wb_url = self.base_url + wb_dict['id']
            wb_link = f"<a href='{wb_url}'>{pb_time}</a>"
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

        self.pb_times = pb_times
        self.wb_links = wb_links
        self.up_nums = up_nums
        self.retweet_nums = retweet_nums
        self.comment_nums = comment_nums
        self.labels = labels

    def _filing(self):
        """Store all the lists(reversed) to dictionary for further use."""
        self.data = {}
        self.data['pb_times'] = self.pb_times
        self.data['wb_links'] = self.wb_links
        self.data['up_nums'] = self.up_nums
        self.data['retweet_nums'] = self.retweet_nums
        self.data['comment_nums'] = self.comment_nums
        self.data['labels'] = self.labels

        for k,v in self.data.items():
            k = v.reverse()

    def find_date_index(self, datetime):
        """Find the index of the given start date."""
        try:
            for index, ele in enumerate(self.pb_times):
                if ele >= datetime:
                    date_index = index
                    break
            return date_index
        except:
            print(f"Missing the data for given date.")
            return None

    def check_date_index(self):
        """Check if the index are valid for visualization."""
        if self.start_index == self.end_index:
            print("No data avaliable for given time period.")

    def retrieve_data(self, start_date, end_date, key='pb_times'):
        """Prepare the data for visualization."""
        self.start_index = self.find_date_index(start_date)
        self.end_index = self.find_date_index(end_date)
        self.check_date_index()

        return self.data[key][self.start_index:self.end_index]

    def visual(self, start_date, end_date, title_name):
        """Make Visualization with given date."""
        self.start_index = self.find_date_index(start_date)
        self.end_index = self.find_date_index(end_date)
        self.check_date_index()

        data = [
            {
                'type': 'bar',
                'name': 'up_nums',
                'x': self.wb_links[self.start_index:self.end_index],
                'y': self.up_nums[self.start_index:self.end_index],
                'hovertext': self.labels[self.start_index:self.end_index],
                'marker': {
                    'color': 'rgb(235, 91, 52)',
                    'line': {'width': 1.5, 'color': 'rgb(235, 91, 52)'}
                },
                'opacity': 0.6,
            },
            {
                'type': 'bar',
                'name': 'retweet_nums',
                'x': self.wb_links[self.start_index:self.end_index],
                'y': self.retweet_nums[self.start_index:self.end_index],
                'hovertext': self.labels[self.start_index:self.end_index],
                'marker': {
                    'color': 'rgb(77, 232, 121)',
                    'line': {'width': 1.5, 'color': 'rgb(77, 232, 121)'}
                },
                'opacity': 0.6,
            },
            {
                'type': 'bar',
                'name': 'comment_nums',
                'x': self.wb_links[self.start_index:self.end_index],
                'y': self.comment_nums[self.start_index:self.end_index],
                'hovertext': self.labels[self.start_index:self.end_index],
                'marker': {
                    'color': 'rgb(7, 140, 242)',
                    'line': {'width': 1.5, 'color': 'rgb(7, 140, 242)'}
                },
                'opacity': 0.6,
            },
        ]

        my_layout = {
            'title': f"Tweets from @KohlerUnited - {title_name}",
            'titlefont': {'size': 28},
            'xaxis': {
                'title': 'Published Time',
                'titlefont': {'size': 24},
                'tickfont': {'size': 14},
                'tickangle': 45,
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
        offline.plot(fig, filename=f"html/2019/2019_12.html")
