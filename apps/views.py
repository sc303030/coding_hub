from django.db.models import (
    Prefetch,
    Count,
    F,
    FloatField,
)
from django.db.models.functions import Cast
from apps.forms import PostForm
from apps.models import Post, Tag
from django.shortcuts import render, redirect, get_object_or_404


def post(request):
    post_list = Post.objects.all()
    return render(request, "apps/post.html", {"post_list": post_list})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            tag_dict = Post.extract_tag_dict(post.text)
            post_qs = Post.objects.exclude(pk=post.pk)
            tag_qs = Tag.objects.filter(pk__in=tag_dict.keys()).prefetch_related(
                Prefetch("post_set", queryset=post_qs, to_attr="tag_in_post")
            )
            under_40_tag = tag_qs.annotate(
                count=Count("post"),
                qs_count=Cast(post_qs.count(), FloatField()),
                percent=Cast((F("count") / F("qs_count")) * 100.0, FloatField()),
            ).filter(percent__lte=40)
            candidate_post = post_qs.filter(tag_set__in=under_40_tag).prefetch_related(
                Prefetch(
                    "tag_set",
                    queryset=under_40_tag,
                    to_attr="under_40_tag",
                )
            )
            post_list = candidate_post.annotate(tag_cnt=Count("tag_set")).filter(
                tag_cnt__gte=2
            )
            post.tag_set.add(*tag_dict.values())
            post.relation_posts.add(*post_list)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, "apps/post_form.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = post.tag_set.all()
    post_qs = post.relation_posts.prefetch_related(Prefetch("tag_set", queryset=tags))
    relation_list = post_qs.annotate(tag_cnt=Count("tag_set")).order_by("-tag_cnt")
    return render(
        request, "apps/post_detail.html", {"post": post, "relation_list": relation_list}
    )