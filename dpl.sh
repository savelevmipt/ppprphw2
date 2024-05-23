docker build -t main -f dockerfile_main .
docker build -t stat -f dockerfile_stat .

kubectl apply -f deployment_main.yaml
kubectl apply -f service.yaml
kubectl apply -f deployment_stat.yaml

kubectl apply -f forbid_ext.yaml
kubectl apply -f http-gateway.yaml
kubectl apply -f external-traffic.yaml
kubectl apply -f virtualservice.yaml