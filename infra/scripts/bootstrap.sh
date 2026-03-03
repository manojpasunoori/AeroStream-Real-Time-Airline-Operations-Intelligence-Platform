#!/usr/bin/env bash
set -euo pipefail

echo "[AeroStream] Starting local dependencies"
docker compose up -d kafka postgres mongo

echo "[AeroStream] Applying local k8s manifests (optional)"
if command -v kubectl >/dev/null 2>&1; then
  kubectl apply -k infra/k8s/eks || true
fi
