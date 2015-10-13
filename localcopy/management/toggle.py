import os
import sys
import urllib

from django.conf import settings
from django.core.management.base import BaseCommand
import requests


class Toggle(BaseCommand):
    host_file = ""
    if 'linux' in sys.platform:
        host_file = "/etc/hosts"

    start_line = "# localcopy start ======"
    end_line = "# localcopy end ======"
