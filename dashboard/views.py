from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ShareablePost
from submissions.models import Media
from datetime import datetime
from django.db.models import Exists,OuterRef
from submissions.models import Idea
from .models import Notifications
from django.db.models import Q
def dashboard(request):
    if request.user.is_authenticated:
        post_list = ShareablePost.objects.all().order_by('-created_on'
        ).exclude(last_date__lt=datetime.now().date()
        ).annotate(is_shared=Exists(Media.objects.filter(
            shared_post__id=OuterRef('id'),
            user=request.user,
            ))
        ).exclude(is_shared=True)
        # Notifications List
        notification_list = Notifications.objects.filter(Q(user=request.user) | Q(user=None)).order_by('-created_on')
        context = {
            'post_list': post_list,
            'heading':'Dashboard',
            'notification_list': notification_list
        }
        return render(request, 'dashboard/dashboard_page.html',context)
    else:
        return render(request, 'dashboard/landing_page.html')


def contactus(request):
    if request.user.is_authenticated:
        # Notifications List
        notification_list = Notifications.objects.filter(
            Q(user=request.user) | Q(user=None)).order_by('-created_on')
        context = {
            'heading': 'Contact us',
            'notification_list': notification_list
        }
        return render(request, 'dashboard/contactus.html', context)
    else:
        return render(request, 'dashboard/landing_page.html')
