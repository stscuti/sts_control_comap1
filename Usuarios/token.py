from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from datetime import datetime, timedelta, tzinfo, time, date
from django.utils import timezone

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            #six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
            six.text_type(user.pk) + six.text_type(datetime.now().month)
        )

token_activacion_cuenta = TokenGenerator()

from django.utils.crypto import get_random_string
import hashlib

def generate_activation_key(identificador):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    clave = str(int(identificador))
    return hashlib.sha256((secret_key + clave).encode('utf-8')).hexdigest()