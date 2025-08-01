---
description: Container Administration Command [T1609]
icon: terminal
---

# Container Administration Command

## Information

* Name: Container Administration Command
* ID: T1609
* Tactics: [TA0002](../)

## Introduction

Container Administration Command is classified under the MITRE ATT\&CK framework as technique T1609, falling under the tactic of Execution. This technique involves adversaries abusing commands related to container management tools (such as Docker, Kubernetes, or containerd) to execute commands within containers or orchestrate malicious activities. Attackers leverage these legitimate administrative tools to gain persistence, escalate privileges, move laterally, or execute arbitrary code within compromised environments. Due to the widespread adoption and reliance on containerization technologies, this technique is becoming increasingly prevalent and impactful in modern infrastructure.

## Deep Dive Into Technique

Attackers exploit container administration commands by leveraging legitimate container runtime interfaces, orchestrators, and management tools. Commonly targeted container technologies include Docker, Kubernetes, containerd, and Podman.

Technical details and execution methods include:

* **Docker Exec**:
  * Attackers utilize `docker exec` to execute commands inside running containers.
  * Example: `docker exec -it [container-id] /bin/bash` allows interactive shell access within a container.
* **Docker Run**:
  * Adversaries may spawn new malicious containers using `docker run`.
  * Example: `docker run -d --privileged attacker/image` creates a privileged container with elevated permissions.
* **Kubernetes Exec**:
  * Using `kubectl exec`, attackers can run commands inside Kubernetes pods.
  * Example: `kubectl exec -it [pod-name] -- /bin/sh`.
* **Containerd and CRI Interfaces**:
  * Attackers may directly communicate with lower-level container runtimes (containerd, CRI-O) via their APIs to manage containers and execute arbitrary commands.
* **Misconfigured APIs and Sockets**:
  * Exposed Docker sockets (`/var/run/docker.sock`) or Kubernetes APIs without proper authentication allow attackers to remotely manage containers.
  * Example: Attackers use curl or Docker CLI to interact with exposed Docker APIs.

Real-world procedures typically involve:

* Privilege escalation through container breakout techniques.
* Persistence by deploying malicious containers that restart automatically.
* Lateral movement across containerized environments by exploiting insecure network configurations and shared volumes.
* Data exfiltration by mounting sensitive host directories into containers.

## When this Technique is Usually Used

Attackers commonly use Container Administration Command techniques during various attack stages and scenarios:

* **Initial Access and Reconnaissance**:
  * Exploiting exposed container management APIs or sockets to gain initial foothold.
* **Execution and Privilege Escalation**:
  * Running commands inside containers to escalate privileges or break out to host systems.
* **Persistence**:
  * Deploying malicious containers with restart policies to maintain presence after reboots.
* **Lateral Movement**:
  * Leveraging container orchestration tools (e.g., Kubernetes namespaces and clusters) to pivot across different nodes and services.
* **Defense Evasion**:
  * Utilizing ephemeral containers or containerized malware to evade traditional security controls and monitoring tools.
* **Exfiltration and Impact**:
  * Mounting sensitive host directories, exfiltrating data, or performing denial-of-service attacks by resource exhaustion.

## How this Technique is Usually Detected

Effective detection of Container Administration Command techniques involves monitoring container runtime activities, analyzing logs, and employing specialized tools:

* **Monitoring Command Execution Logs**:
  * Docker daemon logs (`/var/log/docker.log` or journalctl logs).
  * Kubernetes audit logs for suspicious `kubectl exec` commands.
* **Runtime Security Tools and Agents**:
  * Falco, Aqua Security, Sysdig Secure, Prisma Cloud, and similar tools that monitor container runtime behavior and detect anomalies.
* **Host-Based Detection**:
  * Monitoring access patterns to container runtime sockets (`/var/run/docker.sock`).
  * Detecting unexpected container creations, privileged containers, or unusual container images being pulled from external registries.
* **Behavioral Anomaly Detection**:
  * Machine learning-based anomaly detection tools that identify deviations from baseline container usage patterns.
* **Indicators of Compromise (IoCs)**:
  * Unusual container images or registries (`docker pull` from unknown sources).
  * Abnormal container command executions (`docker exec` or `kubectl exec`).
  * Privileged or host-mounted containers (`docker run --privileged`, `docker run -v /:/host`).
  * Unexpected container resource usage spikes or network connections.

## Why it is Important to Detect This Technique

Early and accurate detection of Container Administration Command abuse is critical due to its severe potential impacts:

* **Privilege Escalation and Host Compromise**:
  * Attackers may escalate privileges by escaping containers, gaining root-level access to underlying hosts or clusters.
* **Persistence and Stealth**:
  * Malicious containers can persist undetected, providing attackers with long-term footholds within infrastructure.
* **Lateral Movement and Spread**:
  * Container environments often span multiple hosts and clusters, enabling attackers to rapidly pivot across systems and networks.
* **Data Theft and Exfiltration**:
  * Attackers can mount sensitive host volumes, access confidential information, and exfiltrate data covertly.
* **Resource Exhaustion and Denial-of-Service**:
  * Malicious containers can exhaust CPU, memory, or network resources, causing service degradation or outages.
* **Regulatory and Compliance Risks**:
  * Undetected container-based attacks can lead to data breaches, compliance violations, and significant reputational and financial damage.

## Examples

Real-world examples and attack scenarios leveraging Container Administration Command techniques include:

* **TeamTNT Malware Campaign**:
  * Attackers targeted exposed Docker APIs to deploy malicious containers running cryptominers and stealing AWS credentials.
  * Tools used: Docker CLI, custom scripts, cryptomining binaries.
  * Impact: Resource exhaustion, financial loss, credential theft.
* **Hildegard Malware**:
  * Exploited misconfigured Kubernetes clusters to deploy cryptominers and conduct lateral movement.
  * Tools used: Kubernetes management commands (`kubectl exec`, `kubectl create`), Monero cryptominer binaries.
  * Impact: Unauthorized resource utilization, lateral movement across clusters.
* **Doki Malware**:
  * Leveraged Docker APIs to execute malicious containers, evade detection, and establish persistence.
  * Tools used: Docker CLI, Ngrok tunneling, cryptomining payloads.
  * Impact: Persistent foothold, cryptomining, unauthorized access to infrastructure.
* **Graboid Worm**:
  * Spread through exposed Docker daemons, pulling malicious images and propagating across container hosts.
  * Tools used: Docker CLI commands, malicious Docker images hosted on Docker Hub.
  * Impact: Rapid lateral spread, unauthorized cryptomining, resource exhaustion.

These examples illustrate the significant impact and widespread use of Container Administration Command techniques, underscoring the importance of monitoring, detection, and robust security measures in containerized environments.
