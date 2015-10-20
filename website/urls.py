from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^account/wall/$', 'website.views.wall', name='wall'),
    url(r'^account/questions/$', 'website.views.get_questions', name='questions'),
    url(r'^account/questions/(?P<pk>\d*)/$', 'website.views.make_answer', name='make_answer'),
    url(r'^(?P<email>.*)/$', 'website.views.make_question', name='make_question'),
    url(r'^$', 'website.views.home', name='home'),
    # url(r'(?P<pk>\d*)/$', 'quest.views.quest_page', name='quest_page'),




)