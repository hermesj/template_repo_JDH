import os
import json

comments = 0
likes = 0
postCount = 0
commentators = 0

comment_likes = 0

for file in os.listdir('./comments_json_anonym'):
    with open('./comments_json_anonym/'+file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for comment in data:
            comment_likes += comment["likes_count"]
            if 'answers' in comment:
                for answer in comment['answers']:
                    comment_likes += answer["likes_count"]

for file in os.listdir('./ichbinsophiescholl'):
    if not file.endswith('.json'):
        continue
    postCount += 1
    with open(os.path.join('./ichbinsophiescholl',file),'r',encoding='utf-8') as f:
        data = json.load(f)['node']
        likes += data['edge_media_preview_like']['count']
        comments += data["edge_media_to_comment"]['count']

with open('userNetSave.json',"r", encoding="utf-8") as f:
    data = json.load(f)
commentators = len(data.keys())

print(f"{likes=},\n{comments=},\n{comment_likes=},\noverall_likes={likes+comment_likes},\n{postCount=},\n{commentators=}")
