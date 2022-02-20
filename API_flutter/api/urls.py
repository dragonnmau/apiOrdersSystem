from django.urls import URLPattern, path
from api.views import userView

urlpatterns = [
    path('users/', userView.as_view(), name='users'),
    path('users/<int:id>', userView.as_view(), name='userSearch')
]
