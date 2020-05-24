#!/bin/bash

echo ECS_CLUSTER=personalassistant-ecs-cluster >> /etc/ecs/ecs.config


#aws ec2 authorize-security-group-ingress --group-id sg-0e34cf1d10334d472 --protocol tcp --port 80 --cidr 0.0.0.0/0
#aws ec2 authorize-security-group-ingress --group-id sg-0e34cf1d10334d472 --protocol tcp --port 22 --cidr 0.0.0.0/0
