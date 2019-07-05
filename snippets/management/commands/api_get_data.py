from django.core.management.base import BaseCommand, CommandError
from snippets.models import ApiUsers
import requests


class Command(BaseCommand):
    help = "Fill data using api to TypiCodeUsers model"

    def handle(self, *args, **options):
        print("calling")
        # Api declare 
        api_url = 'https://jsonplaceholder.typicode.com/users' 

        # Get response
        response = requests.get(url=api_url)
        # Convert data into json
        datas = response.json() 

        if datas:
            for data in datas:
                # This will create object into ApiUser table.
                ApiUsers.objects.create(
                    name=data['name'],
                    username=data['username'],
                    email=data['email'],
                    website=data['website']
                ).save()

        print("End")
