# Generated by Django 2.1.4 on 2019-01-18 11:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0008_topic_aboutblogs_num'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0005_auto_20190110_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100, verbose_name='评论')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniblog.MiniBlog', verbose_name='微博')),
                ('reply_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_user', to=settings.AUTH_USER_MODEL, verbose_name='评论的人')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
