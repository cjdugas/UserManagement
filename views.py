
from service.models import Log, User
from service.serializers import UserSerializer, LogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
import datetime
from rest_framework import generics
from django.shortcuts import get_list_or_404

#api entry point is a link to the users page
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })


#This viewset  provides `list`, `create`, `retrieve`,`update` and `destroy` actions
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #on creation, update, and deletion of User, create new log entry

    def perform_create(self, serializer):
        #save serialized info
        myUser = serializer.save()
        newlog = Log(user_id=myUser.id, action='create', attributes=str(myUser))
        newlog.save()

    def perform_update(self, serializer):
        #save serialized info along with time of update
        myUser = serializer.save(updated_at=datetime.datetime.now())
        newlog = Log(user_id=myUser.id, action='update', attributes=str(myUser))
        newlog.save()

    def perform_destroy(self, instance):
        newlog = Log(user_id=instance.id, action='delete', attributes=str(instance))
        newlog.save()
        #delete the user instance
        instance.delete()


#show a list of all logs
class LogList(generics.ListAPIView):
    serializer_class = LogSerializer
    queryset = Log.objects.all()


#show a list of all logs for a given user
class LogDetail(generics.ListAPIView):
    serializer_class = LogSerializer
    #keyword <userid> in url config
    lookup_url_kwarg = "userid"

    #return a list of all Logs with the given user_id value or raise 404 if user_id does not exist
    def get_queryset(self):
        #find the value of keyword <uid> in url
        userid = self.kwargs.get(self.lookup_url_kwarg)
        #filter logs based on value found
        return get_list_or_404(Log, user_id=userid)


