from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuCreateView, MenuTodayListView

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("restaurants/<int:restaurant_id>/menus/", MenuCreateView.as_view(), name="menu-create"),
    path("menus/today/", MenuTodayListView.as_view(), name="menu-today"),
]
