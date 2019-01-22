from disyo.models import DSApplication
from rest_framework import serializers


class DSApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DSApplication
        fields = (
	    'name',
	    'crunchbaseURI',
	    'githubContributorsCount',
	    'githubLatestCommitDate',
	    'githubStars',
	    'homepage',
	    'HQ',
	    'latestTweetDate',
	    'logoURI',
	    'organization',
	    'SVCUrl',
	    'twitterURI'
    )
