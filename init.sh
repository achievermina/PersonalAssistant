#!/bin/sh
sleep 10
echo "Creating table football-results \n"
aws dynamodb --endpoint-url http://dynamodb-local:8000 create-table --table-name user-info \
  --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
