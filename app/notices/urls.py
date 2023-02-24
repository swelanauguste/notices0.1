from django.urls import path

from .api import api
from .views import (
    NoticeCreateView,
    NoticeDetailView,
    NoticeDraftedListView,
    NoticePublishedListView,
)

urlpatterns = [
    path("", NoticePublishedListView.as_view(), name="notice-list"),
    path("notice-api/", api.urls),
    path("create/", NoticeCreateView.as_view(), name="notice-create"),
    path("detail/<slug:slug>/", NoticeDetailView.as_view(), name="notice-detail"),
    path("drafted/", NoticeDraftedListView.as_view(), name="notice-drafted-list"),
]
