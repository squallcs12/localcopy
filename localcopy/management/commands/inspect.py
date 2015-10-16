import os
import re

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Add domain to watch'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('url', type=str)

    def handle(self, url, **options):
        response = requests.get(url)
        if response.status_code != 200:
            print("URL return status %s" % response.status_code)
        urls = re.findall(r'//[^\'"]+', response.content.decode())
        for url in urls:
            management.call_command('copy', "http:%s" % url)
            