from django.conf.urls import patterns, url

from loginsys import views

urlpatterns = patterns('',
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^registration/', views.registration, name='registration'),
    # url(r'^agreement/', views.agreement, name='agreement'),
    # url(r'^agreement_user/', views.agreement_user, name='agreement_user'),
)