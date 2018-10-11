from django.db import models

# Create your models here.
class Movie(models.Model):
	movie_title = models.CharField(max_length=150, blank=False, null=False)
	movie_trailer = models.URLField(max_length=1000, blank=False, null=False)
	movie_poster = models.URLField(max_length=1000, blank=False, null=False)
	movie_link = models.CharField(max_length=1000, blank=False, null=False)
	movie_genre = models.CharField(max_length=150, default='Unknown', blank=False, null=False)
	movie_year = models.IntegerField(default=0)
	movie_language = models.CharField(choices=[('1', 'English'),('2', 'Hindi'),('3', 'Bengali'), ('4', 'Other')], max_length=1, default='2')
	compatible = models.CharField(choices=[('0', 'None'), ('1', 'Clappr'),('2', 'YouTube'),('3', 'OpenLoad')], max_length=1, default='1')
	mobile_compatibility = models.BooleanField(default=True)

	def __str__(self):
		return self.movie_title

	def get_movie_good_name(self):
		good_name = self.movie_title.replace(" ", '_')
		return good_name