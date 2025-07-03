---
description: Endpoint Denial of Service [T1499]
icon: forward-step
---

# Endpoint Denial of Service

## Information

* Name: Endpoint Denial of Service
* ID: T1499
* Tactics: [TA0040](../)
* Sub-Technique: [T1499.001](t1499.001.md), [T1499.003](t1499.003.md), [T1499.004](t1499.004.md), [T1499.002](t1499.002.md)

## Introduction

Endpoint Denial of Service is categorized under the MITRE ATT\&CK framework as technique T1499.001, a sub-technique of Impact (T1499). This technique involves attackers targeting specific endpoints—such as servers, workstations, or critical network devices—to overwhelm or disrupt their normal operation, rendering them temporarily or permanently unavailable. Unlike traditional network-level denial of service (DoS) attacks, endpoint denial of service focuses on resource exhaustion or disruption at the host or application level, affecting the endpoint directly.

## Deep Dive Into Technique

Endpoint Denial of Service (DoS) attacks specifically target endpoint resources to degrade or completely halt their functionality. Attackers typically employ one or more of the following methods:

* **Resource Exhaustion**:
  * CPU exhaustion: Attackers execute intensive processes or malicious scripts designed to consume excessive CPU cycles, rendering the endpoint unresponsive.
  * Memory exhaustion: Malicious code or scripts allocate large amounts of memory intentionally, causing system instability or crashes.
  * Disk exhaustion: Attackers fill up disk storage by writing large amounts of unnecessary or junk data, preventing legitimate operations that require storage space.
* **Application-Level Denial of Service**:
  * Exploiting vulnerabilities in applications (buffer overflow, memory leaks) to crash or degrade performance.
  * Flooding endpoints with malformed or resource-intensive requests to overwhelm applications and services.
* **Service Disruption**:
  * Manipulating endpoint configuration settings or registry keys to disable critical services.
  * Terminating essential system processes or services through scripts or malware execution.

Real-world procedures include launching scripts or malware payloads that repeatedly execute resource-intensive commands, exploiting known vulnerabilities in endpoint software to cause crashes, or leveraging legitimate administrative tools (e.g., PowerShell, Windows Task Manager, Linux bash scripts) to intentionally overload endpoint resources.

## When this Technique is Usually Used

Endpoint Denial of Service attacks can appear at various stages of the cyber kill chain and in multiple attack scenarios, including:

* **Initial Access and Disruption**:
  * Used by attackers to disrupt endpoint availability as part of a broader sabotage campaign.
  * Preemptively executed to distract defenders or conceal simultaneous intrusion activities elsewhere.
* **Persistence and Defense Evasion**:
  * Attackers might deliberately crash security tools or endpoint monitoring agents to evade detection.
  * Disabling endpoint logging mechanisms through resource exhaustion to prevent forensic analysis.
* **Impact Stage**:
  * Employed as part of destructive cyber operations aiming to cause maximum disruption to critical infrastructure or business operations.
  * Ransomware groups may threaten or execute endpoint denial of service attacks to pressure victims into paying ransom demands.
* **Competitive Advantage and Sabotage**:
  * Competitors or malicious insiders may use endpoint denial of service to disrupt business continuity, cause financial loss, or damage reputation.

## How this Technique is Usually Detected

Detection of Endpoint Denial of Service involves monitoring endpoint behavior, resource usage, and application performance. Common detection methods, tools, and indicators of compromise (IoCs) include:

* **Performance Monitoring**:
  * Endpoint monitoring solutions (EDR/XDR) detecting abnormal spikes in CPU, memory, disk usage, or network I/O.
  * System monitoring tools (Sysmon, Task Manager, top/htop, Resource Monitor) reporting unusual resource consumption patterns.
* **Log Analysis and Alerting**:
  * Security Information and Event Management (SIEM) solutions correlating events from endpoint logs, system logs, and security logs to detect suspicious activity.
  * Detection of repeated application crashes, service restarts, or unexpected reboots in system logs.
* **Endpoint Detection and Response (EDR)**:
  * EDR tools identifying malicious processes or suspicious scripts executing resource-intensive actions.
  * Behavioral analysis detecting rapid or repeated execution of resource-consuming commands or binaries.
* **Indicators of Compromise (IoCs)**:
  * Abnormal high-frequency execution of certain binaries or scripts.
  * Sudden appearance of large files or rapid decrease in available disk space.
  * Frequent system or application crashes without clear cause.
  * Unusual registry modifications or configuration changes disabling critical services.

## Why it is Important to Detect This Technique

Early detection of Endpoint Denial of Service is crucial due to its potentially severe impacts on systems, networks, and organizational operations. The importance of timely detection includes:

* **Operational Continuity**:
  * Preventing prolonged downtime and ensuring availability of critical business systems, applications, and services.
  * Avoiding disruption to business operations, customer services, and revenue-generating activities.
* **Security Posture and Incident Response**:
  * Early identification enables rapid containment and remediation, minimizing damage and reducing recovery time.
  * Identifying endpoint denial of service attempts can uncover broader attacks or simultaneous intrusions occurring within the network.
* **Compliance and Regulatory Requirements**:
  * Demonstrating proactive security monitoring and incident detection capabilities to meet regulatory compliance standards.
  * Avoiding potential regulatory fines or penalties due to prolonged service disruptions or security breaches.
* **Financial and Reputational Impact**:
  * Mitigating financial losses resulting from downtime, lost productivity, or remediation expenses.
  * Protecting organizational reputation by preventing public disclosure or negative publicity caused by persistent service disruptions.

## Examples

Real-world examples of Endpoint Denial of Service attacks include:

* **NotPetya Malware Attack (2017)**:
  * Attack Scenario: Malware utilized EternalBlue exploit and credential theft to spread rapidly across networks, encrypting files and disrupting endpoints.
  * Tools Used: EternalBlue exploit, Mimikatz, and custom malware payload.
  * Impact: Massive disruption to global companies including Maersk, Merck, and FedEx, causing billions of dollars in losses due to endpoint and service unavailability.
* **Shamoon Malware Attack (2012, 2016, 2018)**:
  * Attack Scenario: Malware overwrote Master Boot Record (MBR) and critical system files, rendering endpoints inoperable.
  * Tools Used: Shamoon (Disttrack) malware, custom scripts for disk wiping.
  * Impact: Significant disruption to Saudi Aramco and other Middle Eastern organizations, resulting in thousands of endpoints becoming unusable and requiring extensive recovery efforts.
* **Olympic Destroyer Attack (2018)**:
  * Attack Scenario: Malware designed to disrupt endpoints during the 2018 Winter Olympics opening ceremony.
  * Tools Used: Custom malware payload that deleted files, disabled services, and shut down endpoints.
  * Impact: Temporary disruption of IT systems at the Olympic Games, causing confusion and operational delays.
* **Ransomware Attacks (Various)**:
  * Attack Scenario: Ransomware strains such as WannaCry, Ryuk, and REvil encrypt critical endpoint files, effectively causing endpoint denial of service.
  * Tools Used: Encryption payloads, exploits like EternalBlue, phishing emails, and malicious macros.
  * Impact: Extensive downtime, operational disruption, and financial losses across industries, including healthcare, manufacturing, and government agencies.
