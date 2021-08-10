from django.shortcuts import (
    redirect,
    render,
)
from django.http import Http404
from django.contrib.auth.decorators import login_required
from loan.utils import csv_log_process
from loan.models import (
    BranchData,
    CSVUploadModel,
    Customer,
    CustomerHome,
    CustomerOffice,
    LoanData,
)
from loan.forms import CustomerCSVUploadModelForm
from rest_framework import permissions, viewsets
from .serializers import (
    CustomerSerializer,
    BranchSerializer,
    CustomerHomeSerializer,
    CustomerOfficeSerializer,
    LoanSerializer,
)


@login_required
def customer_csv_upload(request):
    template_name = "customer_csv_upload.html"
    context = {}
    if request.method == "POST":
        customer_upload_form = CustomerCSVUploadModelForm(
            request.POST, request.FILES
        )
        if customer_upload_form.is_valid():
            task_id = csv_log_process(
                customer_upload_form,
                "upload_loan_data_via_csv",
            )

            return redirect("customer_csv_upload_status", task_id)
        else:
            print("The uploaded CSV file is not valid.")
    else:
        customer_upload_form = CustomerCSVUploadModelForm(
            request.GET or None,
        )

    context["customer_upload_form"] = customer_upload_form

    return render(request, template_name, context)


@login_required
def customer_csv_upload_status(request, task_id):
    template_name = "customer_csv_upload_status.html"
    context = {}
    try:
        customer_file_upload_task = CSVUploadModel.objects.get(id=task_id)
    except Exception:
        raise Http404
    context["task"] = customer_file_upload_task
    return render(request, template_name, context)


class CustomerListAPIView(viewsets.ModelViewSet):
    """
    List of all customer details
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.AllowAny,)


class BranchListAPIView(viewsets.ModelViewSet):
    """
    List of all customer details
    """

    queryset = BranchData.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (permissions.AllowAny,)


class CustomerHomeListAPIView(viewsets.ModelViewSet):
    """
    List of all customerHome details
    """

    queryset = CustomerHome.objects.all()
    serializer_class = CustomerHomeSerializer
    permission_classes = (permissions.AllowAny,)


class CustomerOfficeListAPIView(viewsets.ModelViewSet):
    """
    List of all customerOffice details
    """

    queryset = CustomerOffice.objects.all()
    serializer_class = CustomerOfficeSerializer
    permission_classes = (permissions.AllowAny,)


class LoanListAPIView(viewsets.ModelViewSet):
    """
    List of all Loan details
    """

    queryset = LoanData.objects.all()
    serializer_class = LoanSerializer
    permission_classes = (permissions.AllowAny,)
