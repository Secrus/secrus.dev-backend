from django.db import models
import datetime


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    publication_date = models.DateTimeField(blank=True, null=True)



    def publish(self):
        self.publication_date = datetime.datetime.now()
        self.save()


    def __str__(self):
        return self.title
