from django.urls import path, include
from rest_framework import routers

from store.views import ProductView

router = routers.DefaultRouter()
router.register("resources", ProductView)

urlpatterns = [
    path('', include(router.urls)),
]
