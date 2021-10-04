from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Post, Tasks
from django.contrib import messages

# Create your views here.


class PostCreateView(CreateView):
    model=Post
    fields = ['subject', 'tell_us_your_idea']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.warning(self.request, f'Your idea has been submitted! Verification - Pending')
        return super().form_valid(form)

        
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
