from django.urls import path
from .views import home, detail, ArticleAdd

urlpatterns = [
    path('', home, name='home'),
    path('add_article/', ArticleAdd.as_view(), name='add_article'),
    path('article/<int:pk>/', detail, name='detail'),
]
