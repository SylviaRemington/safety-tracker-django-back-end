from django.db import models

# Create your models here.
class Story(models.Model):
    def __str__(self):
        return f'{self.title} - {self.author}'

    # models.CharField is the data type and means "string"
    title = models.CharField(max_length=80, unique=True)
    author = models.ForeignKey(
        "authors.Author",
        related_name = "stories",
        on_delete = models.CASCADE
    )
    content = models.TextField()
    owner = models.ForeignKey(
        "authentication.User",
        related_name = "stories",
        on_delete = models.CASCADE
    )
    