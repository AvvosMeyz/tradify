from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import models


@login_required(login_url="login/")
def index(request):
    try:
        tradify = (User.objects
                   .exclude(id=request.user.id)
                   .exclude(uservote__voter=request.user)
                   .order_by('?')[0])
    except IndexError:
        tradify = None
    context = dict(tradify=tradify)

    return render(request, 'index.html', context)

def create_vote(request, user_id, vote):
    user = User.objects.get(pk=user_id)
    models.UserVote.objects.create(
        user=user,
        voter=request.user,
        vote=vote,
    )
    if vote:
        if models.UserVote.objects.filter(
            user=request.user,
            voter=user,
            vote=True,
        ).count():
            return render(request, 'match.html', dict(
                match=user,
            ))
    return redirect('index')

@login_required
def nice(request, user_id):
    return create_vote(request, user_id, True)

@login_required
def nope(request, user_id):
    return create_vote(request, user_id, False)
