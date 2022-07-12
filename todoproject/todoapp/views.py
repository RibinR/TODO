from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from todoapp.forms import todoform
from todoapp.models import Task


class tasklistview(ListView):
    model = Task
    template_name = "index.html"
    context_object_name = "data"


class taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = "new"
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('cbdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbview')

def demo(request):
    new = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get("task", '')
        priority = request.POST.get("priority", '')
        date = request.POST.get("date", '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "index.html", {'data': new})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    s = todoform(request.POST or None, instance=task)
    if s.is_valid():
        s.save()
        return redirect('/')
    return render(request, 'update.html', {'f': s, 'task': task})
