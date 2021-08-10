import csv
import os
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from loan import constants
from loan.models import CSVUploadModel
from loan.models import (
    Customer,
    CustomerOffice,
    CustomerHome,
    BranchData,
    LoanData,
)


class Command(BaseCommand):
    """
    python manage.py upload_loan_data_via_csv 1

    """

    help_text = "Bulk upload Customer data via CSV"

    def add_arguments(self, parser):
        parser.add_argument("task_id", nargs="?", help="Specify the task id")

    def main_task(self):
        self.task_instance.status = constants.TASK_STATUS_IN_PROGRESS
        self.task_instance.save()
        self.file_path = str(self.task_instance.upload_file)
        with open(
            os.path.join(settings.MEDIA_ROOT, self.file_path)
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    customer_instance = Customer.objects.get(
                        loan_account_number=row["lan"]
                    )

                except Customer.DoesNotExist:
                    customer_instance = Customer(
                        loan_account_number=row["lan"],
                        name=row["name"],
                        father_name=row["father_name"],
                        age=row["age"],
                        education=row["education"],
                        gender=row["gender"],
                        occupation=row["occupation"],
                        income=row["income"],
                    )
                    customer_instance.save()

                except Exception as e:
                    print("Customer Creation failed due to {}".format(e))

                try:
                    branchdata_instance = BranchData(
                        customer=customer_instance
                    )
                except BranchData.DoesNotExist:
                    branchdata_instance = BranchData(
                        customer=customer_instance,
                        zone=row["zone"],
                        region=row["region"],
                        area=row["area"],
                        branch_name=row["branch_name"],
                        branch_code=row["branch_code"],
                    )
                    branchdata_instance.save()
                try:
                    branchdata_instance = CustomerHome(
                        customer=customer_instance
                    )
                except CustomerHome.DoesNotExist:
                    customerhome_instance = CustomerHome(
                        customer=customer_instance,
                        pincode=row["pincode"],
                        landmark=row["landmark"],
                        address_1=row["address_1"],
                        address_2=row["address_2"],
                        address_3=row["address_3"],
                    )
                    customerhome_instance.save()
                try:
                    branchdata_instance = CustomerOffice(
                        customer=customer_instance
                    )
                except CustomerOffice.DoesNotExist:
                    customeroffice_instance = CustomerOffice(
                        customer=customer_instance,
                        office_pincode=row["office_pincode"],
                        office_landmark=row["office_landmark"],
                        office_address_1=row["office_address_1"],
                        office_address_2=row["office_address_2"],
                        office_address_3=row["office_address_3"],
                    )
                    customeroffice_instance.save()
                try:
                    branchdata_instance = LoanData(customer=customer_instance)
                except LoanData.DoesNotExist:
                    agreementdate_instance = datetime.datetime.strptime(
                        row["agreement_date"], "%d-%m-%Y"
                    ).strftime("%Y-%m-%d")
                    loandata_instance = LoanData(
                        customer=customer_instance,
                        agreement_date=agreementdate_instance,
                        lrn=row["lrn"],
                        tenor=row["tenor"],
                        adv_emi=row["adv_emi"],
                        mob=row["mob"],
                    )
                    loandata_instance.save()

                except Exception as e:
                    print(
                        "Customer Office Creation failed due to {}".format(e)
                    )

        self.task_instance.status = constants.TASK_STATUS_COMPLETED
        self.task_instance.save()
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file_path))

    def _load_task_instance(self):
        try:
            self.task_instance = CSVUploadModel.objects.get(id=self.task_id)
        except Exception as e:
            raise CommandError(
                "Task instance with id {} does not exist, error {}".format(
                    self.task_id, e
                )
            )
        self._check_task_status()

    def _check_task_status(self):
        if self.task_instance.status != constants.TASK_STATUS_YET_TO_START:
            raise CommandError(
                "Task {} is not in yet to start state".format(self.task_id)
            )

    def handle(self, *args, **options):
        if not options["task_id"]:
            raise CommandError("Option ` --task_id...` must be specified")
        self.task_id = options.get("task_id")
        self._load_task_instance()
        self.main_task()
        print("Finished executing task {}".format(self.task_id))
