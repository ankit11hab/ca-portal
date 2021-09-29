from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard_page.html')
    else:
        return render(request, 'dashboard/home.html')
