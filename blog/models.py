from django.db import models

#for slug url
from django.utils.text import slugify


#to create a relation between the blog_post & blog_categories table...we pasted this model on top!
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#now this Post class as all necessary func from models.Model!
class Post(models.Model):
    #fields for this table! we see that as columns in Post table
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True) #max len is 200! black true allows absence of img_url! no errors!
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    #magic method
    def __str__(self):
        return self.title
    

