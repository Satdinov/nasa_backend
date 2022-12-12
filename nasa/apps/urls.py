from django.urls import path

from nasa.apps.views import GetInfoView, SaveToDBView

app_name = 'search'
urlpatterns = [
    path('search/', GetInfoView.as_view(), name='search'),
    path('save/', SaveToDBView.as_view(), name='search'),
]