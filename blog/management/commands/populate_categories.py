from django.core.management.base import BaseCommand
from blog.models import Post,Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = "This command inserts category data"

    def handle(self, *args, **options):

        #delete existing data
        Category.objects.all().delete()

        categories = ['Sports','Technology','Science','Art','Food']

        for category_name in categories:
            Category.objects.create(name = category_name)
        
        self.stdout.write(self.style.SUCCESS("Data insertion successful!"))
