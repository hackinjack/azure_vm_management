from azure_authenticator import AzureAuthenticator
from azure_vm_manager import AzureVMManager
from logger import Logger
from error_handler import ErrorHandler

def main():
    # Initialize AzureAuthenticator
    authenticator = AzureAuthenticator()
    credential = authenticator.authenticate()

    # Initialize AzureVMManager
    subscription_id = "<your_subscription_id>"
    vm_manager = AzureVMManager(subscription_id)

    # Retrieve VM list
    vm_list = vm_manager.get_vm_list()

    # Initialize Logger
    log_file = "tag_changes.log"
    logger = Logger(log_file)

    # Initialize ErrorHandler
    error_handler = ErrorHandler()

    # Process VMs
    for vm in vm_list:
        try:
            if vm_manager.check_tags(vm):
                vm_manager.update_tags(vm)
                logger.log_changes(vm.name, vm.tags)
        except Exception as e:
            error_handler.handle_error(str(e))

if __name__ == "__main__":
    main()
