from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: " + str(question_id))


def results(request, question_id):
    return HttpResponse("This is the results view of the question: " + str(question_id))


def vote(request, question_id):
    return HttpResponse("Vote on question:" + str(question_id))
