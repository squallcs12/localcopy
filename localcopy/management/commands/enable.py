import os
import sys
import urllib

from django.conf import settings
from django.core.management.base import BaseCommand
import requests

from localcopy.management.toggle import Toggle


class Command(Toggle):
    help = 'Enable catch file from local'

    def handle(self, **options):
        content = []

        with open(self.host_file, "r") as f:
            content = f.readlines()

        content.append("{start}\n".format(start=self.start_line))

        static_dir = os.path.join(settings.BASE_DIR, 'media')
        dirs = os.listdir(static_dir)

        for dir_name in dirs:
            dir_path = os.path.join(static_dir, dir_name)
            if os.path.isdir(dir_path):
                content.append("127.0.0.1 {host}\n".format(host=dir_name))

        content.append("{end}\n".format(end=self.end_line))

        with open(self.host_file, "w") as f:
            for line in content:
                f.write(line)
