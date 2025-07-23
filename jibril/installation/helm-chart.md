---
icon: subtitles
---

# Helm Chart

This document describes how to deploy Jibril to Kubernetes using the Garnet Helm chart.

## Overview

The Garnet Helm chart supports two deployment modes:

1. **Garnet Mode** - Full integration with Garnet API for policy management and security monitoring
2. **Jibril Standalone Mode** - Deploy Jibril without Garnet API dependencies

## Prerequisites

* Kubernetes 1.16+
* Helm 3.0+
* A valid Garnet API token (required for Garnet mode only)

## Installation

### Jibril Standalone Mode

The standalone mode allows you to deploy Jibril without requiring a Garnet API token or connection. This is useful for:

* Testing and evaluation
* Air-gapped environments
* Custom integrations
* Environments with older kernel versions

#### Basic Standalone Installation

```bash
# From Helm repository
helm repo add garnet https://helm.garnet.ai
helm repo update

helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true

# From local sources
helm install jibril ./helm/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true
```

#### Standalone with Specific Version

For compatibility with older kernels, you can specify a particular Jibril version:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set standalone.jibrilVersion=v2.4
```

### Garnet Mode (Full Integration)

Deploy with full Garnet API integration for centralized policy management:

```bash
helm install garnet garnet/garnet \
  --namespace security \
  --create-namespace \
  --set garnet.token=YOUR_GARNET_API_TOKEN
```

## Configuration

### Key Configuration Parameters

| Parameter                  | Description                                       | Default                 |
| -------------------------- | ------------------------------------------------- | ----------------------- |
| `standalone.enabled`       | Enable standalone mode (no Garnet API)            | `false`                 |
| `standalone.jibrilVersion` | Override Jibril version in standalone mode        | `""`                    |
| `garnet.url`               | Garnet API URL                                    | `https://api.garnet.ai` |
| `garnet.token`             | Your Garnet API token (required in standard mode) | `""`                    |
| `cluster.name`             | Name of the cluster                               | `garnet-cluster`        |
| `jibril.image.repository`  | Repository for Jibril image                       | `garnetlabs/jibril`     |
| `jibril.image.tag`         | Tag for Jibril image                              | `v2.4`                  |

### Custom Jibril Configuration

You can provide a custom Jibril configuration file:

```bash
# Create a custom config file (e.g., jibril-config.yaml)
cat > jibril-config.yaml <<EOF
log-level: debug
stdout: stdout
stderr: stderr
profiler: true
cardinal: true
extension:
  - config
  - data
  - jibril
plugin:
  - jibril:hold
  - jibril:procfs
  - jibril:printers
  - jibril:detect
printer:
  - jibril:printers:varlog
event:
  # Add your custom events here
EOF

# Deploy with custom config
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set jibrilConfig.customConfig=true \
  --set-file jibrilConfig.configYaml=./jibril-config.yaml
```

### Environment Variables

The chart supports two methods for setting environment variables:

#### Method 1: Simple Variables (via --set)

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set jibril.env.LOG_LEVEL=debug \
  --set jibril.env.CUSTOM_VAR=myvalue
```

#### Method 2: Complex Variables (with valueFrom)

Create a values file:

```yaml
jibril:
  customEnv:
    - name: MY_SECRET_VAR
      valueFrom:
        secretKeyRef:
          name: my-secret
          key: secret-key
    - name: MY_CONFIGMAP_VAR
      valueFrom:
        configMapKeyRef:
          name: my-configmap
          key: config-key
```

Then deploy:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  -f custom-env-values.yaml
```

## Network Policy Support

The chart supports deploying Jibril with custom network policies for enhanced security:

### Enabling Network Policy

1. Create a network policy file:

```yaml
# netpolicy.yaml
version: v1
policies:
  - name: block-malicious
    rules:
      - action: drop
        domains:
          - malicious.com
          - badsite.org
        ips:
          - 10.0.0.1
          - 192.168.1.100
```

2. Deploy with network policy:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set networkPolicyConfig.enabled=true \
  --set-file networkPolicyConfig.policyYaml=./netpolicy.yaml
```

3. Update the network policy:

```bash
# Modify your netpolicy.yaml file, then:
helm upgrade jibril garnet/garnet \
  --namespace security \
  --set standalone.enabled=true \
  --set networkPolicyConfig.enabled=true \
  --set-file networkPolicyConfig.policyYaml=./netpolicy.yaml
```

The pods will automatically restart to apply the new policy.

### Network Policy Configuration Requirements

When using network policy, ensure your Jibril configuration includes:

```yaml
plugin:
  - jibril:netpolicy:file=/var/run/secrets/jibril/network-policy.yaml
event:
  - jibril:netpolicy:dropip
  - jibril:netpolicy:dropdomain
```

## Advanced Examples

### Complete Standalone Deployment

Deploy Jibril with custom configuration, network policy, and environment variables:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set standalone.jibrilVersion=v2.4 \
  --set jibrilConfig.customConfig=true \
  --set-file jibrilConfig.configYaml=./jibril-config.yaml \
  --set networkPolicyConfig.enabled=true \
  --set-file networkPolicyConfig.policyYaml=./netpolicy.yaml \
  --set jibril.env.AI_URL="https://api.example.com" \
  --set jibril.env.AI_TOKEN="your-token-here"
```

### Custom Registry and Image Pull Secrets

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set image.registry=my-registry.example.com/ \
  --set image.pullSecrets[0]=my-registry-secret
```

### Resource Customization

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set jibril.resources.requests.memory=512Mi \
  --set jibril.resources.requests.cpu=200m \
  --set jibril.resources.limits.memory=1Gi \
  --set jibril.resources.limits.cpu=500m
```

## Verifying the Deployment

After installation, verify that Jibril is running:

```bash
# Check pods
kubectl get pods -n security

# Check logs
kubectl logs -n security daemonset/jibril-jibril

# Run helm tests
helm test jibril -n security
```

## Troubleshooting

### Common Issues

1. **Pods not starting**: Check logs for missing configuration or permissions
2. **Network policy not working**: Ensure the netpolicy plugin is enabled in Jibril config
3. **High CPU usage**: Consider adjusting the profiler settings or event filters

### Debug Commands

```bash
# Get detailed pod information
kubectl describe pod -n security -l app.kubernetes.io/name=jibril

# Check configuration
kubectl exec -n security daemonset/jibril-jibril -- cat /etc/jibril/config.yaml

# Check network policy (if enabled)
kubectl exec -n security daemonset/jibril-jibril -- cat /var/run/secrets/jibril/network-policy.yaml
```

## Uninstalling

To remove the Jibril deployment:

```bash
helm uninstall jibril -n security
```

## Additional Resources

* [Jibril Architecture](../readme/architecture.md)
* [Network Policy Configuration](../components/network-policy.md)
* [Components Overview](../components/)
* [Installation Methods](./)
