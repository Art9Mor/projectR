import re

from rest_framework.exceptions import ValidationError


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^[a-zA-z0-9\-\_]+$')
        tmp = dict(value).get(self.field)
        if not bool(reg.match(tmp)):
            raise ValidationError('Title is not ok')