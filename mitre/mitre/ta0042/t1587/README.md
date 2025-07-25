---
description: Develop Capabilities [T1587]
icon: lock
---

# Develop Capabilities

## Information

* Name: Develop Capabilities
* ID: T1587
* Tactics: [TA0042](../)
* Sub-Technique: [T1587.003](t1587.003.md), [T1587.001](t1587.001.md), [T1587.002](t1587.002.md), [T1587.004](t1587.004.md)

## Introduction

Develop Capabilities (Technique ID: T1587) is a tactic categorized under the "Resource Development" phase of the MITRE ATT\&CK framework. This technique refers to adversaries' activities aimed at creating, purchasing, or acquiring resources and capabilities necessary to support their cyber operations. This can include developing malware, exploits, command-and-control (C2) infrastructure, phishing kits, and other tools or techniques required to execute attacks. Understanding this technique is crucial for defenders, as it provides insight into adversary preparation and planning stages prior to actual attack execution.

## Deep Dive Into Technique

The "Develop Capabilities" technique encompasses multiple sub-techniques and activities that adversaries perform to enable their cyber operations:

* **Malware Development:**
  * Creating custom malware tailored to specific targets or scenarios.
  * Modifying existing malware strains to evade detection or adapt to new environments.
  * Developing malware loaders, droppers, or payloads to achieve persistence, lateral movement, or data exfiltration.
* **Exploit Development:**
  * Researching software or hardware vulnerabilities to develop zero-day or known exploits.
  * Utilizing fuzzing, reverse engineering, or static/dynamic analysis to identify exploitable vulnerabilities.
  * Developing customized exploitation frameworks or modules for existing frameworks such as Metasploit, Cobalt Strike, or Empire.
* **Command-and-Control (C2) Infrastructure Development:**
  * Establishing robust C2 infrastructure using servers, domains, proxies, and cloud services.
  * Developing or customizing C2 protocols (HTTP/S, DNS, ICMP) to evade detection.
  * Implementing encryption and obfuscation techniques to secure communications between compromised systems and attacker-controlled servers.
* **Phishing Kit Creation:**
  * Developing phishing kits to facilitate credential harvesting or malware delivery.
  * Customizing email templates, landing pages, and payloads to increase phishing effectiveness.
  * Hosting phishing infrastructure on compromised or attacker-controlled servers.
* **Tool Development and Acquisition:**
  * Writing custom scripts, utilities, and tools for reconnaissance, lateral movement, privilege escalation, and data exfiltration.
  * Acquiring open-source or underground tools from cybercriminal marketplaces or forums.
  * Modifying legitimate security and administrative tools (e.g., PsExec, PowerShell scripts) for malicious purposes.

## When this Technique is Usually Used

The Develop Capabilities technique typically appears during early stages of an attack lifecycle, particularly in the "Resource Development" phase. Adversaries utilize this technique to prepare and build capabilities prior to launching attacks. Common scenarios include:

* **Preparation for Advanced Persistent Threat (APT) Campaigns:**
  * Custom malware or exploits developed specifically for targeted, persistent attacks against high-value organizations.
* **Cyber Espionage Operations:**
  * Development of stealthy malware, implants, and C2 infrastructure to conduct reconnaissance and data exfiltration without detection.
* **Financially Motivated Cybercriminal Activities:**
  * Creation of ransomware, banking trojans, or credential-stealing malware to monetize attacks.
* **Hacktivist Campaigns:**
  * Developing defacement scripts, denial-of-service (DoS) tools, or phishing kits to disrupt targets or spread propaganda.
* **Supply Chain Attacks:**
  * Developing implants or backdoors to compromise third-party software or hardware components.

## How this Technique is Usually Detected

Detection of the Develop Capabilities technique involves monitoring various indicators and leveraging multiple detection methodologies:

* **Threat Intelligence Monitoring:**
  * Tracking underground forums, marketplaces, and dark web resources for new malware, exploits, or tool sales.
  * Monitoring open-source repositories (GitHub, GitLab) for suspicious tool or exploit development activities.
