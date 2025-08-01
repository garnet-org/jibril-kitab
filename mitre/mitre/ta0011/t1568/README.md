---
description: Dynamic Resolution [T1568]
icon: lock
---

# Dynamic Resolution

## Information

* Name: Dynamic Resolution
* ID: T1568
* Tactics: [TA0011](../)
* Sub-Technique: [T1568.002](t1568.002.md), [T1568.001](t1568.001.md), [T1568.003](t1568.003.md)

## Introduction

Dynamic Resolution is a technique categorized under the MITRE ATT\&CK framework (Technique ID: T1568). It involves malware or adversaries dynamically resolving domain names or IP addresses at runtime to evade static analysis and detection mechanisms. By performing domain resolution dynamically, attackers can maintain flexibility, avoid blacklists, and ensure their infrastructure remains resilient against defensive measures.

## Deep Dive Into Technique

Dynamic Resolution refers to the process of resolving network addresses or domains during the execution of malicious code rather than using static, hard-coded values. This technique allows attackers to:

* Dynamically update command-and-control (C2) servers, making it harder for defenders to block or track malicious infrastructure.
* Leverage various runtime methods such as DNS APIs, direct socket connections, or third-party libraries to perform name resolution at execution.
* Use algorithms like Domain Generation Algorithms (DGAs) to generate multiple domain names, ensuring at least some remain active and unblocked.
* Employ legitimate services (such as cloud DNS providers or CDN services) to mask malicious traffic and blend in with normal network activity.

Common execution methods and mechanisms include:

* **API Calls:** Malware leveraging system APIs such as `gethostbyname()`, `DnsQuery()`, or `getaddrinfo()` to dynamically resolve domain names.
* **Scripting Languages:** Utilizing scripting languages (e.g., PowerShell, Python) to perform runtime DNS lookups or connect to dynamically resolved IP addresses.
* **Domain Generation Algorithms (DGAs):** Automatically generating and resolving multiple domain names to establish resilient C2 communications.
* **Encrypted or Obfuscated Resolution:** Employing encryption or obfuscation techniques to hide domain names or IP addresses in memory, making static analysis difficult.

Real-world procedures often involve malware families or threat actors that regularly rotate infrastructure, use fast-flux DNS techniques, or dynamically select C2 servers based on victim location, IP reputation, or availability.

## When this Technique is Usually Used

Attackers commonly employ Dynamic Resolution at various stages of an attack lifecycle, including:

* **Initial Access and Command-and-Control Establishment:** Malware dynamically resolves C2 servers upon initial infection to avoid hard-coded IP addresses.
* **Persistence and Defense Evasion:** Attackers regularly update their infrastructure dynamically to evade detection, blacklists, and network filters.
* **Exfiltration Stage:** Dynamically resolved domains or IP addresses are used to send stolen data to attacker-controlled servers, complicating detection and attribution.

Scenarios where Dynamic Resolution frequently appears include:

* Advanced Persistent Threat (APT) campaigns that require stealthy and resilient infrastructure.
* Botnets and ransomware operations that frequently rotate or generate domain names to maintain operational continuity.
* Malware campaigns that rely on fast-flux DNS techniques to rapidly switch IP addresses associated with malicious domains.

## How this Technique is Usually Detected

Detection methods and tools for identifying Dynamic Resolution include:

* **Network Traffic Analysis:**
  * Monitoring DNS query patterns for unusual or randomized domain names indicative of DGAs.
  * Identifying sudden spikes in DNS resolution requests or frequent changes in resolved IP addresses.
* **Endpoint Detection and Response (EDR):**
  * Observing suspicious API calls (`gethostbyname()`, `DnsQuery()`) from unusual processes or at unexpected times.
  * Analyzing scripting engine logs (PowerShell, Python) for scripts performing suspicious DNS lookups or network connections.
* **SIEM and Log Analysis:**
  * Correlating DNS logs with threat intelligence feeds to identify known malicious or suspicious domains.
  * Detecting frequent DNS resolution failures or unusual DNS server usage patterns.
* **Threat Intelligence Integration:**
  * Leveraging threat intelligence platforms to identify known malicious domains or IP addresses associated with dynamic resolution techniques.
  * Regularly updating IoC lists to detect newly generated malicious domains.

Indicators of Compromise (IoCs) associated with Dynamic Resolution include:

* Unusual DNS query patterns (e.g., high-frequency lookups, randomized subdomains).
* DNS requests to known malicious or suspicious domains (identified via threat intelligence).
* Suspicious processes performing DNS lookups or connections without legitimate business purpose.
* Rapid DNS resolution changes or frequent IP address rotations for specific domains.

## Why it is Important to Detect This Technique

Detecting Dynamic Resolution is critical due to its potential impacts on systems and networks, which include:

* **Persistent Access and Command-and-Control:** Attackers can maintain resilient, persistent communication channels with infected hosts, complicating remediation efforts.
* **Data Exfiltration and Loss:** Dynamic resolution enables attackers to discreetly exfiltrate sensitive data to constantly changing domains or servers, making detection more challenging.
* **Defense Evasion and Detection Difficulty:** By dynamically resolving domains or IP addresses, attackers effectively evade static detection mechanisms, firewall rules, and threat intelligence feeds.
* **Operational and Financial Impacts:** Failure to detect this technique can lead to prolonged infection, increased remediation costs, reputational damage, and regulatory penalties.

Early detection and response are essential to:

* Quickly identify and block malicious domains or IP addresses.
* Mitigate damage by limiting attackers' ability to communicate with compromised systems.
* Reduce the window of opportunity for attackers to exfiltrate sensitive data or escalate privileges.
* Minimize operational disruption and costs associated with incident response and recovery.

## Examples

Real-world examples of Dynamic Resolution include:

* **Emotet Malware:**
  * Uses Domain Generation Algorithms (DGAs) to dynamically generate and resolve domain names.
  * Regularly rotates C2 infrastructure to evade detection and maintain persistence.
  * Impact: Significant infection rates, credential theft, and subsequent deployment of ransomware (e.g., Ryuk).
* **TrickBot Trojan:**
  * Performs dynamic DNS resolution to connect to various C2 servers.
  * Employs fast-flux DNS techniques to frequently change IP addresses associated with malicious domains.
  * Impact: Credential theft, lateral movement, and deployment of ransomware such as Conti and Ryuk.
* **APT29 (Cozy Bear):**
  * Uses dynamic DNS resolution techniques to communicate with C2 infrastructure.
  * Employs scripting languages (PowerShell) to dynamically resolve and connect to attacker-controlled domains.
  * Impact: Espionage campaigns targeting government and private sector entities, significant data breaches, and long-term persistence.
* **QakBot (Qbot):**
  * Incorporates dynamic DNS resolution to establish resilient C2 communications.
  * Frequently updates infrastructure and domains to evade network-based detection.
  * Impact: Credential harvesting, lateral movement, and subsequent ransomware deployment.

In these examples, attackers use Dynamic Resolution to enhance their operational security, maintain persistence, evade detection, and increase the effectiveness and longevity of their campaigns.
