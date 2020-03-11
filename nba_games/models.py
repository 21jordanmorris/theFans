from django.db import models
from datetime import date

class Game(models.Model):
    date = models.DateField()
    home_team = models.CharField(max_length=3)
    visitor_team = models.CharField(max_length=3)
    home_score = models.IntegerField(null=True, blank=True)
    visitor_score = models.IntegerField(null=True, blank=True)
    home_probability = models.FloatField()
    visitor_probability = models.FloatField()

    REQUIRED_FIELDS = ['date', 'home_team', 'visitor_team', 'home_probability', 'visitor_probability']

    def __str__(self):
        game = self.home_team + '/' + self.visitor_team
        return game
    
    @property
    def is_today(self):
        return date.today() == self.date
    
    @property
    def get_today(self):
        return str(date.today())
    
    @property
    def get_prob_for_circle(self):
        home_prob = float(self.home_probability/100)
        return  (314.16 * (1 - home_prob))