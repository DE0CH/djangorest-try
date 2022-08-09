from django.urls import path, include

from django.contrib import admin

from rest_framework import routers

admin.autodiscover()

import hello.views
import restapi.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


rest_router = routers.DefaultRouter()
rest_router.register(r'users', restapi.views.UserViewSet)
rest_router.register(r'groups', restapi.views.GroupViewSet)


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("api/", include(rest_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
