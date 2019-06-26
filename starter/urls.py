from django.contrib import admin
from django.urls import include, path
from starter import views
import allauth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    # path('blog/', include('blog.urls')),
]
