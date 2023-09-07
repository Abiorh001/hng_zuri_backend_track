from django.db import models


class ZuriApiModel(models.Model):
    slack_name = models.CharField(max_length=255)
    current_date = models.CharField(max_length=100)
    utc_now = models.DateTimeField()
    track = models.CharField(max_length=255)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()

