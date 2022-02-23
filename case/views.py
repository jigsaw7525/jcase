from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # 登入後才能做的事
from case.forms import CreateCaseForm
from .models import Case
from datetime import datetime
# Create your views here.

# 指定網址


@login_required(login_url='login')  # 安全性機制，沒登入就轉跳登入畫面
def case(request, id):
    case = Case.objects.get(id=id)
    case.view += 1
    case.save()

    responose = render(request, './case/case.html', {'case': case})
    responose.set_cookie('page', 'case')

    return responose


@login_required(login_url='login')
def update_case(request, id):
    page = request.COOKIES.get('page')
    case = Case.objects.get(id=id)

    if request.method == "GET":
        form = CreateCaseForm(instance=case)  # 填入對應表單ID的內文

    if request.method == "POST":
        case.updatedon = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        form = CreateCaseForm(request.POST, instance=case)  # 覆蓋過去
        if form.is_valid():
            form.save()

            if page == 'case':
                return redirect('case', id=case.id)

            return redirect('profile', id=request.user.id)

    return render(request, './case/update-case.html', {'form': form, 'page': page})


@login_required(login_url='login')
def delete_case(request, id):
    case = Case.objects.get(id=id)
    page = request.COOKIES.get('page')

    if request.method == "POST":

        if request.POST.get('confirm'):
            case.delete()
            if page == 'case':
                return redirect('cases')

        elif request.POST.get('cancel'):
            if page == 'case':
                return redirect('case', id=case.id)

        return redirect('profile', request.user.id)

    return render(request, './case/delete-case.html', {'case': case})


def create_case(request):
    if request.method == "GET":
        form = CreateCaseForm()
    if request.method == "POST":
        form = CreateCaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            # 指定使用者
            case.owner = request.user
            case.save()
            # 儲存多對多關係
            form.save_m2m()
            return redirect('cases')

    return render(request, './case/create-case.html', {'form': form})


def cases(request):
    cases = Case.objects.all()

    return render(request, './case/cases.html', {'cases': cases})
