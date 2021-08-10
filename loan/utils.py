from os.path import join
import os
from loan import constants
import subprocess


def csv_log_process(form_name, manage_command_name):
    """
    This function is executing the process of adding the uploaded csv data to
    the database and logging the errors (if any) in log files.
    """
    task = form_name.save(commit=False)
    task.status = constants.TASK_STATUS_YET_TO_START
    task.save()
    log_dir = join(os.getcwd(), "csvlogs")
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_file = open(join(log_dir, "csv.log"), "a+")
    error_log_file = open(join(log_dir, "csverror.log"), "a+")
    manage_py_location = join(os.getcwd(), "manage.py")
    python_path = join(os.getcwd(), ".heroku", "python", "bin", "python")
    command_run_args = [
        python_path,
        manage_py_location,
        manage_command_name,
    ]
    args = [
        str(task.id),
    ]
    subprocess.Popen(
        command_run_args + args,
        env=os.environ.copy(),
        stdout=log_file,
        stderr=error_log_file,
    )
    return task.id
