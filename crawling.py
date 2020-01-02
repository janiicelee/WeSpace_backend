import requests as rq
import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'wespace.settings')
CSV_PATH = './main_recommend.csv'
import django
django.setup()
from space.models import *
with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        print(row)
        Spaces.objects.create(
            title=row['title'],
            short_intro=row['sub_title'],
            long_intro=row['desc'],
            location = row['location'],
            open_time=row['open_time'],
            close_time=row['close_time'],
            price=row['price'],
            host_id=row['host_id']
        )
