from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Check migrations'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Migrations check ready'))
