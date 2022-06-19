from urllib.request import Request
from django.http import HttpResponse


def index(request: Request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")