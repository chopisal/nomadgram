from django.urls import path

from nomadgram.users.views import (
    explore_users_view,
    # user_redirect_view,
    # user_update_view,
    # user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("explore", view=explore_users_view, name="explore_users"),
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
