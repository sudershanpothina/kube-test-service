# kube-test-service
simple service to test kubernetes 

venv
```
python -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

```
docker build
```
docker build -t sdrshnrcks/kube-test:v2 .
docker push sdrshnrcks/kube-test:v2
```

kube
```
kubectl create ns kube-test
kubectl label namespace kube-test istio-injection=enabled
kubectl -n kube-test create -f deployment.yml 
kubectl -n kube-test create -f gateway.yml 

```