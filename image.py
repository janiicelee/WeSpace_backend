import requests as rq
import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'wespace.settings')
CSV_PATH = './image.csv'
import django
django.setup()
from space.models import *
with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        print(row)
        Images.objects.create(
                space_image = row['image_url'],
                space_id = row['space_id']
        )
