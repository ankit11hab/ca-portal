from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ShareablePost
from subIdea.models import Tasks

def dashboard(request):
    if request.user.is_authenticated:
        post_list = ShareablePost.objects.all().order_by('-created_on')
        tasks_done = Tasks.objects.filter(user=request.user.id)
        context = {
            'post_list': post_list,
            'tasks_done':tasks_done,
        }
        return render(request, 'dashboard/dashboard_page.html',context)
    else:
        return render(request, 'dashboard/landing_page.html')
