from django.db import models

# Create your models here.
class Article(models.Model):
	categories = (
		('R','russia'),
		('W','world'),
		('U','ussr'),
		('E','economics'),
		('T','science_and_tech'),
		('S','sport'),
		('C','culture'),
		)
	title = models.CharField(max_length = 200)
	preview = models.CharField(max_length = 200)
	main_text = models.TextField()
	article_image_large = models.ImageField(upload_to='static/news_site/imgs/article_images_large')
	article_image_small = models.ImageField(upload_to = 'static/news_site/imgs/article_images_small')
	desc_for_pic = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date_published')
	category = models.CharField(max_length = 200, choices = categories)

	def __unicode__(self):
		return self.title