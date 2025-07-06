from django.db import models
from django.contrib.auth.models import User

class SurveyResponse(models.Model):
    age_group = models.CharField(max_length=50)
    gender_identity = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    stress_level = models.CharField(max_length=10)
    peer_support_availability = models.CharField(max_length=50)
    comfort_level = models.CharField(max_length=50)
    stress_sources = models.CharField(max_length=100)
    used_peer_support = models.CharField(max_length=10)
    reason_not_seeking = models.TextField(blank=True)
    societal_stance = models.CharField(max_length=100)
    desired_features = models.TextField()
    opinion_on_app = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gender_identity} | {self.age_group}"
    


