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

    def find_date_index(self, year, month, day):
        """Find the index of the given start date."""
        try:
            for index, ele in enumerate(self.pb_times):
                if ele.year == year and ele.month == month and ele.day == day:
                    date_index = index
                    break
            return date_index
        except:
            print("Missing the given date data.")
            return None

    def find_month_index(self, year, month):
            """Find the index of the given start date."""
            try:
                for index, ele in enumerate(self.pb_times):
                    if ele.year == year and ele.month == month and ele.day >= 1:
                        date_index = index
                        break
                return date_index
            except:
                print("Missing the given month data.")
                return None

    def find_year_index(self, year):
            """Find the index of the given start date."""
            try:
                for index, ele in enumerate(self.pb_times):
                    if ele.year == year and ele.month >=1 and ele.day >= 1:
                        date_index = index
                        break
                return date_index
            except:
                print("Missing the given year data.")
                return None
