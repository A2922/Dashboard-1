from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('transactions/', views.transactions, name='transactions'),
    path('<int:trans_id>/', views.tran_details, name = 'tran_details'),
    path("_reload_", include("django_browser_reload.urls")),
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)