---
description: Execution Guardrails [T1480]
icon: play
---

# Execution Guardrails

## Information

* Name: Execution Guardrails
* ID: T1480
* Tactics: [TA0005](../)
* Sub-Technique: [T1480.002](t1480.002.md), [T1480.001](t1480.001.md)

## Introduction

Execution describes techniques used by adversaries to run malicious code on targeted systems. Within the MITRE ATT\&CK framework, execution represents a critical tactic (TA0002) encompassing various methods attackers leverage to execute unauthorized commands or scripts. These methods can range from simple command-line execution to more sophisticated techniques involving scripting languages, remote services, or exploiting legitimate system processes. Understanding execution techniques helps defenders recognize and mitigate unauthorized activity and reduce potential damage.

## Deep Dive Into Technique

Execution techniques can be categorized into several distinct methods and mechanisms, each with unique characteristics:

### Command-Line Interface (CLI) Execution

* Attackers frequently utilize command-line interfaces such as Windows Command Prompt (`cmd.exe`), PowerShell, or Unix shells (`bash`, `sh`) to execute commands directly on compromised systems.
* CLI execution enables attackers to quickly run commands, perform reconnaissance, establish persistence, or escalate privileges.
* Common commands include:
  * Windows: `cmd.exe /c`, `powershell.exe -ExecutionPolicy Bypass`
  * Linux/Unix: `/bin/sh -c`, `/bin/bash -i`

### Scripting and Interpreter-Based Execution

* Attackers often leverage scripting languages like Python, Perl, JavaScript, VBScript, and PowerShell to automate tasks or execute payloads.
* Scripting provides flexibility, stealth, and ease of obfuscation.
* Scripts can be executed directly or embedded within legitimate files or documents.

### Scheduled Tasks and Cron Jobs

* Attackers schedule malicious code to execute automatically using built-in task scheduling utilities such as Windows Task Scheduler or Unix cron jobs.
* Scheduled tasks provide persistence and recurrent execution of malicious payloads.

### Remote Execution and Remote Services

* Attackers often exploit remote execution capabilities such as SSH, RDP, WinRM, or SMB for lateral movement and command execution.
* Remote execution methods enable attackers to control compromised hosts remotely, execute commands, and exfiltrate data.

### Application and Service Exploitation

* Attackers exploit vulnerabilities or misconfigurations in legitimate applications and services to execute arbitrary code.
* Exploited applications commonly include web servers, databases, and custom enterprise software.

### Exploitation of Client Applications

* Malicious actors exploit client-side applications, such as browsers, PDF readers, or office productivity software, to execute malicious payloads.
* Techniques include macro execution, embedded scripts, and exploit kits.

## When this Technique is Usually Used

Execution techniques appear across multiple attack stages and scenarios, including:

* **Initial Access**
  * Execution of payloads delivered via phishing emails, malicious documents, or drive-by downloads.
  * Exploiting client-side vulnerabilities to execute initial malware.
* **Execution and Persistence**
  * Running scripts or binaries to establish persistent access on compromised systems.
  * Scheduling recurring malicious tasks or cron jobs.
* **Privilege Escalation**
  * Exploiting vulnerabilities or misconfigurations in applications and services to elevate privileges.
  * Execution of scripts or binaries with elevated privileges.
* **Defense Evasion**
  * Execution of obfuscated scripts or binaries to evade detection.
  * Leveraging legitimate system tools (living-off-the-land binaries or scripts, LOLBAS) for stealthy execution.
* **Lateral Movement**
  * Remote execution of commands on other hosts within the targeted network via RDP, SSH, or SMB.
* **Exfiltration and Impact**
  * Execution of commands or scripts to collect, compress, encrypt, and exfiltrate sensitive data.
  * Running destructive commands or scripts to disrupt operations or destroy data.

## How this Technique is Usually Detected

Detection methods for execution techniques typically involve:

