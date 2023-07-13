import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_changes(self, vm_name, tags):
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
        logging.info(f"Tags updated for VM {vm_name}: {tags}")
