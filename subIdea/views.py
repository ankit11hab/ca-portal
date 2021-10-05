from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Post, Tasks, POC
from django.contrib import messages
import csv,io
# Create your views here.
from django import forms



class PostCreateView(CreateView):
    model=Post
    fields = ['subject', 'tell_us_your_idea']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.warning(self.request, f'Your idea has been submitted! Verification - Pending')
        return super().form_valid(form)



@login_required
def poccsv(request):
    # declaring template
    template = "ca/poc-csv.html"
    data = POC.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, designation,college, contact',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    for column in csv.reader(io_string, delimiter=',', quotechar="|") :

        _, created = POC.objects.create(
        name=column[1],
        design=column[2],
        college=column[3],
        contact=column[4],
    
    )
    context = {}
    return render(request, template, context)


@login_required(login_url='login')
def home(request):
    userNow = request.user
    
    t = userNow.tasks_set.first()
    if userNow.post_set.first():
        t.ideaDone = userNow.post_set.first().validate
        t.save()

    t.points = 25*(int(t.ideaDone==1)+int(t.pocDone==1)+int(t.socialDone==1))
    t.save()
    contextTasks = {
        'tasks': userNow.tasks_set.all()
    }
    return render(request,'subIdea/home.html', contextTasks)


@login_required(login_url='login')
def ideas(request):
    userNow = request.user
    context = {
        'posts': userNow.post_set.all()
    }
    return render(request,'subIdea/ideas.html',context)

@login_required(login_url='login')
def tasks(request):
    return render(request,'subIdea/tasks.html')
