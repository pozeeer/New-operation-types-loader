from django.contrib import admin
from django.urls import path, include

from status_upload.views import NewTypeOperation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('status_upload.urls'))
]
