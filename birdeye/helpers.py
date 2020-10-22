import string
from django.http import Http404


class PhoneTranslator:

    def __init__(self, keep=string.digits):
        self.comp = dict((ord(c), c) for c in keep)

    def __getitem__(self, k):
        return self.comp.get(k)


def parse_phone_number(phone_number):
    translator = PhoneTranslator()
    return phone_number.translate(translator)


def dictfetchall(cursor):
    columns = [col[0].lower() for col in cursor.description]
    data = cursor.fetchall()
    if not data: raise Http404("No Results found, 404.")
    return [dict(zip(columns, row)) for row in data]