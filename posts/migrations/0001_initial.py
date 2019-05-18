# Generated by Django 2.1.7 on 2019-03-31 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='image/post/cover/', verbose_name='封面图')),
                ('like_count', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('is_sticky', models.BooleanField(default=False, verbose_name='是否顶置')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL, verbose_name='点赞的用户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='板块名')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_topics', to=settings.AUTH_USER_MODEL, verbose_name='版主')),
            ],
            options={
                'verbose_name': '板块',
                'verbose_name_plural': '板块',
                'ordering': ('-created',),
            },
        ),
    ]
