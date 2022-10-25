from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.routers import SimpleRouter

from .api import post, profile, info, follow, authentication

app_name = 'backend'

router = SimpleRouter()
router.register(r'api_v1', post.PostViewSet)

urlpatterns = [
    # user logging and administration
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('signup/', authentication.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('ajax/validate_username/', authentication.validate_username, name='validate_username'),
    path('api-auth/', include('rest_framework.urls')),


    path(r'^', include(router.urls)),
    path('api/post/rate/', post.PostRateViewSet.as_view(), name='rate'),
    path('api/post/rating/<int:pk>/', post.PostRateViewSet.as_view(), name='rating'),
    path('api/post/retrieve-comments/<int:pk>/', post.CommentList.as_view(), name='retrieve-comments'),
    
    path('api/profile/', profile.ProfileViewSet.as_view(), name='profile-change'),
    path('api/profile/<int:pk>/', profile.ProfileViewSet.as_view(), name='profile-retrieve'),
    
    path('api/follow/<int:pk>/', follow.follow, name='follow'),
    path('api/following/<int:pk>/', follow.Following.as_view(), name='following'),
    path('api/followers/<int:pk>/', follow.Followers.as_view(), name='followers'),
]
