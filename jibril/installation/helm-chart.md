# Helm Chart

This document describes how to deploy Jibril to Kubernetes using the Garnet Helm chart.

## Overview

The Garnet Helm chart supports two deployment modes:

1. **Garnet Mode** - Full integration with Garnet API for policy management and security monitoring
2. **Jibril Standalone Mode** - Deploy Jibril without Garnet API dependencies

## Prerequisites

- Kubernetes 1.16+
- Helm 3.0+
- A valid Garnet API token (required for Garnet mode only)

## Installation

### Jibril Standalone Mode

The standalone mode allows you to deploy Jibril without requiring a Garnet API token or connection. This is useful for:
- Testing and evaluation
- Air-gapped environments
- Custom integrations
- Environments with older kernel versions

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
  --set standalone.jibrilVersion=v2.2.1
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

| Parameter | Description | Default |
|-----------|-------------|---------|
| `standalone.enabled` | Enable standalone mode (no Garnet API) | `false` |
| `standalone.jibrilVersion` | Override Jibril version in standalone mode | `""` |
| `garnet.url` | Garnet API URL | `https://api.garnet.ai` |
| `garnet.token` | Your Garnet API token (required in standard mode) | `""` |
| `cluster.name` | Name of the cluster | `garnet-cluster` |
| `jibril.image.repository` | Repository for Jibril image | `garnetlabs/jibril` |
| `jibril.image.tag` | Tag for Jibril image | `v2.4` |

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

## Fluent Bit Integration

The Garnet Helm chart includes optional Fluent Bit integration for collecting and forwarding Jibril logs to various destinations.

### Enabling Fluent Bit

Fluent Bit runs as a DaemonSet to collect logs from all Jibril pods:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set fluent-bit.enabled=true
```

### Basic Fluent Bit Configuration

By default, Fluent Bit will:
- Collect logs from `/var/log/containers/jibril-*.log`
- Parse JSON-formatted logs from Jibril
- Output to stdout for debugging

### Configuring OpenSearch Output

To send Jibril logs to OpenSearch/Elasticsearch:

#### Basic OpenSearch Configuration

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set fluent-bit.enabled=true \
  --set fluent-bit.opensearch.enabled=true \
  --set fluent-bit.opensearch.host=opensearch.example.com \
  --set fluent-bit.opensearch.port=9200
```

#### OpenSearch with Authentication

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set fluent-bit.enabled=true \
  --set fluent-bit.opensearch.enabled=true \
  --set fluent-bit.opensearch.host=opensearch.example.com \
  --set fluent-bit.opensearch.port=9200 \
  --set fluent-bit.opensearch.httpUser=admin \
  --set fluent-bit.opensearch.httpPasswd=mypassword \
  --set fluent-bit.opensearch.tls=On \
  --set fluent-bit.opensearch.tlsVerify=On
```

#### AWS OpenSearch Service

For AWS OpenSearch Service (formerly Elasticsearch Service):

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set fluent-bit.enabled=true \
  --set fluent-bit.opensearch.enabled=true \
  --set fluent-bit.opensearch.host=my-domain.us-east-1.es.amazonaws.com \
  --set fluent-bit.opensearch.port=443 \
  --set fluent-bit.opensearch.tls=On \
  --set fluent-bit.opensearch.awsAuth=On \
  --set fluent-bit.opensearch.awsRegion=us-east-1 \
  --set fluent-bit.opensearch.awsServiceName=es \
  --set fluent-bit.opensearch.logstashPrefix=jibril-logs \
  --set fluent-bit.opensearch.compress=gzip
```

With IAM role for service account (IRSA) on EKS:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set fluent-bit.enabled=true \
  --set fluent-bit.opensearch.enabled=true \
  --set fluent-bit.opensearch.host=my-domain.us-west-2.es.amazonaws.com \
  --set fluent-bit.opensearch.port=443 \
  --set fluent-bit.opensearch.tls=On \
  --set fluent-bit.opensearch.awsAuth=On \
  --set fluent-bit.opensearch.awsRegion=us-west-2 \
  --set fluent-bit.opensearch.awsServiceName=es \
  --set fluent-bit.opensearch.awsRoleArn=arn:aws:iam::123456789012:role/fluent-bit-opensearch-role \
  --set fluent-bit.opensearch.logstashPrefix=jibril-logs
