from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pandasdemo import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('pandasdemo.urls')),
    path('main/', views.main.home, name='osnova'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('csv_bef/',views.main.csv_bef),
    path('csv_del/', views.main.csv_del),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui',
    ),
]
