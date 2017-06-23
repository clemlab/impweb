from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User, UserManager


class UserProfile(AbstractBaseUser):
    # Links UserProfile to a User model instance
    objects = UserManager()

    # The additional attributes we wish to include
    username = models.CharField(max_length=100, default='some_rando')
    institution = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    job_priority = models.IntegerField(default=-100)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username


class Seq(models.Model):
    seqid = models.TextField()
    nucseq = models.TextField()

    def __str__(self):
        return self.nucseq


class Predictor(models.Model):
    name = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.name


class SeqPred(models.Model):
    user = models.ForeignKey(User)
    seq = models.ForeignKey(Seq)
    pred = models.ForeignKey(Predictor)

    views = models.IntegerField(default=0)

    def __str__(self):
        return "{user}_{seq}_{pred}".format(
            User, Seq, Predictor)
