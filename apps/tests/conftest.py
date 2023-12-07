import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from apps.models import Post, Tag
from django.urls import reverse


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def post_1_obj(db, client):
    url = reverse("apps:post_new")
    data = {"title": f"1", "text": "하나 둘 셋"}
    response = client.post(url, data)

@pytest.fixture
def post_11_dumps(db, client):
    url = reverse("apps:post_new")
    for i in range(1, 11):
        data = {"title": f"{i}", "text": "하나 둘 셋"}
        response = client.post(url, data)
    payload = {"title": f"11", "text": "하나 둘 셋 넷 다섯"}
    response = client.post(url, payload)