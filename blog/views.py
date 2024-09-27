
import os.path

from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import YouTube
from django.conf import settings
import os
import assemblyai as aai
import openai

# This allows only currently logged-in users or only a user that is logged in to access a particular view. for example if we log out from
# aiBlog.html and refresh it we still can see the page
# which is bad(only logged-in user should see this page). so
# we add a library to check that. (1:49:21 in Youtube video)
from django.contrib.auth.decorators import login_required




# Create your views here.


def welcome(request):
    return render(request, 'pages/welcome.html')



# if @login_required set on top of a certain method that method needs a logged-in user to work!
@login_required # this will let only a logged-in user can have access to this page
def mainPage(request):
    return render(request, 'pages/aiBlog.html')



def signupuser(request):
    form = UserCreationForm()
    
    if request.method == 'GET':
        return render(request, 'pages/signup.html', {'form': form , 'error': ''})
    else:
        username = request.POST['username']
        email = request.POST['uEmail']
        first_password = request.POST['fPassword']
        second_password = request.POST['sPassword']

        if first_password == second_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=first_password)        # we can see the create_user parameter names by ctrl click on it
                user.save()
                login(request, user)
                return redirect('aiBlogPage')
            except IntegrityError:
                return render(request, 'pages/signup.html', {'form': form, 'error': 'User is already Signed Up!'})
        else:
            return render(request, 'pages/signup.html', {'form': form, 'error': "password didn't match"})


def loginuser(request):
    form = AuthenticationForm()
    
    if request.method == "GET":
        return render(request, 'pages/login.html', {'form': form, 'error': ""})
    else:
        username = request.POST['username']
        password =request.POST['password']

        # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'pages/login.html', {'form': form, 'error': "User not found!"})
        else:
            login(request, user)
            return redirect('aiBlogPage')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('welcomePage')



@csrf_exempt        # will pass the csrf_token to this method
def generateBlog(request):
    if request.method == "GET":
        return JsonResponse({'error': "invalid request method"}, status=405)
    else:
        try:
            data = json.loads(request.body)     # request.body is aiBlog.html line 106 body: JSON.stringify({ link: youtubeLink }) // load the json and store it in data variable.
            yt_link = data['link']              # now data is a dictionary so we get accessed to link variable in dictionary by using [''] and store the youtube link in yt_link
            return JsonResponse({'content': yt_link})
        except (KeyError, json.JSONDecodeError):    # if we have one error we dont use () but if we have 2 errors we use ()
            return JsonResponse({'error': "invalid data sent"}, status=400)

        # get yt video title
        title = yt_title(yt_link)

        # get transcript
        transcription = get_transcription(yt_link)
        if not transcription:
            return JsonResponse({'error': "failed to get transcript"}, status=500)

        # use open AI to generate the blog

        # save blog article to database

        # return blog article as a response



def yt_title(link):     # return the video title in YouTube
    yt = YouTube(link)
    title = yt.title
    return title


def download_audio(link):       # creating an audio file from YouTube link
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=settings.MEDIA_ROOT)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def get_transcription(link):
    audio_file = download_audio(link)
    aai.settings.api_key = '8379b643b26c478080c925d220ab61dc'   # go to assemblyai.com and login and take the token and enter here

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)

    return transcript.text

def allBlogs(request):

    if request.method == "GET":
        return render(request, 'pages/AllBlogs.html')


def blogDetail(request):
    pass




























