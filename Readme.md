Sample REST API Project Using Flask running on 9080
Access the APIs:

Open your browser or use a tool like Postman to access 
http://localhost:9080/api/hello

You can also try 
http://localhost:9080/api/greet/Krishna to see the custom greeting.

python run.py

curl -X POST -H "Content-Type: application/json" -d '{"name":"krishna"}' http://localhost:9080/api/echo

in windows powershell curl might not work, try below
Invoke-RestMethod -Method Post -Uri http://localhost:9080/api/echo -Headers @{"Content-Type" = "application/json"} -Body '{"key":"value"}'
----------------------
AWS EKS commands
docker build -t my-repo .

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

kubectl get services
