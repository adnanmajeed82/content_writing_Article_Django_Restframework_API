from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Article Content writing API",
      default_version='v1',
      description="AdnanMajeed API",
      terms_of_service="https://computerlearningcenter.website2.me",
      contact=openapi.Contact(email="adnanmajeed82@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Replace 'your_app' with the name of your Django app
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
