from django.db import models
from django.contrib.auth.models import User


class TagManager(models.Manager):
    def get_all_tags(self):
        tags = Tag.objects.all()
        return tags

    def get_tag(self, tagName):
        tag = Tag.objects.get(name=tagName)
        print(type(tag))
        return tag


class Tag(models.Model):
    name = models.CharField(max_length=30)
    objects = TagManager()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    image = models.ImageField(upload_to='image_store/')
    upvotes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User)

    def __str__(self):
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
        return not UserUpvote.objects.filter(post_id=Post.id).filter(
            user_id=User.id).exists()


class UserUpvote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    objects = UserUpvoteManager()
