---
description: Web Service [T1102]
icon: server
---

# Web Service

## Information

* Name: Web Service
* ID: T1102
* Tactics: [TA0011](../)
* Sub-Technique: [T1102.003](t1102.003.md), [T1102.002](t1102.002.md), [T1102.001](t1102.001.md)

## Introduction

Web Service is a technique described in the MITRE ATT\&CK framework under the tactic of Command and Control (C2). Adversaries may leverage legitimate web services to facilitate communication between compromised systems and attacker-controlled infrastructure. By blending malicious traffic within normal web traffic, attackers can evade detection, bypass firewall rules, and maintain persistent access to compromised hosts. Web services commonly exploited include cloud storage platforms, online collaboration tools, social media services, and other legitimate web-based platforms.

## Deep Dive Into Technique

Attackers leveraging Web Service techniques typically rely on established, legitimate online platforms to establish reliable command-and-control channels. This method allows attackers to hide malicious traffic within standard HTTPS or HTTP requests, making detection more difficult. Technical details include:

* **Communication Protocols:** Attackers often use HTTP or HTTPS protocols, leveraging TLS encryption to mask malicious traffic.
* **Data Encoding:** Attackers may encode data using Base64, JSON, XML, or other formats to blend in with legitimate web requests.
* **Command and Control Infrastructure:** Attackers frequently utilize popular cloud platforms such as AWS, Azure, Google Cloud, Dropbox, GitHub, Slack, Pastebin, Twitter, or Google Drive to host payloads or facilitate communication.
* **Polling and Beaconing:** Compromised systems regularly poll attacker-controlled web services for new commands or payloads, making detection more challenging due to periodic, low-volume traffic.
* **Proxy Usage:** Attackers may leverage web proxies or Content Delivery Networks (CDNs) to obscure the true origin of command-and-control traffic.

## When this Technique is Usually Used

Attackers commonly employ Web Service techniques across multiple stages of an attack lifecycle, including:

* **Initial Access and Persistence:**
  * Delivering initial payloads or malicious scripts hosted on legitimate cloud storage platforms.
* **Command and Control (C2):**
  * Establishing persistent communication channels between compromised hosts and attacker-controlled infrastructure.
* **Exfiltration:**
  * Uploading stolen data to cloud storage or other web services for later retrieval.
* **Defense Evasion:**
  * Blending malicious traffic with legitimate web traffic to evade detection by security tools and monitoring solutions.
* **Reconnaissance and Lateral Movement:**
  * Using web services to distribute commands or scripts to compromised systems within the network.

## How this Technique is Usually Detected

Detection of Web Service-based attacks can be challenging but possible using multiple layered detection methods and tools, such as:

* **Network Traffic Analysis:**
  * Monitoring for unusual traffic patterns or periodic beaconing behavior to external web services.
  * Identifying abnormal volumes of traffic or anomalous HTTP methods (POST, PUT, DELETE) to uncommon destinations.
* **Endpoint Detection and Response (EDR):**
  * Detecting suspicious processes or scripts initiating communication with external web services.
  * Identifying anomalous behavior or unusual use of legitimate applications (e.g., browsers, PowerShell scripts) connecting to cloud services.
* **Log Analysis and SIEM Tools:**
  * Correlating logs from web proxies, firewalls, and endpoints to detect suspicious outbound connections.
  * Identifying unusual user-agent strings, headers, or abnormal TLS certificates.
* **Threat Intelligence Integration:**
  * Leveraging threat intelligence feeds to identify known malicious domains or URLs.
* **Indicators of Compromise (IoCs):**
  * Suspicious URLs or domains associated with known malicious campaigns.
  * Unusual user-agent strings or HTTP headers indicating automated or scripted communication.
  * Unexpected connections to cloud storage services or collaboration tools from internal hosts.
  * Abnormal HTTP traffic volume or frequency from specific hosts.

## Why it is Important to Detect This Technique

Early detection of Web Service-based command-and-control activities is critical due to the significant risks posed to organizations, including:

* **Data Exfiltration and Intellectual Property Theft:**
  * Attackers can quietly exfiltrate sensitive data and intellectual property through legitimate cloud services, causing severe financial and reputational damage.
* **Persistence and Long-term Compromise:**
  * Using legitimate web services allows attackers to maintain persistent access, making remediation difficult and costly.
* **Bypassing Security Controls:**
  * Web Service techniques often bypass traditional security measures such as firewall rules, proxy filters, and intrusion detection systems, making detection critical for defense.
* **Operational Disruption:**
  * Attackers can leverage these channels to deliver additional payloads, ransomware, or destructive malware, causing severe operational disruptions.
* **Regulatory and Compliance Implications:**
  * Undetected Web Service-based attacks can lead to regulatory non-compliance, fines, and legal consequences due to data breaches or unauthorized data transfers.

## Examples

Real-world examples illustrating the use of Web Service techniques include:

* **APT29 (Cozy Bear):**
  * Utilized cloud storage services such as Dropbox to host payloads and exfiltrate data, enabling long-term espionage activities while evading detection.
  * Leveraged legitimate web services for command-and-control traffic, blending malicious communication with benign cloud traffic.
* **Turla Group:**
  * Used legitimate services like Google Drive and Pastebin to host payloads, scripts, and instructions, allowing compromised hosts to periodically poll for commands and updates.
* **OilRig (APT34):**
  * Leveraged GitHub repositories and Pastebin to distribute malicious scripts and payloads, providing reliable and covert command-and-control channels.
* **FIN7:**
  * Employed cloud-based collaboration tools (such as Slack) to facilitate communication between compromised hosts and attacker infrastructure, effectively bypassing traditional security controls.
* **DarkHydrus:**
  * Used Google Drive to host malicious payloads, enabling compromised hosts to retrieve instructions and exfiltrate data while blending in with normal user traffic.

These examples highlight attackers' strategic use of legitimate web services to evade detection, achieve persistence, and conduct long-term espionage or financial crime operations.
