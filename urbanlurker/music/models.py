from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    # logo is url
    album_logo = models.CharField(max_length = 2000)

    def __str__(self):
        return "Artist: {}\nTitle: {}\nGenre: {}".format(self.artist,self.album_title,self.genre)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)