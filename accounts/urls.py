from django.conf.urls import url
from . import views
from django.urls import path
from .views import clientList
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    # url(r'^login/$', views.login, name='login'),
	# url(r'^logout/$', views.logout, name='logout'),
	url(r'^borrower/$',clientList.as_view(), name="clientlist" ),
	url(r'^borrower/update/(?P<id>\d+)/$',views.clientUpdate, name='update_client'),
	url(r'^borrower/create/$',views.createCLient, name='create_client'),
	url(r'^borrower/delete/(?P<id>\d+)/$', views.clientDelete, name='delete_client'),
    

	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_reset'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
]                                                                         

	

