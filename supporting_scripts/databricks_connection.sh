pip install databricks-cli

databricks configure --token
https://dbc-1dd9f0c8-6186.cloud.databricks.com/
<your token>

databricks secrets create-scope --scope aws-secrets

databricks secrets put --scope aws-secrets --key aws-access-key
<your access key>

databricks secrets put --scope aws-secrets --key aws-secret-key
<your secret key>