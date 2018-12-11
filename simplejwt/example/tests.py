import pytest
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework_simplejwt.state import User

from django.test import TestCase

from .views import ExampleView

@pytest.mark.django_db()
@pytest.mark.parametrize('user', (
    ({'username': 'test_user', 'password': 'secret'}),
))
def test_example_view(user):
    factory = APIRequestFactory()
    test_user = User.objects.create_user(username=user['username'], password=user['password'])
    view = ExampleView.as_view()
    request = factory.get('/example/')
    force_authenticate(request, user=test_user)
    response = view(request)
    assert response.status_code == 200
