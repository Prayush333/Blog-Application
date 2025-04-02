from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    

    ## 1 - 1 relationship 
    # 1 user can have only 1 profile => 1
    # 1 profile is associated to only 1 user => 1
    # OneToOneField() => Any Model


    ## 1 - M relationship
    # 1 user can add M post =>M
    # 1 post is associated to  only 1 user => 1
    # in django use ForeignKey() => use in many side Model

    ## M - M relationship
    # 1 student can learn fron M teacher => M
    # 1 teacher can teach m student => M
    # ManyToManyField() => Any place

