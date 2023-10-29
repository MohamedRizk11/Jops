import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from job.models import Job ,Company,Category
import random
from faker import Faker




def create_categroy(n):
    faker = Faker()
    for x in range(n):
        Category.objects.create(
            name = faker.name()

        )
    print(f"{n} catogory was added successfully")    



def create_company(n):
    faker = Faker()
    images=['job-list1.png','job-list2.png','job-list3.png','job-list4.png']
    for x in range(n):
        Company.objects.create(

                name=faker.company(),
                website=faker.url(),
                subtitle=faker.text(),
                email=faker.email(),
                logo=f"company/{images[random.randint(0,3)]}",


        )
    print(f"{n} company was added successfully")    



def create_job(n):
    faker=Faker()
    job_nature=['FullTime','PartTime','Remote','FreeLance']

    for x in range(n):
        Job.objects.create(
            title=faker.name(),
            company =Company.objects.all().order_by('?')[0],
            vecancy=random.randint(1,5),
            salary_start=random.randint(2000,2500),
            salary_end=random.randint(2300,2800),
            description=faker.sentence(),
            experience=random.randint(1,5),
            category=Category.objects.all().order_by('?')[0],
            job_nature=job_nature[random.randint(0,3)],




        )
    print(f"{n} job was added successfully")

create_categroy(5)
create_company(100)
create_job(1000)








