from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def user_login(request):

    username, password = '', ''

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # request.user可以使用
                return redirect('cases')  # 回首頁
            else:
                print('登入失敗')
        except Exception as e:
            print(e)

        return render(request, './user/login.html', {'username': username, 'password': password})

    if request.method == 'GET':

        return render(request, './user/login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')  # 回首頁
