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
            skip = False
            for line in f:
                if self.start_line in line:
                    skip = True
                if not skip:
                    content.append(line)
                if self.end_line in line:
                    skip = False

        with open(self.host_file, "w") as f:
            for line in content:
                f.write(line)
