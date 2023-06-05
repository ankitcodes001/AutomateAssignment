from Users.models import Users
from django.contrib.auth import authenticate, login, logout

class UserServices:
    
    def register_user(request):
        user = Users.objects.create_user(name= request. data. name, email= request.data.email, password= request.data.password)
        user.save()
        return user

    
    def login_user(request):
        user = authenticate(username= request.data.email, password= request.data.password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False

    def logout_user(request):
        logout(request)
