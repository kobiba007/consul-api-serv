#!/bin/bash

echo "################# Cluster Members ######################"
curl -s http://localhost:5000/v1/api/consulCluster/members | jq
echo -e " "

echo "################# Cluster Status ######################"
curl -s http://localhost:5000/v1/api/consulCluster/status | jq
echo -e " "

echo "################# SystemInfo (Container) ######################"
curl -s http://localhost:5000/v1/api/consulCluster/systemInfo | jq
echo -e " "

echo "################# Cluster Summary ######################"
curl -s http://localhost:5000/v1/api/consulCluster/summary | jq
echo -e " "
