from django.urls import path
from .views import BlogListView,BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.views.generic import TemplateView

urlpatterns=[
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('',BlogListView.as_view(),name='blog'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
]