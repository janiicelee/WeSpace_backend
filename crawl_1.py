import requests
import json
import csv
import random
dict_text = {}
dict_review = {}
dict_image = {}
dic_tag = {}
recommend_url = [
        'https://new-api.spacecloud.kr/spaces/13259',
        'https://new-api.spacecloud.kr/spaces/8646',
        'https://new-api.spacecloud.kr/spaces/14495',
        'https://new-api.spacecloud.kr/spaces/8259',
        'https://new-api.spacecloud.kr/spaces/22513',
        'https://new-api.spacecloud.kr/spaces/22882',
        ]
def filewrite():
    with open('./main_recommend.csv', "w", newline="") as csvfile:
        fieldnames = ['category', 'location', 'title', 'sub_title', 'desc', 'open_time', 'close_time',
                      'price', 'tag','host_id']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()


        for i in recommend_url:
            req = requests.get(i)
            html = req.text
            result = json.loads(html)


            img_url = []
            categories = []
            tags = []
            for k in result['images']:
                img_url.append(k['image_url'])
            for j in result['products'][0]['categories']:
                categories.append(j['name'])
            for p in result['tags']:
                tags.append(p['tag'])
            dict_text = {
                'category': str(categories),
                'location': result['location']['addr'],
                'title': result['info']['name'],
                'sub_title': result['info']['sub_title'],
                'desc': result['info']['desc'],
                'open_time': result['break_times'][0]['end_time'],
                'close_time': result['break_times'][0]['start_time'],
                'price': result['products'][0]['info']['price'],
                'host_id' : random.randint(1,3)
            }
            csvwriter.writerow(dict_text)
def imageCSV():
    with open('./image.csv', 'w', newline="") as imagefile:
        fieldnames = ['image_url', 'space_id']
        imagewriter = csv.DictWriter(imagefile, fieldnames=fieldnames)
        imagewriter.writeheader()
        for i in recommend_url:
            req = requests.get(i)
            html = req.text
            result = json.loads(html)
            for k in result['images']:
                dict_image = {
                    'image_url': k['image_url'],
                    'space_id': random.randint(1, 11)
                }
                imagewriter.writerow(dict_image)
            # filewrite("./main_recommend.csv", recommend_url)
def tagCSV():
    with open('./tag.csv', 'w', newline="") as imagefile:
        fieldnames = ['tag', 'space_id']
        tagwriter = csv.DictWriter(imagefile, fieldnames=fieldnames)
        tagwriter.writeheader()
        for i in recommend_url:
            req = requests.get(i)
            html = req.text
            result = json.loads(html)
            for k in result['tags']:
                dict_tag = {
                    'tag': k['tag'],
                    'space_id': random.randint(1, 11)
                }
                tagwriter.writerow(dict_tag)
filewrite()
tagCSV()
imageCSV()
