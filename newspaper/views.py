from datetime import timedelta
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from newspaper.models import Category, Post, Tag
from django.views.generic import ListView, TemplateView
from django.utils import timezone

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "aznews/home.html"
    context_object_name = "posts"

    queryset = Post.objects.filter(
        published_at__isnull=False,
        status="active",
    ).order_by("-published_at")[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_post"] = (
            Post.objects.filter(published_at__isnull=False, status="active")
            .order_by("-published_at", "-views_count")
            .first()
        )

        context["featured_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at", "-views_count")[1:4]

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_top_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active",
            published_at__gte=one_week_ago,
        ).order_by("-published_at")[:7]

        context["recent_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active",
        ).order_by("-published_at")[:7]

        context["tags"] = Tag.objects.all()[:12]
        context["categories"] = Category.objects.all()[:4]

        context["trending_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active",
        ).order_by("-views_count")[:3]

        return context


class AboutView(TemplateView):
    template_name = "aznews/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()[:12]
        context["categories"] = Category.objects.all()[:4]

        context["trending_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active",
        ).order_by("-views_count")[:3]

        return context


class PostListView(ListView):
    model = Post
    template_name = "aznews/list/list.html"
    context_object_name = "posts"
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False,
            status="active",
        ).order_by("-published_at")
