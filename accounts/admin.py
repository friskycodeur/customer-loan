from django.contrib import admin
from .models import User

admin.site.site_url = "/"


@admin.register(User)
class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "age",
        "date_of_birth",
        "phone_number",
    )
    search_fields = ("email", "phone_number")
    list_filter = ("age",)
