from django.test import TestCase

from apps.employee.utils.email_field import EmailField


class TestsEmailField(TestCase):
    def test_email_field_lower_case(self):
        email = EmailField()
        assert email.get_prep_value('Email@email.com') == 'email@email.com'

    def test_email_field_none(self):
        email = EmailField()
        assert email.get_prep_value(None) is None
