from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)                 # book title
    author = models.CharField(max_length=100)                # author name
    description = models.TextField(blank=True, null=True)    # book description
    published_date = models.DateField(blank=True, null=True) # optional published date
    isbn = models.CharField(max_length=13, unique=True)      # ISBN number
    available = models.BooleanField(default=True)           # availability status
    created_at = models.DateTimeField(auto_now_add=True)    # record creation timestamp

    def __str__(self):
        return f"{self.title} by {self.author}"