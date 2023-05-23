from django.urls import path
from .views import Loginview, RegisterApi,UserProfileView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('UserProfileView/',UserProfileView.as_view(),name='UserProfileView'),
    path('Loginview/',Loginview.as_view(),name='Loginview'),
    path('api/register/',RegisterApi.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
