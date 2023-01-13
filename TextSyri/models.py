from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

CATEGORY = (('Mix', 'Mix'), ('Love', 'Love'), ('Dosti', 'Dosti'), ('Wish', 'Wish'), ('Sad', 'Sad'), ('Dhokha', 'Dhokha'),
            ('Alone', 'Alone'), ('BreakUp', 'BreakUp'), ('Bhakti', 'Bhakti'), ('Deshbhakti', 'Deshbhakti'), ('Thought', 'Thought'))


class AllShayari(models.Model):
    category = models.CharField(max_length=25, choices=CATEGORY)
    tag = models.CharField(max_length=45)
    content = models.TextField()
    author = models.CharField(max_length=25)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} -{self.category} - {self.dt}"


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f" {self.first_name} - {self.dt} "
