from rest_framework import serializers
from ..models import (
    Customer,
    BranchData,
    CustomerHome,
    CustomerOffice,
    LoanData,
)


class CustomerSerializer(serializers.ModelSerializer):
    """
    serializer for customer that serialize all of the fields
    based on Category model
    """

    class Meta:
        model = Customer
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    """
    serializer for Branch that serialize all of the fields
    based on Category model
    """

    class Meta:
        model = BranchData
        fields = "__all__"


class CustomerHomeSerializer(serializers.ModelSerializer):
    """
    serializer for customerHome that serialize all of the fields
    based on Category model
    """

    class Meta:
        model = CustomerHome
        fields = "__all__"


class CustomerOfficeSerializer(serializers.ModelSerializer):
    """
    serializer for customerOffice that serialize all of the fields
    based on Category model
    """

    class Meta:
        model = CustomerOffice
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    """
    serializer for Loan that serialize all of the fields
    based on Category model
    """

    class Meta:
        model = LoanData
        fields = "__all__"
