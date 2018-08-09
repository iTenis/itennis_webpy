from django.db import models
from apc.models import UserInfo


class RelationCates(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    relationid = models.CharField(max_length=32)  # 关系id
    relationname = models.CharField(max_length=40)  # 关系名称


class UserRelations(models.Model):
    id = models.CharField(max_length=32,primary_key=True)  # 编号
    fuid = models.ForeignKey(UserInfo, on_delete=True,related_name='rfuid_tuid')  # 主动用户
    tuid = models.ForeignKey(UserInfo, on_delete=True,related_name='rtuid_fuid')  # 被动用户
    tuname = models.CharField(max_length=40)  # 关注备注
    ftime = models.DateTimeField(auto_now=True, auto_now_add=False)  # 关注时间
    ftrelationid = models.ForeignKey(RelationCates, on_delete=True)  # 关系类别id
    delflag = models.CharField(max_length=2)  # 删除标记


class ChatInfo(models.Model):
    id = models.CharField(max_length=32,primary_key=True)  # 编号
    fuid = models.ForeignKey(UserInfo, on_delete=True,related_name='cfuid_tuid')  # 发送用户
    tuid = models.ForeignKey(UserInfo, on_delete=True,related_name='ctuid_fuid')  # 接受用户
    ftime = models.DateTimeField(auto_now=False, auto_now_add=True)  # 发送时间
    fcontent = models.CharField(max_length=32)  # 聊天内容
    isread = models.CharField(max_length=2)  # 是否阅读
    readtime = models.DateTimeField(auto_now=True, auto_now_add=False)  # 读时间
