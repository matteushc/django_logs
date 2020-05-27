from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'logs', views.LogsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('lista/', views.IndexView.as_view(), name='lista'),
    path('buscar/', views.LogsView.as_view(), name='buscar'),
    path('buscar_log/', views.your_view, name='buscar_log'),
]