from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm,SearchForm
from .models import Movie
# Create your views here.
def index_view(req):
    categories=['Action','Adventure']
    data={}
    search_form=SearchForm()
    for i in categories:
        movies=Movie.objects.filter(category__name=i)
        '''rendering search results incase of post request'''
        if req.method=='POST': 
            text_search=req.POST.get('search_val')
            '''filtering movie objects if the movie name contains the search query'''
            movies=Movie.objects.filter(movie_name__icontains=text_search)
            return render(req,'netflix/search_result.html',{"search_val":text_search,"obj":movies,"search_form":search_form})
        '''passing only 20 results for display on home screen'''
        data[i]=movies[:20]
    
    return render(req,'netflix/index.html',{"obj":data.items(),"search_form":search_form})

def register_view(req):
    if req.method=='GET':
        register_form=RegisterForm()
        return render(req,'netflix/register.html',locals())
    else:
        register_form=RegisterForm(req.POST)
        '''creating user obj if the form is valid'''
        if register_form.is_valid():
            User.objects.create(
                first_name=req.POST.get('firstname'),
                last_name=req.POST.get('lastname'),
                email=req.POST.get('email'),
                username=req.POST.get('email'),
                password=make_password(req.POST.get('password'))
            )
            '''redirecting to login page once registered'''
            return HttpResponseRedirect('login')
        return render(req, 'netflix/register.html', locals())

def login_view(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'netflix/login.html', locals())
    else:
        username = request.POST['email']
        password = request.POST['password']
        '''authenticating user with given pw and email'''
        user = authenticate(username=username, password=password)
        if user is not None:
            '''if user exists we then login the user and redirect them to homepage'''
            login(request, user)
            return HttpResponseRedirect('/')
        '''if wrong credentials render the login page with wrong credentials message'''
        return render(
            request,
            'netflix/login.html',
            {
                'wrong_credentials': True,
                'login_form': LoginForm(request.POST)
            }
        )
    

def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/')

'''setting login_required condition to watch movie'''
@login_required(login_url='/login')
def watch_movie_view(request):
    movie_primarykey=request.GET.get('movie_pk')
    try:
        movie=Movie.objects.get(pk=movie_primarykey)
    except:
        movie=None
    return render(request,'netflix/watch.html',{"movie":movie})
