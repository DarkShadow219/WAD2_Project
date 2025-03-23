from django.db import models
from django.contrib.auth.models import User
#TODO: Create model,Population Script.

class UserProfile(models.Model):
    #TODO: add other related fields 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Subject(models.Model):
    # comment
    subject_id = models.AutoField(primary_key=True, unique=True)
    subject_name = models.CharField(max_length=128)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="subjects")
    
    def __str__(self):
        return self.subject_name


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True, unique=True)
    topic_name = models.CharField(max_length=128)
    learning_score = models.IntegerField(default=0)
    study_next = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topics")
    
    def __str__(self):
        return self.topic_name


class Card(models.Model):
    card_id = models.AutoField(primary_key=True, unique=True)
    card_front = models.TextField()
    card_back = models.TextField()
    confidence_level = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="cards")
    
    def __str__(self):
        return f"Front: {self.card_front}\nBack: {self.card_back}"
    


class Explanation(models.Model):
    explain_id = models.AutoField(primary_key=True, unique=True)
    ai_explanation = models.TextField()
    #TODO: set as int instaed of time depending on implementaion it will be edited.
    ai_explanation_date = models.IntegerField(default=0)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="explanations")
    
    def __str__(self):
        return self.ai_explanation

