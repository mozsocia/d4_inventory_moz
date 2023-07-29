from django.core.management.base import BaseCommand
from firstapp.seed_data import load_data

class Command(BaseCommand):
    help = 'Seeds the database with sample data.'

    def handle(self, *args, **options):
        load_data()