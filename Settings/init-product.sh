#!/bin/sh
echo "Creating table football-results \n"

AWS_DEFAULT_REGION=us-east-2

aws dynamodb create-table --table-name user-info \
  --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

