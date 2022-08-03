import uuid
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import serializers

from .serializers import RegisterUserSerializer


# Create your views here.


class RegisterUserViewSet(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
