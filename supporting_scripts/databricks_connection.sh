pip install databricks-cli

databricks configure --token
https://dbc-401be88c-2053.cloud.databricks.co
<your token>

databricks secrets create-scope --scope aws-secrets

databricks secrets put --scope aws-secrets --key aws-access-key
<your access key>

databricks secrets put --scope aws-secrets --key aws-secret-key
<your secret key>