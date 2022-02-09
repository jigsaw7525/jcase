from django.shortcuts import render
from .models import Case
# Create your views here.

# 指定網址


def cases(request):
    cases = Case.objects.all()

    return render(request, './case/cases.html', {'cases': cases})
