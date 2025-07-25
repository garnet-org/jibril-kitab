---
description: Resource Hijacking [T1496]
icon: square-person-confined
---

# Resource Hijacking

## Information

* Name: Resource Hijacking
* ID: T1496
* Tactics: [TA0040](../)
* Sub-Technique: T1496.003, T1496.002, T1496.004, [T1496.001](t1496.001.md)

## Introduction

Resource Hijacking, categorized under MITRE ATT\&CK ID T1496, refers to adversaries leveraging computational resources from compromised systems to execute unauthorized tasks, most commonly cryptocurrency mining. Attackers exploit system resources such as CPU, GPU, memory, or network bandwidth without authorization, resulting in degraded system performance, increased operational costs, and potential hardware damage. Resource Hijacking is typically stealthy, aiming to remain undetected for extended periods.

## Deep Dive Into Technique

Resource Hijacking typically manifests through unauthorized cryptocurrency mining (cryptojacking) or distributed computing tasks. Attackers deploy malware or scripts that run silently in the background, utilizing system resources without explicit user consent.

Technical execution methods and mechanisms include:

* **Cryptojacking malware**:
  * Malicious programs or scripts embedded in websites (JavaScript-based miners like Coinhive, Crypto-Loot).
  * Standalone executables or binaries installed through phishing emails, malicious downloads, or compromised software.
  * Hidden processes or services running persistently in the background.
* **Malicious browser extensions**:
  * Extensions that secretly mine cryptocurrencies using browser resources without user knowledge.
* **Cloud resource hijacking**:
  * Attackers compromise cloud accounts (AWS, Azure, GCP) and deploy unauthorized mining infrastructure.
  * Automated scripts or bots scanning for misconfigured cloud instances or weak credentials.
* **Container and Kubernetes cluster hijacking**:
  * Attackers exploit vulnerabilities or misconfigurations in container orchestration systems (Docker, Kubernetes) to deploy mining workloads.
  * Unauthorized deployment of malicious containers or pods.
* **Leveraging vulnerabilities and exploits**:
  * Exploiting known vulnerabilities in web servers, CMS platforms, or software to inject mining scripts or binaries.
  * Utilizing remote code execution (RCE) vulnerabilities to establish persistence and deploy miners.

Real-world procedures often involve:

* Automated exploitation toolkits scanning the internet for vulnerable systems.
* Use of legitimate services and processes (e.g., PowerShell, cron jobs, scheduled tasks) to maintain persistence.
* Obfuscation and evasion techniques to avoid detection, such as process hollowing, fileless malware, and encrypted payloads.
* Communication with mining pools or command-and-control (C2) servers through encrypted channels to relay mined cryptocurrency.

## When this Technique is Usually Used

Resource Hijacking can appear at various stages and scenarios of cyberattacks, including:

* **Initial Access and Exploitation**:
  * Attackers exploit vulnerabilities or weak credentials to gain initial access and quickly deploy mining payloads.
* **Post-Exploitation and Persistence**:
  * After compromising systems, attackers deploy resource hijacking scripts or malware to monetize compromised infrastructure.
* **Opportunistic Attacks**:
  * Attackers scan the internet continuously for vulnerable systems (e.g., open Docker APIs, misconfigured Kubernetes clusters) to deploy mining workloads automatically.
* **Supply Chain Attacks**:
  * Compromised third-party software or libraries include hidden mining scripts, infecting numerous downstream users.
* **Insider Threat Scenarios**:
  * Malicious insiders deploy mining software on corporate infrastructure or cloud accounts for personal financial gain.

## How this Technique is Usually Detected

Detection methods and indicators of compromise (IoCs) for Resource Hijacking include:

* **Performance and Resource Monitoring**:
  * Unexplained CPU/GPU spikes or consistently high resource usage.
  * Sudden increases in power consumption or cloud billing costs.
  * Performance degradation or instability of affected systems.
