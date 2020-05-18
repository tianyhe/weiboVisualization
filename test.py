from wb_data import Weibo

file_path = 'weibo/科勒United/readable_wb_data.json'
base_url = 'https://weibo.com/1676455960/'

wb = Weibo(file_path, base_url)

# # Testing
# for i in range(0, 10):
#     print(f"pb_times: {wb.data['pb_times'][i]}")
#     print(f"wb_links: {wb.data['wb_links'][i]}")
#     print(f"up_nums: {wb.data['up_nums'][i]}")
#     print(f"retweet_nums: {wb.data['retweet_nums'][i]}")
#     print(f"comments_nums: {wb.data['comment_nums'][i]}")
#     print(f"labels: {wb.data['labels'][i]}\n")

# start_index = wb.find_date_index(2018, 8, 6)
# end_index = wb.find_date_index(2020, 5, 1)
# print(start_index)
# print(wb.data['pb_times'][start_index])
# print(wb.data['labels'][start_index])
# print(end_index)
# print(wb.data['pb_times'][end_index])
# print(wb.data['labels'][end_index])

# print('\n')
# start_index = wb.find_month_index(2018, 8)
# end_index = wb.find_month_index(2020, 5)
# print(start_index)
# print(wb.data['pb_times'][start_index])
# print(wb.data['labels'][start_index])
# print(end_index)
# print(wb.data['pb_times'][end_index])
# print(wb.data['labels'][end_index])

# print('\n')
# start_index = wb.find_year_index(2018)
# end_index = wb.find_year_index(2020)
# print(start_index)
# print(wb.data['pb_times'][start_index])
# print(wb.data['labels'][start_index])
# print(end_index)
# print(wb.data['pb_times'][end_index])
# print(wb.data['labels'][end_index])
