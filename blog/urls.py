from django.urls import path
from blog.views import BlogDetailsView,BlogView
from blog.views import BlogSearchview

urlpatterns = [
    path('Blogview/',BlogView.as_view(),name='BlogView'),
    path('BlogDetailsView/<int:pk>/',BlogDetailsView.as_view(),name='BlogDetailsView'),
    path('BlogSearchview/<str:pk>/',BlogSearchview.as_view(),name='BlogSearchview'),
]
