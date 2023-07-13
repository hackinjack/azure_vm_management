from azure.mgmt.compute import ComputeManagementClient
from azure.core.exceptions import HttpResponseError

class AzureVMManager:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.compute_client = ComputeManagementClient(
            credential=None, subscription_id=self.subscription_id
        )

    def get_vm_list(self):
        try:
            vm_list = self.compute_client.virtual_machines.list_all()
            return vm_list
        except HttpResponseError as e:
            raise Exception(f"Failed to retrieve VM list: {e}")

    def check_tags(self, vm):
        if vm.tags is not None and "PMEnabled" in vm.tags and "PMEnabledDaily" in vm.tags:
            return True
        return False

    def update_tags(self, vm):
        try:
            if vm.tags["PMEnabled"] == "null":
                vm.tags["PMEnabled"] = "true"
            if vm.tags["PMEnabledDaily"] == "null":
                vm.tags["PMEnabledDaily"] = "true"
            self.compute_client.virtual_machines.create_or_update(
                vm.resource_group, vm.name, vm
            )
        except HttpResponseError as e:
            raise Exception(f"Failed to update tags for VM {vm.name}: {e}")
