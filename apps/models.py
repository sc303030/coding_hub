from typing import Dict

from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(verbose_name="생성날짜", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정날짜", auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    title = models.CharField(verbose_name="제목", max_length=100)
    text = models.TextField(verbose_name="본문")
    relation_posts = models.ManyToManyField(
        "self",
        verbose_name="연관게시글",
        blank=True,
        related_name="relation_post",
        symmetrical=False,
    )
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    @staticmethod
    def extract_tag_dict(text) -> Dict:
        tag_name_list = text.split(" ")
        tag_dict = {}
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_dict[tag.pk] = tag
        return tag_dict

    def get_absolute_url(self):
        return reverse("apps:post_detail", args=[self.pk])


class Tag(TimestampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
