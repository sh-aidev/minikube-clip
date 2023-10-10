# Minikube clip deployment logs

## Logs

1. kubectl describe clip-deployment
    ```bash
        Name:                   clip-deployment
        Namespace:              default
        CreationTimestamp:      Wed, 11 Oct 2023 00:45:35 +0530
        Labels:                 app=clip
        Annotations:            deployment.kubernetes.io/revision: 1
        Selector:               app=clip
        Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
        StrategyType:           RollingUpdate
        MinReadySeconds:        0
        RollingUpdateStrategy:  25% max unavailable, 25% max surge
        Pod Template:
        Labels:  app=clip
        Containers:
        clip:
            Image:        clip-deploy:latest
            Port:         8000/TCP
            Host Port:    0/TCP
            Environment:  <none>
            Mounts:       <none>
        Volumes:        <none>
        Conditions:
        Type           Status  Reason
        ----           ------  ------
        Available      True    MinimumReplicasAvailable
        Progressing    True    NewReplicaSetAvailable
        OldReplicaSets:  <none>
        NewReplicaSet:   clip-deployment-76cc744cdd (2/2 replicas created)
        Events:
        Type    Reason             Age    From                   Message
        ----    ------             ----   ----                   -------
        Normal  ScalingReplicaSet  6m31s  deployment-controller  Scaled up replica set clip-deployment-76cc744cdd to 2
    ```
2. kubectl describe pod/clip-deployment-76cc744cdd-866nb
    ```bash
        Name:             clip-deployment-76cc744cdd-866nb
        Namespace:        default
        Priority:         0
        Service Account:  default
        Node:             minikube/192.168.49.2
        Start Time:       Wed, 11 Oct 2023 00:45:35 +0530
        Labels:           app=clip
                        pod-template-hash=76cc744cdd
        Annotations:      <none>
        Status:           Running
        IP:               10.244.0.6
        IPs:
        IP:           10.244.0.6
        Controlled By:  ReplicaSet/clip-deployment-76cc744cdd
        Containers:
        clip:
            Container ID:   docker://c8aafa86011c1824addbad9c15d6d7ca2a49d98efbb17c806a08cd25b818f323
            Image:          clip-deploy:latest
            Image ID:       docker://sha256:b48f8aa0566b2be95f8bf0577b4bae699c01d1dc8d155ba73766c4ab3ceef8aa
            Port:           8000/TCP
            Host Port:      0/TCP
            State:          Running
            Started:      Wed, 11 Oct 2023 00:45:36 +0530
            Ready:          True
            Restart Count:  0
            Environment:    <none>
            Mounts:
            /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rrxgj (ro)
        Conditions:
        Type              Status
        Initialized       True 
        Ready             True 
        ContainersReady   True 
        PodScheduled      True 
        Volumes:
        kube-api-access-rrxgj:
            Type:                    Projected (a volume that contains injected data from multiple sources)
            TokenExpirationSeconds:  3607
            ConfigMapName:           kube-root-ca.crt
            ConfigMapOptional:       <nil>
            DownwardAPI:             true
        QoS Class:                   BestEffort
        Node-Selectors:              <none>
        Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                    node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
        Events:
        Type    Reason     Age    From               Message
        ----    ------     ----   ----               -------
        Normal  Scheduled  8m59s  default-scheduler  Successfully assigned default/clip-deployment-76cc744cdd-866nb to minikube
        Normal  Pulled     8m58s  kubelet            Container image "clip-deploy:latest" already present on machine
        Normal  Created    8m58s  kubelet            Created container clip
        Normal  Started    8m58s  kubelet            Started container clip
    ```

3. kubectl describe ingress clip-ingress
    ```bash
        Name:             clip-ingress
        Labels:           <none>
        Namespace:        default
        Address:          192.168.49.2
        Ingress Class:    nginx
        Default backend:  <default>
        Rules:
        Host        Path  Backends
        ----        ----  --------
        clip.emlo   
                    /   clip-service:80 (10.244.0.6:8000,10.244.0.7:8000)
        Annotations:  <none>
        Events:
        Type    Reason  Age                From                      Message
        ----    ------  ----               ----                      -------
        Normal  Sync    11m (x2 over 12m)  nginx-ingress-controller  Scheduled for sync
    ```

4. kubectl top pod
    ```bash
        NAME                               CPU(cores)   MEMORY(bytes)   
        clip-deployment-76cc744cdd-866nb   4m           1672Mi          
        clip-deployment-76cc744cdd-khpt2   4m           1670Mi 
    ```

5. kubectl top node
    ```bash
        NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
        minikube   203m         1%     3595Mi          11%       
    ```

