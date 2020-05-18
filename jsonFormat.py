import json

unformatted_file = 'weibo/科勒United/1676455960.json'
readable_file = 'weibo/科勒United/readable_wb_data.json'

with open(unformatted_file) as f, open(readable_file, 'w', encoding='utf8') as g:
    json.dump(json.load(f), g, indent=4, ensure_ascii=False)