* **Network Detection and Monitoring:**
  * Identifying unusual traffic patterns associated with testing or deploying malware and exploits.
  * Detecting domain registrations and DNS activities indicative of malicious infrastructure setup.
* **Endpoint Detection and Response (EDR):**
  * Identifying suspicious binaries, scripts, or execution patterns on endpoints indicative of malware or exploit testing.
  * Monitoring for the presence of exploit frameworks (e.g., Metasploit, Cobalt Strike) or suspicious toolkits.
* **Sandbox and Malware Analysis:**
  * Analyzing suspicious files or payloads in sandbox environments to detect malicious behavior and intent.
  * Utilizing static and dynamic analysis tools to identify indicators of malware or exploit development.
* **Indicators of Compromise (IoCs):**
  * Suspicious domain registrations (recently registered domains, typosquatting, DNS tunneling).
  * Newly observed malware hashes or signatures.
  * Unusual SSL/TLS certificates or encryption methods associated with C2 infrastructure.
  * Known malicious IP addresses and hosting providers frequently used by threat actors.

## Why it is Important to Detect This Technique

Timely detection of adversaries developing capabilities is crucial for several reasons:

* **Early Warning and Prevention:**
  * Detecting adversary preparation activities can provide defenders with early warning, enabling proactive defense measures before attacks are launched.
* **Reduced Impact and Damage:**
  * Identifying and mitigating threats during the capability development stage can significantly reduce the potential impact, minimizing data loss, downtime, and financial damage.
* **Improved Incident Response:**
  * Early detection allows security teams to better understand adversary goals, methods, and infrastructure, improving the efficiency and effectiveness of incident response activities.
* **Enhanced Security Posture:**
  * Continuous monitoring and detection of capability development activities can guide organizations in strengthening defenses, updating security policies, and implementing targeted security controls.
* **Threat Intelligence Enrichment:**
  * Detecting adversary capability development contributes valuable intelligence, helping organizations predict and defend against future threats and campaigns.

## Examples

Real-world examples demonstrating the Develop Capabilities technique include:

* **APT29 (Cozy Bear) and SolarWinds Supply Chain Attack:**
  * Attack Scenario: Developed custom implants (SUNBURST and SUNSPOT) embedded into SolarWinds Orion software updates.
  * Tools Used: Custom malware implants, sophisticated C2 infrastructure, stealthy malware deployment mechanisms.
  * Impact: Compromised numerous high-profile organizations and government agencies worldwide, leading to significant data breaches and espionage activities.
* **Lazarus Group and WannaCry Ransomware:**
  * Attack Scenario: Developed and deployed WannaCry ransomware exploiting EternalBlue vulnerability.
  * Tools Used: Custom ransomware payload, SMB exploit (EternalBlue), robust propagation mechanisms.
  * Impact: Massive global impact affecting thousands of organizations, resulting in significant operational disruptions and financial losses.
* **FIN7 Cybercriminal Group and Carbanak Malware:**
  * Attack Scenario: Developed advanced banking malware (Carbanak) targeting financial institutions for theft of sensitive financial data.
  * Tools Used: Custom malware implants, tailored phishing kits, sophisticated C2 infrastructure.
  * Impact: Theft of millions of dollars from banks and financial institutions worldwide, causing severe financial and reputational damage.
* **APT41 and Supply Chain Attacks:**
  * Attack Scenario: Developed custom backdoors and implants embedded into legitimate software updates (e.g., ASUS Live Update Utility).
  * Tools Used: Custom malware implants, malicious software updates, stealthy C2 infrastructure.
  * Impact: Compromised numerous end-users globally, enabling espionage activities, credential theft, and lateral movement within victim networks.
* **Magecart Group and Web Skimming Attacks:**
  * Attack Scenario: Developed web skimming scripts injected into compromised e-commerce websites to steal payment card information.
  * Tools Used: Custom JavaScript skimmers, compromised web servers, phishing infrastructure.
  * Impact: Theft of millions of payment card records from major online retailers, resulting in financial losses, regulatory fines, and loss of customer trust.
