from django.test import TestCase
from django.urls import reverse
import pytest
# Create your tests here.


@pytest.fixture
def test_user(db, django_user_model):  # django_user_model is a build-in fixture from django
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple


def test_login_user(client, test_user):  # wow, this test checks if a new user can login by using built in models and a method on client called login()
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True
