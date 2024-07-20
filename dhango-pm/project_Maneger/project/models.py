from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.
from django.utils.translation import gettext

    

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    class Mete:
        verbose_name=gettext('Categorys')
        verbose_name_plural=gettext('Categorys')
    

class projectStatus(models.IntegerChoices):
    PENDING=1,gettext("pending")
    COMPLETED=2,gettext("completed")
    POSTPOEND=3,gettext("postpoend")
    CANCELED=4,gettext("canceled")



class Project(models.Model):
    title=models.CharField(null=False)
    descreption=models.TextField()
    satutes=models.IntegerField(
        choices=projectStatus.choices,
        default=projectStatus.PENDING
    )
    created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.title
    class Mete:
        verbase_name=gettext('Project')
        verbase_name_plural=gettext('Project')
    

class Task(models.Model):
    descreption=models.TextField()
    is_completed=models.BooleanField(default=False)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.descreption
    



