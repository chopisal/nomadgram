from django.conf.urls import url
from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/comment/',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    )
]
