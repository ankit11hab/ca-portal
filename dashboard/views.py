from logging import currentframe
from time import timezone
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Promotions, ShareablePost
from users.models import Profile, UserGroup, NewUser
from submissions.models import Media,User
from django.db.models import Exists,OuterRef
import datetime
from datetime import datetime
from submissions.models import Idea
from .models import Notifications
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
import time
  

# start_time = datetime.now().date()
"""user_name = 'a64guha'
password = 'Ankit@123#'
api = Client(user_name, password) """

def dashboard(request):
    if request.user.is_authenticated:
        post_list = ShareablePost.objects.all().order_by('-created_on'
        ).exclude(last_date__lt=datetime.now().date()
        ).annotate(is_shared=Exists(Media.objects.filter(
            shared_post__id=OuterRef('id'),
            user=request.user,
            ))
        ).exclude(is_shared=True)
        promotions = Promotions.objects.all().order_by('-created_on')
        # Leaderboard

        all_points=[]
        all_points.sort(key=lambda x:x[1]) 
        profile = Profile.objects.filter(user = request.user).first()
        comp = []
        sum = 0
        if request.user.instahandle:
            sum+=1
        if request.user.position_of_responsibility:
            sum+=1
        if request.user.interested_modules:
            sum+=1
        if profile.fb_handle:
            sum+=1
        if sum==0:
            comp = [60, 40]
        elif sum==1:
            comp = [70, 30]
        elif sum==2:
            comp = [80, 20]
        elif sum==3:
            comp = [90, 10]
        else:
            comp = [100,0]
        top_solousers = NewUser.objects.all().order_by('-points')[:10]
        top_solousers1 = NewUser.objects.all().order_by('-points')
        
        rank=1
        while rank:
            if request.user == top_solousers1[rank]:
                break
            rank=rank+1;

        groupUsers=sorted(UserGroup.objects.all(), key=lambda t: t.getPoints,reverse=True)[:5]
        isread=True
        notification_list = Notifications.objects.filter(Q(user=request.user) | Q(user=None)).order_by('-created_on')
        if list(UserGroup.objects.filter(leader=request.user)):
            grp_points = request.user.points + UserGroup.objects.filter(leader=request.user).first().executive.points
            grp_tasks = request.user.tasks + UserGroup.objects.filter(leader=request.user).first().executive.tasks
            grp_referrals = request.user.referrals + UserGroup.objects.filter(leader=request.user).first().executive.referrals
            grp_leaderimg=request.user.img
            grp_exeimg=UserGroup.objects.filter(leader=request.user).first().executive.img
            all_points.append({ 'leader':request.user.firstname,'points': grp_points,'Lpimg':grp_leaderimg,'Epimg':grp_exeimg})
        elif list(UserGroup.objects.filter(executive=request.user)):
            grp_points = request.user.points + UserGroup.objects.filter(executive=request.user).first().executive.points
            grp_tasks = request.user.tasks + UserGroup.objects.filter(executive=request.user).first().executive.tasks
            grp_referrals = request.user.referrals + UserGroup.objects.filter(executive=request.user).first().executive.referrals
            grp_leaderimg=request.user.img
            grp_exeimg=UserGroup.objects.filter(leader=request.user).first().executive.img
            all_points.append({ 'leader':request.user.firstname,'points': grp_points,'Lpimg':grp_leaderimg,'Epimg':grp_exeimg})
        else:
             grp_points = request.user.points
             grp_tasks = request.user.tasks
             grp_referrals = request.user.referrals
             grp_leaderimg=request.user.img
             
             all_points.append({ 'leader':request.user.firstname,'points': grp_points,'Lpimg':grp_leaderimg})
        for notif in notification_list:
            if not notif.isread:
                isread=False
                break

        context = {
            'post_list': post_list,
            'promotions': promotions,
            'heading':'Dashboard',
            'notification_list': notification_list,
            'grp_points':grp_points,
            'grp_tasks':grp_tasks,
            'grp_referrals':grp_referrals,
            'top_solousers': top_solousers,
            'rank':rank+1,
            'isread':isread,
            'comp': comp,
            'grpusers':groupUsers
        }
        
        if sum<4:
            context['show_popup'] = 1
        if sum<4:
            context['color_code'] = '#E86B73'
        else:
            context['color_code'] = 'rgba(0, 201, 92, 1)'

        if profile.update_status==1 and sum==4:
            request.user.points+=200
            profile.update_status=0
        
        return render(request, 'dashboard/dashboard_page.html',context)
    else:
        return render(request, 'dashboard/landing_page.html')

@login_required
def contactus(request):
    if request.user.is_authenticated:
        # Notifications List
        notification_list = Notifications.objects.filter(
            Q(user=request.user) | Q(user=None)).order_by('-created_on')
        isread = True
        notification_list = Notifications.objects.filter(
            Q(user=request.user) | Q(user=None)).order_by('-created_on')
        for notif in notification_list:
            if not notif.isread:
                isread = False
                break
        context = {
            'heading': 'Contact us',
            'notification_list': notification_list, 'isread': isread
        }
        return render(request, 'dashboard/contactus.html', context)
    else:
        return render(request, 'dashboard/landing_page.html')

