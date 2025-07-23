---
description: Learn How to Create Detection Recipes
icon: grill-hot
---

# Create Recipes

## <mark style="color:yellow;">YAML Recipe Structure</mark>

Detection recipes are defined in YAML files with the following structure:

```yaml
# Recipe definition
- kind: unique_recipe_identifier
  name: recipe_name
  enabled: true|false
  version: 1.0
  description: Brief description of what this detects
  documentation: |
    https://link.to.documentation

  # Classification fields
  breed: file_access|execution|remote_domains|...
  mechanism: file_access|execution|network_peers|...
  tactic: MITRE_ATTACK_tactic
  technique: MITRE_ATTACK_technique
  subtechnique: MITRE_ATTACK_subtechnique
  importance: low|medium|high|critical

  # Noise reduction
  times:
    - kind: times_per_proc|times_per_exe|times_per_full_ancestry|...
      max: number

  # Additional filters
  arbitrary: [] # Advanced filtering rules


  # Type-specific fields (see below)
```

## <mark style="color:yellow;">File Access Detection Recipe</mark>

For detecting file access patterns:

```yaml
- kind: sensitive_file_access
  name: sensitive_file_access
  enabled: true
  version: 1.0
  description: Detects access to sensitive system files
  documentation: |
    https://docs.example.com/sensitive_file_access
  breed: file_access
  mechanism: file_access
  tactic: credential_access
  technique: credentials_from_password_stores
  subtechnique: credentials_from_files
  importance: high

  # Noise reduction
  times:
    - kind: times_per_proc
      max: 5
    - kind: times_per_exe
      max: 10

  # File actions to monitor
  file_actions: read_related|write_related|modify_related
  file_actions_how: any|all
  file_actions_excl: mmap # Optional: exclude specific actions

  # File patterns (can use one or multiple)
  base: shadow # Simple filename
  dir: /etc # Directory path
  regex: .*\.key$ # Regex pattern

  # Or multiple file patterns
  bases:
    - base: passwd
      dir: /etc
    - base: shadow
      dir: /etc
    - regex: /home/.*/.ssh/id_rsa$
    - regex: /root/.ssh/.*$
```

## <mark style="color:yellow;">Execution Detection Recipe</mark>

For detecting process execution patterns:

```yaml
- kind: suspicious_tool_execution
  name: suspicious_tool_execution
  enabled: true
  version: 1.0
  description: Detects execution of suspicious tools
  documentation: |
    https://docs.example.com/suspicious_tools
  breed: file_access
  mechanism: execution
  tactic: discovery
  technique: system_network_configuration_discovery
  subtechnique: ""
  importance: medium

  times:
    - kind: times_per_parent_proc
      max: 3

  # Must include execve for execution detection
  file_actions: execve
  file_actions_how: any

  # Executables to monitor
  bases:
    - base: nmap
    - base: masscan
    - base: zmap
    - base: nikto
    - base: dirb
    - base: gobuster
```

## <mark style="color:yellow;">Network Peer Detection Recipe</mark>

For detecting network communication patterns:

```yaml
- kind: malicious_domain_access
  name: malicious_domain_access
  enabled: true
  version: 1.0
  description: Detects communication with known malicious domains
  documentation: |
    https://docs.example.com/malicious_domains
  breed: remote_domains
  mechanism: network_peers
  tactic: command_and_control
  technique: application_layer_protocol
  subtechnique: web_protocols
  importance: critical

  times:
    - kind: times_per_proc
      max: 2

  # Network configuration
  protocol: tcp|udp|icmp
  local_cidrs:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16
  remote_cidrs:
    - 1.2.3.0/24
  local_port: 0 # 0 means any port
  remote_port: 443

  # Domain matching
  remote_domains_trie_type: exact|suffix|prefix
  remote_domains:
    - evil.com
    - malicious.net
    - c2server.org

  # Flow actions
  flow_actions: created|ongoing|ended
  flow_actions_how: any|all
  flow_actions_excl: ingress # Optional
```

## <mark style="color:yellow;">Advanced Filtering with Arbitrary Rules</mark>

The `arbitrary` field allows complex filtering based on process attributes:

```yaml
arbitrary:
  - how: AND|OR
    which: pertinent|irrelevant
    items:
      - what: exe|comm|cmd|args|uid|pid|parent_exe|...
        which: pertinent|irrelevant
        pattern: "regex_pattern"
        number: 1000
        numbers: [1000, 1001, 1002]
        time: "2024-01-01T00:00:00Z"
        cidr: "192.168.1.0/24"
        when: smaller|bigger|equal
```
