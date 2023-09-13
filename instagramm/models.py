from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class AbstractPost(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # user = models.ForeignKey('account.User', on_delete=models.CASCADE)

    # from django.contrib.auth.models import User
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Post(AbstractPost):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Comment(AbstractPost):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment - {self.post.title}'
