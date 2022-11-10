from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializer import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializer import UserSerializer, CustomTokenObtainPairSerializer

class UserView(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"message": "회원 가입이 완료되었습니다"}, status=status.HTTP_201_CREATED)
		else:
			return Response({"message":f"%{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
	serializer_class = CustomTokenObtainPairSerializer