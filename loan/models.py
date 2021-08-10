from django.db import models
from . import constants

# Create your models here.


class CustomerProfile(models.Model):
    """
    Customer Profile Model , to be inherited by Customer Model.
    """

    gender_choice_options = (("M", "Male"), ("F", "Female"), ("O", "Others"))
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=gender_choice_options)
    occupation = models.CharField(max_length=100)
    income = models.FloatField(default=0)

    class Meta:
        abstract = True


class Customer(CustomerProfile):
    """
    Customer model with all customer details.
    """

    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    loan_account_number = models.PositiveIntegerField(max_length=15)

    def __str__(self):
        return self.name


class BranchData(models.Model):
    """
    BranchData Model handles all branch details.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zone = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    branch_code = models.PositiveIntegerField(max_length=11)

    def __str__(self):
        return self.customer.name


class CustomerHome(models.Model):
    """
    CustomerHome model handles all the Customer Home details.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pincode = models.PositiveIntegerField(max_length=6)
    landmark = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)

    def __str__(self):
        return self.customer.name


class CustomerOffice(models.Model):
    """
    CustomerOffice model handles all the Customer Office details.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    office_pincode = models.PositiveIntegerField(max_length=6)
    office_landmark = models.CharField(max_length=255)
    office_address_1 = models.CharField(max_length=255)
    office_address_2 = models.CharField(max_length=255)
    office_address_3 = models.CharField(max_length=255)

    def __str__(self):
        return self.customer.name


class LoanData(models.Model):
    """
    LoanData model handles all the Loan Data details.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agreement_date = models.DateField()
    lrn = models.PositiveIntegerField()
    tenor = models.FloatField()
    adv_emi = models.IntegerField()
    mob = models.IntegerField()

    def __str__(self):
        return self.customer.name


class CSVUploadModel(models.Model):
    """
    model for uploading csv files
    """

    STATUS_CHOICES = (
        (
            constants.TASK_STATUS_YET_TO_START,
            constants.TASK_STATUS_YET_TO_START_STR,
        ),
        (
            constants.TASK_STATUS_IN_PROGRESS,
            constants.TASK_STATUS_IN_PROGRESS_STR,
        ),
        (
            constants.TASK_STATUS_COMPLETED,
            constants.TASK_STATUS_COMPLETED_STR,
        ),
        (
            constants.TASK_STATUS_FAILED,
            constants.TASK_STATUS_FAILED_STR,
        ),
    )

    STATUS_CHOICES_MAP = {
        constants.TASK_STATUS_YET_TO_START: constants.TASK_STATUS_YET_TO_START_STR,
        constants.TASK_STATUS_IN_PROGRESS: constants.TASK_STATUS_IN_PROGRESS_STR,
        constants.TASK_STATUS_COMPLETED: constants.TASK_STATUS_COMPLETED_STR,
        constants.TASK_STATUS_FAILED: constants.TASK_STATUS_FAILED_STR,
    }

    upload_file = models.FileField(upload_to="csv_uploads/")
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=0
    )

    def __str__(self):
        return "{}".format(self.id)

    @property
    def get_status_str(self):
        return self.STATUS_CHOICES_MAP.get(self.status, self.status)

    class Meta:
        db_table = "csv_uploads"
