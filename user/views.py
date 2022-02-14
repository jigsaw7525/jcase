from .forms import ProfileForm
from .models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def profile(request, id):
    user = Profile.objects.get(id=id)
    print(user)
    return render(request, './user/profile.html', {'user': user})


def user_register(request):

    if request.method == 'GET':
        form = ProfileForm()  # get的情況

    elif request.method == 'POST':
        print(request.POST)
        form = ProfileForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # 不需要存
            user.username = user.username.lower()
            user.save()

            login(request, user)  # request.user
            return redirect('cases')

    return render(request, './user/register.html', {'form': form})


def user_login(request):

    username, password, message = '', '', ''

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        try:

            user = authenticate(request, username=username, password=password)
            # print(user)

            if user is not None:
                login(request, user)  # request.user可以使用
                return redirect('cases')  # 回首頁
            else:
                print('登入失敗')

            if Profile.objects.filter(username=username).exists():
                message = '密碼錯誤'
            else:
                message = '帳號錯誤'
        except Exception as e:
            print(e)

        return render(request, './user/login.html', {'username': username, 'password': password, 'message': message})

    if request.method == 'GET':

        return render(request, './user/login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')  # 回首頁
