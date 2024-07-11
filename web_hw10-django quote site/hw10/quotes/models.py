from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=150)
    born_date = models.CharField(max_length=150)
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="superuser")

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=300, null=False, unique=True)
    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="superuser")
    