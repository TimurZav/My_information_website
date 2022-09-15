from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'containers', views.PortView)
# router.register(r'lines', views.LineView)

urlpatterns = [
    path('', views.index, name='index'),
    path('snippets/', include(router.urls))
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('snippets/users/', views.snippet_list),
#     path('snippets/users/<int:pk>/', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)