from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import NewUser

@api_view(['PUT'])
def points_referal_id(request):
    if(request.data.get('alcherid')):
        user = NewUser.objects.filter(alcherid = request.data.get('alcherid')).first()
        user.points += int(request.data.get('points'))
        user.save()
        # print('success')
        return Response('success')
    else:
        # print('error')
        return Response('error')
