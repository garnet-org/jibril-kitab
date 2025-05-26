---
description: Defense Evasion [TA0005]
icon: shield
---

# Defense Evasion [TA0005]

## Information

- ID: TA0005

## Introduction

Defense Evasion is a tactic within the MITRE ATT&CK framework that encompasses techniques adversaries employ to avoid detection by security controls, evade analysis, or bypass defensive measures. Attackers utilize these methods to maintain persistence, execute further malicious actions, and reduce the likelihood of being discovered by defenders. Defense evasion techniques can range from simple obfuscation to sophisticated rootkits, concealment of artifacts, and disabling or tampering with security tools.

## Deep Dive Into Technique

Defense evasion techniques involve various technical methods attackers use to evade detection and analysis:

- **Obfuscation and Encoding:**

  - Attackers may encode payloads using Base64, XOR, or other encoding schemes.
  - Obfuscation tools such as Obfuscar, ProGuard, or custom scripts may be used to alter malware signatures.

- **Masquerading:**

  - Malicious files or processes disguised as legitimate system files or processes.
  - Renaming malware to match legitimate binaries (e.g., svchost.exe, explorer.exe).

- **Process Injection:**

  - Injecting malicious code into legitimate processes to evade detection.
  - Techniques include DLL injection, reflective DLL injection, and process hollowing.

- **Rootkits and Bootkits:**

  - Kernel-level or firmware-level malware that hides malicious processes, files, and network connections.
  - Bootkits persist through system reboots by infecting boot sectors or firmware.

- **Disabling Security Tools:**

  - Disabling antivirus, firewall, logging, and monitoring tools to prevent detection.
  - Modifying registry keys, policies, or services to disable or weaken security controls.

- **File Deletion and Artifact Removal:**

  - Removing logs, temporary files, or malware samples to eliminate forensic evidence.
  - Utilizing secure deletion tools or scripts to overwrite and permanently delete artifacts.

- **Signed Binary Proxy Execution:**

  - Leveraging legitimate signed binaries (e.g., rundll32.exe, mshta.exe, regsvr32.exe) to execute malicious code, bypassing application whitelisting and security controls.

- **Virtualization/Sandbox Evasion:**
  - Detecting virtualized environments or sandboxes and altering behavior to avoid analysis.
  - Techniques include checking hardware IDs, registry keys, or system artifacts indicative of virtualization.

## When this Technique is Usually Used

Defense evasion techniques are commonly employed throughout various stages of the attack lifecycle:

- **Initial Access:**

  - Obfuscating malicious payloads or phishing attachments to bypass email filters and antivirus scanning.

- **Execution and Persistence:**

  - Injecting malicious code into legitimate processes to maintain persistence and avoid detection.
  - Masquerading malware as legitimate system binaries to evade endpoint detection and response (EDR) tools.

- **Privilege Escalation:**

  - Utilizing rootkits or kernel-level exploits to escalate privileges while remaining undetected.

- **Lateral Movement:**

  - Leveraging signed binaries or legitimate system tools to move laterally without triggering alerts.

- **Exfiltration and Command and Control (C2):**

  - Encoding or encrypting communications to evade network detection tools and intrusion detection systems (IDS).
  - Removing logs and artifacts post-exfiltration to obfuscate traces of attacker activities.

- **Cleanup and Exit:**
  - Deleting or modifying logs, files, and artifacts to remove evidence and hinder forensic analysis.

## How this Technique is Usually Detected

Detection methods for defense evasion techniques typically involve multiple layers of monitoring, analysis, and alerting:

- **Endpoint Detection and Response (EDR) Solutions:**

  - Monitoring process creation, injection attempts, and suspicious process behaviors.
  - Detecting attempts to disable security tools or modify system configurations.

- **Behavioral Analysis and Heuristics:**

  - Identifying abnormal behaviors such as unusual process injection, file deletion, or masquerading.
  - Behavioral rules and machine learning models that detect deviations from baseline system activities.

- **File Integrity Monitoring (FIM):**

  - Monitoring critical system files, registry keys, and configuration settings for unauthorized changes.
  - Detecting tampering or deletion of security-related artifacts.

- **Network Traffic Analysis (NTA):**

  - Analyzing encrypted or encoded communications indicative of command and control channels.
  - Identifying unusual traffic patterns or anomalous data transfers.

- **Sandbox and Malware Analysis Platforms:**

  - Executing suspicious files or URLs within sandbox environments to detect evasion attempts.
  - Identifying virtual machine detection techniques or sandbox-aware malware behaviors.

- **Log Analysis and SIEM Tools:**

  - Correlating logs from endpoints, servers, and network devices to identify evasion patterns.
  - Detecting log deletion attempts, security tool disablement, and suspicious administrative activities.

- **Indicators of Compromise (IoCs):**
  - Suspicious registry keys (e.g., disabling antivirus via registry entries).
  - Unexpected system file modifications or unusual binaries in system directories.
  - Evidence of encoded or obfuscated scripts (e.g., PowerShell encoded commands).
  - Unusual scheduled tasks or services created for persistence.

## Why it is Important to Detect This Technique

Detecting defense evasion techniques early is critical due to the following impacts:

- **Persistence and Long-Term Compromise:**

  - Undetected evasion allows attackers prolonged access to systems, increasing potential damage.

- **Data Exfiltration and Intellectual Property Theft:**

  - Attackers can stealthily extract sensitive data, intellectual property, or personal information without detection.

- **Damage to Operational Integrity:**

  - Undetected malware can degrade system performance, disrupt services, or lead to critical system failures.

- **Increased Remediation Costs:**

  - Late detection results in higher costs for incident response, forensic analysis, and system recovery.

- **Regulatory and Compliance Risks:**

  - Failure to detect and respond to intrusions promptly can result in regulatory penalties, legal liabilities, and reputational damage.

- **Security Control Erosion:**

  - Attackers disabling or bypassing security tools can weaken overall security posture, leaving organizations vulnerable to further attacks.

- **Compromise of Sensitive Credentials:**
  - Defense evasion often facilitates credential theft, enabling lateral movement and privilege escalation across networks.

## Examples

Real-world examples demonstrating defense evasion techniques include:

- **APT29 (Cozy Bear):**

  - Utilized encoded PowerShell scripts and reflective DLL injection to evade detection.
  - Leveraged legitimate system binaries like rundll32.exe for proxy execution to bypass security controls.
  - Impact: Long-term espionage campaigns targeting government, defense, and financial sectors.

- **FIN7 Cybercriminal Group:**

  - Employed process hollowing and DLL injection techniques to evade endpoint detection.
  - Used obfuscated JavaScript and PowerShell scripts embedded in phishing emails.
  - Impact: Massive financial losses due to payment card data theft and fraudulent transactions.

- **TrickBot Malware:**

  - Implemented rootkit modules to hide malicious processes and network connections.
  - Disabled antivirus and security tools through registry modifications and service disruptions.
  - Impact: Credential theft, ransomware distribution (Ryuk), and significant financial and operational disruptions.

- **NotPetya Ransomware:**

  - Masqueraded as legitimate software updates and used signed binaries for malicious code execution.
  - Deleted logs and artifacts to hinder forensic analysis and incident response.
  - Impact: Global disruption of critical infrastructure, financial institutions, and multinational corporations, resulting in billions of dollars in damages.

- **Stuxnet Worm:**
  - Rootkit techniques to hide malicious files and processes from detection.
  - Exploited legitimate signed drivers and certificates to evade security measures.
  - Impact: Physical damage to nuclear centrifuges, demonstrating potential for cyber-physical attacks and infrastructure disruption.
