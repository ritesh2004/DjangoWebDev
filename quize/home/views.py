from django.shortcuts import render,redirect
from .models import quiz
from time import time
# Create your views here.

t = time()
T = str(t)

def index(request):
    return render(request, 'index.html')

def create(request):
    obj = quiz.objects.filter(quizid=T)
    objects = {
        'obj':obj
    }
    return render(request, 'create.html', objects)

def view(request):
    obj = quiz.objects.filter(quizid=T)
    objects = {
        'obj':obj
    }
    return render(request, 'view.html', objects)

def addQuiz(request):
    if request.method == "POST":
        qn = request.POST.get('qn')
        qnno = request.POST.get('no')
        Op_a = request.POST.get('op_a')
        Op_b = request.POST.get('op_b')
        Op_c = request.POST.get('op_c')
        Op_d = request.POST.get('op_d')
        correct = request.POST.get('correct')
        id = T
        obj = quiz.objects.create(
            qn = qn,
            qnno = qnno,
            Op_a = Op_a,
            Op_b = Op_b,
            Op_c = Op_c,
            Op_d = Op_d,
            correct = correct,
            quizid = id
        )
        obj.save()
        return redirect("/create")
    return render(request, 'create.html')

def submit(request):        
    return render(request, 'view.html')