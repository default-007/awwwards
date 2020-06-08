from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('project/<post>', views.project, name='project'),
    path('search/', views.search_project, name='search'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="myawards/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="myawards/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="myawards/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="myawards/password_reset_done.html"), 
        name="password_reset_complete"),
]