from django.core.management.base import BaseCommand
from tqdm import tqdm
import csv
from works.models import Contributor, Metadata
from django.db import models


def insert_and_get_contributors(contributors_names):
    result = []
    for name in contributors_names:
        try:
            contributor = Contributor.objects.get(name=name)
        except models.ObjectDoesNotExist:
            contributor = Contributor(name=name)
            contributor.save()
        result.append(contributor)
    return result


def to_set(contributors):
    return {c.name for c in contributors}


class Command(BaseCommand):
    help = 'Uploads metadata from csv file to database'

    def handle(self, *args, **options):
        input_filepath = options['csv_file']
        verbose = options['verbosity'] > 0
        with open(input_filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile, quoting=csv.QUOTE_NONE)
            for row in tqdm(reader, disable=not verbose):
                title = row['title']
                contributors_names = row['contributors'].split('|')
                ISWC = row['iswc'] or None
                contributors = insert_and_get_contributors(contributors_names)
                contributors_names = to_set(contributors)

                try:
                    if ISWC:
                        meta = Metadata.objects.get(ISWC=ISWC)
                    else:
                        raise models.ObjectDoesNotExist()
                except models.ObjectDoesNotExist:
                    meta = Metadata(title=title, ISWC=ISWC)
                    meta.save()

                for contributor in contributors:
                    meta.contributors.add(contributor)
                meta.save()

                similar_metas = Metadata.objects.filter(title=title)
                contributors_names = set(contributors_names)
                for similar_meta in similar_metas:
                    if meta == similar_meta:
                        continue
                    similar_contributors = similar_meta.contributors.all()
                    if to_set(similar_contributors) & contributors_names:
                        meta.ISWC = meta.ISWC or similar_meta.ISWC
                        for similar_contributor in similar_contributors:
                            if similar_contributor.name not in contributors_names:
                                meta.contributors.add(similar_contributor)
                        similar_meta.delete()
                meta.save()

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='input csv file with headers')
