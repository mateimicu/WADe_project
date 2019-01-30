from django.db import models

class DSApplication(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)
    crunchbaseURI = models.URLField()
    githubContributorsCount = models.IntegerField()
    githubLatestCommitDate = models.DateTimeField()
    githubStars = models.IntegerField()
    homepage = models.URLField()
    HQ = models.TextField(max_length=1000)
    latestTweetDate = models.DateTimeField()
    logoURI = models.URLField()
    organization = models.TextField(max_length=1000)
    SVCUrl = models.URLField()
    twitterURI = models.URLField()
    category = models.TextField(max_length=1000)
    license = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
