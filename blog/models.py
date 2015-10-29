from django.db import models
from django.utils import timezone
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USZipCodeField


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Model for Race events hosted by an organizer
class Races(models.Model):

    # Tuple for all the race types
    RACE_TYPES = (
        ('RA', 'Stage Rally'),
        ('RX', 'RallyCross'),
        ('TX', 'Tarmac RallyCross'),
        ('EX', 'Enduro RallyCross'),
        ('AX', 'Autocross'),

    )
    # TUPLE FOR United States
    STATES = US_STATES

    # Fields for Races Object
    organizer = models.ForeignKey('auth.User')
    race_type = models.CharField(max_length=2, choices=RACE_TYPES)
    event_name = models.CharField(max_length=30)
    event_details = models.TextField()
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=5)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATES)
    zip = USZipCodeField(null=True)
    max_entries = models.CharField(max_length=3)
    posted_date = models.DateTimeField(default=timezone.now)
    race_date = models.DateTimeField(blank=True, null=True)
    # country

    def __str__(self):
        return self.event_name
