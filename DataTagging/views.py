from django.shortcuts import render, redirect
from django.contrib import auth
# from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from inputs.models import Input
from records.models import Record
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import *

# github_login, twitter_login, facebook_login = None
def get_account(request):
    user = request.user
    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    return github_login, twitter_login, facebook_login, google_login
def index(request):
    random_text = Input.objects.order_by('?')[0]
    return render(request, 'index.html', {'texts':random_text})

@login_required
def homePost(request, text_id):
    github_login, twitter_login, facebook_login, google_login = get_account(request)
    if request.method == 'POST':
        innput = get_object_or_404(Input, pk=text_id)
        temp_accuracy = 0.0
        total = innput.happy + innput.sad + innput.stupefied + innput.angry + innput.others + 1
        if request.POST.get('expression') == "1":
            innput.happy += 1
            temp_accuracy = innput.happy / total
        elif request.POST.get('expression') == "2":
            innput.sad += 1
            temp_accuracy = innput.sad / total
        elif request.POST.get('expression') == "3":
            innput.stupefied += 1
            temp_accuracy = innput.stupefied / total
        elif request.POST.get('expression') == "4":
            innput.angry += 1
            temp_accuracy = innput.angry / total
        elif request.POST.get('expression') == "5":
            innput.others += 1
            temp_accuracy = innput.others / total
        innput.save()

        user = User.objects.get(pk=request.user.pk)
        record = Record.objects.filter(user=request.user)
        print("RECORD:::: ")
        print(record)
        if not record:
            record = Record(user=user)
            record.save()
        record = Record.objects.get(user_id=user.id)
        record.total_tags += 1
        record.total_accuracy = Decimal(record.total_accuracy) +  Decimal(temp_accuracy)
        record.accuracy = Decimal(record.total_accuracy) / Decimal(record.total_tags)
        record.accuracy = Decimal(record.accuracy) * Decimal(100.0)
        record.save()

    else:
        pass
    random_text = Input.objects.order_by('?')[0]
    return render(request, 'index.html', {
                            'texts':random_text,
                            'github_login': github_login,
                            'twitter_login': twitter_login,
                            'facebook_login': facebook_login,
                            'google_login':google_login
                        })



@login_required
def settings(request):
    user = request.user
    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    random_text = Input.objects.order_by('?')[0]
    return render(request, 'index.html', {
        'texts':random_text,
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'google_login':google_login,
    })

@login_required
def leaderBoard_default(request):
    current_user = request.user
    records = Record.objects.all().order_by('-total_tags')
    # zippedList = zip(users, records)
    return render(request, 'leaderboard.html', {'current_user':current_user, 'records':records})


@login_required
def leaderBoard_by_accuracy(request):
    current_user = request.user
    records = Record.objects.all().order_by('-accuracy', '-total_tags')
    # zippedList = zip(users, records)
    return render(request, 'leaderboard.html', {'current_user':current_user, 'records':records})

def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


# @login_required
# def password(request):
#     if request.user.has_usable_password():
#         PasswordForm = PasswordChangeForm
#     else:
#         PasswordForm = AdminPasswordChangeForm

#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordForm(request.user)
#     return render(request, 'password.html', {'form': form})