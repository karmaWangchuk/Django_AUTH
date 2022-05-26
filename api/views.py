from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission  # <-- Here

class Token:

    def __init__(self, token = ""):
        self.token = "545fdv-srb84dssd-b84851favd-gbhg2zd" 

    def get_token(self):
        return self.token

class login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        token = Token()

        if username == "admin" and password == "admin":
            token = token.get_token()
            return Response({"token":token})
        else:
            return Response({"token":None})
    
class BasicAuth(BasePermission):
    def has_permission(self, request, view):
        obj_token = request.headers['Token']
        token = Token()
        token = token.get_token()
        
        if token == obj_token:
            return True
        else:
            return False

class index(APIView):
    permission_classes = [BasicAuth]
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
