from django.core.management.base import BaseCommand
from tqdm import tqdm
import csv
from works.models import Metadata


class Command(BaseCommand):
    help = 'Uploads metadata from csv file to database'

    def handle(self, *args, **options):
        input_filepath = options['csv_file']
        verbose = options['verbosity'] > 0
        with open(input_filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in tqdm(reader, disable=not verbose):
                m = Metadata(title=row['title'], contributors=row['contributors'], ISWC=row['iswc'])
                m.save()

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='input csv file with headers')
