import random
import string

from django.conf import settings
SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_gen(size=SHORTCODE_MIN, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_code(instance,size=SHORTCODE_MIN):
    new_code = code_gen(size=size)
    qs = instance.__class__.objects.filter(code=new_code).exists()
    if qs:
        return create_code(size = size)
    return new_code


# for i in shortURL.objects.all().values('url'):
#     print(i['url'])
