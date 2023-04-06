from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        value = six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        return value


generate_token = TokenGenerator()
