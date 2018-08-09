from django.db import models
from tinymce.models import HTMLField
from apc.models import UserInfo


import uuid
# Create your models here.

#操作类型
class OptType(models.Model):
    id=models.CharField(max_length=32,primary_key=True)#自动生成主键
    optid=models.CharField(max_length=32)#操作类型id
    optname=models.CharField(max_length=40)#操作类型名称

    def __str__(self):
        return self.optname.encode('utf-8')


#操作对象表
class OptTarget(models.Model):
    id = models.CharField(max_length=32, primary_key=True)  # 自动生成主键
    targetid=models.CharField(max_length=32)#操作对象类型id
    targetname=models.CharField(max_length=40)#操作对象类型名称

#用户操作文章、说说
class UserOperate(models.Model):
    id = models.CharField(max_length=32, primary_key=True)  # 自动生成主键
    opuser=models.CharField(max_length=32)#评论人
    optime=models.DateTimeField(auto_now_add=True)#评论时间
    opcontent=HTMLField(null=True)#评论内容
    optarget=models.ForeignKey(OptTarget,on_delete=True)#操作对象类型
    optypeid=models.ForeignKey(OptType,on_delete=True)#操作类型
    delflag=models.CharField(max_length=1)#删除标记

    def __str__(self):
        return self.optuser.encode('utf-8')

#说说表
class SaySomethings(models.Model):
    id = models.CharField(max_length=32, primary_key=True)  # 自动生成主键
    saytime=models.DateTimeField(auto_now_add=True)#说说时间
    saycontent=HTMLField()#说说内容
    uid=models.ForeignKey(UserInfo,on_delete=True)#发表人
    delflag = models.CharField(max_length=1)#删除标记

    def __str__(self):
        return self.uid.encode('utf-8')
#文章类型表
class ArtcleCates(models.Model):
    id = models.CharField(max_length=32, primary_key=True)  # 自动生成主键
    acateid=models.CharField(max_length=32)#文章类型id
    acatename=models.CharField(max_length=40)#文章类型名称

    def __str__(self):
        return self.acatename.encode('utf-8')
#文章表
class Articles(models.Model):
    id = models.CharField(max_length=32, primary_key=True)  # 自动生成主键
    saytime=models.DateTimeField(auto_now_add=True)#文章发布时间
    saycontent=HTMLField()#文章发布内容
    uid=models.ForeignKey(UserInfo,on_delete=True)#发表人
    posttittle=models.CharField(max_length=40)#文章标题
    postcate=models.ForeignKey(ArtcleCates,on_delete=True)#文章类型
    articlephoto = models.ImageField(upload_to='cars/')
    delflag = models.CharField(max_length=1)#删除标记

    def __str__(self):
        return self.posttittle.encode('utf-8')

