# -*- coding: utf-8 -*-
import yaml

pod_data = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": "nginx-k8s",
        "namespace": "default",
    },
    "spec": {
        "containers": [
            {"name": "openthings-container"},
            {"image": "tensorflow/tensorflow:latest-gpu"},
            {"imagePullPolicy": "Always"},
            {"command": []},
            {"args": []},
            {"volumeMounts": [
                {"name": "nfs"},
                {"mountPath": "/mnt"},
                {"readOnly": "boolean"}
            ]},
            {"ports": [
                {"name": "port"},
                {"containerPort": 80},
                {"hostPort": 80},
                {"protocol": "TCP"}
            ]},
            {"resources": {
                "limits": {
                    "cpu": "1",
                    "memory": "2GB",
                    "nvidia.com/gpu": 1
                },
                "requests": {
                    "cpu": "1",
                    "memory": "2GB",
                    "nvidia.com/gpu": 1
                }
            }}
        ]
    }
}

tensorflow_data = pod_data
tensorflow_data["metadata"]["name"] = "tensorflow"
tensorflow_data["spec"]["containers"][0]["name"] = "tensorflow"
print(yaml.dump(pod_data))

