---
description: Jibril versus ...
icon: chart-mixed
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Compare

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt="" width="256"><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Falco" %}
| Feature / Tool    | Jibril                                                                     | Falco                                      |
| ----------------- | -------------------------------------------------------------------------- | ------------------------------------------ |
| Developer         | Garnet Labs                                                                | Sysdig (CNCF Graduated)                    |
| Primary Focus     | LOW overhead Runtime detection and policy enforcement                      | Runtime threat detection and alerting      |
| Core Technology   | eBPF, static and dynamic analysis                                          | eBPF, kernel modules                       |
| Detection         | Yes (built-in rule based)                                                  | Yes (rule-based, real-time)                |
| Enforcement       | Yes (eBPF, cgroups)                                                        | Limited (via Falco, post-event response)   |
| Policy Definition | Custom rules                                                               | Default public rules                       |
| Default Policies  | Yes (MITRE), complete recipes set                                          | Comprehensive default ruleset              |
| Scope             | CI/CD, Containers, VMs, Kubernetes, IoT/Edge, Classic IT                   | Containers, Kubernetes, cloud, hosts       |
| Observability     | JSON events and per agent dashboard                                        | Logs, metrics (via Falco Sidekick), traces |
| Performance       | Lightweight resources use with minimum detection losses                    | Low latency, High resource use (eBPF)      |
| Integration       | Garnet Security, Custom integration with event printers                    | Broad SIEM support, Falco Sidekick         |
| Use Case          | Real-time threat detection, network enforcement                            | Real-time threat detection, compliance     |
| Strengths         | Low overhead, Realtime enforce, Min detect losses, BIG public recipes list | Mature, Wide Adoption, Public ruleset      |
| Weaknesses        | No exec enforcement, Less mature, Recipes description lang TBD             | Limited Enforcement, Rule Complexity       |
{% endtab %}

{% tab title="Tracee" %}
| Feature / Tool    | Jibril                                                                     | Tracee                                             |
| ----------------- | -------------------------------------------------------------------------- | -------------------------------------------------- |
| Developer         | Garnet Labs                                                                | Aqua Security                                      |
| Primary Focus     | LOW overhead Runtime detection and policy enforcement                      | Runtime detection and forensics                    |
| Core Technology   | eBPF, static and dynamic analysis                                          | eBPF                                               |
| Detection         | Yes (built-in rule based)                                                  | Yes (detailed event tracing)                       |
| Enforcement       | Yes (eBPF, cgroups)                                                        | No (detection only)                                |
| Policy Definition | Custom rules                                                               | JSON-based policies with scope and rules           |
| Default Policies  | Yes (MITRE), complete recipes set                                          | Basic default policy                               |
| Scope             | CI/CD, Containers, VMs, Kubernetes, IoT/Edge, Classic IT                   | Containers, Kubernetes, Linux hosts                |
| Observability     | JSON events and per agent dashboard                                        | Detailed JSON event logs                           |
| Performance       | Lightweight resources use with minimum detection losses                    | High resource use                                  |
| Integration       | Garnet Security, Custom integration with event printers                    | Trivy, Kubernetes operators                        |
| Use Case          | Real-time threat detection, network enforcement                            | Forensics, suspicious event analysis               |
| Strengths         | Low overhead, Realtime enforce, Min detect losses, BIG public recipes list | Detailed Forensics, Public signatures, OPA support |
| Weaknesses        | No exec enforcement, Less mature, Recipes description lang TBD             | No enforcement, Resource Intensive                 |
{% endtab %}

{% tab title="Tetragon" %}
| Feature / Tool    | Jibril                                                                     | Tetragon                                         |
| ----------------- | -------------------------------------------------------------------------- | ------------------------------------------------ |
| Developer         | Garnet Labs                                                                | Cilium/Isovalent (CNCF Incubating)               |
| Primary Focus     | LOW overhead Runtime detection and policy enforcement                      | Security observability and runtime enforcement   |
| Core Technology   | eBPF, static and dynamic analysis                                          | eBPF                                             |
| Detection         | Yes (built-in rule based)                                                  | Yes (real-time observability)                    |
| Enforcement       | Yes (eBPF, cgroups)                                                        | Yes (real-time policy enforcement)               |
| Policy Definition | Custom rules                                                               | TracingPolicy CRDs, Kernel level filters         |
| Default Policies  | Yes (MITRE), complete recipes set                                          | No preloaded policies, customizable              |
| Scope             | CI/CD, Containers, VMs, Kubernetes, IoT/Edge, Classic IT                   | Kubernetes, Linux hosts, Cilium integration      |
| Observability     | JSON events and per agent dashboard                                        | Rich event logs, low-latency observability       |
| Performance       | Lightweight resources use with minimum detection losses                    | Low latency, Resource efficient                  |
| Integration       | Garnet Security, Custom integration with event printers                    | Cilium ecosystem, OpenTelemetry                  |
| Use Case          | Real-time threat detection, network enforcement                            | Observability, enforcement, network security     |
| Strengths         | Low overhead, Realtime enforce, Min detect losses, BIG public recipes list | Low overhead, Enforcement, Cilium Integration    |
| Weaknesses        | No exec enforcement, Less mature, Recipes description lang TBD             | Less mature, Fewer integrations, Rule complexity |
{% endtab %}

