from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, mixins
from rest_framework.views import APIView

from accounts.serilaizers import (RegisterSerializer,
            UserProfileUpdateSerializer,
            UserSerializer)

from accounts.models import (Profile, SystemUser)




### Registration Api View .....
class RegisterApi(generics.GenericAPIView):
    
    queryset = SystemUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":  UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

 



#### Login user view....
class Loginview(generics.ListAPIView):

    queryset = SystemUser.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request):

        if 'Phone' in request.data:

            queryset = self.get_queryset().filter(Phone=request.data['Phone'])
            serializer = self.serializer_class(queryset, many=True)
            data = serializer.data
            return Response({'Message': 'Users active logged successfully', 'data': data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": "give Phone number data"})


###User profile view....
class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):

        list = []
        userprofile = Profile.objects.all().values('id','user','profile_pic','bio','othersitelink')
        for users in userprofile:

            list.append(users)
        serializer = UserProfileUpdateSerializer(userprofile,many=True)
        if userprofile:
            return Response({"message":list })
        else:
            return Response({"message": "Currently we don't have any user profile"})



    def post(self,request,format=None):
        user = SystemUser.objects.get(id=request.user.id)
        profile = Profile.objects.filter(user=user)
        if not profile:
              serializer = UserProfileUpdateSerializer(data=request.data)
              if serializer.is_valid():
                s=serializer.save(user=user)
                return Response({"message": "User profile Create. "},status=status.HTTP_200_OK)

              else:
                return Response(serializer.errors, status=status.HTTP_200_OK)                
        else:
            return Response({"message": "User Profile alreday create."}, status=status.HTTP_404_NOT_FOUND)



    def put(self, request, format=None):
        user = SystemUser.objects.get(id=request.user.id)
        if user:
              serializer = UserProfileUpdateSerializer(data=request.data)
              if serializer.is_valid():
                return Response({"message": "User profile updated. "},status=status.HTTP_200_OK)
              else:
                return Response(serializer.errors, status=status.HTTP_200_OK)
        else:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


