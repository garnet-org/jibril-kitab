---
description: Obtain Capabilities [T1588]
icon: lock
---

# Obtain Capabilities

## Information

* Name: Obtain Capabilities
* ID: T1588
* Tactics: [TA0042](../)
* Sub-Technique: [T1588.007](t1588.007.md), [T1588.004](t1588.004.md), [T1588.006](t1588.006.md), [T1588.001](t1588.001.md), [T1588.002](t1588.002.md), [T1588.003](t1588.003.md), [T1588.005](t1588.005.md)

## Introduction

"Obtain Capabilities" is a technique categorized under the "Resource Development" tactic within the MITRE ATT\&CK framework. This technique involves adversaries acquiring various tools, exploits, malware, or other capabilities necessary to execute cyber-attacks effectively. The acquisition of these capabilities can occur through multiple methods, including purchasing from underground forums, developing custom malware, or leveraging publicly available resources. Understanding this technique is crucial, as it represents a foundational step adversaries take before actively conducting cyber operations.

## Deep Dive Into Technique

Adversaries employ multiple methods and channels to obtain capabilities required for their operations. These capabilities primarily include:

* Malware:
  * Trojans
  * Ransomware
  * Remote Access Tools (RATs)
  * Keyloggers
  * Rootkits
* Exploits:
  * Zero-day vulnerabilities
  * Known vulnerabilities (e.g., CVEs)
  * Exploit kits
* Tools and Utilities:
  * Credential dumping utilities (e.g., Mimikatz)
  * Network scanning tools (e.g., Nmap, Masscan)
  * Penetration testing frameworks (e.g., Metasploit, Cobalt Strike)
* Infrastructure:
  * Botnets
  * Command and Control (C2) servers
  * Proxies and VPNs for anonymity
* Credentials and Access:
  * Stolen credentials
  * Compromised accounts
  * Initial access brokers

Common methods adversaries use to obtain capabilities include:

* Purchasing from underground marketplaces and forums on the dark web.
* Developing custom malware or exploits in-house.
* Modifying and repurposing publicly available tools and open-source frameworks.
* Leveraging leaked or stolen tools from legitimate cybersecurity entities or government agencies.
* Collaborating with other threat actors through partnerships or affiliate programs.

## When this Technique is Usually Used

"Obtain Capabilities" typically occurs during the initial preparation and resource development stages of a cyber-attack lifecycle. It precedes active exploitation, reconnaissance, and lateral movement phases. Attack scenarios and stages where this technique is prominently observed include:

* Initial Preparation:
  * Adversaries planning targeted attacks acquire specialized malware or exploits tailored to specific victim environments.
* Opportunistic Attacks:
  * Threat actors purchase or download widely available exploit kits or malware to target large numbers of victims indiscriminately.
* Advanced Persistent Threat (APT) Campaigns:
  * Sophisticated threat actors develop or procure custom tools and zero-day exploits to evade detection and increase persistence.
* Ransomware Operations:
  * Ransomware groups purchase initial access from brokers, malware loaders, or exploit kits to deploy ransomware payloads.
* Credential Harvesting Attacks:
  * Attackers obtain credential-stealing malware or phishing kits to facilitate unauthorized access.

## How this Technique is Usually Detected

Detection of "Obtain Capabilities" is challenging, as it often occurs outside the organization's direct visibility. However, certain methods, indicators, and tools can aid detection:

* Threat Intelligence:
  * Monitoring dark web forums, marketplaces, and underground communities for mentions of tools, exploits, or planned attacks.
  * Tracking known threat actor groups and their capabilities through threat intelligence feeds and reports.
* Network Monitoring:
  * Identifying suspicious downloads or transfers of hacking tools and malware from external sources.
  * Detecting unusual outbound connections to known malicious infrastructure or repositories hosting malicious tools.
* Endpoint Detection and Response (EDR):
  * Recognizing the presence of known malicious tools or malware signatures on endpoints.
  * Behavioral analysis to detect suspicious or unauthorized software installations.
