# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Game
# Create your views here.

def index (Request ):
    hey='Hello world from variable'
    games=Game.objects.all()

    return render(Request,'index.html', {'games': games})