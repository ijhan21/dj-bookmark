from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank = True) # verbos name : 별칭
    url = models.URLField('URL', unique=True)
    def __str__(self):
        # return self.title # __str__ 함수는 객체를 문자열로 표현할 때 사용하는 함수
        return "%s %s"%(self.title, self.url)