import os
from azure.identity import ClientSecretCredential

class AzureAuthenticator:
    def __init__(self):
        self.client_id = os.environ.get('AZURE_CLIENT_ID')
        self.client_secret = os.environ.get('AZURE_CLIENT_SECRET')
        self.tenant_id = os.environ.get('AZURE_TENANT_ID')

    def authenticate(self):
        credential = ClientSecretCredential(
            client_id=self.client_id,
            client_secret=self.client_secret,
            tenant_id=self.tenant_id
        )
        return credential
