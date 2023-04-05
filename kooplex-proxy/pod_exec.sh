#!/bin/bash

PODS=$(kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo get pods -o jsonpath='{.items[*].metadata.name}')

TARGET_POD=$(echo "$PODS" | grep -o 'kooplex-proxy-deployments-[[:alnum:]-]*' | head -n 1)

if [ -n "$TARGET_POD" ]; then
  kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo exec -it $TARGET_POD bash
else
  echo "No pods with prefix 'kooplex-proxy-deployments-' found"
fi
