sudo apt-get update
sudo apt-get install python3

python3 -m venv myenv
source myenv/bin/activate

pip install azure-identity azure-mgmt-compute

export AZURE_CLIENT_ID="<your_client_id>"
export AZURE_CLIENT_SECRET="<your_client_secret>"
export AZURE_TENANT_ID="<your_tenant_id>"

python main.py
