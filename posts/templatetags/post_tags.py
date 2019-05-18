# encoding: utf-8
"""
@desc: 帖子模板标签
"""

from django import template

from ..models import Post, Topic

register = template.Library()


@register.simple_tag
def get_topic_list():
    """
    获取板块列表
    :return:
    """
    return Topic.objects.all().order_by('created')


@register.simple_tag
def get_hot_posts(count=8):
    """
    获取热门帖子列表
    :param count: 默认帖子数量
    :return:
    """
    return Post.objects.order_by('-like_count')[:count]


@register.simple_tag
def get_all_posts():
    """
    获取帖子列表
    :return:
    """
    return Post.objects.order_by('-is_sticky','-created')


@register.simple_tag
def check_is_like_post(post_id, user):
    """
    检查用户是否已经点赞了帖子
    :param post_id:
    :param user:
    :return:
    """
    return Post.objects.filter(id=post_id, like_users=user).exists()


