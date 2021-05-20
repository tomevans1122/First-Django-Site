from . import views
from django.urls import path
from .views import AboutPageView # new

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('about/', AboutPageView.as_view(), name = 'about'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]