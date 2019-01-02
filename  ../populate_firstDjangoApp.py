import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
import django
django.setup()

# fake script

import random
from firstDjangoApp.models import AccessRecord, Topic, WebPage
from faker import Faker

fakergen = Faker()
topics = ['news','search','marketing','politics']

def add_topic():
    t = Topic.objects.get_or_create(Topic_name = random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    top = add_topic()
    for i in range(N):
        fake_url = fakergen.url()
        fake_name = fakergen.company()
        fake_date = fakergen.date()

        webpg = WebPage.objects.get_or_create(topic = top,url = fake_url, name = fake_name)[0]
        accs = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)

if __name__ == '__main__':
    print("population script.")
    populate(25)
    print("completed.")
