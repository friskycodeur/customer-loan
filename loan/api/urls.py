from django.urls import path, include
from rest_framework import routers
from loan.api import views

router = routers.DefaultRouter()
router.register("customer", views.CustomerListAPIView)
router.register("branch", views.BranchListAPIView)
router.register("home", views.CustomerHomeListAPIView)
router.register("office", views.CustomerOfficeListAPIView)
router.register("loan", views.LoanListAPIView)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "csv",
        views.customer_csv_upload,
        name="customer_csv_upload",
    ),
    path(
        "csv/<int:task_id>",
        views.customer_csv_upload_status,
        name="customer_csv_upload_status",
    ),
]
