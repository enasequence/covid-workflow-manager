mkdir -p ~/src/github.com/kubernetes-sigs/
cd ~/src/github.com/kubernetes-sigs/
git clone http://github.com/kubernetes-sigs/kube-batch -b release-0.5
# helm install ~/src/github.com/kubernetes-sigs/kube-batch/deployment/kube-batch --namespace kube-system
#  Helm 3
# helm install kube-batch ~/src/github.com/kubernetes-sigs/kube-batch/deployment/kube-batch --namespace kube-system

helm upgrade --install kube-batch ~/src/github.com/kubernetes-sigs/kube-batch/deployment/kube-batch --namespace kube-system