@login_required
def guidelines(request):
    if request.user.is_authenticated:
        # Notifications List
        notification_list = Notifications.objects.filter(
            Q(user=request.user) | Q(user=None)).order_by('-created_on')
        isread = True
        notification_list = Notifications.objects.filter(
            Q(user=request.user) | Q(user=None)).order_by('-created_on')
        for notif in notification_list:
            if not notif.isread:
                isread = False
                break
        context = {
            'heading': 'Guidelines',
            'notification_list': notification_list, 'isread': isread
        }
        return render(request, 'dashboard/guidelines.html', context)
    else:
        return render(request, 'dashboard/landing_page.html')


@login_required
def leaderboard(request):
    notification_list = Notifications.objects.filter(
            Q(user=request.user) | Q(user=None)).order_by('-created_on')
    isread = True
    notification_list = Notifications.objects.filter(
        Q(user=request.user) | Q(user=None)).order_by('-created_on')
    for notif in notification_list:
        if not notif.isread:
            isread = False
            break
    users = NewUser.objects.all().order_by('-points')[:10]
    teamPoints=[]
    teamPoints.append(UserGroup.objects.first().getPoints)
    
    groupUsers=sorted(UserGroup.objects.all(), key=lambda t: t.getPoints,reverse=True)[:5]
    paginator1 = Paginator(users,5)
    paginator2 = Paginator(groupUsers,5)
    page_number1 = request.GET.get('page')
    page_number2 = request.GET.get('page')
    page_obj1= paginator1.get_page(page_number1)
    page_obj2= paginator2.get_page(page_number2)
    context = {
        'heading': "Leaderboard",
        'users': users,
        'grpusers': groupUsers,
        'notification_list': notification_list, 'isread': isread,
        'index': page_obj1,
        'index1':page_obj2,
    }
    return render(request, 'dashboard/complete_leaderboard.html', context)

@login_required
def verify_like(request):

    
    # print(start_time)
    post = ShareablePost.objects.get(id=str(list(request.GET.keys())[0]))
    curr_time = time.localtime() 
    curr_time1 = time.strftime("%H:%M:%S") 
    created_on=post.created_on
    created_on1=created_on.strftime("%H:%M:%S")
    last_date=post.last_date.strftime("%H:%M:%S")
    timeformat = "%H:%M:%S"
    delta = (datetime.strptime(curr_time1, timeformat) - datetime.strptime(created_on1, timeformat))
    diff=delta.seconds
    # check = 1
    # if post.likedusers != '':
    #     arr = post.likedusers.split()
    #     for item in arr:
    #         if item==request.user.instahandle:
    #             check=0
    #             break
    # if check == 0:
    #     messages.error(request,"You have already liked this post!")
    # else:
    #     #api = auth.login_instagram('fun_tas_tic_12','Qwerty@123')
        
    # curr_time=datetime.now().date()
    #     delta = curr_time-start_time
    #     if delta.days >50:
    #         user_name = 'a64guha'
    #         password = 'Ankit@123#'
    #         api2 = Client(user_name, password)
    #         results = api2.media_likers_chrono(post.media_id)
    #     else:
    #         results = api.media_likers_chrono(post.media_id)
    #     items = results['users']
        # flag=0
        
    #     for item in items: 
    #         print(item['username'])
    #         if item['username'] == request.user.instahandle:
    #             flag=1
    #             break
    if flag==1:
            # if curr_time1<last_date:
                if(diff<3600):
                    request.user.points+=25
                    request.user.tasks+=1
                    request.user.save()
                    messages.success(request,"Thank you for liking this post! You have gained 25 points")
                    post.likedusers+=request.user.instahandle+' '
                    post.save()
                elif(diff<7200):
                    request.user.points+=15
                    request.user.tasks+=1
                    request.user.save()
                    messages.success(request,"Thank you for liking this post! You have gained 15 points")
                    post.likedusers+=request.user.instahandle+' '
                    post.save()
                elif(diff<9800):
                    request.user.points+=10
                    request.user.tasks+=1
                    request.user.save()
                    messages.success(request,"Thank you for liking this post! You have gained 10 points")
                    post.likedusers+=request.user.instahandle+' '
                    post.save()
                else:
                    request.user.points+=5
                    request.user.tasks+=1
                    request.user.save()
                    messages.success(request,"Thank you for liking this post! You have gained 5 points")
                    post.likedusers+=request.user.instahandle+' '
                    post.save()


    else:
        messages.warning(request,f"Looks like you have not liked this post yet!")
    return redirect('dashboard_page') 

@login_required
def notif_unread(request):
    if request.method == 'PUT':
        notification_list = Notifications.objects.filter(
        Q(user=request.user) | Q(user=None)).order_by('-created_on')
        for notif in notification_list:
            if not notif.isread:
                notif.isread=True
                notif.save()
        return HttpResponse("OK")

