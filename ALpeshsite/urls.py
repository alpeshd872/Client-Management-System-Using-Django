
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Hotel Admin"
admin.site.site_title = "Hotel Admin Portal"
admin.site.index_title = "Welcome Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', include('home.urls')),
    path('products/', include('home.urls')),
    path('customers/', include('home.urls')),
    path('dashboard/', include('home.urls')),


]
