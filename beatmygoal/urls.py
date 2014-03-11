from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

import core.views

urlpatterns = patterns('',

	# Examples:
	# url(r'^$', 'beatmygoal.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^$', core.views.index),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
	url(r'^goals/create', core.views.goal_create_goal, name='goal_create_goal'),
	url(r'^goals/remove', core.views.goal_remove_goal, name='goal_remove_goal'),
	url(r'^goals/edit', core.views.goal_edit_goal, name='goal_edit_goal'),

	url(r'^users/create', core.views.create_user, name='create_user'),

	url(r'^users/(\d)+/edit', core.views.edit_user, name='edit_user'),
	url(r'^users/(\d)+/$', core.views.view_user, name='view_user'),
	url(r'^users/login', core.views.user_login, name='user_login'),
	url(r'^users/logout', core.views.user_logout, name='user_logout'),
	
	url(r'^users/test/$', core.views.test_user),
	url(r'^users/test/view', core.views.view_user2),
	url(r'^users/test/edit', core.views.edit_user2),                       
    

)
