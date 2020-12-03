from django.db import models

class WebUser(models.Model):
    qr_code = models.CharField(max_length=225)

    def __str__(self):
        return self.qr_code

    class Meta:
        db_table = 'WebUser'

class Track(models.Model): 
    track_id = models.IntegerField()
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    picture_big = models.URLField()
    played = models.BooleanField()
    web_user_id = models.ForeignKey(WebUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- ' + self.artist

    class Meta:
        db_table = 'Track'
