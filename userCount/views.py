from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .models import Count
from rest_framework import viewsets
from .serializer import CountSerializer
from django.http import JsonResponse
from django.core.exceptions import ValidationError


    
def get_users(request):
    queryset = Count.objects.all().filter(gender = 2)
    Femalequeryset = Count.objects.all().filter(gender = 1)

    count = queryset.count()
    
    fcount = Femalequeryset.count()
    return JsonResponse({
        'count' : count,
        'fcount' : fcount
    })


class FemaleViewSet(viewsets.ModelViewSet):
    queryset = Count.objects.all().filter(gender = 2)
    count = queryset.count()
    serializer_class = CountSerializer

    def get(self, request, format=None):
        queryset = Count.objects.all().filter(gender = 2)

        user_type = str(self.request.userCount.Count.gender)
        try :
            if user_type == "male":
                return Response({'count' : count
        })
            else:
                raise APIException({'error': 'True', 'message': 'You do not have the permission'})
        except ValidationError:
            raise APIException({'error': 'True', 'message': 'Unexpected Error'})



from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class MaleViewSet(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = Count.objects.filter(gender=1).count()
        content = {'user_count': user_count}
        return Response(content)

