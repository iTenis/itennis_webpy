from django.db import models
from tinymce.models import HTMLField

#用户角色表
class UserRoles(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    roleid = models.CharField(max_length=32)#角色id
    rolename = models.CharField(max_length=40)#角色名称
    def __str__(self):
        return self.rolename

#用户登录表
class UserCheck(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    uname = models.CharField(max_length=32)#登录id
    upwd = models.CharField(max_length=50)#登录密码
    uroleid = models.ForeignKey(UserRoles,on_delete=True)#角色
    delflag = models.CharField(max_length=2)#删除标记

#状态信息表
class StatusFlag(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    sfid = models.CharField(max_length=32)#状态id
    sfname = models.CharField(max_length=40)#状态名称
    def __str__(self):
        return self.sfname

#用户信息表
class UserInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    ufullname = models.CharField(max_length=40)#用户名称
    ucheckid = models.ForeignKey(UserCheck,on_delete=True)#关联登录表id
    uphoto = models.CharField(max_length=200)#用户头像
    umail = models.CharField(max_length=100)#邮箱
    uphone = models.CharField(max_length=20,null=True)#电话
    uqq = models.CharField(max_length=20,null=True)#QQ
    uregtime = models.DateTimeField(auto_now=False, auto_now_add=True)#注册时间
    usexid = models.CharField(max_length=1,null=True)#性别
    ubrith = models.DateTimeField(auto_now=True, auto_now_add=False,null=True)#生日
    upage = HTMLField(null=True)#主页
    ujob = models.CharField(max_length=200,null=True)#职业
    utaste = models.CharField(max_length=200,null=True)#兴趣
    ueducation = models.CharField(max_length=200,null=True)#教育程度
    ulanguage = models.CharField(max_length=200,null=True)#语言
    uregion = models.CharField(max_length=100,null=True)#区域
    uaddress = models.CharField(max_length=200,null=True)#地址
    ubrief = HTMLField(null=True)#个人简介
    ustatusid = models.ForeignKey(StatusFlag,on_delete=True)#用户状态
