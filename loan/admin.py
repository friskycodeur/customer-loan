from django.contrib import admin
from .models import (
    Customer,
    CustomerHome,
    CustomerOffice,
    BranchData,
    LoanData,
)

# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerHome)
admin.site.register(CustomerOffice)
admin.site.register(BranchData)
admin.site.register(LoanData)
