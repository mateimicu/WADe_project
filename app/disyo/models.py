from django.db import models

class DSApplication(models.Model):
    name = models.CharField(max_length=1000, primary_key=True)
    crunchbaseURI = models.URLField()
    githubContributorsCount = models.IntegerField()
    githubLatestCommitDate = models.DateTimeField()
    githubStars =  models.IntegerField()
    homepage = models.URLField()
    HQ = models.TextField()
    latestTweetDate = models.DateTimeField()
    logoURI = models.URLField()
    organization = models.TextField()
    SVCUrl = models.URLField()
    twitterURI = models.URLField()
    category = models.TextField()
    license = models.TextField()
