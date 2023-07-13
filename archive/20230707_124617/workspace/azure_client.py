from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

class AzureClient:
    def __init__(self, tenant_id, client_id, client_secret, subscription_id):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.subscription_id = subscription_id
        self.compute_client = None
        self.resource_client = None

    def authenticate(self):
        credentials = ClientSecretCredential(
            tenant_id=self.tenant_id,
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        self.compute_client = ComputeManagementClient(credentials, self.subscription_id)
        self.resource_client = ResourceManagementClient(credentials, self.subscription_id)

    def get_virtual_machines(self):
        vm_list = self.compute_client.virtual_machines.list_all()
        return [vm for vm in vm_list]

    def update_vm_tags(self, resource_group_name, vm_name, tags):
        self.resource_client.tags.update_at_scope(
            scope=f"/subscriptions/{self.subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}",
            tags=tags
        )
