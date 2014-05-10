from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from models import Category, Goods

import sys


def home_page(request):
    return render(request, 'home.html',
                  {'nodes': Category.objects.all(),
                   'goods': Goods.objects.order_by('-receipt_date')[:10] },
                  context_instance=RequestContext(request)
                  )


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('magazin:index'))
    return HttpResponseRedirect(reverse('magazin:index'))


@login_required
def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    return HttpResponseRedirect(reverse('magazin:index'))


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = User.objects.create_user(username, '', password=password)
        u.save()
        new_user = authenticate(username=username, password=password)
        auth_login(request, new_user)
        return HttpResponseRedirect(reverse('magazin:index'))
    else:
        return render(request, 'signup.html')


def view_goods(request, category_id):
    return render(request, 'home.html',
                  {'nodes': Category.objects.all(),
                   'goods': Goods.objects.filter(category=category_id)},
                  context_instance=RequestContext(request)
                  )
