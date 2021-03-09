from django.urls import path
from egyNationalId.views import NationalIDView

urlpatterns = [
    path('', NationalIDView.as_view({'get': 'list', 'post': 'create'})),
]
