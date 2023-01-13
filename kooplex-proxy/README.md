# Creating docker image for the pod

docker build -t kooplex-proxy --no-cache .

docker images
>find [IMAGE ID]

docker tag [IMAGE ID] milm/kooplex-proxy:latest

docker push milm/kooplex-proxy:latest

# Launch of the pod

export KUBECONFIG=[PATH TO CONFIG]

kubectl --kubeconfig $KUBECONFIG delete --namespace=kooplex-veo -f ./kooplex_svc+deployment.yml

kubectl --kubeconfig $KUBECONFIG apply --namespace=kooplex-veo -f kooplex_svc+deployment.yml

# Launch of the client tests

kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo get pods
>find [POD ID]

kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo exec -it [POD ID] bash

python3 /proxy/tests/test_client.py

# Getting pod information and logs

kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo describe pod [POD ID]

kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo logs [POD ID]
