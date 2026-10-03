#!/usr/bin/env bash

set -e

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
network="ktdl-network"

stacks=(
  "postgres/docker-compose.dev.yaml"
  "mongo/docker-compose.dev.yaml"
  "kafka/docker-compose.dev.yaml"
  "spark/docker-compose.dev.yaml"
  "hadoop/docker-compose.dev.yaml"
)

# host:port targets to validate once everything is up
targets=(
  "db:5432"
  "mongo:27017"
  "kafka-0:9092"
  "kafka-1:9092"
  "kafka-2:9092"
  "spark:7077"
  "spark:8080"
  "spark-worker:8081"
  "namenode:9000"
  "namenode:9870"
  "datanode:9864"
  "resourcemanager:8088"
  "nodemanager:8042"
)

echo "--- Ensuring shared network '$network' exists"
docker network inspect "$network" >/dev/null 2>&1 || docker network create "$network"

for stack in "${stacks[@]}"; do
  echo "--- docker compose -f $stack up -d"
  docker compose -f "$root/$stack" up -d
done

echo "--- Waiting for services to settle..."
sleep 25

echo "--- Containers:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo
echo "--- Validating container connectivity on '$network'"
for t in "${targets[@]}"; do
  host="${t%%:*}"
  port="${t##*:}"
  if docker run --rm --network "$network" busybox sh -c "nc -z -w 2 $host $port" >/dev/null 2>&1; then
    echo "[OK]   $t"
  else
    echo "[FAIL] $t"
  fi
done
