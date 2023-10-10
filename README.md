# Clip Deployment with Minikube

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Docker](https://docs.docker.com/get-docker/)
- Craete a alias for Minikube

    ```bash
    alias kubectl="minikube kubectl --"
    ```

## Setup

1. Start Minikube

    ```bash
    minikube start --driver=docker
    ```
2. Enable the ingress addon

    ```bash
    minikube addons enable ingress
    ```
3. Create Docker image

    ```bash
    docker build -t clip-deploy .
    ```
4. Push docker image to Minikube

    ```bash
    minikube image load clip-deploy
    ```
5. Create deployment

    ```bash
    kubectl apply -f clip-deployment.yaml
    ```
6. Create service

    ```bash
    kubectl apply -f clip-service.yaml
    ```
7. Create ingress

    ```bash
    kubectl apply -f clip-ingress.yaml
    ```
8. Get Minikube IP

    ```bash
    minikube ip
    ```
9. Add the IP to your hosts file with Ingress mentioned host

    ```bash
    sudo vim /etc/hosts
    ```
10. Tunnel ingress

    ```bash
    minikube tunnel
    ```
11. Open the host mentioned in the ingress file in your browser to see fastapi swagger docs

    ```bash
    http://clip.emlo/docs
    ```
12. run the following command to get all details:
    
    ```bash
    kubectl get all
    ```

## Browser Output

![Swagger Docs](/images/clip1.png)
