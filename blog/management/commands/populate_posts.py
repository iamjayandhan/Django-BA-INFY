# demo data generator
from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args:Any, **options: Any):
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
            "Django is a powerful web framework that simplifies web development. This guide walks you through setting up your first project and understanding its core components.",
            "Choosing between Django and Flask can be tough. This post compares the two frameworks, highlighting their features, pros, and cons to help you decide.",
            "Django Models make database interactions simple. Learn how to define models, create relationships, and manage your database effectively.",
            "Step-by-step tutorial to build a functional blog application in Django. Learn about models, views, templates, and how they work together.",
            "Templates in Django allow dynamic rendering of HTML content. This post explores template tags, filters, and inheritance for building reusable templates.",
            "Django Admin is a powerful tool for managing your application. Learn how to customize it to suit your needs and speed up development.",
            "Security is critical in web applications. This post covers best practices for protecting your Django application against common vulnerabilities.",
            "Django ORM is robust and easy to use. Discover tips and tricks for writing efficient queries and optimizing database performance.",
            "REST APIs are essential for modern applications. Learn how to use Django Rest Framework (DRF) to integrate APIs into your project.",
            "Deploying your Django application is the final step. This guide shows how to deploy a Django app on Heroku, including configuring settings and managing databases.",
        ]

        img_urls = [
            "https://picsum.photos/seed/django1/800/400",  # Getting Started with Django
            "https://picsum.photos/seed/django2/800/400",  # Django vs. Flask
            "https://picsum.photos/seed/django3/800/400",  # Understanding Django Models
            "https://picsum.photos/seed/django4/800/400",  # Building Your First Blog Application
            "https://picsum.photos/seed/django5/800/400",  # Mastering Django Templates
            "https://picsum.photos/seed/django6/800/400",  # Using Django Admin
            "https://picsum.photos/seed/django7/800/400",  # Securing Django Applications
            "https://picsum.photos/seed/django8/800/400",  # Django ORM Tips
            "https://picsum.photos/seed/django9/800/400",  # Integrating REST APIs
            "https://picsum.photos/seed/django10/800/400", # Deploying Django on Heroku
        ]

        for title, content, img_url in zip(titles,content,img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))

        