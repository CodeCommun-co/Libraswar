import datetime
import uuid
from dataclasses import dataclass
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST

from django.http import HttpRequest
from faker import Faker
from django_htmx.middleware import HtmxDetails

from django.shortcuts import render

# Create your views here.

fake = Faker()

@dataclass
class FakeEvent():
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.name = fake.name()
        self.url = fake.url()
        self.imageUrl = fake.image_url(width=1920, height=1080)
        self.startDate = fake.date_time_between(start_date='now', end_date='+3y')
        self.description = fake.text()


events = [FakeEvent() for i in range(1, 235)]


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
# noinspection PyCompatibility
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_GET
def index(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, "index.html")
