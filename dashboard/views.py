from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ShareablePost
from submissions.models import Media
from datetime import datetime
from django.db.models import Exists,OuterRef


def dashboard(request):
    if request.user.is_authenticated:
        post_list = ShareablePost.objects.all().order_by('-created_on'
        ).exclude(last_date__lt=datetime.now().date()
        ).annotate(is_shared=Exists(Media.objects.filter(
            shared_post__id=OuterRef('id'),
            user=request.user
            ))
        ).exclude(is_shared=True)
        context = {
            'post_list': post_list,
        }
        return render(request, 'dashboard/dashboard_page.html',context)
    else:
        return render(request, 'dashboard/landing_page.html')
