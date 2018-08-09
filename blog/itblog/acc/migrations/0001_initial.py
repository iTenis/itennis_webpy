# Generated by Django 2.0.4 on 2018-08-09 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatInfo',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('ftime', models.DateTimeField(auto_now_add=True)),
                ('fcontent', models.CharField(max_length=32)),
                ('isread', models.CharField(max_length=2)),
                ('readtime', models.DateTimeField(auto_now=True)),
                ('fuid', models.ForeignKey(on_delete=True, related_name='cfuid_tuid', to='apc.UserInfo')),
                ('tuid', models.ForeignKey(on_delete=True, related_name='ctuid_fuid', to='apc.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='RelationCates',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('relationid', models.CharField(max_length=32)),
                ('relationname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserRelations',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('tuname', models.CharField(max_length=40)),
                ('ftime', models.DateTimeField(auto_now=True)),
                ('delflag', models.CharField(max_length=2)),
                ('ftrelationid', models.ForeignKey(on_delete=True, to='acc.RelationCates')),
                ('fuid', models.ForeignKey(on_delete=True, related_name='rfuid_tuid', to='apc.UserInfo')),
                ('tuid', models.ForeignKey(on_delete=True, related_name='rtuid_fuid', to='apc.UserInfo')),
            ],
        ),
    ]