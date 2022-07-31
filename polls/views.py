from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("This is the index page.")


def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: " + str(question_id))


def results(request, question_id):
    return HttpResponse("This is the results view of the question: " + str(question_id))


def vote(request, question_id):
    return HttpResponse("Vote on question:" + str(question_id))
