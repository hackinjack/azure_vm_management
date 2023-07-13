class VMTagUpdater:
    def __init__(self, azure_client):
        self.azure_client = azure_client

    def check_tags(self, vm):
        tags = vm.tags
        if tags and "PMEnabled" in tags and "PMEnabledDaily" in tags:
            pm_enabled = tags.get("PMEnabled")
            pm_enabled_daily = tags.get("PMEnabledDaily")
            if pm_enabled == "null" or pm_enabled_daily == "null":
                return True
        return False

    def update_tags(self, vm):
        resource_group_name = vm.id.split("/")[4]
        vm_name = vm.name
        tags = {
            "PMEnabled": "true",
            "PMEnabledDaily": "true"
        }
        self.azure_client.update_vm_tags(resource_group_name, vm_name, tags)
