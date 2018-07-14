from django.db import models

# Create your models here.
# 创建两个字段，最大长度32,类型是char
class UserInfo (models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)