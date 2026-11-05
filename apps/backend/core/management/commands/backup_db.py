import os
import datetime
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Backup database'

    def add_arguments(self, parser):
        parser.add_argument('--output', type=str, help='Output file path')

    def handle(self, *args, **options):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = options.get('output') or f'/tmp/backup_{timestamp}.sql'
        db = settings.DATABASES['default']
        cmd = f"pg_dump -h {db['HOST']} -U {db['USER']} -d {db['NAME']} > {filename}"
        os.system(cmd)
        self.stdout.write(self.style.SUCCESS(f'Backup created: {filename}'))
