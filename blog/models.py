from django.db import models

#for slug url
from django.utils.text import slugify

#now this Post class as all necessary func from models.Model!
class Post(models.Model):
    #fields for this table! we see that as columns in Post table
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True) #max len is 200! black true allows absence of img_url! no errors!
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    #magic method
    def __str__(self):
        return self.title