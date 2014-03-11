from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wufoo-quizzes.apps.wufoo_responder.views.email_response', 
        name='email_response'),
    url(r'^(?P<pk>\d+)/$', apps.wufoo_responder.views.EntryView.as_view(),
        name='entry-view',),

    # Examples:
    # url(r'^quizzes/', include('quizzes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    )
