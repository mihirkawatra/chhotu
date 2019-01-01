from django.core.management.base import BaseCommand, CommandError
from chhotufy.models import shortURL

class Command(BaseCommand):
    help="Shows all codes"

    def handle(self, *args, **options):
        qs = shortURL.objects.filter(id__gte=1).order_by('-id')
        s=""
        for q in qs:
            s+=str(q.url) + " : " + str(q.code) + "\n"
        return s
        
