from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 hello1에 오신것을 환영합니다.")
def question(request):
    return HttpResponse("질문 목록")





