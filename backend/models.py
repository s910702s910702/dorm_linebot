from django.db import models

# Create your models here
class Ppl(models.Model):
    name = models.CharField(max_length=50)
    sid = models.CharField(max_length=50, unique = True)
    grade = models.CharField(max_length=50)
    pnum = models.CharField(max_length=50)
    rnum = models.CharField(max_length=50)
    lineuid = models.CharField(max_length=50, null = True)
    secret = models.CharField(max_length=50, null = True)       #not true
    def __str__(self):
        return self.name + "_" + self.sid

class Acc(models.Model):
	un = models.CharField(max_length=100)
	pw = models.CharField(max_length=500)
	
	# 1 - 5, 5 for boss
	lvl = models.IntegerField()