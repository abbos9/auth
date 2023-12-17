from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from login_register import settings
from user.views import reg, login, users, user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', reg, name='reg'),
    path('', login, name='login'),
    path('users/', users, name='users'),
    path('user/', user, name='user')
] + static(settings.STATIC_URL, docoment_root=settings.STATIC_ROOT)
