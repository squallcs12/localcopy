import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add domain to watch'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('domain', type=str)

    def handle(self, domain, **options):
        target_dir = os.path.join(settings.BASE_DIR, 'media', domain)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
            print("Added to local %s" % domain)
        else:
            print("Already exists %s" % domain)
