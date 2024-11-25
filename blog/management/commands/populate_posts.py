from django.core.management.base import BaseCommand
from blog.models import Post,Category
from django.utils.text import slugify
import random

class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args, **options):

        Post.objects.all().delete()

        titles = [
            "Getting Started with Django: A Beginner's Guide",
            "Django vs. Flask: Which Framework Should You Choose?",
            "Understanding Django Models: The Backbone of Your Application",
            "Building Your First Blog Application with Django",
            "Mastering Django Templates for Dynamic Content",
            "How to Use Django Admin for Rapid Application Development",
            "Best Practices for Securing Django Applications",
            "Django ORM Tips and Tricks for Efficient Querying",
            "Integrating REST APIs into Your Django Application",
            "Deploying Django Applications on Heroku",
        ]
        
        content = [
            "Django is a powerful web framework that simplifies web development...",
            "Choosing between Django and Flask can be tough...",
            "Django Models make database interactions simple...",
            "Step-by-step tutorial to build a functional blog application in Django...",
            "Templates in Django allow dynamic rendering of HTML content...",
            "Django Admin is a powerful tool for managing your application...",
            "Security is critical in web applications...",
            "Django ORM is robust and easy to use...",
            "REST APIs are essential for modern applications...",
            "Deploying your Django application is the final step...",
        ]
        
        img_urls = [
            "https://picsum.photos/seed/django1/800/400",
            "https://picsum.photos/seed/django2/800/400",
            "https://picsum.photos/seed/django3/800/400",
            "https://picsum.photos/seed/django4/800/400",
            "https://picsum.photos/seed/django5/800/400",
            "https://picsum.photos/seed/django6/800/400",
            "https://picsum.photos/seed/django7/800/400",
            "https://picsum.photos/seed/django8/800/400",
            "https://picsum.photos/seed/django9/800/400",
            "https://picsum.photos/seed/django10/800/400",
        ]

        categories = Category.objects.all()

        for title, content_text, img_url in zip(titles, content, img_urls):

            category = random.choice(categories)

            words = slugify(title).split("-")[:2]  # First two words
            slug = "-".join(words)[:50]
            
            # Ensure the slug is unique
            original_slug = slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            Post.objects.create(title=title, content=content_text, img_url=img_url, slug=slug,category=category)
        
        self.stdout.write(self.style.SUCCESS("Data has been inserted successfully!"))
