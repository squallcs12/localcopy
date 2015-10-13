import os
import urllib

from django.conf import settings
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Copy file to local'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('url', type=str)

    def handle(self, url, **options):
        response = requests.get(url)
        if response.status_code >= 400:
            print("URL return status {code}".format(code=response.status_code))
            return
        url_info = urllib.parse.urlparse(url)

        dirs = url_info.path.split("/")
        dirs[0] = url_info.hostname  # hostname as root
        file_name = dirs.pop()  # remove file name

        target_dir = os.path.join(settings.BASE_DIR, 'media')
        for dir_name in dirs:
            target_dir = os.path.join(target_dir, dir_name)
            if not os.path.isdir(target_dir):
                os.mkdir(target_dir)

        target_file = os.path.join(target_dir, file_name)
        with open(target_file, "wb") as f:
            f.write(response.content)
