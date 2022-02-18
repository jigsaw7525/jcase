from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # 登入後才能做的事
from case.forms import CreateCaseForm
from .models import Case
# Create your views here.

# 指定網址


@login_required(login_url='login')  # 安全性機制
def case(request, id):
    case = Case.objects.get(id=id)
    case.view += 1
    case.save()

    return render(request, './case/case.html', {'case': case})


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