* Indicators of Compromise (IoCs):
  * Hashes of known malicious tools or malware samples.
  * IP addresses or domain names associated with known malicious infrastructure.
  * Email addresses or usernames linked to underground forums or marketplaces.

Specific tools and platforms for detection include:

* Threat Intelligence Platforms (TIPs): Recorded Future, ThreatConnect, Anomali
* Security Information and Event Management (SIEM): Splunk, IBM QRadar, Elastic Stack
* Endpoint Detection and Response (EDR): CrowdStrike Falcon, SentinelOne, Microsoft Defender for Endpoint
* Network Detection and Response (NDR): Darktrace, ExtraHop, Cisco Secure Network Analytics

## Why it is Important to Detect This Technique

Early detection of adversaries obtaining capabilities is critical due to the following reasons:

* Prevention of Attacks:
  * Early identification enables proactive security measures, reducing the likelihood of successful attacks.
* Minimizing Impact:
  * Detecting capability acquisition allows organizations to strengthen defenses and mitigate potential damage from future attacks.
* Timely Threat Intelligence:
  * Understanding adversaries' capabilities provides insights into their targets, tactics, techniques, and procedures (TTPs), enabling better threat anticipation.
* Resource Allocation:
  * Early detection helps organizations prioritize security resources effectively, focusing on high-risk threats and vulnerabilities.
* Compliance and Regulatory Requirements:
  * Identifying early stages of attacks helps organizations meet compliance and regulatory standards, protecting sensitive data and infrastructure.

Potential impacts if this technique remains undetected include:

* Data breaches leading to loss of sensitive information.
* Financial losses due to ransomware attacks or fraudulent activities.
* Operational disruptions and downtime.
* Damage to organizational reputation and customer trust.
* Legal and regulatory consequences resulting from security incidents.

## Examples

Several real-world examples illustrate how adversaries obtain capabilities:

* **WannaCry Ransomware (2017)**:
  * Attack Scenario: Leveraged the NSA-developed "EternalBlue" exploit, leaked by the Shadow Brokers group.
  * Tools Used: EternalBlue exploit, WannaCry ransomware.
  * Impact: Over 230,000 computers infected globally, significant operational disruptions, and financial damages.
* **NotPetya Attack (2017)**:
  * Attack Scenario: Attackers utilized leaked NSA exploits, specifically EternalBlue and EternalRomance, to propagate malware rapidly.
  * Tools Used: EternalBlue exploit, EternalRomance exploit, NotPetya destructive malware.
  * Impact: Global operational disruptions, estimated financial losses of over $10 billion.
* **SolarWinds Supply Chain Attack (2020)**:
  * Attack Scenario: Threat actors (APT29/Cozy Bear) developed custom malware (SUNBURST) to compromise SolarWinds Orion software updates.
  * Tools Used: Custom-developed SUNBURST malware, Cobalt Strike, Teardrop malware.
  * Impact: Compromised multiple U.S. government agencies and private sector organizations, significant national security implications.
* **REvil Ransomware Group Operations**:
  * Attack Scenario: Purchased initial access credentials from underground marketplaces, deployed ransomware via affiliates.
  * Tools Used: Ransomware payloads, credential harvesting malware, exploit kits.
  * Impact: High-profile attacks on organizations like JBS Foods, Kaseya, resulting in operational downtime and multi-million-dollar ransom payments.
* **DarkSide Ransomware Attack on Colonial Pipeline (2021)**:
  * Attack Scenario: Acquired ransomware capabilities and employed affiliates to gain initial access and deploy ransomware.
  * Tools Used: DarkSide ransomware, credential harvesting tools.
  * Impact: Temporary shutdown of major U.S. fuel pipeline, fuel shortages, significant economic and operational impact.

These examples highlight diverse methods adversaries employ to obtain capabilities, emphasizing the critical importance of detecting and mitigating this technique proactively.
