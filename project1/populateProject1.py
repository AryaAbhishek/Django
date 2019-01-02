import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
import django
django.setup()
from faker import Faker
from newApp.models import User
fakergen = Faker()
def populate(N=10):
    for i in range(N):
        name = fakergen.name()
        fake_first = name.split(' ')[0]
        fake_last = name.split(' ')[0]
        fake_email = fakergen.email()
        usr = User.objects.get_or_create(FirstName = fake_first,LastName = fake_last, Email = fake_email)[0]

if __name__ == '__main__':
    print("Create user.")
    populate(50)
    print("user creation completed.")
