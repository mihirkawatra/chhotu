from django.core.management.base import BaseCommand, CommandError
from chhotufy.models import shortURL

class Command(BaseCommand):
    help="Refreshes all codes"

    def add_arguments(self,parser):
        parser.add_argument('items',type=int)

    def handle(self, *args, **options):
        return shortURL.objects.refresh_codes(items=options['items'])
