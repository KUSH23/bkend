from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/groups/', include('customergroups.api.urls', namespace='api-group')),
    url(r'^api/assign/', include('assignProject.api.urls', namespace='api-assign')),
    url(r'^api/projects/', include('customerprojects.api.urls', namespace='api-projects')),
    url(r'^api/o/', include('customerorders.api.urls', namespace='api-order')),
    url(r'^api/t/', include('tickets.api.urls', namespace='api-tickets')),
    url(r'^api/place/', include('place.api.urls', namespace='api-place')),
    url(r'^api/p/', include('poc.api.urls', namespace='api-poc')),

]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     url(r'^(?P<path>.*)', TemplateView.as_view(template_name='index.html'), name='home'),
# ]