{% tab title="KubeArmor" %}
| Feature / Tool    | Jibril                                                                     | KubeArmor                                            |
| ----------------- | -------------------------------------------------------------------------- | ---------------------------------------------------- |
| Developer         | Garnet Labs                                                                | AccuKnox (CNCF Sandbox)                              |
| Primary Focus     | LOW overhead Runtime detection and policy enforcement                      | Runtime protection and policy enforcement            |
| Core Technology   | eBPF, static and dynamic analysis                                          | eBPF (integration), LSM (AppArmor, SELinux, BPF-LSM) |
| Detection         | Yes (built-in rule based)                                                  | Yes (via eBPF logs and alerts)                       |
| Enforcement       | Yes (eBPF, cgroups)                                                        | Yes (inline mitigation via LSM)                      |
| Policy Definition | Custom rules                                                               | YAML-based Kubernetes-native                         |
| Default Policies  | Yes (MITRE), complete recipes set                                          | No preloaded policies                                |
| Scope             | CI/CD, Containers, VMs, Kubernetes, IoT/Edge, Classic IT                   | Containers, VMs, Kubernetes, IoT/Edge, 5G            |
| Observability     | JSON events and per agent dashboard                                        | Logs for policy breaches, process monitoring         |
| Performance       | Lightweight resources use with minimum detection losses                    | Moderate latency                                     |
| Integration       | Garnet Security, Custom integration with event printers                    | Kubernetes-native, limited SIEM support              |
| Use Case          | Real-time threat detection, network enforcement                            | Hardening workloads, zero-trust enforcement          |
| Strengths         | Low overhead, Realtime enforce, Min detect losses, BIG public recipes list | Simplifies LSM complexity                            |
| Weaknesses        | No exec enforcement, Less mature, Recipes description lang TBD             | Lacks default policies, Higher Latencies             |
{% endtab %}

{% tab title="Kubescape" %}
| Feature / Tool    | Jibril                                                                     | Kubescape                                                            |
| ----------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Developer         | Garnet Labs                                                                | ARMO                                                                 |
| Primary Focus     | LOW overhead Runtime detection and policy enforcement                      | Kubernetes security scanning and compliance                          |
| Core Technology   | eBPF, static and dynamic analysis                                          | Static analysis, Kubernetes API, optional runtime (via integrations) |
| Detection         | Yes (built-in rule based)                                                  | Yes (misconfig detection, vuln scanning)                             |
| Enforcement       | Yes (eBPF, cgroups)                                                        | Limited (via integration with tools like KubeArmor)                  |
| Policy Definition | Custom rules                                                               | YAML-based (OPA, NSA, MITRE frameworks)                              |
| Default Policies  | Yes (MITRE), complete recipes set                                          | Yes (NSA, MITRE, custom frameworks)                                  |
| Scope             | CI/CD, Containers, VMs, Kubernetes, IoT/Edge, Classic IT                   | Kubernetes clusters, workloads                                       |
| Observability     | JSON events and per agent dashboard                                        | Reports, dashboards, runtime insights (via integrations)             |
| Performance       | Lightweight resources use with minimum detection losses                    | Lightweight (static), runtime depends on integrations                |
| Integration       | Garnet Security, Custom integration with event printers                    | Helm, CI/CD, KubeArmor, Prometheus                                   |
| Use Case          | Real-time threat detection, network enforcement                            | Compliance, misconfiguration detection, vuln management              |
| Strengths         | Low overhead, Realtime enforce, Min detect losses, BIG public recipes list | Easy compliance checks, broad framework support                      |
| Weaknesses        | No exec enforcement, Less mature, Recipes description lang TBD             | Limited Enforcement, Relies on Integrations                          |
{% endtab %}
{% endtabs %}
