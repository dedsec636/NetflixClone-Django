from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField(null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created=models.TimeField(auto_now_add=True)
    movie_file=models.FileField(upload_to='movies/')
    movie_thumbnail=models.ImageField(upload_to='thumbnail/')
    watch_count=models.IntegerField(default=0)
    
    def __str__(self):
        return self.movie_name
    