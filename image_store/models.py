from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    image = models.ImageField(upload_to='image_store/')
    upvotes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class CommentManager(models.Manager):
    def get_comments_for_post(self, Post):
        comments = Comment.objects.filter(post_id=Post.id)
        return comments


class Comment(models.Model):
    text = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    objects = CommentManager()


class UserUpvoteManager(models.Manager):
    def can_user_upvote(self, Post, User):
        return not UserUpvote.objects.filter(post_id=Post.id).filter(user_id=User.id).exists()


class UserUpvote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    objects = UserUpvoteManager()