* **Endpoint Detection and Response (EDR) Tools**
  * Monitoring and logging command-line activities, script execution, and processes spawned.
  * Detecting suspicious parent-child process relationships (e.g., Word spawning PowerShell).
* **Security Information and Event Management (SIEM)**
  * Centralized log analysis to detect anomalies in execution patterns, frequency, and timing.
  * Correlating events across multiple sources to identify suspicious execution behavior.
* **Behavioral Analysis and Machine Learning**
  * Detecting deviations from baseline execution behavior patterns.
  * Identifying anomalous command-line arguments, scripting activity, or scheduled task creation.
* **Application Whitelisting and Blacklisting**
  * Restricting execution of unauthorized scripts, binaries, or applications.
  * Alerting on attempts to execute blacklisted scripts or binaries.
* **Network Traffic Analysis**
  * Identifying unusual remote execution activity via protocols like SMB, SSH, WinRM, or RDP.
  * Detecting command-and-control (C2) traffic associated with executed payloads.

**Indicators of Compromise (IoCs)** include:

* Suspicious command-line arguments (e.g., encoded PowerShell commands).
* Unusual parent-child process relationships (e.g., Office applications spawning scripting engines).
* Creation or modification of scheduled tasks or cron jobs.
* Execution of binaries or scripts from uncommon locations (e.g., temporary folders).
* Unexpected network connections from processes or scripts.

## Why it is Important to Detect This Technique

Detecting execution techniques early is critical due to their potential severe impacts:

* **Early Detection and Mitigation**
  * Prevents attackers from establishing persistence, escalating privileges, and performing lateral movement.
  * Enables faster containment and eradication of threats.
* **Reduced Risk of Data Breaches**
  * Prevents unauthorized execution of commands used for data exfiltration.
  * Protects sensitive information and intellectual property from theft or leakage.
* **Minimized Operational Disruption**
  * Detecting and blocking malicious execution prevents destructive attacks (e.g., ransomware, disk wiping).
  * Maintains system availability and business continuity.
* **Compliance and Regulatory Requirements**
  * Early detection and response to execution-based threats help organizations meet regulatory and compliance standards.
  * Reduces risk of fines, legal actions, or reputational damage.
* **Improved Security Posture**
  * Understanding and detecting execution techniques enhances overall security capabilities.
  * Provides valuable threat intelligence and insights for proactive defense strategies.

## Examples

Real-world examples illustrating execution techniques include:

* **APT29 (Cozy Bear)**
  * Utilized PowerShell scripts executed via phishing emails and malicious documents.
  * Leveraged legitimate Windows binaries (LOLBAS) for stealthy execution.
  * Impact: Data exfiltration, espionage, and persistent access.
* **Emotet Malware**
  * Executed malicious scripts embedded within Microsoft Office macros.
  * Leveraged scheduled tasks for persistence and recurrent execution.
  * Impact: Credential theft, lateral movement, and deployment of additional malware (e.g., TrickBot, Ryuk ransomware).
* **NotPetya Ransomware Attack**
  * Executed malicious binaries leveraging compromised update servers and SMB protocol.
  * Used scheduled tasks and remote execution to propagate across networks.
  * Impact: Massive operational disruption, data loss, and significant financial damages.
* **WannaCry Ransomware**
  * Leveraged SMB vulnerabilities (EternalBlue exploit) to execute malicious payloads remotely.
  * Executed ransomware binaries to encrypt data and demand ransom payments.
  * Impact: Global disruption, financial loss, and widespread operational downtime.
* **FIN7 Group**
  * Exploited client-side vulnerabilities in browsers, PDF readers, and Office applications.
  * Executed malicious scripts and binaries to establish persistence and exfiltrate payment card data.
  * Impact: Large-scale financial fraud, data breaches, and significant financial losses.

These examples highlight the diverse methods attackers use to execute malicious code, underscoring the importance of robust detection and mitigation strategies.
