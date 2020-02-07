import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
import django
django.setup()

# Fake-ing scripts
from SecondApp.models import Topic, Webpage, AccessRecord
import random
import faker

generator = faker.Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    topicName = random.choice(topics)
    t = Topic.objects.get_or_create(topic_name=topicName)[0] # get_or_create gets if it exists, and creates if it doesn't
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        topic = add_topic()

        # Generate the other info for Webpage and AccessRecord objects
        fakeName = generator.company()
        fakeUrl = generator.url()
        fakeDate = generator.date()

        webPage = Webpage.objects.get_or_create(topic=topic, name=fakeName, url=fakeUrl)[0] # Notice topic is a foreign key, so I passed in the actual object
        accessRecord = AccessRecord.objects.get_or_create(name=webPage, date=fakeDate)[0] # Notice webPage is a foreign key, so I passed in the actual object

if __name__ == "__main__":
    print("populating script!")
    populate()