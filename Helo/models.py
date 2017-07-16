# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Team(models.Model):
    TeamName  = models.CharField(max_length=100)
    TeamLogo  = models.URLField
    def __str__(self):
        return str(self.TeamName)

class Game(models.Model):
    pass
    LeftTeam  = models.ForeignKey(Team,related_name='%(class)s_left_team',on_delete=models.CASCADE)
    RightTeam = models.ForeignKey(Team,related_name='%(class)s_Right_Team',on_delete=models.CASCADE)
    Winer     = models.ForeignKey(Team,related_name='%(class)s_Winner_Team',on_delete=models.CASCADE)

