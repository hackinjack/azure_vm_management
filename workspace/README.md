The core classes, functions, and methods that will be necessary for this tool are:

1. AzureAuthenticator: A class responsible for authenticating the Python tool with the Azure service principal and secret.
2. AzureVMManager: A class responsible for managing Azure VMs, including retrieving the list of VMs, checking and updating tags.
3. Logger: A class responsible for logging the changes made to the tags in a logfile.
4. ErrorHandler: A class responsible for handling potential errors or exceptions that may occur during the process.

Now let's proceed with the file contents.

**azure_authenticator.py**
