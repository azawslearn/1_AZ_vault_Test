import msal
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

keyVaultName = "lekeyvaultforpyapp22"
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

# Get the secrets
client_id = client.get_secret("ID").value
client_secret = client.get_secret("secret").value

authority = "https://login.microsoftonline.com/82da1502-e6a1-491d-9f8a-de005a5dff60"
scope = ["https://graph.microsoft.com/.default"]

# Create an MSAL instance providing the client_id, authority and client_credential parameters
client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# First, try to lookup an access token in cache
token_result = client.acquire_token_silent(scope, account=None)

# If the token is available in cache, save it to a variable
# if token_result:
#   access_token = 'Bearer ' + token_result['access_token']
#   print('Access token was loaded from cache')

# If the token is not available in cache, acquire a new one from Azure AD and save it to a variable

token_result = client.acquire_token_for_client(scopes=scope)
access_token = 'Bearer ' + token_result['access_token']
print('New access token was acquired from Azure AD')
print(access_token)


