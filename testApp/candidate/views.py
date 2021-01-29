from django.shortcuts import render
from .models import Candidate
from .serializers import CandidatesSerializer,RegisterSerializer,UserTokenSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import requests
from rest_framework import generics
import json    
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class UserLogin(APIView):
    """return user token if user credetials are correct"""
    serializer_class = UserTokenSerializer

    def get(self, request, format=None):
        """user sign in form"""
        serializer = UserTokenSerializer()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """post user request"""
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data.get('email'),
                password=serializer.data.get('password'))
            if user is not None:
                token, create_or_fetch = Token.objects.get_or_create(
                    user=user)
                return Response({'token': token.key,'isAdmin':user.is_superuser}, status=status.HTTP_200_OK)
            msg = 'Wrong credentials. Please try again'
            return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Register(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = RegisterSerializer


class CandidatesListCreate(viewsets.ModelViewSet):

    def get_queryset(self):
        return Candidate.objects.all()
        
    def get_all(self, request, *args, **kwargs):
        if request.user.is_superuser:       
            return Response(CandidatesSerializer(self.get_queryset().order_by('-date_of_birth'),many=True).data)
        else:  
            return Response(CandidatesSerializer(self.get_queryset(),many=True).data)


    def details(self, request, *args, **kwargs):
        specific_candidates=None
        try:
            specific_candidates=Candidate.objects.get(id=self.kwargs['id'])
        except Candidate.DoesNotExist:
            return Response({"details:candidate not found"})
        return Response(CandidatesSerializer(specific_candidates).data)
       
    def download(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"details:you don't have permissions to download candidate cv"})    
        specific_candidates=None
        try:
            specific_candidates=Candidate.objects.get(id=self.kwargs['id'])
        except Candidate.DoesNotExist:
            return Response({"details:candidate not found"})
        filename = specific_candidates.resume.file.name.split('/')[-1]
        return Response({"details:candidate cv link:  "+filename})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        created = serializer.save()
        return Response(created.data)


