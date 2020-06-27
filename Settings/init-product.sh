#!/bin/sh
echo "Creating table football-results \n"

AWS_DEFAULT_REGION=us-east-2  # 코드가 실행될떄 기본값을 불러들이는데 환경변수에서 가져옴

aws dynamodb create-table --table-name user-info \
  --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

