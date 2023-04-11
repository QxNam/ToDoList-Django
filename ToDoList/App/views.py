from django.shortcuts import render, redirect
from App.models import Task
from django.views import View

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        time = request.POST['time']
        ins = Task(title=title, desc=desc, time=time)
        ins.save()
        context =  {'success': True}
    
    return render(request, 'home.html', context)

def task(request):
    tasks=Task.objects.all()
    return render(request, 'task.html', locals())

class editTask(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        return render(request, 'edit.html', locals())
    
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.title = request.POST['title']
        task.desc = request.POST['desc']
        # task.time = request.POST['time']
        task.save()
        return redirect('/task')

class delete(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/task')