from django.db import models

# Create your models here.
class Series(models.Model):
	series_title = models.CharField(max_length=200, blank=False)
	series_season = models.CharField(max_length=10, blank=True)
	series_icon = models.URLField(max_length=1000, blank=False)
	series_language = models.CharField(choices=[('1', 'English'),('2', 'Hindi'),('3','Bengali'),('4', 'Other')], max_length=1, default='2')
	mobile_compatibility = models.BooleanField(default=True)

	def __str__(self):
		return self.series_title+' S'+self.series_season

class Episode(models.Model):
	series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='allepisodes')
	episode_no = models.CharField(max_length=12, blank=True)
	episode_title = models.CharField(max_length=200, blank=True)
	episode_link = models.CharField(max_length=1000, blank=False)
	compatible = models.CharField(choices=[('0', 'None'), ('1', 'Clappr'),('2', 'YouTube'),('3', 'OpenLoad')], max_length=1, default='3')

	def __str__(self):
		return self.episode_title + ' - ' + self.episode_no