from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    text = models.CharField(max_length=1000)
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved = True)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk':self.pk})

    def __str__(self):
        return f"{self.title} - {self.author}"


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments') #change on_delete later because you cant delete the entire post once you delete a comment
    author = models.CharField(max_length=1000)
    text = models.CharField(max_length=1000)
    create_date = models.DateTimeField(default = timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text[:50]













