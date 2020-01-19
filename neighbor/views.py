from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import News,Neighborhood,Business,UserProfile
from .forms import NewsForm, UserProfileForm,BusinessForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    Displays the home page details such as news alerts
    '''
    news=News.objects.all()
    business=Business.objects.all()
    profile=UserProfile.objects.all()
    hood=Neighborhood.get_hood()

    return render(request,'testhome.html',{"news":news,"business":business,"profile":profile,"hood":hood})
@login_required(login_url='/accounts/login/')
def add_news(request):
    '''
    Processes news data from the form and stores it in the database
    '''
    current_user=request.user
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid:
            news=form.save(commit=False)
            news.editor=current_user
            news.save()
        return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'postnews.html', {"form":form})
@login_required(login_url='/accounts/login/')    
def single_news(request,newsid):
    '''
    Shows the details of a single alert posted
    '''
    single_post=News.single_news(newsid)

    return render(request,'singlenews.html',{"single_post":single_post})
@login_required(login_url='/accounts/login/')
def add_business(request):
    '''
    Processes business data provided and stores it in the database
    '''
    current_user=request.user
    if request.method == 'POST':
        form=BusinessForm(request.POST, request.FILES)
        if form.is_valid:
            business=form.save(commit=False)
            business.editor=current_user
            business.save()
        return redirect('home')
    else:
        form=BusinessForm()
    return render(request,'postbusiness.html',{"form":form})
@login_required(login_url='/accounts/login/')
def single_business(request,businessid):
    '''
    Shows the details of a single business that has been posted 
    '''
    single_biz=Business.single_business(businessid)

    return render(request,'singlebiz.html',{"singlebiz":single_biz})
@login_required(login_url='/accounts/login/')
def createprofile(request):
    '''
    Processes profile form data and stores in the database
    '''
    current_user=request.user
    if request.method == 'POST':
        form =UserProfileForm(request.POST, request.FILES)
        if form.is_valid:
            profile=form.save(commit=False)
            profile.editor=current_user
            profile.save()
        return redirect('home')
    else:
        form=UserProfileForm()
    return render(request,'postprofile.html',{"form":form})
@login_required(login_url='/accounts/login/')
def updateprofile(request):
    if request.method == 'POST':
        form =UserProfileForm(request.POST, request.FILES,instance=request.user.userprofile)
        if form.is_valid:
            profile=form.save(commit=False)
            profile.save()
        return redirect('home')
    else:
        form=UserProfileForm(instance=request.user.userprofile)
    return render(request,'updateprofile.html',{"form":form})

   
@login_required(login_url='/accounts/login/')
def single_profile(request,userid):
    '''
    Displays a single user profile, their business and alerts if any
    '''
    profile=UserProfile.objects.all()

    try:
        singleprofile=UserProfile.single_profile(userid)
        businessowned=Business.bizbyowner(userid)
        newsbyuser=News.newsbyuser(userid)

    except UserProfile.DoesNotExist:
        messages.info(request,'The user has not created a profile yet')

    except Business.DoesNotExist:
        messages.info(request,'The user has no business posted')

    except News.DoesNotExist:
        messages.info(request,'The user has not posted any alerts')

    return render(request,'profile.html',{"profile":profile})
@login_required(login_url='/accounts/login/')
def search_neighborhood(request):
    '''
    Searching for a neighborhood by name
    '''
    if 'neighborhood' in request.GET and request.GET["neighborhood"]:
        search_term = request.GET.get("neighborhood")
        searched_categories = Neighborhood.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'searchhood.html',{"message":message,"hoodsearched": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'searchhood.html',{"message":message})

@login_required(login_url='/accounts/login/')
def search_business(request):
    '''
    Searching for a business by name
    '''
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_categories = Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request, 'searchbiz.html',{"message":message,"bizsearched": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'searchbiz.html',{"message":message})



    

