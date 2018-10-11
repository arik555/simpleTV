from django.db import models

# Create your models here.
class Live(models.Model):
	channel_title = models.CharField(max_length=150, blank=False, null=False)
	channel_description = models.CharField(max_length=500, blank=True, null=False)
	channel_link = models.URLField(max_length=1000, blank=False, null=False)
	channel_icon = models.URLField(max_length=1000, blank=True, null=False)
	mobile_compatibility = models.BooleanField(default=True)

	def __str__(self):
		return self.channel_title

	def get_channel_good_name(self):
		good_name = self.channel_title.replace(" ", '_')
		return good_name


class StarJalsha(models.Model):
	serial_name = models.CharField(max_length=100, blank=False)
	serial_link = models.URLField(max_length=1000, blank=False)
	timeStamp = models.DateField(auto_now_add=True)
	activate = models.BooleanField(default=True)
	mobile_compatibility = models.BooleanField(default=True)

	def __str__(self):
		return self.serial_name

	def get_todays_link(self):
		import re, datetime
		today = datetime.date.today()
		if datetime.datetime.now().hour < 18:
			counter = (today - self.timeStamp).days - 1
		else:
			counter = (today - self.timeStamp).days
		ep_no = re.search('[\d]+', self.serial_link)
		n = int(ep_no.group()) + counter
		main_link = self.serial_link.replace(ep_no.group(), str(n))
		return main_link