* **Process and Network Analysis**:
  * Unfamiliar or suspicious processes running persistently (e.g., xmrig, minerd, cryptonight).
  * Suspicious outbound network connections to mining pools or unknown IP addresses.
  * Detection of mining-related protocols and ports (e.g., Stratum protocol on ports 3333, 4444, 5555).
* **Endpoint Detection and Response (EDR) Tools**:
  * Identifying fileless malware, suspicious PowerShell scripts, or persistence mechanisms related to mining activities.
  * Behavioral analysis detecting anomalous process behaviors indicative of cryptojacking.
* **Log Analysis and SIEM Correlation**:
  * Reviewing logs for unauthorized container deployments, cloud instance creations, or scheduled task modifications.
  * Correlating multiple indicators, such as unusual login patterns and resource usage anomalies.
* **Threat Intelligence Feeds**:
  * Utilizing threat intelligence feeds to identify known mining pools, malicious domains, IP addresses, and file hashes associated with cryptojacking campaigns.

Specific IoCs include:

* Known cryptomining binaries and scripts (e.g., xmrig, cgminer, claymore).
* Suspicious cron jobs or scheduled tasks executing unknown scripts.
* Unusual Docker images or Kubernetes pods running mining workloads.
* Malicious browser extensions or JavaScript files embedded in compromised websites.

## Why it is Important to Detect This Technique

Early detection of Resource Hijacking is critical due to the following impacts on systems and networks:

* **Performance Degradation**:
  * Significant slowing down of systems, negatively impacting user productivity and business operations.
* **Increased Operational Costs**:
  * Unauthorized use of cloud resources leading to substantial and unexpected financial charges.
* **Hardware Damage and Reduced Lifespan**:
  * Continuous intensive resource usage causing overheating and potential physical damage to CPUs, GPUs, and other hardware components.
* **Security Risks and Further Compromise**:
  * Resource hijacking indicates system compromise, which attackers may leverage for lateral movement, data exfiltration, or more severe attacks.
* **Reputational Damage**:
  * Organizations unknowingly hosting cryptojacking scripts or malware could experience reputational harm and loss of trust from customers and partners.
* **Compliance and Legal Risks**:
  * Unauthorized use of resources or hosting malicious activities may lead to regulatory violations, compliance issues, and potential legal consequences.

## Examples

Real-world examples illustrating Resource Hijacking include:

* **Coinhive Cryptojacking Campaign (2017-2019)**:
  * Attackers embedded Coinhive JavaScript miners into thousands of compromised websites.
  * Visitors unknowingly mined Monero cryptocurrency, causing increased CPU usage and battery drain on user devices.
  * Impact: Millions of users affected, significant performance degradation, and widespread media coverage.
* **Tesla Cloud Infrastructure Hijacking (2018)**:
  * Attackers compromised Tesla's Kubernetes console due to misconfiguration.
  * Unauthorized mining pods deployed within Tesla's AWS environment, mining cryptocurrency without detection initially.
  * Impact: Increased cloud costs, potential security risks, and reputational damage.
* **Docker API Exploitation Campaigns (2019-Present)**:
  * Attackers scanned for exposed Docker APIs and deployed malicious containers running cryptominers (e.g., xmrig).
  * Automated scripts continuously exploited vulnerable Docker hosts globally.
  * Impact: Resource exhaustion, increased cloud bills, and compromised container infrastructure.
* **Graboid Worm (2019)**:
  * First-ever cryptojacking worm targeting Docker hosts.
  * Spread across unsecured Docker daemons, deploying malicious containers to mine Monero.
  * Impact: Rapid spread, resource exhaustion, and increased operational costs for affected organizations.
* **Lemon\_Duck Cryptomining Botnet (2019-Present)**:
  * Malware infecting Windows and Linux systems through exploits (e.g., EternalBlue, SMBGhost) and phishing emails.
  * Deploying xmrig miners and establishing persistence through scheduled tasks and cron jobs.
  * Impact: Persistent infections, severe resource degradation, and ongoing security threats to enterprises worldwide.
