# Generated by Django 2.1.7 on 2019-04-01 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0003_post_view_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('like_count', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_reply', to=settings.AUTH_USER_MODEL, verbose_name='点赞的用户')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='reviews.Reply')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('like_count', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_comments', to=settings.AUTH_USER_MODEL, verbose_name='点赞的用户')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.Post', verbose_name='所属帖子')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_replies', to='reviews.Review', verbose_name='评论'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reply', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