6. kubectl get all -A -o yaml
    ```bash
        apiVersion: v1
        items:
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:15:35Z"
            generateName: clip-deployment-76cc744cdd-
            labels:
            app: clip
            pod-template-hash: 76cc744cdd
            name: clip-deployment-76cc744cdd-866nb
            namespace: default
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: clip-deployment-76cc744cdd
            uid: cc7e80cb-89ed-402b-ba72-b42954338f9d
            resourceVersion: "711"
            uid: e34634ea-8033-49d9-a694-c1c9cbdd68c1
        spec:
            containers:
            - image: clip-deploy:latest
            imagePullPolicy: Never
            name: clip
            ports:
            - containerPort: 8000
                protocol: TCP
            resources: {}
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-rrxgj
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: default
            serviceAccountName: default
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - name: kube-api-access-rrxgj
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:35Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:37Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:37Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:35Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://c8aafa86011c1824addbad9c15d6d7ca2a49d98efbb17c806a08cd25b818f323
            image: clip-deploy:latest
            imageID: docker://sha256:b48f8aa0566b2be95f8bf0577b4bae699c01d1dc8d155ba73766c4ab3ceef8aa
            lastState: {}
            name: clip
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:15:36Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.6
            podIPs:
            - ip: 10.244.0.6
            qosClass: BestEffort
            startTime: "2023-10-10T19:15:35Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:15:35Z"
            generateName: clip-deployment-76cc744cdd-
            labels:
            app: clip
            pod-template-hash: 76cc744cdd
            name: clip-deployment-76cc744cdd-khpt2
            namespace: default
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: clip-deployment-76cc744cdd
            uid: cc7e80cb-89ed-402b-ba72-b42954338f9d
            resourceVersion: "715"
            uid: 24c6b266-ea67-418d-a95a-0b1d29af26fb
        spec:
            containers:
            - image: clip-deploy:latest
            imagePullPolicy: Never
            name: clip
            ports:
            - containerPort: 8000
                protocol: TCP
            resources: {}
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-msrhs
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: default
            serviceAccountName: default
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - name: kube-api-access-msrhs
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:36Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:37Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:37Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:15:35Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://085bcfe924469eb2e4f2a1e5d9a6025b8c3df4d4ce2bf0e388e47393addc5f75
            image: clip-deploy:latest
            imageID: docker://sha256:b48f8aa0566b2be95f8bf0577b4bae699c01d1dc8d155ba73766c4ab3ceef8aa
            lastState: {}
            name: clip
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:15:36Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.7
            podIPs:
            - ip: 10.244.0.7
            qosClass: BestEffort
            startTime: "2023-10-10T19:15:36Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:12:04Z"
            generateName: ingress-nginx-admission-create-
            labels:
            app.kubernetes.io/component: admission-webhook
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            batch.kubernetes.io/controller-uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
            batch.kubernetes.io/job-name: ingress-nginx-admission-create
            controller-uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
            job-name: ingress-nginx-admission-create
            name: ingress-nginx-admission-create-r4thr
            namespace: ingress-nginx
            ownerReferences:
            - apiVersion: batch/v1
            blockOwnerDeletion: true
            controller: true
            kind: Job
            name: ingress-nginx-admission-create
            uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
            resourceVersion: "492"
            uid: 53bf6f80-eeb8-4539-87e3-770a2817124a
        spec:
            containers:
            - args:
            - create
            - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
            - --namespace=$(POD_NAMESPACE)
            - --secret-name=ingress-nginx-admission
            env:
            - name: POD_NAMESPACE
                valueFrom:
                fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
            image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
            imagePullPolicy: IfNotPresent
            name: create
            resources: {}
            securityContext:
                allowPrivilegeEscalation: false
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-pbcpp
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            minikube.k8s.io/primary: "true"
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: OnFailure
            schedulerName: default-scheduler
            securityContext:
            runAsNonRoot: true
            runAsUser: 2000
            serviceAccount: ingress-nginx-admission
            serviceAccountName: ingress-nginx-admission
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - name: kube-api-access-pbcpp
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            reason: PodCompleted
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            reason: PodCompleted
            status: "False"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            reason: PodCompleted
            status: "False"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://e9de2c8355fa95188654e1c8bf4b624653468c270836d666e1ee154e59545157
            image: sha256:7e7451bb70423d31bdadcf0a71a3107b64858eccd7827d066234650b5e7b36b0
            imageID: docker-pullable://registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
            lastState: {}
            name: create
            ready: false
            restartCount: 0
            started: false
            state:
                terminated:
                containerID: docker://e9de2c8355fa95188654e1c8bf4b624653468c270836d666e1ee154e59545157
                exitCode: 0
                finishedAt: "2023-10-10T19:12:48Z"
                reason: Completed
                startedAt: "2023-10-10T19:12:48Z"
            hostIP: 192.168.49.2
            phase: Succeeded
            podIP: 10.244.0.4
            podIPs:
            - ip: 10.244.0.4
            qosClass: BestEffort
            startTime: "2023-10-10T19:12:04Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:12:04Z"
            generateName: ingress-nginx-admission-patch-
            labels:
            app.kubernetes.io/component: admission-webhook
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            batch.kubernetes.io/controller-uid: d3db7523-18cc-4556-8751-f5ae233975fb
            batch.kubernetes.io/job-name: ingress-nginx-admission-patch
            controller-uid: d3db7523-18cc-4556-8751-f5ae233975fb
            job-name: ingress-nginx-admission-patch
            name: ingress-nginx-admission-patch-hhsmj
            namespace: ingress-nginx
            ownerReferences:
            - apiVersion: batch/v1
            blockOwnerDeletion: true
            controller: true
            kind: Job
            name: ingress-nginx-admission-patch
            uid: d3db7523-18cc-4556-8751-f5ae233975fb
            resourceVersion: "510"
            uid: 2038c085-7123-4636-88b1-555bc729db3c
        spec:
            containers:
            - args:
            - patch
            - --webhook-name=ingress-nginx-admission
            - --namespace=$(POD_NAMESPACE)
            - --patch-mutating=false
            - --secret-name=ingress-nginx-admission
            - --patch-failure-policy=Fail
            env:
            - name: POD_NAMESPACE
                valueFrom:
                fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
            image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
            imagePullPolicy: IfNotPresent
            name: patch
            resources: {}
            securityContext:
                allowPrivilegeEscalation: false
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-vllvx
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            minikube.k8s.io/primary: "true"
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: OnFailure
            schedulerName: default-scheduler
            securityContext:
            runAsNonRoot: true
            runAsUser: 2000
            serviceAccount: ingress-nginx-admission
            serviceAccountName: ingress-nginx-admission
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - name: kube-api-access-vllvx
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            reason: PodCompleted
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            reason: PodCompleted
            status: "False"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            reason: PodCompleted
            status: "False"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://a1cbfd50380b1ee8f4add75866eb46bbe669ba4f7527fb91b8f9c2924cd718c9
            image: sha256:7e7451bb70423d31bdadcf0a71a3107b64858eccd7827d066234650b5e7b36b0
            imageID: docker-pullable://registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
            lastState: {}
            name: patch
            ready: false
            restartCount: 2
            started: false
            state:
                terminated:
                containerID: docker://a1cbfd50380b1ee8f4add75866eb46bbe669ba4f7527fb91b8f9c2924cd718c9
                exitCode: 0
                finishedAt: "2023-10-10T19:12:54Z"
                reason: Completed
                startedAt: "2023-10-10T19:12:54Z"
            hostIP: 192.168.49.2
            phase: Succeeded
            podIP: 10.244.0.3
            podIPs:
            - ip: 10.244.0.3
            qosClass: BestEffort
            startTime: "2023-10-10T19:12:04Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:12:04Z"
            generateName: ingress-nginx-controller-7799c6795f-
            labels:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            gcp-auth-skip-secret: "true"
            pod-template-hash: 7799c6795f
            name: ingress-nginx-controller-7799c6795f-p4w45
            namespace: ingress-nginx
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: ingress-nginx-controller-7799c6795f
            uid: bb789b18-6036-4c52-91b8-a616b942769d
            resourceVersion: "561"
            uid: ec5a2f1f-548f-4582-bb7d-179301588d56
        spec:
            containers:
            - args:
            - /nginx-ingress-controller
            - --election-id=ingress-nginx-leader
            - --controller-class=k8s.io/ingress-nginx
            - --watch-ingress-without-class=true
            - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
            - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
            - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
            - --validating-webhook=:8443
            - --validating-webhook-certificate=/usr/local/certificates/cert
            - --validating-webhook-key=/usr/local/certificates/key
            env:
            - name: POD_NAME
                valueFrom:
                fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.name
            - name: POD_NAMESPACE
                valueFrom:
                fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
            - name: LD_PRELOAD
                value: /usr/local/lib/libmimalloc.so
            image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
            imagePullPolicy: IfNotPresent
            lifecycle:
                preStop:
                exec:
                    command:
                    - /wait-shutdown
            livenessProbe:
                failureThreshold: 5
                httpGet:
                path: /healthz
                port: 10254
                scheme: HTTP
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 1
            name: controller
            ports:
            - containerPort: 80
                hostPort: 80
                name: http
                protocol: TCP
            - containerPort: 443
                hostPort: 443
                name: https
                protocol: TCP
            - containerPort: 8443
                name: webhook
                protocol: TCP
            readinessProbe:
                failureThreshold: 3
                httpGet:
                path: /healthz
                port: 10254
                scheme: HTTP
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 1
            resources:
                requests:
                cpu: 100m
                memory: 90Mi
            securityContext:
                allowPrivilegeEscalation: true
                capabilities:
                add:
                - NET_BIND_SERVICE
                drop:
                - ALL
                runAsUser: 101
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /usr/local/certificates/
                name: webhook-cert
                readOnly: true
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-t494p
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            minikube.k8s.io/primary: "true"
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: ingress-nginx
            serviceAccountName: ingress-nginx
            terminationGracePeriodSeconds: 0
            tolerations:
            - effect: NoSchedule
            key: node-role.kubernetes.io/master
            operator: Equal
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - name: webhook-cert
            secret:
                defaultMode: 420
                secretName: ingress-nginx-admission
            - name: kube-api-access-t494p
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:13:38Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:13:38Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:04Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://1dacb40731c2c8e9cf3cefbe62eb06ed6cb7c5cee30eda501c89993d5c95e2b8
            image: registry.k8s.io/ingress-nginx/controller@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
            imageID: docker-pullable://registry.k8s.io/ingress-nginx/controller@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
            lastState: {}
            name: controller
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:13:20Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.5
            podIPs:
            - ip: 10.244.0.5
            qosClass: Burstable
            startTime: "2023-10-10T19:12:04Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:12:01Z"
            generateName: coredns-5d78c9869d-
            labels:
            k8s-app: kube-dns
            pod-template-hash: 5d78c9869d
            name: coredns-5d78c9869d-lkxlx
            namespace: kube-system
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: coredns-5d78c9869d
            uid: 0e22824d-b5df-48d6-85d2-1e1826eecfc4
            resourceVersion: "430"
            uid: 1455fa55-a159-4958-9430-b5299ebf61bb
        spec:
            affinity:
            podAntiAffinity:
                preferredDuringSchedulingIgnoredDuringExecution:
                - podAffinityTerm:
                    labelSelector:
                    matchExpressions:
                    - key: k8s-app
                        operator: In
                        values:
                        - kube-dns
                    topologyKey: kubernetes.io/hostname
                weight: 100
            containers:
            - args:
            - -conf
            - /etc/coredns/Corefile
            image: registry.k8s.io/coredns/coredns:v1.10.1
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 5
                httpGet:
                path: /health
                port: 8080
                scheme: HTTP
                initialDelaySeconds: 60
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 5
            name: coredns
            ports:
            - containerPort: 53
                name: dns
                protocol: UDP
            - containerPort: 53
                name: dns-tcp
                protocol: TCP
            - containerPort: 9153
                name: metrics
                protocol: TCP
            readinessProbe:
                failureThreshold: 3
                httpGet:
                path: /ready
                port: 8181
                scheme: HTTP
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 1
            resources:
                limits:
                memory: 170Mi
                requests:
                cpu: 100m
                memory: 70Mi
            securityContext:
                allowPrivilegeEscalation: false
                capabilities:
                add:
                - NET_BIND_SERVICE
                drop:
                - all
                readOnlyRootFilesystem: true
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /etc/coredns
                name: config-volume
                readOnly: true
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-tlvsh
                readOnly: true
            dnsPolicy: Default
            enableServiceLinks: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            preemptionPolicy: PreemptLowerPriority
            priority: 2000000000
            priorityClassName: system-cluster-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: coredns
            serviceAccountName: coredns
            terminationGracePeriodSeconds: 30
            tolerations:
            - key: CriticalAddonsOnly
            operator: Exists
            - effect: NoSchedule
            key: node-role.kubernetes.io/control-plane
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - configMap:
                defaultMode: 420
                items:
                - key: Corefile
                path: Corefile
                name: coredns
            name: config-volume
            - name: kube-api-access-tlvsh
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:01Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:11Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:11Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:01Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://e0b868409b40b0e78a68bbec3f6800489d1b37aa4c42d536d3a7f42729f43021
            image: registry.k8s.io/coredns/coredns:v1.10.1
            imageID: docker-pullable://registry.k8s.io/coredns/coredns@sha256:a0ead06651cf580044aeb0a0feba63591858fb2e43ade8c9dea45a6a89ae7e5e
            lastState: {}
            name: coredns
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:12:02Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.2
            podIPs:
            - ip: 10.244.0.2
            qosClass: Burstable
            startTime: "2023-10-10T19:12:01Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            annotations:
            kubeadm.kubernetes.io/etcd.advertise-client-urls: https://192.168.49.2:2379
            kubernetes.io/config.hash: 8af0e85a28544808d52bb7c47ad824ed
            kubernetes.io/config.mirror: 8af0e85a28544808d52bb7c47ad824ed
            kubernetes.io/config.seen: "2023-10-10T19:11:47.774171886Z"
            kubernetes.io/config.source: file
            creationTimestamp: "2023-10-10T19:11:47Z"
            labels:
            component: etcd
            tier: control-plane
            name: etcd-minikube
            namespace: kube-system
            ownerReferences:
            - apiVersion: v1
            controller: true
            kind: Node
            name: minikube
            uid: 4653a48a-1fb1-472b-8da1-73001b937148
            resourceVersion: "265"
            uid: 7a813a1b-9184-4b47-9be7-15de2a3b8837
        spec:
            containers:
            - command:
            - etcd
            - --advertise-client-urls=https://192.168.49.2:2379
            - --cert-file=/var/lib/minikube/certs/etcd/server.crt
            - --client-cert-auth=true
            - --data-dir=/var/lib/minikube/etcd
            - --experimental-initial-corrupt-check=true
            - --experimental-watch-progress-notify-interval=5s
            - --initial-advertise-peer-urls=https://192.168.49.2:2380
            - --initial-cluster=minikube=https://192.168.49.2:2380
            - --key-file=/var/lib/minikube/certs/etcd/server.key
            - --listen-client-urls=https://127.0.0.1:2379,https://192.168.49.2:2379
            - --listen-metrics-urls=http://127.0.0.1:2381
            - --listen-peer-urls=https://192.168.49.2:2380
            - --name=minikube
            - --peer-cert-file=/var/lib/minikube/certs/etcd/peer.crt
            - --peer-client-cert-auth=true
            - --peer-key-file=/var/lib/minikube/certs/etcd/peer.key
            - --peer-trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
            - --proxy-refresh-interval=70000
            - --snapshot-count=10000
            - --trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
            image: registry.k8s.io/etcd:3.5.7-0
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 8
                httpGet:
                host: 127.0.0.1
                path: /health?exclude=NOSPACE&serializable=true
                port: 2381
                scheme: HTTP
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            name: etcd
            resources:
                requests:
                cpu: 100m
                memory: 100Mi
            startupProbe:
                failureThreshold: 24
                httpGet:
                host: 127.0.0.1
                path: /health?serializable=false
                port: 2381
                scheme: HTTP
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/lib/minikube/etcd
                name: etcd-data
            - mountPath: /var/lib/minikube/certs/etcd
                name: etcd-certs
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            hostNetwork: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 2000001000
            priorityClassName: system-node-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext:
            seccompProfile:
                type: RuntimeDefault
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            operator: Exists
            volumes:
            - hostPath:
                path: /var/lib/minikube/certs/etcd
                type: DirectoryOrCreate
            name: etcd-certs
            - hostPath:
                path: /var/lib/minikube/etcd
                type: DirectoryOrCreate
            name: etcd-data
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:54Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:54Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://878336f232837dcd4087235e8c50a6376e2f2163638330bfb6d0334649242975
            image: registry.k8s.io/etcd:3.5.7-0
            imageID: docker-pullable://registry.k8s.io/etcd@sha256:51eae8381dcb1078289fa7b4f3df2630cdc18d09fb56f8e56b41c40e191d6c83
            lastState: {}
            name: etcd
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:11:43Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 192.168.49.2
            podIPs:
            - ip: 192.168.49.2
            qosClass: Burstable
            startTime: "2023-10-10T19:11:47Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            annotations:
            kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 192.168.49.2:8443
            kubernetes.io/config.hash: f241819aff4d77a34fc71bea1fac9af8
            kubernetes.io/config.mirror: f241819aff4d77a34fc71bea1fac9af8
            kubernetes.io/config.seen: "2023-10-10T19:11:42.127101448Z"
            kubernetes.io/config.source: file
            creationTimestamp: "2023-10-10T19:11:46Z"
            labels:
            component: kube-apiserver
            tier: control-plane
            name: kube-apiserver-minikube
            namespace: kube-system
            ownerReferences:
            - apiVersion: v1
            controller: true
            kind: Node
            name: minikube
            uid: 4653a48a-1fb1-472b-8da1-73001b937148
            resourceVersion: "352"
            uid: 594bf06b-16f0-4f76-bcb5-28bf23d96edc
        spec:
            containers:
            - command:
            - kube-apiserver
            - --advertise-address=192.168.49.2
            - --allow-privileged=true
            - --authorization-mode=Node,RBAC
            - --client-ca-file=/var/lib/minikube/certs/ca.crt
            - --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota
            - --enable-bootstrap-token-auth=true
            - --etcd-cafile=/var/lib/minikube/certs/etcd/ca.crt
            - --etcd-certfile=/var/lib/minikube/certs/apiserver-etcd-client.crt
            - --etcd-keyfile=/var/lib/minikube/certs/apiserver-etcd-client.key
            - --etcd-servers=https://127.0.0.1:2379
            - --kubelet-client-certificate=/var/lib/minikube/certs/apiserver-kubelet-client.crt
            - --kubelet-client-key=/var/lib/minikube/certs/apiserver-kubelet-client.key
            - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
            - --proxy-client-cert-file=/var/lib/minikube/certs/front-proxy-client.crt
            - --proxy-client-key-file=/var/lib/minikube/certs/front-proxy-client.key
            - --requestheader-allowed-names=front-proxy-client
            - --requestheader-client-ca-file=/var/lib/minikube/certs/front-proxy-ca.crt
            - --requestheader-extra-headers-prefix=X-Remote-Extra-
            - --requestheader-group-headers=X-Remote-Group
            - --requestheader-username-headers=X-Remote-User
            - --secure-port=8443
            - --service-account-issuer=https://kubernetes.default.svc.cluster.local
            - --service-account-key-file=/var/lib/minikube/certs/sa.pub
            - --service-account-signing-key-file=/var/lib/minikube/certs/sa.key
            - --service-cluster-ip-range=10.96.0.0/12
            - --tls-cert-file=/var/lib/minikube/certs/apiserver.crt
            - --tls-private-key-file=/var/lib/minikube/certs/apiserver.key
            image: registry.k8s.io/kube-apiserver:v1.27.4
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 8
                httpGet:
                host: 192.168.49.2
                path: /livez
                port: 8443
                scheme: HTTPS
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            name: kube-apiserver
            readinessProbe:
                failureThreshold: 3
                httpGet:
                host: 192.168.49.2
                path: /readyz
                port: 8443
                scheme: HTTPS
                periodSeconds: 1
                successThreshold: 1
                timeoutSeconds: 15
            resources:
                requests:
                cpu: 250m
            startupProbe:
                failureThreshold: 24
                httpGet:
                host: 192.168.49.2
                path: /livez
                port: 8443
                scheme: HTTPS
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /etc/ssl/certs
                name: ca-certs
                readOnly: true
            - mountPath: /etc/ca-certificates
                name: etc-ca-certificates
                readOnly: true
            - mountPath: /var/lib/minikube/certs
                name: k8s-certs
                readOnly: true
            - mountPath: /usr/local/share/ca-certificates
                name: usr-local-share-ca-certificates
                readOnly: true
            - mountPath: /usr/share/ca-certificates
                name: usr-share-ca-certificates
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            hostNetwork: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 2000001000
            priorityClassName: system-node-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext:
            seccompProfile:
                type: RuntimeDefault
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            operator: Exists
            volumes:
            - hostPath:
                path: /etc/ssl/certs
                type: DirectoryOrCreate
            name: ca-certs
            - hostPath:
                path: /etc/ca-certificates
                type: DirectoryOrCreate
            name: etc-ca-certificates
            - hostPath:
                path: /var/lib/minikube/certs
                type: DirectoryOrCreate
            name: k8s-certs
            - hostPath:
                path: /usr/local/share/ca-certificates
                type: DirectoryOrCreate
            name: usr-local-share-ca-certificates
            - hostPath:
                path: /usr/share/ca-certificates
                type: DirectoryOrCreate
            name: usr-share-ca-certificates
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:02Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:02Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://e87845953f7f8f699fd723e7238a5a14a9ae6cec3720f3a5fc5beb720282512b
            image: registry.k8s.io/kube-apiserver:v1.27.4
            imageID: docker-pullable://registry.k8s.io/kube-apiserver@sha256:697cd88d94f7f2ef42144cb3072b016dcb2e9251f0e7d41a7fede557e555452d
            lastState: {}
            name: kube-apiserver
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:11:43Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 192.168.49.2
            podIPs:
            - ip: 192.168.49.2
            qosClass: Burstable
            startTime: "2023-10-10T19:11:47Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            annotations:
            kubernetes.io/config.hash: b3702ceb912504d37098b922ccdcfa41
            kubernetes.io/config.mirror: b3702ceb912504d37098b922ccdcfa41
            kubernetes.io/config.seen: "2023-10-10T19:11:47.774174170Z"
            kubernetes.io/config.source: file
            creationTimestamp: "2023-10-10T19:11:47Z"
            labels:
            component: kube-controller-manager
            tier: control-plane
            name: kube-controller-manager-minikube
            namespace: kube-system
            ownerReferences:
            - apiVersion: v1
            controller: true
            kind: Node
            name: minikube
            uid: 4653a48a-1fb1-472b-8da1-73001b937148
            resourceVersion: "358"
            uid: cdac70c1-3b70-43db-b312-6a88946f334c
        spec:
            containers:
            - command:
            - kube-controller-manager
            - --allocate-node-cidrs=true
            - --authentication-kubeconfig=/etc/kubernetes/controller-manager.conf
            - --authorization-kubeconfig=/etc/kubernetes/controller-manager.conf
            - --bind-address=127.0.0.1
            - --client-ca-file=/var/lib/minikube/certs/ca.crt
            - --cluster-cidr=10.244.0.0/16
            - --cluster-name=mk
            - --cluster-signing-cert-file=/var/lib/minikube/certs/ca.crt
            - --cluster-signing-key-file=/var/lib/minikube/certs/ca.key
            - --controllers=*,bootstrapsigner,tokencleaner
            - --kubeconfig=/etc/kubernetes/controller-manager.conf
            - --leader-elect=false
            - --requestheader-client-ca-file=/var/lib/minikube/certs/front-proxy-ca.crt
            - --root-ca-file=/var/lib/minikube/certs/ca.crt
            - --service-account-private-key-file=/var/lib/minikube/certs/sa.key
            - --service-cluster-ip-range=10.96.0.0/12
            - --use-service-account-credentials=true
            image: registry.k8s.io/kube-controller-manager:v1.27.4
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 8
                httpGet:
                host: 127.0.0.1
                path: /healthz
                port: 10257
                scheme: HTTPS
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            name: kube-controller-manager
            resources:
                requests:
                cpu: 200m
            startupProbe:
                failureThreshold: 24
                httpGet:
                host: 127.0.0.1
                path: /healthz
                port: 10257
                scheme: HTTPS
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /etc/ssl/certs
                name: ca-certs
                readOnly: true
            - mountPath: /etc/ca-certificates
                name: etc-ca-certificates
                readOnly: true
            - mountPath: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
                name: flexvolume-dir
            - mountPath: /var/lib/minikube/certs
                name: k8s-certs
                readOnly: true
            - mountPath: /etc/kubernetes/controller-manager.conf
                name: kubeconfig
                readOnly: true
            - mountPath: /usr/local/share/ca-certificates
                name: usr-local-share-ca-certificates
                readOnly: true
            - mountPath: /usr/share/ca-certificates
                name: usr-share-ca-certificates
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            hostNetwork: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 2000001000
            priorityClassName: system-node-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext:
            seccompProfile:
                type: RuntimeDefault
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            operator: Exists
            volumes:
            - hostPath:
                path: /etc/ssl/certs
                type: DirectoryOrCreate
            name: ca-certs
            - hostPath:
                path: /etc/ca-certificates
                type: DirectoryOrCreate
            name: etc-ca-certificates
            - hostPath:
                path: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
                type: DirectoryOrCreate
            name: flexvolume-dir
            - hostPath:
                path: /var/lib/minikube/certs
                type: DirectoryOrCreate
            name: k8s-certs
            - hostPath:
                path: /etc/kubernetes/controller-manager.conf
                type: FileOrCreate
            name: kubeconfig
            - hostPath:
                path: /usr/local/share/ca-certificates
                type: DirectoryOrCreate
            name: usr-local-share-ca-certificates
            - hostPath:
                path: /usr/share/ca-certificates
                type: DirectoryOrCreate
            name: usr-share-ca-certificates
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:02Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:02Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://45024b12a81876efffd8f2264989e744fc45891cd9769901e2eaf0ffc6fb8d92
            image: registry.k8s.io/kube-controller-manager:v1.27.4
            imageID: docker-pullable://registry.k8s.io/kube-controller-manager@sha256:6286e500782ad6d0b37a1b8be57fc73f597dc931dfc73ff18ce534059803b265
            lastState: {}
            name: kube-controller-manager
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:11:43Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 192.168.49.2
            podIPs:
            - ip: 192.168.49.2
            qosClass: Burstable
            startTime: "2023-10-10T19:11:47Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:12:01Z"
            generateName: kube-proxy-
            labels:
            controller-revision-hash: 86cc8bcbf7
            k8s-app: kube-proxy
            pod-template-generation: "1"
            name: kube-proxy-jk44r
            namespace: kube-system
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: DaemonSet
            name: kube-proxy
            uid: e959e86d-5dcc-4250-9610-84b5b6cfc9ed
            resourceVersion: "360"
            uid: 7ddc540c-5513-42bb-b59d-547b52e7455b
        spec:
            affinity:
            nodeAffinity:
                requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchFields:
                    - key: metadata.name
                    operator: In
                    values:
                    - minikube
            containers:
            - command:
            - /usr/local/bin/kube-proxy
            - --config=/var/lib/kube-proxy/config.conf
            - --hostname-override=$(NODE_NAME)
            env:
            - name: NODE_NAME
                valueFrom:
                fieldRef:
                    apiVersion: v1
                    fieldPath: spec.nodeName
            image: registry.k8s.io/kube-proxy:v1.27.4
            imagePullPolicy: IfNotPresent
            name: kube-proxy
            resources: {}
            securityContext:
                privileged: true
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/lib/kube-proxy
                name: kube-proxy
            - mountPath: /run/xtables.lock
                name: xtables-lock
            - mountPath: /lib/modules
                name: lib-modules
                readOnly: true
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-zndjz
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            hostNetwork: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            preemptionPolicy: PreemptLowerPriority
            priority: 2000001000
            priorityClassName: system-node-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: kube-proxy
            serviceAccountName: kube-proxy
            terminationGracePeriodSeconds: 30
            tolerations:
            - operator: Exists
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            - effect: NoSchedule
            key: node.kubernetes.io/disk-pressure
            operator: Exists
            - effect: NoSchedule
            key: node.kubernetes.io/memory-pressure
            operator: Exists
            - effect: NoSchedule
            key: node.kubernetes.io/pid-pressure
            operator: Exists
            - effect: NoSchedule
            key: node.kubernetes.io/unschedulable
            operator: Exists
            - effect: NoSchedule
            key: node.kubernetes.io/network-unavailable
            operator: Exists
            volumes:
            - configMap:
                defaultMode: 420
                name: kube-proxy
            name: kube-proxy
            - hostPath:
                path: /run/xtables.lock
                type: FileOrCreate
            name: xtables-lock
            - hostPath:
                path: /lib/modules
                type: ""
            name: lib-modules
            - name: kube-api-access-zndjz
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:01Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:03Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:03Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:01Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://ff039fba87d926b1ffa08449858695ed5225b89cdd865ca442dc53c9d5ccc373
            image: registry.k8s.io/kube-proxy:v1.27.4
            imageID: docker-pullable://registry.k8s.io/kube-proxy@sha256:4bcb707da9898d2625f5d4edc6d0c96519a24f16db914fc673aa8f97e41dbabf
            lastState: {}
            name: kube-proxy
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:12:02Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 192.168.49.2
            podIPs:
            - ip: 192.168.49.2
            qosClass: BestEffort
            startTime: "2023-10-10T19:12:01Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            annotations:
            kubernetes.io/config.hash: eb675835e10503c79265cf0e2983f93c
            kubernetes.io/config.mirror: eb675835e10503c79265cf0e2983f93c
            kubernetes.io/config.seen: "2023-10-10T19:11:47.774168947Z"
            kubernetes.io/config.source: file
            creationTimestamp: "2023-10-10T19:11:47Z"
            labels:
            component: kube-scheduler
            tier: control-plane
            name: kube-scheduler-minikube
            namespace: kube-system
            ownerReferences:
            - apiVersion: v1
            controller: true
            kind: Node
            name: minikube
            uid: 4653a48a-1fb1-472b-8da1-73001b937148
            resourceVersion: "263"
            uid: 1eb532dc-bc8d-4221-b963-d7ae8d6900b4
        spec:
            containers:
            - command:
            - kube-scheduler
            - --authentication-kubeconfig=/etc/kubernetes/scheduler.conf
            - --authorization-kubeconfig=/etc/kubernetes/scheduler.conf
            - --bind-address=127.0.0.1
            - --kubeconfig=/etc/kubernetes/scheduler.conf
            - --leader-elect=false
            image: registry.k8s.io/kube-scheduler:v1.27.4
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 8
                httpGet:
                host: 127.0.0.1
                path: /healthz
                port: 10259
                scheme: HTTPS
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            name: kube-scheduler
            resources:
                requests:
                cpu: 100m
            startupProbe:
                failureThreshold: 24
                httpGet:
                host: 127.0.0.1
                path: /healthz
                port: 10259
                scheme: HTTPS
                initialDelaySeconds: 10
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 15
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /etc/kubernetes/scheduler.conf
                name: kubeconfig
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            hostNetwork: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 2000001000
            priorityClassName: system-node-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext:
            seccompProfile:
                type: RuntimeDefault
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            operator: Exists
            volumes:
            - hostPath:
                path: /etc/kubernetes/scheduler.conf
                type: FileOrCreate
            name: kubeconfig
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:53Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:53Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:11:47Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://12705c1065886471c5594023cc2a1160722f02fdeffa62825bc6daf9555a1897
            image: registry.k8s.io/kube-scheduler:v1.27.4
            imageID: docker-pullable://registry.k8s.io/kube-scheduler@sha256:5897d7a97d23dce25cbf36fcd6e919180a8ef904bf5156583ffdb6a733ab04af
            lastState: {}
            name: kube-scheduler
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:11:43Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 192.168.49.2
            podIPs:
            - ip: 192.168.49.2
            qosClass: Burstable
            startTime: "2023-10-10T19:11:47Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:29:18Z"
            generateName: metrics-server-7746886d4f-
            labels:
            k8s-app: metrics-server
            pod-template-hash: 7746886d4f
            name: metrics-server-7746886d4f-sdzt8
            namespace: kube-system
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: metrics-server-7746886d4f
            uid: 9c091172-8f2a-43f9-aa41-856a9c3e586b
            resourceVersion: "1679"
            uid: bd0daccd-13d8-4457-ad56-6c1c1f46b382
        spec:
            containers:
            - args:
            - --cert-dir=/tmp
            - --secure-port=4443
            - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
            - --kubelet-use-node-status-port
            - --metric-resolution=60s
            - --kubelet-insecure-tls
            image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 3
                httpGet:
                path: /livez
                port: https
                scheme: HTTPS
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 1
            name: metrics-server
            ports:
            - containerPort: 4443
                name: https
                protocol: TCP
            readinessProbe:
                failureThreshold: 3
                httpGet:
                path: /readyz
                port: https
                scheme: HTTPS
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 1
            resources:
                requests:
                cpu: 100m
                memory: 200Mi
            securityContext:
                readOnlyRootFilesystem: true
                runAsNonRoot: true
                runAsUser: 1000
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /tmp
                name: tmp-dir
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-7n2sg
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 2000000000
            priorityClassName: system-cluster-critical
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: metrics-server
            serviceAccountName: metrics-server
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - emptyDir: {}
            name: tmp-dir
            - name: kube-api-access-7n2sg
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:18Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:30:29Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:30:29Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:18Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://9d172d437731bd353b0864cb7c4b7b69dad293f01afe2abb52d2064e4197a779
            image: registry.k8s.io/metrics-server/metrics-server@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
            imageID: docker-pullable://registry.k8s.io/metrics-server/metrics-server@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
            lastState: {}
            name: metrics-server
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:29:24Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.8
            podIPs:
            - ip: 10.244.0.8
            qosClass: Burstable
            startTime: "2023-10-10T19:29:18Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","integration-test":"storage-provisioner"},"name":"storage-provisioner","namespace":"kube-system"},"spec":{"containers":[{"command":["/storage-provisioner"],"image":"gcr.io/k8s-minikube/storage-provisioner:v5","imagePullPolicy":"IfNotPresent","name":"storage-provisioner","volumeMounts":[{"mountPath":"/tmp","name":"tmp"}]}],"hostNetwork":true,"serviceAccountName":"storage-provisioner","volumes":[{"hostPath":{"path":"/tmp","type":"Directory"},"name":"tmp"}]}}
            creationTimestamp: "2023-10-10T19:11:48Z"
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            integration-test: storage-provisioner
            name: storage-provisioner
            namespace: kube-system
            resourceVersion: "449"
            uid: 9a26475a-f29c-4014-9a01-a2883f9811ee
        spec:
            containers:
            - command:
            - /storage-provisioner
            image: gcr.io/k8s-minikube/storage-provisioner:v5
            imagePullPolicy: IfNotPresent
            name: storage-provisioner
            resources: {}
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /tmp
                name: tmp
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-r6nkd
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            hostNetwork: true
            nodeName: minikube
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: storage-provisioner
            serviceAccountName: storage-provisioner
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - hostPath:
                path: /tmp
                type: Directory
            name: tmp
            - name: kube-api-access-r6nkd
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:00Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:33Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:33Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:12:00Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://112646e3ae4ef953b8a47c91e1037266f4a7fe43868153a4e7943be7d192570d
            image: gcr.io/k8s-minikube/storage-provisioner:v5
            imageID: docker-pullable://gcr.io/k8s-minikube/storage-provisioner@sha256:18eb69d1418e854ad5a19e399310e52808a8321e4c441c1dddad8977a0d7a944
            lastState:
                terminated:
                containerID: docker://678e4bf1094bb18532a0741c465ab35d2e2ec73ff5845cc416f04502ce0b7af8
                exitCode: 1
                finishedAt: "2023-10-10T19:12:32Z"
                reason: Error
                startedAt: "2023-10-10T19:12:02Z"
            name: storage-provisioner
            ready: true
            restartCount: 1
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:12:32Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 192.168.49.2
            podIPs:
            - ip: 192.168.49.2
            qosClass: BestEffort
            startTime: "2023-10-10T19:12:00Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            annotations:
            seccomp.security.alpha.kubernetes.io/pod: runtime/default
            creationTimestamp: "2023-10-10T19:29:35Z"
            generateName: dashboard-metrics-scraper-5dd9cbfd69-
            labels:
            k8s-app: dashboard-metrics-scraper
            pod-template-hash: 5dd9cbfd69
            name: dashboard-metrics-scraper-5dd9cbfd69-nq46d
            namespace: kubernetes-dashboard
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: dashboard-metrics-scraper-5dd9cbfd69
            uid: e35b080d-dcdb-4f19-8297-ee60bde32d69
            resourceVersion: "1638"
            uid: 0592e3ef-1c27-4bfb-ae2c-8c14b87f1226
        spec:
            containers:
            - image: docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 3
                httpGet:
                path: /
                port: 8000
                scheme: HTTP
                initialDelaySeconds: 30
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 30
            name: dashboard-metrics-scraper
            ports:
            - containerPort: 8000
                protocol: TCP
            resources: {}
            securityContext:
                allowPrivilegeEscalation: false
                readOnlyRootFilesystem: true
                runAsGroup: 2001
                runAsUser: 1001
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /tmp
                name: tmp-volume
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-rkmr4
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: kubernetes-dashboard
            serviceAccountName: kubernetes-dashboard
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoSchedule
            key: node-role.kubernetes.io/master
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - emptyDir: {}
            name: tmp-volume
            - name: kube-api-access-rkmr4
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:35Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:54Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:54Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:35Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://5d26595ae9b48cd6787048b644222eee8e8beb2f08fab615474e1d960ca0d589
            image: kubernetesui/metrics-scraper@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c
            imageID: docker-pullable://kubernetesui/metrics-scraper@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c
            lastState: {}
            name: dashboard-metrics-scraper
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:29:53Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.10
            podIPs:
            - ip: 10.244.0.10
            qosClass: BestEffort
            startTime: "2023-10-10T19:29:35Z"
        - apiVersion: v1
        kind: Pod
        metadata:
            creationTimestamp: "2023-10-10T19:29:35Z"
            generateName: kubernetes-dashboard-5c5cfc8747-
            labels:
            gcp-auth-skip-secret: "true"
            k8s-app: kubernetes-dashboard
            pod-template-hash: 5c5cfc8747
            name: kubernetes-dashboard-5c5cfc8747-hv8g5
            namespace: kubernetes-dashboard
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: ReplicaSet
            name: kubernetes-dashboard-5c5cfc8747
            uid: 567aed1d-958a-45be-8002-a534e5e36cc9
            resourceVersion: "1623"
            uid: 5992f6cd-33f4-46e4-9f9c-a4ca16b42799
        spec:
            containers:
            - args:
            - --namespace=kubernetes-dashboard
            - --enable-skip-login
            - --disable-settings-authorizer
            image: docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93
            imagePullPolicy: IfNotPresent
            livenessProbe:
                failureThreshold: 3
                httpGet:
                path: /
                port: 9090
                scheme: HTTP
                initialDelaySeconds: 30
                periodSeconds: 10
                successThreshold: 1
                timeoutSeconds: 30
            name: kubernetes-dashboard
            ports:
            - containerPort: 9090
                protocol: TCP
            resources: {}
            securityContext:
                allowPrivilegeEscalation: false
                readOnlyRootFilesystem: true
                runAsGroup: 2001
                runAsUser: 1001
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /tmp
                name: tmp-volume
            - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
                name: kube-api-access-kksjj
                readOnly: true
            dnsPolicy: ClusterFirst
            enableServiceLinks: true
            nodeName: minikube
            nodeSelector:
            kubernetes.io/os: linux
            preemptionPolicy: PreemptLowerPriority
            priority: 0
            restartPolicy: Always
            schedulerName: default-scheduler
            securityContext: {}
            serviceAccount: kubernetes-dashboard
            serviceAccountName: kubernetes-dashboard
            terminationGracePeriodSeconds: 30
            tolerations:
            - effect: NoSchedule
            key: node-role.kubernetes.io/master
            - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
            - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
            volumes:
            - emptyDir: {}
            name: tmp-volume
            - name: kube-api-access-kksjj
            projected:
                defaultMode: 420
                sources:
                - serviceAccountToken:
                    expirationSeconds: 3607
                    path: token
                - configMap:
                    items:
                    - key: ca.crt
                    path: ca.crt
                    name: kube-root-ca.crt
                - downwardAPI:
                    items:
                    - fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                    path: namespace
        status:
            conditions:
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:35Z"
            status: "True"
            type: Initialized
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:48Z"
            status: "True"
            type: Ready
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:48Z"
            status: "True"
            type: ContainersReady
            - lastProbeTime: null
            lastTransitionTime: "2023-10-10T19:29:35Z"
            status: "True"
            type: PodScheduled
            containerStatuses:
            - containerID: docker://4c1d8e2ff771b04b0ab5c4d9552b1e0b98c26c8ed52c8ea5b1562f26c24d8039
            image: kubernetesui/dashboard@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93
            imageID: docker-pullable://kubernetesui/dashboard@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93
            lastState: {}
            name: kubernetes-dashboard
            ready: true
            restartCount: 0
            started: true
            state:
                running:
                startedAt: "2023-10-10T19:29:47Z"
            hostIP: 192.168.49.2
            phase: Running
            podIP: 10.244.0.9
            podIPs:
            - ip: 10.244.0.9
            qosClass: BestEffort
            startTime: "2023-10-10T19:29:35Z"
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"clip-service","namespace":"default"},"spec":{"ports":[{"port":80,"protocol":"TCP","targetPort":8000}],"selector":{"app":"clip"}}}
            creationTimestamp: "2023-10-10T19:15:36Z"
            name: clip-service
            namespace: default
            resourceVersion: "700"
            uid: 7b591767-01fe-4fe8-8722-a919dd883269
        spec:
            clusterIP: 10.109.160.168
            clusterIPs:
            - 10.109.160.168
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - port: 80
            protocol: TCP
            targetPort: 8000
            selector:
            app: clip
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            creationTimestamp: "2023-10-10T19:11:45Z"
            labels:
            component: apiserver
            provider: kubernetes
            name: kubernetes
            namespace: default
            resourceVersion: "194"
            uid: 3ce81f46-77f7-4bda-b7de-ef027f66f2b9
        spec:
            clusterIP: 10.96.0.1
            clusterIPs:
            - 10.96.0.1
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - name: https
            port: 443
            protocol: TCP
            targetPort: 8443
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"},"spec":{"ipFamilies":["IPv4"],"ipFamilyPolicy":"SingleStack","ports":[{"appProtocol":"http","name":"http","port":80,"protocol":"TCP","targetPort":"http"},{"appProtocol":"https","name":"https","port":443,"protocol":"TCP","targetPort":"https"}],"selector":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"type":"NodePort"}}
            creationTimestamp: "2023-10-10T19:12:04Z"
            labels:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            name: ingress-nginx-controller
            namespace: ingress-nginx
            resourceVersion: "384"
            uid: c73d3786-8754-4a98-a10d-58c73d793e0f
        spec:
            clusterIP: 10.103.167.98
            clusterIPs:
            - 10.103.167.98
            externalTrafficPolicy: Cluster
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - appProtocol: http
            name: http
            nodePort: 30316
            port: 80
            protocol: TCP
            targetPort: http
            - appProtocol: https
            name: https
            nodePort: 32080
            port: 443
            protocol: TCP
            targetPort: https
            selector:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            sessionAffinity: None
            type: NodePort
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller-admission","namespace":"ingress-nginx"},"spec":{"ports":[{"appProtocol":"https","name":"https-webhook","port":443,"targetPort":"webhook"}],"selector":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"type":"ClusterIP"}}
            creationTimestamp: "2023-10-10T19:12:04Z"
            labels:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            name: ingress-nginx-controller-admission
            namespace: ingress-nginx
            resourceVersion: "388"
            uid: e2a7f6c8-61e4-49d2-82f8-fe29df474646
        spec:
            clusterIP: 10.103.228.231
            clusterIPs:
            - 10.103.228.231
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - appProtocol: https
            name: https-webhook
            port: 443
            protocol: TCP
            targetPort: webhook
            selector:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            prometheus.io/port: "9153"
            prometheus.io/scrape: "true"
            creationTimestamp: "2023-10-10T19:11:47Z"
            labels:
            k8s-app: kube-dns
            kubernetes.io/cluster-service: "true"
            kubernetes.io/name: CoreDNS
            name: kube-dns
            namespace: kube-system
            resourceVersion: "225"
            uid: 638c7ba2-e209-4518-8e2e-fcbb7fca74c7
        spec:
            clusterIP: 10.96.0.10
            clusterIPs:
            - 10.96.0.10
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - name: dns
            port: 53
            protocol: UDP
            targetPort: 53
            - name: dns-tcp
            port: 53
            protocol: TCP
            targetPort: 53
            - name: metrics
            port: 9153
            protocol: TCP
            targetPort: 9153
            selector:
            k8s-app: kube-dns
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"metrics-server","kubernetes.io/minikube-addons":"metrics-server","kubernetes.io/minikube-addons-endpoint":"metrics-server","kubernetes.io/name":"Metrics-server"},"name":"metrics-server","namespace":"kube-system"},"spec":{"ports":[{"name":"https","port":443,"protocol":"TCP","targetPort":"https"}],"selector":{"k8s-app":"metrics-server"}}}
            creationTimestamp: "2023-10-10T19:29:18Z"
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            k8s-app: metrics-server
            kubernetes.io/minikube-addons: metrics-server
            kubernetes.io/minikube-addons-endpoint: metrics-server
            kubernetes.io/name: Metrics-server
            name: metrics-server
            namespace: kube-system
            resourceVersion: "1515"
            uid: b553a6e8-b1c9-44b0-bee5-4dba06648c64
        spec:
            clusterIP: 10.105.28.253
            clusterIPs:
            - 10.105.28.253
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - name: https
            port: 443
            protocol: TCP
            targetPort: https
            selector:
            k8s-app: metrics-server
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"dashboard-metrics-scraper","kubernetes.io/minikube-addons":"dashboard"},"name":"dashboard-metrics-scraper","namespace":"kubernetes-dashboard"},"spec":{"ports":[{"port":8000,"targetPort":8000}],"selector":{"k8s-app":"dashboard-metrics-scraper"}}}
            creationTimestamp: "2023-10-10T19:29:35Z"
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            k8s-app: dashboard-metrics-scraper
            kubernetes.io/minikube-addons: dashboard
            name: dashboard-metrics-scraper
            namespace: kubernetes-dashboard
            resourceVersion: "1597"
            uid: 92ab3861-3413-4371-9010-5d3c1940bd9b
        spec:
            clusterIP: 10.98.49.173
            clusterIPs:
            - 10.98.49.173
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - port: 8000
            protocol: TCP
            targetPort: 8000
            selector:
            k8s-app: dashboard-metrics-scraper
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: v1
        kind: Service
        metadata:
            annotations:
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"kubernetes-dashboard","kubernetes.io/minikube-addons":"dashboard"},"name":"kubernetes-dashboard","namespace":"kubernetes-dashboard"},"spec":{"ports":[{"port":80,"targetPort":9090}],"selector":{"k8s-app":"kubernetes-dashboard"}}}
            creationTimestamp: "2023-10-10T19:29:35Z"
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            k8s-app: kubernetes-dashboard
            kubernetes.io/minikube-addons: dashboard
            name: kubernetes-dashboard
            namespace: kubernetes-dashboard
            resourceVersion: "1579"
            uid: b402374d-9daa-4c8c-8510-d1b64e2a2bc9
        spec:
            clusterIP: 10.103.201.178
            clusterIPs:
            - 10.103.201.178
            internalTrafficPolicy: Cluster
            ipFamilies:
            - IPv4
            ipFamilyPolicy: SingleStack
            ports:
            - port: 80
            protocol: TCP
            targetPort: 9090
            selector:
            k8s-app: kubernetes-dashboard
            sessionAffinity: None
            type: ClusterIP
        status:
            loadBalancer: {}
        - apiVersion: apps/v1
        kind: DaemonSet
        metadata:
            annotations:
            deprecated.daemonset.template.generation: "1"
            creationTimestamp: "2023-10-10T19:11:47Z"
            generation: 1
            labels:
            k8s-app: kube-proxy
            name: kube-proxy
            namespace: kube-system
            resourceVersion: "361"
            uid: e959e86d-5dcc-4250-9610-84b5b6cfc9ed
        spec:
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                k8s-app: kube-proxy
            template:
            metadata:
                creationTimestamp: null
                labels:
                k8s-app: kube-proxy
            spec:
                containers:
                - command:
                - /usr/local/bin/kube-proxy
                - --config=/var/lib/kube-proxy/config.conf
                - --hostname-override=$(NODE_NAME)
                env:
                - name: NODE_NAME
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: spec.nodeName
                image: registry.k8s.io/kube-proxy:v1.27.4
                imagePullPolicy: IfNotPresent
                name: kube-proxy
                resources: {}
                securityContext:
                    privileged: true
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /var/lib/kube-proxy
                    name: kube-proxy
                - mountPath: /run/xtables.lock
                    name: xtables-lock
                - mountPath: /lib/modules
                    name: lib-modules
                    readOnly: true
                dnsPolicy: ClusterFirst
                hostNetwork: true
                nodeSelector:
                kubernetes.io/os: linux
                priorityClassName: system-node-critical
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: kube-proxy
                serviceAccountName: kube-proxy
                terminationGracePeriodSeconds: 30
                tolerations:
                - operator: Exists
                volumes:
                - configMap:
                    defaultMode: 420
                    name: kube-proxy
                name: kube-proxy
                - hostPath:
                    path: /run/xtables.lock
                    type: FileOrCreate
                name: xtables-lock
                - hostPath:
                    path: /lib/modules
                    type: ""
                name: lib-modules
            updateStrategy:
            rollingUpdate:
                maxSurge: 0
                maxUnavailable: 1
            type: RollingUpdate
        status:
            currentNumberScheduled: 1
            desiredNumberScheduled: 1
            numberAvailable: 1
            numberMisscheduled: 0
            numberReady: 1
            observedGeneration: 1
            updatedNumberScheduled: 1
        - apiVersion: apps/v1
        kind: Deployment
        metadata:
            annotations:
            deployment.kubernetes.io/revision: "1"
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app":"clip"},"name":"clip-deployment","namespace":"default"},"spec":{"replicas":2,"selector":{"matchLabels":{"app":"clip"}},"template":{"metadata":{"labels":{"app":"clip"}},"spec":{"containers":[{"image":"clip-deploy:latest","imagePullPolicy":"Never","name":"clip","ports":[{"containerPort":8000}]}]}}}}
            creationTimestamp: "2023-10-10T19:15:35Z"
            generation: 1
            labels:
            app: clip
            name: clip-deployment
            namespace: default
            resourceVersion: "720"
            uid: b81bf859-2dad-48c6-8b62-742d88303481
        spec:
            progressDeadlineSeconds: 600
            replicas: 2
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                app: clip
            strategy:
            rollingUpdate:
                maxSurge: 25%
                maxUnavailable: 25%
            type: RollingUpdate
            template:
            metadata:
                creationTimestamp: null
                labels:
                app: clip
            spec:
                containers:
                - image: clip-deploy:latest
                imagePullPolicy: Never
                name: clip
                ports:
                - containerPort: 8000
                    protocol: TCP
                resources: {}
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                dnsPolicy: ClusterFirst
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                terminationGracePeriodSeconds: 30
        status:
            availableReplicas: 2
            conditions:
            - lastTransitionTime: "2023-10-10T19:15:37Z"
            lastUpdateTime: "2023-10-10T19:15:37Z"
            message: Deployment has minimum availability.
            reason: MinimumReplicasAvailable
            status: "True"
            type: Available
            - lastTransitionTime: "2023-10-10T19:15:35Z"
            lastUpdateTime: "2023-10-10T19:15:37Z"
            message: ReplicaSet "clip-deployment-76cc744cdd" has successfully progressed.
            reason: NewReplicaSetAvailable
            status: "True"
            type: Progressing
            observedGeneration: 1
            readyReplicas: 2
            replicas: 2
            updatedReplicas: 2
        - apiVersion: apps/v1
        kind: Deployment
        metadata:
            annotations:
            deployment.kubernetes.io/revision: "1"
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"},"spec":{"minReadySeconds":0,"revisionHistoryLimit":10,"selector":{"matchLabels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"}},"strategy":{"rollingUpdate":{"maxUnavailable":1},"type":"RollingUpdate"},"template":{"metadata":{"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx","gcp-auth-skip-secret":"true"}},"spec":{"containers":[{"args":["/nginx-ingress-controller","--election-id=ingress-nginx-leader","--controller-class=k8s.io/ingress-nginx","--watch-ingress-without-class=true","--configmap=$(POD_NAMESPACE)/ingress-nginx-controller","--tcp-services-configmap=$(POD_NAMESPACE)/tcp-services","--udp-services-configmap=$(POD_NAMESPACE)/udp-services","--validating-webhook=:8443","--validating-webhook-certificate=/usr/local/certificates/cert","--validating-webhook-key=/usr/local/certificates/key"],"env":[{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"LD_PRELOAD","value":"/usr/local/lib/libmimalloc.so"}],"image":"registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd","imagePullPolicy":"IfNotPresent","lifecycle":{"preStop":{"exec":{"command":["/wait-shutdown"]}}},"livenessProbe":{"failureThreshold":5,"httpGet":{"path":"/healthz","port":10254,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"name":"controller","ports":[{"containerPort":80,"hostPort":80,"name":"http","protocol":"TCP"},{"containerPort":443,"hostPort":443,"name":"https","protocol":"TCP"},{"containerPort":8443,"name":"webhook","protocol":"TCP"}],"readinessProbe":{"failureThreshold":3,"httpGet":{"path":"/healthz","port":10254,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"resources":{"requests":{"cpu":"100m","memory":"90Mi"}},"securityContext":{"allowPrivilegeEscalation":true,"capabilities":{"add":["NET_BIND_SERVICE"],"drop":["ALL"]},"runAsUser":101},"volumeMounts":[{"mountPath":"/usr/local/certificates/","name":"webhook-cert","readOnly":true}]}],"dnsPolicy":"ClusterFirst","nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"serviceAccountName":"ingress-nginx","terminationGracePeriodSeconds":0,"tolerations":[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Equal"}],"volumes":[{"name":"webhook-cert","secret":{"secretName":"ingress-nginx-admission"}}]}}}}
            creationTimestamp: "2023-10-10T19:12:04Z"
            generation: 1
            labels:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            name: ingress-nginx-controller
            namespace: ingress-nginx
            resourceVersion: "567"
            uid: 817bd743-519c-4fc9-a04e-80e77e383aa7
        spec:
            progressDeadlineSeconds: 600
            replicas: 1
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                app.kubernetes.io/component: controller
                app.kubernetes.io/instance: ingress-nginx
                app.kubernetes.io/name: ingress-nginx
            strategy:
            rollingUpdate:
                maxSurge: 25%
                maxUnavailable: 1
            type: RollingUpdate
            template:
            metadata:
                creationTimestamp: null
                labels:
                app.kubernetes.io/component: controller
                app.kubernetes.io/instance: ingress-nginx
                app.kubernetes.io/name: ingress-nginx
                gcp-auth-skip-secret: "true"
            spec:
                containers:
                - args:
                - /nginx-ingress-controller
                - --election-id=ingress-nginx-leader
                - --controller-class=k8s.io/ingress-nginx
                - --watch-ingress-without-class=true
                - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
                - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
                - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
                - --validating-webhook=:8443
                - --validating-webhook-certificate=/usr/local/certificates/cert
                - --validating-webhook-key=/usr/local/certificates/key
                env:
                - name: POD_NAME
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.name
                - name: POD_NAMESPACE
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                - name: LD_PRELOAD
                    value: /usr/local/lib/libmimalloc.so
                image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
                imagePullPolicy: IfNotPresent
                lifecycle:
                    preStop:
                    exec:
                        command:
                        - /wait-shutdown
                livenessProbe:
                    failureThreshold: 5
                    httpGet:
                    path: /healthz
                    port: 10254
                    scheme: HTTP
                    initialDelaySeconds: 10
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                name: controller
                ports:
                - containerPort: 80
                    hostPort: 80
                    name: http
                    protocol: TCP
                - containerPort: 443
                    hostPort: 443
                    name: https
                    protocol: TCP
                - containerPort: 8443
                    name: webhook
                    protocol: TCP
                readinessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /healthz
                    port: 10254
                    scheme: HTTP
                    initialDelaySeconds: 10
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                resources:
                    requests:
                    cpu: 100m
                    memory: 90Mi
                securityContext:
                    allowPrivilegeEscalation: true
                    capabilities:
                    add:
                    - NET_BIND_SERVICE
                    drop:
                    - ALL
                    runAsUser: 101
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /usr/local/certificates/
                    name: webhook-cert
                    readOnly: true
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                minikube.k8s.io/primary: "true"
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: ingress-nginx
                serviceAccountName: ingress-nginx
                terminationGracePeriodSeconds: 0
                tolerations:
                - effect: NoSchedule
                key: node-role.kubernetes.io/master
                operator: Equal
                volumes:
                - name: webhook-cert
                secret:
                    defaultMode: 420
                    secretName: ingress-nginx-admission
        status:
            availableReplicas: 1
            conditions:
            - lastTransitionTime: "2023-10-10T19:12:04Z"
            lastUpdateTime: "2023-10-10T19:12:04Z"
            message: Deployment has minimum availability.
            reason: MinimumReplicasAvailable
            status: "True"
            type: Available
            - lastTransitionTime: "2023-10-10T19:12:04Z"
            lastUpdateTime: "2023-10-10T19:13:38Z"
            message: ReplicaSet "ingress-nginx-controller-7799c6795f" has successfully progressed.
            reason: NewReplicaSetAvailable
            status: "True"
            type: Progressing
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
            updatedReplicas: 1
        - apiVersion: apps/v1
        kind: Deployment
        metadata:
            annotations:
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:11:47Z"
            generation: 2
            labels:
            k8s-app: kube-dns
            name: coredns
            namespace: kube-system
            resourceVersion: "434"
            uid: 0e3aae58-967f-4daf-b5be-10918907838f
        spec:
            progressDeadlineSeconds: 600
            replicas: 1
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                k8s-app: kube-dns
            strategy:
            rollingUpdate:
                maxSurge: 25%
                maxUnavailable: 1
            type: RollingUpdate
            template:
            metadata:
                creationTimestamp: null
                labels:
                k8s-app: kube-dns
            spec:
                affinity:
                podAntiAffinity:
                    preferredDuringSchedulingIgnoredDuringExecution:
                    - podAffinityTerm:
                        labelSelector:
                        matchExpressions:
                        - key: k8s-app
                            operator: In
                            values:
                            - kube-dns
                        topologyKey: kubernetes.io/hostname
                    weight: 100
                containers:
                - args:
                - -conf
                - /etc/coredns/Corefile
                image: registry.k8s.io/coredns/coredns:v1.10.1
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 5
                    httpGet:
                    path: /health
                    port: 8080
                    scheme: HTTP
                    initialDelaySeconds: 60
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 5
                name: coredns
                ports:
                - containerPort: 53
                    name: dns
                    protocol: UDP
                - containerPort: 53
                    name: dns-tcp
                    protocol: TCP
                - containerPort: 9153
                    name: metrics
                    protocol: TCP
                readinessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /ready
                    port: 8181
                    scheme: HTTP
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                resources:
                    limits:
                    memory: 170Mi
                    requests:
                    cpu: 100m
                    memory: 70Mi
                securityContext:
                    allowPrivilegeEscalation: false
                    capabilities:
                    add:
                    - NET_BIND_SERVICE
                    drop:
                    - all
                    readOnlyRootFilesystem: true
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /etc/coredns
                    name: config-volume
                    readOnly: true
                dnsPolicy: Default
                nodeSelector:
                kubernetes.io/os: linux
                priorityClassName: system-cluster-critical
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: coredns
                serviceAccountName: coredns
                terminationGracePeriodSeconds: 30
                tolerations:
                - key: CriticalAddonsOnly
                operator: Exists
                - effect: NoSchedule
                key: node-role.kubernetes.io/control-plane
                volumes:
                - configMap:
                    defaultMode: 420
                    items:
                    - key: Corefile
                    path: Corefile
                    name: coredns
                name: config-volume
        status:
            availableReplicas: 1
            conditions:
            - lastTransitionTime: "2023-10-10T19:12:01Z"
            lastUpdateTime: "2023-10-10T19:12:01Z"
            message: Deployment has minimum availability.
            reason: MinimumReplicasAvailable
            status: "True"
            type: Available
            - lastTransitionTime: "2023-10-10T19:12:01Z"
            lastUpdateTime: "2023-10-10T19:12:12Z"
            message: ReplicaSet "coredns-5d78c9869d" has successfully progressed.
            reason: NewReplicaSetAvailable
            status: "True"
            type: Progressing
            observedGeneration: 2
            readyReplicas: 1
            replicas: 1
            updatedReplicas: 1
        - apiVersion: apps/v1
        kind: Deployment
        metadata:
            annotations:
            deployment.kubernetes.io/revision: "1"
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"metrics-server","kubernetes.io/minikube-addons":"metrics-server"},"name":"metrics-server","namespace":"kube-system"},"spec":{"selector":{"matchLabels":{"k8s-app":"metrics-server"}},"strategy":{"rollingUpdate":{"maxUnavailable":0}},"template":{"metadata":{"labels":{"k8s-app":"metrics-server"},"name":"metrics-server"},"spec":{"containers":[{"args":["--cert-dir=/tmp","--secure-port=4443","--kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname","--kubelet-use-node-status-port","--metric-resolution=60s","--kubelet-insecure-tls"],"image":"registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e","imagePullPolicy":"IfNotPresent","livenessProbe":{"failureThreshold":3,"httpGet":{"path":"/livez","port":"https","scheme":"HTTPS"},"periodSeconds":10},"name":"metrics-server","ports":[{"containerPort":4443,"name":"https","protocol":"TCP"}],"readinessProbe":{"failureThreshold":3,"httpGet":{"path":"/readyz","port":"https","scheme":"HTTPS"},"periodSeconds":10},"resources":{"requests":{"cpu":"100m","memory":"200Mi"}},"securityContext":{"readOnlyRootFilesystem":true,"runAsNonRoot":true,"runAsUser":1000},"volumeMounts":[{"mountPath":"/tmp","name":"tmp-dir"}]}],"priorityClassName":"system-cluster-critical","serviceAccountName":"metrics-server","volumes":[{"emptyDir":{},"name":"tmp-dir"}]}}}}
            creationTimestamp: "2023-10-10T19:29:18Z"
            generation: 1
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            k8s-app: metrics-server
            kubernetes.io/minikube-addons: metrics-server
            name: metrics-server
            namespace: kube-system
            resourceVersion: "1684"
            uid: 1dad8129-72bc-4c1c-a60a-85144bd8f5cd
        spec:
            progressDeadlineSeconds: 600
            replicas: 1
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                k8s-app: metrics-server
            strategy:
            rollingUpdate:
                maxSurge: 25%
                maxUnavailable: 0
            type: RollingUpdate
            template:
            metadata:
                creationTimestamp: null
                labels:
                k8s-app: metrics-server
                name: metrics-server
            spec:
                containers:
                - args:
                - --cert-dir=/tmp
                - --secure-port=4443
                - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
                - --kubelet-use-node-status-port
                - --metric-resolution=60s
                - --kubelet-insecure-tls
                image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /livez
                    port: https
                    scheme: HTTPS
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                name: metrics-server
                ports:
                - containerPort: 4443
                    name: https
                    protocol: TCP
                readinessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /readyz
                    port: https
                    scheme: HTTPS
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                resources:
                    requests:
                    cpu: 100m
                    memory: 200Mi
                securityContext:
                    readOnlyRootFilesystem: true
                    runAsNonRoot: true
                    runAsUser: 1000
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /tmp
                    name: tmp-dir
                dnsPolicy: ClusterFirst
                priorityClassName: system-cluster-critical
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: metrics-server
                serviceAccountName: metrics-server
                terminationGracePeriodSeconds: 30
                volumes:
                - emptyDir: {}
                name: tmp-dir
        status:
            availableReplicas: 1
            conditions:
            - lastTransitionTime: "2023-10-10T19:30:29Z"
            lastUpdateTime: "2023-10-10T19:30:29Z"
            message: Deployment has minimum availability.
            reason: MinimumReplicasAvailable
            status: "True"
            type: Available
            - lastTransitionTime: "2023-10-10T19:29:18Z"
            lastUpdateTime: "2023-10-10T19:30:29Z"
            message: ReplicaSet "metrics-server-7746886d4f" has successfully progressed.
            reason: NewReplicaSetAvailable
            status: "True"
            type: Progressing
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
            updatedReplicas: 1
        - apiVersion: apps/v1
        kind: Deployment
        metadata:
            annotations:
            deployment.kubernetes.io/revision: "1"
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"dashboard-metrics-scraper","kubernetes.io/minikube-addons":"dashboard"},"name":"dashboard-metrics-scraper","namespace":"kubernetes-dashboard"},"spec":{"replicas":1,"revisionHistoryLimit":10,"selector":{"matchLabels":{"k8s-app":"dashboard-metrics-scraper"}},"template":{"metadata":{"annotations":{"seccomp.security.alpha.kubernetes.io/pod":"runtime/default"},"labels":{"k8s-app":"dashboard-metrics-scraper"}},"spec":{"containers":[{"image":"docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c","livenessProbe":{"httpGet":{"path":"/","port":8000,"scheme":"HTTP"},"initialDelaySeconds":30,"timeoutSeconds":30},"name":"dashboard-metrics-scraper","ports":[{"containerPort":8000,"protocol":"TCP"}],"securityContext":{"allowPrivilegeEscalation":false,"readOnlyRootFilesystem":true,"runAsGroup":2001,"runAsUser":1001},"volumeMounts":[{"mountPath":"/tmp","name":"tmp-volume"}]}],"nodeSelector":{"kubernetes.io/os":"linux"},"serviceAccountName":"kubernetes-dashboard","tolerations":[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master"}],"volumes":[{"emptyDir":{},"name":"tmp-volume"}]}}}}
            creationTimestamp: "2023-10-10T19:29:35Z"
            generation: 1
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            k8s-app: dashboard-metrics-scraper
            kubernetes.io/minikube-addons: dashboard
            name: dashboard-metrics-scraper
            namespace: kubernetes-dashboard
            resourceVersion: "1642"
            uid: 7c144fb8-d3b3-4675-a245-cb93063120a9
        spec:
            progressDeadlineSeconds: 600
            replicas: 1
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                k8s-app: dashboard-metrics-scraper
            strategy:
            rollingUpdate:
                maxSurge: 25%
                maxUnavailable: 25%
            type: RollingUpdate
            template:
            metadata:
                annotations:
                seccomp.security.alpha.kubernetes.io/pod: runtime/default
                creationTimestamp: null
                labels:
                k8s-app: dashboard-metrics-scraper
            spec:
                containers:
                - image: docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /
                    port: 8000
                    scheme: HTTP
                    initialDelaySeconds: 30
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 30
                name: dashboard-metrics-scraper
                ports:
                - containerPort: 8000
                    protocol: TCP
                resources: {}
                securityContext:
                    allowPrivilegeEscalation: false
                    readOnlyRootFilesystem: true
                    runAsGroup: 2001
                    runAsUser: 1001
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /tmp
                    name: tmp-volume
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: kubernetes-dashboard
                serviceAccountName: kubernetes-dashboard
                terminationGracePeriodSeconds: 30
                tolerations:
                - effect: NoSchedule
                key: node-role.kubernetes.io/master
                volumes:
                - emptyDir: {}
                name: tmp-volume
        status:
            availableReplicas: 1
            conditions:
            - lastTransitionTime: "2023-10-10T19:29:54Z"
            lastUpdateTime: "2023-10-10T19:29:54Z"
            message: Deployment has minimum availability.
            reason: MinimumReplicasAvailable
            status: "True"
            type: Available
            - lastTransitionTime: "2023-10-10T19:29:35Z"
            lastUpdateTime: "2023-10-10T19:29:54Z"
            message: ReplicaSet "dashboard-metrics-scraper-5dd9cbfd69" has successfully
                progressed.
            reason: NewReplicaSetAvailable
            status: "True"
            type: Progressing
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
            updatedReplicas: 1
        - apiVersion: apps/v1
        kind: Deployment
        metadata:
            annotations:
            deployment.kubernetes.io/revision: "1"
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"kubernetes-dashboard","kubernetes.io/minikube-addons":"dashboard"},"name":"kubernetes-dashboard","namespace":"kubernetes-dashboard"},"spec":{"replicas":1,"revisionHistoryLimit":10,"selector":{"matchLabels":{"k8s-app":"kubernetes-dashboard"}},"template":{"metadata":{"labels":{"gcp-auth-skip-secret":"true","k8s-app":"kubernetes-dashboard"}},"spec":{"containers":[{"args":["--namespace=kubernetes-dashboard","--enable-skip-login","--disable-settings-authorizer"],"image":"docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93","livenessProbe":{"httpGet":{"path":"/","port":9090},"initialDelaySeconds":30,"timeoutSeconds":30},"name":"kubernetes-dashboard","ports":[{"containerPort":9090,"protocol":"TCP"}],"securityContext":{"allowPrivilegeEscalation":false,"readOnlyRootFilesystem":true,"runAsGroup":2001,"runAsUser":1001},"volumeMounts":[{"mountPath":"/tmp","name":"tmp-volume"}]}],"nodeSelector":{"kubernetes.io/os":"linux"},"serviceAccountName":"kubernetes-dashboard","tolerations":[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master"}],"volumes":[{"emptyDir":{},"name":"tmp-volume"}]}}}}
            creationTimestamp: "2023-10-10T19:29:35Z"
            generation: 1
            labels:
            addonmanager.kubernetes.io/mode: Reconcile
            k8s-app: kubernetes-dashboard
            kubernetes.io/minikube-addons: dashboard
            name: kubernetes-dashboard
            namespace: kubernetes-dashboard
            resourceVersion: "1627"
            uid: f2a1594a-d99e-43ca-b444-176aeb45cca6
        spec:
            progressDeadlineSeconds: 600
            replicas: 1
            revisionHistoryLimit: 10
            selector:
            matchLabels:
                k8s-app: kubernetes-dashboard
            strategy:
            rollingUpdate:
                maxSurge: 25%
                maxUnavailable: 25%
            type: RollingUpdate
            template:
            metadata:
                creationTimestamp: null
                labels:
                gcp-auth-skip-secret: "true"
                k8s-app: kubernetes-dashboard
            spec:
                containers:
                - args:
                - --namespace=kubernetes-dashboard
                - --enable-skip-login
                - --disable-settings-authorizer
                image: docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /
                    port: 9090
                    scheme: HTTP
                    initialDelaySeconds: 30
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 30
                name: kubernetes-dashboard
                ports:
                - containerPort: 9090
                    protocol: TCP
                resources: {}
                securityContext:
                    allowPrivilegeEscalation: false
                    readOnlyRootFilesystem: true
                    runAsGroup: 2001
                    runAsUser: 1001
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /tmp
                    name: tmp-volume
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: kubernetes-dashboard
                serviceAccountName: kubernetes-dashboard
                terminationGracePeriodSeconds: 30
                tolerations:
                - effect: NoSchedule
                key: node-role.kubernetes.io/master
                volumes:
                - emptyDir: {}
                name: tmp-volume
        status:
            availableReplicas: 1
            conditions:
            - lastTransitionTime: "2023-10-10T19:29:48Z"
            lastUpdateTime: "2023-10-10T19:29:48Z"
            message: Deployment has minimum availability.
            reason: MinimumReplicasAvailable
            status: "True"
            type: Available
            - lastTransitionTime: "2023-10-10T19:29:35Z"
            lastUpdateTime: "2023-10-10T19:29:48Z"
            message: ReplicaSet "kubernetes-dashboard-5c5cfc8747" has successfully progressed.
            reason: NewReplicaSetAvailable
            status: "True"
            type: Progressing
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
            updatedReplicas: 1
        - apiVersion: apps/v1
        kind: ReplicaSet
        metadata:
            annotations:
            deployment.kubernetes.io/desired-replicas: "2"
            deployment.kubernetes.io/max-replicas: "3"
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:15:35Z"
            generation: 1
            labels:
            app: clip
            pod-template-hash: 76cc744cdd
            name: clip-deployment-76cc744cdd
            namespace: default
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: Deployment
            name: clip-deployment
            uid: b81bf859-2dad-48c6-8b62-742d88303481
            resourceVersion: "719"
            uid: cc7e80cb-89ed-402b-ba72-b42954338f9d
        spec:
            replicas: 2
            selector:
            matchLabels:
                app: clip
                pod-template-hash: 76cc744cdd
            template:
            metadata:
                creationTimestamp: null
                labels:
                app: clip
                pod-template-hash: 76cc744cdd
            spec:
                containers:
                - image: clip-deploy:latest
                imagePullPolicy: Never
                name: clip
                ports:
                - containerPort: 8000
                    protocol: TCP
                resources: {}
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                dnsPolicy: ClusterFirst
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                terminationGracePeriodSeconds: 30
        status:
            availableReplicas: 2
            fullyLabeledReplicas: 2
            observedGeneration: 1
            readyReplicas: 2
            replicas: 2
        - apiVersion: apps/v1
        kind: ReplicaSet
        metadata:
            annotations:
            deployment.kubernetes.io/desired-replicas: "1"
            deployment.kubernetes.io/max-replicas: "2"
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:12:04Z"
            generation: 1
            labels:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            gcp-auth-skip-secret: "true"
            pod-template-hash: 7799c6795f
            name: ingress-nginx-controller-7799c6795f
            namespace: ingress-nginx
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: Deployment
            name: ingress-nginx-controller
            uid: 817bd743-519c-4fc9-a04e-80e77e383aa7
            resourceVersion: "566"
            uid: bb789b18-6036-4c52-91b8-a616b942769d
        spec:
            replicas: 1
            selector:
            matchLabels:
                app.kubernetes.io/component: controller
                app.kubernetes.io/instance: ingress-nginx
                app.kubernetes.io/name: ingress-nginx
                pod-template-hash: 7799c6795f
            template:
            metadata:
                creationTimestamp: null
                labels:
                app.kubernetes.io/component: controller
                app.kubernetes.io/instance: ingress-nginx
                app.kubernetes.io/name: ingress-nginx
                gcp-auth-skip-secret: "true"
                pod-template-hash: 7799c6795f
            spec:
                containers:
                - args:
                - /nginx-ingress-controller
                - --election-id=ingress-nginx-leader
                - --controller-class=k8s.io/ingress-nginx
                - --watch-ingress-without-class=true
                - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
                - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
                - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
                - --validating-webhook=:8443
                - --validating-webhook-certificate=/usr/local/certificates/cert
                - --validating-webhook-key=/usr/local/certificates/key
                env:
                - name: POD_NAME
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.name
                - name: POD_NAMESPACE
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                - name: LD_PRELOAD
                    value: /usr/local/lib/libmimalloc.so
                image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
                imagePullPolicy: IfNotPresent
                lifecycle:
                    preStop:
                    exec:
                        command:
                        - /wait-shutdown
                livenessProbe:
                    failureThreshold: 5
                    httpGet:
                    path: /healthz
                    port: 10254
                    scheme: HTTP
                    initialDelaySeconds: 10
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                name: controller
                ports:
                - containerPort: 80
                    hostPort: 80
                    name: http
                    protocol: TCP
                - containerPort: 443
                    hostPort: 443
                    name: https
                    protocol: TCP
                - containerPort: 8443
                    name: webhook
                    protocol: TCP
                readinessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /healthz
                    port: 10254
                    scheme: HTTP
                    initialDelaySeconds: 10
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                resources:
                    requests:
                    cpu: 100m
                    memory: 90Mi
                securityContext:
                    allowPrivilegeEscalation: true
                    capabilities:
                    add:
                    - NET_BIND_SERVICE
                    drop:
                    - ALL
                    runAsUser: 101
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /usr/local/certificates/
                    name: webhook-cert
                    readOnly: true
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                minikube.k8s.io/primary: "true"
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: ingress-nginx
                serviceAccountName: ingress-nginx
                terminationGracePeriodSeconds: 0
                tolerations:
                - effect: NoSchedule
                key: node-role.kubernetes.io/master
                operator: Equal
                volumes:
                - name: webhook-cert
                secret:
                    defaultMode: 420
                    secretName: ingress-nginx-admission
        status:
            availableReplicas: 1
            fullyLabeledReplicas: 1
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
        - apiVersion: apps/v1
        kind: ReplicaSet
        metadata:
            annotations:
            deployment.kubernetes.io/desired-replicas: "1"
            deployment.kubernetes.io/max-replicas: "2"
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:12:01Z"
            generation: 1
            labels:
            k8s-app: kube-dns
            pod-template-hash: 5d78c9869d
            name: coredns-5d78c9869d
            namespace: kube-system
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: Deployment
            name: coredns
            uid: 0e3aae58-967f-4daf-b5be-10918907838f
            resourceVersion: "433"
            uid: 0e22824d-b5df-48d6-85d2-1e1826eecfc4
        spec:
            replicas: 1
            selector:
            matchLabels:
                k8s-app: kube-dns
                pod-template-hash: 5d78c9869d
            template:
            metadata:
                creationTimestamp: null
                labels:
                k8s-app: kube-dns
                pod-template-hash: 5d78c9869d
            spec:
                affinity:
                podAntiAffinity:
                    preferredDuringSchedulingIgnoredDuringExecution:
                    - podAffinityTerm:
                        labelSelector:
                        matchExpressions:
                        - key: k8s-app
                            operator: In
                            values:
                            - kube-dns
                        topologyKey: kubernetes.io/hostname
                    weight: 100
                containers:
                - args:
                - -conf
                - /etc/coredns/Corefile
                image: registry.k8s.io/coredns/coredns:v1.10.1
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 5
                    httpGet:
                    path: /health
                    port: 8080
                    scheme: HTTP
                    initialDelaySeconds: 60
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 5
                name: coredns
                ports:
                - containerPort: 53
                    name: dns
                    protocol: UDP
                - containerPort: 53
                    name: dns-tcp
                    protocol: TCP
                - containerPort: 9153
                    name: metrics
                    protocol: TCP
                readinessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /ready
                    port: 8181
                    scheme: HTTP
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                resources:
                    limits:
                    memory: 170Mi
                    requests:
                    cpu: 100m
                    memory: 70Mi
                securityContext:
                    allowPrivilegeEscalation: false
                    capabilities:
                    add:
                    - NET_BIND_SERVICE
                    drop:
                    - all
                    readOnlyRootFilesystem: true
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /etc/coredns
                    name: config-volume
                    readOnly: true
                dnsPolicy: Default
                nodeSelector:
                kubernetes.io/os: linux
                priorityClassName: system-cluster-critical
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: coredns
                serviceAccountName: coredns
                terminationGracePeriodSeconds: 30
                tolerations:
                - key: CriticalAddonsOnly
                operator: Exists
                - effect: NoSchedule
                key: node-role.kubernetes.io/control-plane
                volumes:
                - configMap:
                    defaultMode: 420
                    items:
                    - key: Corefile
                    path: Corefile
                    name: coredns
                name: config-volume
        status:
            availableReplicas: 1
            fullyLabeledReplicas: 1
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
        - apiVersion: apps/v1
        kind: ReplicaSet
        metadata:
            annotations:
            deployment.kubernetes.io/desired-replicas: "1"
            deployment.kubernetes.io/max-replicas: "2"
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:29:18Z"
            generation: 1
            labels:
            k8s-app: metrics-server
            pod-template-hash: 7746886d4f
            name: metrics-server-7746886d4f
            namespace: kube-system
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: Deployment
            name: metrics-server
            uid: 1dad8129-72bc-4c1c-a60a-85144bd8f5cd
            resourceVersion: "1682"
            uid: 9c091172-8f2a-43f9-aa41-856a9c3e586b
        spec:
            replicas: 1
            selector:
            matchLabels:
                k8s-app: metrics-server
                pod-template-hash: 7746886d4f
            template:
            metadata:
                creationTimestamp: null
                labels:
                k8s-app: metrics-server
                pod-template-hash: 7746886d4f
                name: metrics-server
            spec:
                containers:
                - args:
                - --cert-dir=/tmp
                - --secure-port=4443
                - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
                - --kubelet-use-node-status-port
                - --metric-resolution=60s
                - --kubelet-insecure-tls
                image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /livez
                    port: https
                    scheme: HTTPS
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                name: metrics-server
                ports:
                - containerPort: 4443
                    name: https
                    protocol: TCP
                readinessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /readyz
                    port: https
                    scheme: HTTPS
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 1
                resources:
                    requests:
                    cpu: 100m
                    memory: 200Mi
                securityContext:
                    readOnlyRootFilesystem: true
                    runAsNonRoot: true
                    runAsUser: 1000
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /tmp
                    name: tmp-dir
                dnsPolicy: ClusterFirst
                priorityClassName: system-cluster-critical
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: metrics-server
                serviceAccountName: metrics-server
                terminationGracePeriodSeconds: 30
                volumes:
                - emptyDir: {}
                name: tmp-dir
        status:
            availableReplicas: 1
            fullyLabeledReplicas: 1
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
        - apiVersion: apps/v1
        kind: ReplicaSet
        metadata:
            annotations:
            deployment.kubernetes.io/desired-replicas: "1"
            deployment.kubernetes.io/max-replicas: "2"
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:29:35Z"
            generation: 1
            labels:
            k8s-app: dashboard-metrics-scraper
            pod-template-hash: 5dd9cbfd69
            name: dashboard-metrics-scraper-5dd9cbfd69
            namespace: kubernetes-dashboard
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: Deployment
            name: dashboard-metrics-scraper
            uid: 7c144fb8-d3b3-4675-a245-cb93063120a9
            resourceVersion: "1641"
            uid: e35b080d-dcdb-4f19-8297-ee60bde32d69
        spec:
            replicas: 1
            selector:
            matchLabels:
                k8s-app: dashboard-metrics-scraper
                pod-template-hash: 5dd9cbfd69
            template:
            metadata:
                annotations:
                seccomp.security.alpha.kubernetes.io/pod: runtime/default
                creationTimestamp: null
                labels:
                k8s-app: dashboard-metrics-scraper
                pod-template-hash: 5dd9cbfd69
            spec:
                containers:
                - image: docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /
                    port: 8000
                    scheme: HTTP
                    initialDelaySeconds: 30
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 30
                name: dashboard-metrics-scraper
                ports:
                - containerPort: 8000
                    protocol: TCP
                resources: {}
                securityContext:
                    allowPrivilegeEscalation: false
                    readOnlyRootFilesystem: true
                    runAsGroup: 2001
                    runAsUser: 1001
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /tmp
                    name: tmp-volume
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: kubernetes-dashboard
                serviceAccountName: kubernetes-dashboard
                terminationGracePeriodSeconds: 30
                tolerations:
                - effect: NoSchedule
                key: node-role.kubernetes.io/master
                volumes:
                - emptyDir: {}
                name: tmp-volume
        status:
            availableReplicas: 1
            fullyLabeledReplicas: 1
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
        - apiVersion: apps/v1
        kind: ReplicaSet
        metadata:
            annotations:
            deployment.kubernetes.io/desired-replicas: "1"
            deployment.kubernetes.io/max-replicas: "2"
            deployment.kubernetes.io/revision: "1"
            creationTimestamp: "2023-10-10T19:29:35Z"
            generation: 1
            labels:
            gcp-auth-skip-secret: "true"
            k8s-app: kubernetes-dashboard
            pod-template-hash: 5c5cfc8747
            name: kubernetes-dashboard-5c5cfc8747
            namespace: kubernetes-dashboard
            ownerReferences:
            - apiVersion: apps/v1
            blockOwnerDeletion: true
            controller: true
            kind: Deployment
            name: kubernetes-dashboard
            uid: f2a1594a-d99e-43ca-b444-176aeb45cca6
            resourceVersion: "1626"
            uid: 567aed1d-958a-45be-8002-a534e5e36cc9
        spec:
            replicas: 1
            selector:
            matchLabels:
                k8s-app: kubernetes-dashboard
                pod-template-hash: 5c5cfc8747
            template:
            metadata:
                creationTimestamp: null
                labels:
                gcp-auth-skip-secret: "true"
                k8s-app: kubernetes-dashboard
                pod-template-hash: 5c5cfc8747
            spec:
                containers:
                - args:
                - --namespace=kubernetes-dashboard
                - --enable-skip-login
                - --disable-settings-authorizer
                image: docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93
                imagePullPolicy: IfNotPresent
                livenessProbe:
                    failureThreshold: 3
                    httpGet:
                    path: /
                    port: 9090
                    scheme: HTTP
                    initialDelaySeconds: 30
                    periodSeconds: 10
                    successThreshold: 1
                    timeoutSeconds: 30
                name: kubernetes-dashboard
                ports:
                - containerPort: 9090
                    protocol: TCP
                resources: {}
                securityContext:
                    allowPrivilegeEscalation: false
                    readOnlyRootFilesystem: true
                    runAsGroup: 2001
                    runAsUser: 1001
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                volumeMounts:
                - mountPath: /tmp
                    name: tmp-volume
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                restartPolicy: Always
                schedulerName: default-scheduler
                securityContext: {}
                serviceAccount: kubernetes-dashboard
                serviceAccountName: kubernetes-dashboard
                terminationGracePeriodSeconds: 30
                tolerations:
                - effect: NoSchedule
                key: node-role.kubernetes.io/master
                volumes:
                - emptyDir: {}
                name: tmp-volume
        status:
            availableReplicas: 1
            fullyLabeledReplicas: 1
            observedGeneration: 1
            readyReplicas: 1
            replicas: 1
        - apiVersion: batch/v1
        kind: Job
        metadata:
            annotations:
            batch.kubernetes.io/job-tracking: ""
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-create","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-create"},"spec":{"containers":[{"args":["create","--host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc","--namespace=$(POD_NAMESPACE)","--secret-name=ingress-nginx-admission"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"create","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
            creationTimestamp: "2023-10-10T19:12:04Z"
            generation: 1
            labels:
            app.kubernetes.io/component: admission-webhook
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            name: ingress-nginx-admission-create
            namespace: ingress-nginx
            resourceVersion: "493"
            uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
        spec:
            backoffLimit: 6
            completionMode: NonIndexed
            completions: 1
            parallelism: 1
            selector:
            matchLabels:
                batch.kubernetes.io/controller-uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
            suspend: false
            template:
            metadata:
                creationTimestamp: null
                labels:
                app.kubernetes.io/component: admission-webhook
                app.kubernetes.io/instance: ingress-nginx
                app.kubernetes.io/name: ingress-nginx
                batch.kubernetes.io/controller-uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
                batch.kubernetes.io/job-name: ingress-nginx-admission-create
                controller-uid: cb47522f-0fcc-4f46-88d5-0c73224e0f3d
                job-name: ingress-nginx-admission-create
                name: ingress-nginx-admission-create
            spec:
                containers:
                - args:
                - create
                - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
                - --namespace=$(POD_NAMESPACE)
                - --secret-name=ingress-nginx-admission
                env:
                - name: POD_NAMESPACE
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
                imagePullPolicy: IfNotPresent
                name: create
                resources: {}
                securityContext:
                    allowPrivilegeEscalation: false
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                minikube.k8s.io/primary: "true"
                restartPolicy: OnFailure
                schedulerName: default-scheduler
                securityContext:
                runAsNonRoot: true
                runAsUser: 2000
                serviceAccount: ingress-nginx-admission
                serviceAccountName: ingress-nginx-admission
                terminationGracePeriodSeconds: 30
        status:
            completionTime: "2023-10-10T19:12:51Z"
            conditions:
            - lastProbeTime: "2023-10-10T19:12:51Z"
            lastTransitionTime: "2023-10-10T19:12:51Z"
            status: "True"
            type: Complete
            ready: 0
            startTime: "2023-10-10T19:12:04Z"
            succeeded: 1
            uncountedTerminatedPods: {}
        - apiVersion: batch/v1
        kind: Job
        metadata:
            annotations:
            batch.kubernetes.io/job-tracking: ""
            kubectl.kubernetes.io/last-applied-configuration: |
                {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch"},"spec":{"containers":[{"args":["patch","--webhook-name=ingress-nginx-admission","--namespace=$(POD_NAMESPACE)","--patch-mutating=false","--secret-name=ingress-nginx-admission","--patch-failure-policy=Fail"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"patch","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
            creationTimestamp: "2023-10-10T19:12:04Z"
            generation: 1
            labels:
            app.kubernetes.io/component: admission-webhook
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
            name: ingress-nginx-admission-patch
            namespace: ingress-nginx
            resourceVersion: "509"
            uid: d3db7523-18cc-4556-8751-f5ae233975fb
        spec:
            backoffLimit: 6
            completionMode: NonIndexed
            completions: 1
            parallelism: 1
            selector:
            matchLabels:
                batch.kubernetes.io/controller-uid: d3db7523-18cc-4556-8751-f5ae233975fb
            suspend: false
            template:
            metadata:
                creationTimestamp: null
                labels:
                app.kubernetes.io/component: admission-webhook
                app.kubernetes.io/instance: ingress-nginx
                app.kubernetes.io/name: ingress-nginx
                batch.kubernetes.io/controller-uid: d3db7523-18cc-4556-8751-f5ae233975fb
                batch.kubernetes.io/job-name: ingress-nginx-admission-patch
                controller-uid: d3db7523-18cc-4556-8751-f5ae233975fb
                job-name: ingress-nginx-admission-patch
                name: ingress-nginx-admission-patch
            spec:
                containers:
                - args:
                - patch
                - --webhook-name=ingress-nginx-admission
                - --namespace=$(POD_NAMESPACE)
                - --patch-mutating=false
                - --secret-name=ingress-nginx-admission
                - --patch-failure-policy=Fail
                env:
                - name: POD_NAMESPACE
                    valueFrom:
                    fieldRef:
                        apiVersion: v1
                        fieldPath: metadata.namespace
                image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
                imagePullPolicy: IfNotPresent
                name: patch
                resources: {}
                securityContext:
                    allowPrivilegeEscalation: false
                terminationMessagePath: /dev/termination-log
                terminationMessagePolicy: File
                dnsPolicy: ClusterFirst
                nodeSelector:
                kubernetes.io/os: linux
                minikube.k8s.io/primary: "true"
                restartPolicy: OnFailure
                schedulerName: default-scheduler
                securityContext:
                runAsNonRoot: true
                runAsUser: 2000
                serviceAccount: ingress-nginx-admission
                serviceAccountName: ingress-nginx-admission
                terminationGracePeriodSeconds: 30
        status:
            completionTime: "2023-10-10T19:12:57Z"
            conditions:
            - lastProbeTime: "2023-10-10T19:12:57Z"
            lastTransitionTime: "2023-10-10T19:12:57Z"
            status: "True"
            type: Complete
            ready: 0
            startTime: "2023-10-10T19:12:04Z"
            succeeded: 1
            uncountedTerminatedPods: {}
        kind: List
        metadata:
        resourceVersion: ""
    ```