```

### Fluent Bit Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| `fluent-bit.enabled` | Enable Fluent Bit DaemonSet | `false` |
| `fluent-bit.opensearch.enabled` | Enable OpenSearch output | `false` |
| `fluent-bit.opensearch.host` | OpenSearch host | `localhost` |
| `fluent-bit.opensearch.port` | OpenSearch port | `9200` |
| `fluent-bit.opensearch.index` | Index name (if not using logstash format) | `jibril` |
| `fluent-bit.opensearch.logstashFormat` | Use daily indices | `true` |
| `fluent-bit.opensearch.logstashPrefix` | Prefix for daily indices | `jibril` |
| `fluent-bit.opensearch.httpUser` | Basic auth username | `""` |
| `fluent-bit.opensearch.httpPasswd` | Basic auth password | `""` |
| `fluent-bit.opensearch.tls` | Enable TLS | `Off` |
| `fluent-bit.opensearch.tlsVerify` | Verify TLS certificates | `On` |
| `fluent-bit.opensearch.awsAuth` | Enable AWS authentication | `Off` |
| `fluent-bit.opensearch.awsRegion` | AWS region | `""` |
| `fluent-bit.opensearch.compress` | Enable compression | `gzip` |

### Advanced Fluent Bit Examples

#### Custom Index Pattern with Authentication

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  --set standalone.enabled=true \
  --set fluent-bit.enabled=true \
  --set fluent-bit.opensearch.enabled=true \
  --set fluent-bit.opensearch.host=opensearch.example.com \
  --set fluent-bit.opensearch.port=9200 \
  --set fluent-bit.opensearch.logstashFormat=true \
  --set fluent-bit.opensearch.logstashPrefix=security-jibril \
  --set fluent-bit.opensearch.logstashDateFormat="%Y.%m" \
  --set fluent-bit.opensearch.httpUser=fluentbit \
  --set fluent-bit.opensearch.httpPasswd=secretpassword \
  --set fluent-bit.opensearch.includeTagKey=true \
  --set fluent-bit.opensearch.tagKey=k8s_tag
```

#### Complete Production Setup

Create a values file for production:

```yaml
# production-values.yaml
standalone:
  enabled: true

fluent-bit:
  enabled: true
  image:
    tag: 4.0.4
  resources:
    limits:
      memory: 256Mi
      cpu: 500m
    requests:
      memory: 128Mi
      cpu: 200m
  
  opensearch:
    enabled: true
    host: opensearch-cluster.elastic.svc.cluster.local
    port: 9200
    logstashFormat: true
    logstashPrefix: prod-jibril
    logstashDateFormat: "%Y.%m.%d"
    httpUser: fluent
    httpPasswd: ${OPENSEARCH_PASSWORD}
    tls: On
    tlsVerify: On
    compress: gzip
    bufferSize: "8MB"
    includeTagKey: true
    tagKey: "@log_tag"
    replaceDots: On
    suppressTypeName: On
```

Deploy with:

```bash
helm install jibril garnet/garnet \
  --namespace security \
  --create-namespace \
  -f production-values.yaml \
  --set fluent-bit.opensearch.httpPasswd=$OPENSEARCH_PASSWORD
```

### Verifying Fluent Bit

Check Fluent Bit status:

```bash
# Check Fluent Bit pods
kubectl get pods -n security -l app.kubernetes.io/name=fluent-bit

# View Fluent Bit logs
kubectl logs -n security -l app.kubernetes.io/name=fluent-bit -f

# Check if logs are being collected
kubectl logs -n security -l app.kubernetes.io/name=fluent-bit | grep -i "jibril"
```

### Troubleshooting Fluent Bit

1. **Fluent Bit pods not starting**:
   ```bash
   kubectl describe pod -n security <fluent-bit-pod-name>
   ```

2. **Logs not appearing in OpenSearch**:
   - Check Fluent Bit logs for errors
   - Verify network connectivity to OpenSearch
   - Check authentication credentials
   - Ensure proper index permissions in OpenSearch

3. **High memory usage**:
   - Reduce `mem_buf_limit` in configuration
   - Adjust `buffer_chunk_size` and `buffer_max_size`

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
  --set standalone.jibrilVersion=v2.2.2 \
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

- [Jibril Architecture](../readme/architecture.md)
- [Network Policy Configuration](../components/network-policy.md)
- [Components Overview](../components/)
- [Installation Methods](../installation/)