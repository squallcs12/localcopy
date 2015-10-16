import os

from django.conf import settings

from localcopy.management.toggle import Toggle


class Command(Toggle):
    help = 'Enable catch file from local'

    def handle(self, **options):
        content = []

        with open(self.host_file, "r") as f:
            content = f.readlines()

        content.append("%s\n" %self.start_line)

        static_dir = os.path.join(settings.BASE_DIR, 'media')
        dirs = os.listdir(static_dir)

        for dir_name in dirs:
            dir_path = os.path.join(static_dir, dir_name)
            if os.path.isdir(dir_path):
                content.append("127.0.0.1 %s\n" % dir_name)

        content.append("%s\n" % self.end_line)

        with open(self.host_file, "w") as f:
            for line in content:
                f.write(line)

        print("Write localcopy domains to host file")