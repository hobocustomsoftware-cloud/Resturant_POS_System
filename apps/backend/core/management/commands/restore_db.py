import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Restore database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Backup file path')

    def handle(self, *args, **options):
        filename = options['file']
        db = settings.DATABASES['default']
        cmd = f"psql -h {db['HOST']} -U {db['USER']} -d {db['NAME']} < {filename}"
        os.system(cmd)
        self.stdout.write(self.style.SUCCESS(f'Restored from: {filename}'))
