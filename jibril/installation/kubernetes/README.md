---
icon: box-open
---

# Kubernetes

<figure><img src="../../../.gitbook/assets/Kubernetes (1).png" alt="" width="125"><figcaption></figcaption></figure>

> Check out Jibril's public recipes repository at [https://github.com/garnet-org/jibril-balag](https://github.com/garnet-org/jibril-balag).

## <mark style="color:yellow;">Deploy Jibril on Kubernetes Clusters</mark>

To deploy Jibril as a DaemonSet on Kubernetes clusters, use the [`setup-k8s.sh`](kubernetes-script.md) script (also available at [GitHub](https://github.com/listendev/jibril-releases/blob/main/deploy/k8s/setup-k8s.sh). This script automatically creates a **Deployment** file with the necessary **ConfigMap**, **DaemonSet**, and related resources.

{% hint style="info" %}
Make sure to use `--dry-run` so it does not apply the deployment automatically.
{% endhint %}

{% hint style="success" %}
Currently almost all development-like Kubernetes distributions (Minikube, Microk8s, ...) are supported, as long as compute nodes are virtual-machines or real hosts.
{% endhint %}

{% hint style="danger" %}
Container based compute nodes distributions, like [Kind](https://kind.sigs.k8s.io/), will make resource consumption bigger and is unsupported for now).
{% endhint %}

## <mark style="color:yellow;">Usage</mark>

```shell-session
$ ./setup-k8s.sh [OPTIONS]
```

### Options

<table data-header-hidden><thead><tr><th width="345.171875">Option</th><th width="578.35546875">Description</th></tr></thead><tbody><tr><td><code>--namespace=NAME</code></td><td>Kubernetes namespace<br>Default: security</td></tr><tr><td><code>--image=IMAGE</code></td><td>Jibril container image<br>Default: garnetlabs/jibril:v1.4</td></tr><tr><td><code>--log-level=LEVEL</code></td><td>Log level (quiet, fatal, error, warn, info, debug)<br>Default: info</td></tr><tr><td><code>--config=FILE</code></td><td>Path to custom Jibril config.yaml file<br>Defaullt: built-in</td></tr><tr><td><code>--memory-request=SIZE</code></td><td>Memory request<br>Default: 256Mi</td></tr><tr><td><code>--memory-limit=SIZE</code></td><td>Memory limit<br>Default: 512Mi</td></tr><tr><td><code>--cpu-request=AMOUNT</code></td><td>CPU request<br>Default: 100m</td></tr><tr><td><code>--cpu-limit=AMOUNT</code></td><td>CPU limit<br>Default: 500m</td></tr><tr><td><code>--node-selector=EXPR</code></td><td>Node selector expression (e.g. 'role=security')</td></tr><tr><td><code>--toleration=KEY:VAL:EFFECT</code></td><td>Add toleration (can be used multiple times)</td></tr><tr><td><code>--output=FILE</code></td><td>Output YAML to file<br>Default: jibril-k8s.yaml</td></tr><tr><td><code>--dry-run</code></td><td>Print configuration without applying</td></tr><tr><td><code>--cleanup</code></td><td>Remove existing Jibril resources from the cluster</td></tr><tr><td><code>--help</code></td><td>Show help</td></tr></tbody></table>

### Examples

1.  **Basic deployment with defaults**

    ```sh
    $ ./setup-k8s.sh
    ```
2.  **Deploy to a custom namespace**

    ```sh
    $ ./setup-k8s.sh --namespace=monitoring
    ```
3.  **Add node toleration**

    ```sh
    $ ./setup-k8s.sh --toleration=security-agent:true:NoSchedule
    ```
4.  **Set custom memory limits**

    ```sh
    $ ./setup-k8s.sh --memory-limit=1Gi --memory-request=512Mi
    ```
5.  **Target specific nodes with a node selector**

    ```sh
    $ ./setup-k8s.sh --node-selector=role=security
    ```
6.  **Deploy on GPU nodes with higher CPU limits**

    ```sh
    $ ./setup-k8s.sh --node-selector=gpu=true --cpu-limit=2 --cpu-request=500m
    ```
7.  **Configure multiple tolerations**

    ```sh
    $ ./setup-k8s.sh --toleration=security:true:NoSchedule --toleration=critical:true:NoExecute
    ```
8.  **Use a custom Jibril configuration file**

    ```sh
    $ ./setup-k8s.sh --config=/path/to/my-jibril-config.yaml
    ```
9.  **Preview configuration without applying**

    ```sh
    $ ./setup-k8s.sh --dry-run
    ```
10. **Save configuration to a custom file**

    ```sh
    $ ./setup-k8s.sh --output=jibril-prod.yaml
    ```
11. **Clean up existing deployment**

    ```sh
    $ ./setup-k8s.sh --cleanup --namespace=security
    ```
12. **Complete production deployment example**

    ```sh
    $ ./setup-k8s.sh --namespace=security-prod \
      --image=garnetlabs/jibril:latest \
      --config=/etc/jibril/prod-config.yaml \
      --memory-limit=2Gi \
      --memory-request=1Gi \
      --cpu-limit=1 \
      --toleration=security-monitoring:true:NoSchedule \
      --node-selector=security-tier=high
    ```

## Notes

{% hint style="info" %}
* Jibril requires privileged access to run eBPF programs.
* The script mounts necessary paths from the host:
  * `/sys/fs/bpf`
  * `/sys/kernel/debug`
  * `/sys`
  * `/proc`
  * `/var/log/jibril`
* Log files are stored in `/var/log/jibril` on the host.
* Configuration is supplied via a ConfigMap.
{% endhint %}
