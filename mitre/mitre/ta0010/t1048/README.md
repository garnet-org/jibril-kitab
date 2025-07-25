---
description: Exfiltration Over Alternative Protocol [T1048]
icon: lock
---

# Exfiltration Over Alternative Protocol

## Information

* Name: Exfiltration Over Alternative Protocol
* ID: T1048
* Tactics: [TA0010](../)
* Sub-Technique: [T1048.001](t1048.001.md), [T1048.002](t1048.002.md), [T1048.003](t1048.003.md)

## Introduction

Exfiltration Over Alternative Protocol (MITRE ATT\&CK ID: T1048) refers to adversaries leveraging uncommon or non-standard network protocols to transfer stolen data out of a compromised network. By using protocols that are less frequently monitored, attackers attempt to evade detection and bypass traditional security controls. Commonly exploited protocols include DNS, ICMP, SMTP, and other application-layer protocols that are not typically associated with data transfer or exfiltration.

## Deep Dive Into Technique

Adversaries employing Exfiltration Over Alternative Protocol typically exploit legitimate network protocols in unintended ways:

* **DNS Tunneling:** Attackers encode data into DNS queries or responses, leveraging DNS as a covert channel for data exfiltration. DNS is rarely blocked or closely monitored, making it an attractive choice.
  * Tools commonly used include:
    * `iodine`
    * `DNSCat2`
    * `dnscapy`
* **ICMP Tunneling:** Data is encapsulated within ICMP Echo Request/Reply packets, allowing attackers to bypass firewalls or IDS that do not deeply inspect ICMP traffic.
  * Tools commonly used include:
    * `PingTunnel`
    * `icmpsh`
* **SMTP Exfiltration:** Attackers may use SMTP to send sensitive data as email attachments or within email bodies to external servers, often using legitimate email servers to mask their activities.
  * Tools commonly used include:
    * Custom scripts leveraging SMTP libraries (Python smtplib, PowerShell scripts)
    * `Empire` framework modules
* **Other Application-Layer Protocols:** Less frequently monitored application protocols such as FTP, IRC, or instant messaging protocols can also be abused for data exfiltration.

Mechanisms generally involve:

* Encoding data to avoid immediate detection (base64, encryption).
* Fragmenting data into smaller packets to evade network monitoring thresholds.
* Employing legitimate services or cloud-based platforms to relay traffic, making detection more difficult.

## When this Technique is Usually Used

Attackers typically use Exfiltration Over Alternative Protocol in the following scenarios and stages of an attack:

* **Late-stage post-exploitation:** After attackers have gained persistence and collected sensitive data, they use alternative protocols to stealthily remove data from the victim network.
* **Highly secured environments:** In networks with strict firewall rules, deep packet inspection, or well-monitored outbound traffic, attackers resort to protocols that are less scrutinized.
* **Advanced Persistent Threat (APT) campaigns:** Sophisticated adversaries use this technique to maintain long-term stealth and avoid detection by standard security controls.
* **Environments with limited visibility or logging:** Attackers exploit environments lacking proper monitoring of DNS, ICMP, or SMTP traffic.

## How this Technique is Usually Detected

Detection of Exfiltration Over Alternative Protocol requires specialized methods and tools due to its covert nature:

* **Network Traffic Analysis:**
  * Anomaly detection through unusual DNS query volume, size, or frequency.
  * Monitoring ICMP traffic volume, packet size anomalies, or unusual ICMP payload content.
  * SMTP traffic analysis for unusual email volume, attachment sizes, or unusual recipient domains.
* **Deep Packet Inspection (DPI):**
  * Analyzing payloads within DNS or ICMP packets to detect encoded or encrypted data.
  * Identifying non-standard use of protocols through payload analysis.
* **Security Information and Event Management (SIEM):**
  * Correlation rules identifying anomalies such as unusual protocol usage, abnormal traffic patterns, or excessive outbound traffic to suspicious external destinations.
* **Endpoint Detection and Response (EDR):**
  * Monitoring endpoint processes and activities associated with known exfiltration tools.
  * Detecting command-line executions or scripts indicative of exfiltration attempts.

Specific Indicators of Compromise (IoCs) include:

* Unusual DNS queries (high frequency, large payload size, uncommon subdomains).
* Elevated ICMP traffic volume or abnormal ICMP packet sizes.
* SMTP traffic to unknown or suspicious email domains or recipients.
* Presence of known tunneling tools (`iodine`, `DNSCat2`, `PingTunnel`, `icmpsh`) on endpoints.

## Why it is Important to Detect This Technique

Detecting Exfiltration Over Alternative Protocol is critical due to the potential severe impacts on organizations:

* **Data Loss:** Sensitive, confidential, or proprietary data can be exfiltrated, causing financial damage, regulatory penalties, and loss of competitive advantage.
* **Stealth and Persistence:** Attackers employing this technique often remain undetected for extended periods, allowing prolonged unauthorized access and continual data theft.
* **Compliance Violations:** Failure to detect and prevent data exfiltration can lead to regulatory non-compliance, resulting in hefty fines, lawsuits, and reputational damage.
* **Operational Disruption:** Undetected exfiltration can lead to long-term compromise, forcing costly incident response, remediation efforts, and potential operational downtime.
* **Reputational Damage:** Breaches involving sensitive data exfiltration can severely impact public trust, customer relationships, and brand reputation.

Early detection allows organizations to:

* Limit the impact of breaches by quickly containing and remediating incidents.
* Prevent prolonged unauthorized access and reduce the scope of data loss.
* Maintain compliance with regulatory requirements and standards.
* Protect organizational reputation and customer trust.

## Examples

Real-world examples highlighting Exfiltration Over Alternative Protocol include:

* **APT32 (OceanLotus):**
  * Scenario: APT32 utilized DNS tunneling to exfiltrate sensitive data from compromised networks, encoding stolen information within DNS queries.
  * Tools Used: Custom DNS tunneling malware and scripts, DNSCat2 variants.
  * Impact: Significant data loss, prolonged stealthy access, and difficulty in detection due to covert exfiltration methods.
* **Operation Sharpshooter:**
  * Scenario: Attackers used DNS tunneling to exfiltrate reconnaissance data and credentials from targeted organizations.
  * Tools Used: Custom malware leveraging DNS protocol for covert data transfer.
  * Impact: Compromise of sensitive corporate and governmental data, persistent attacker presence, and extended incident response efforts.
* **FIN7 Group:**
  * Scenario: FIN7 leveraged SMTP protocol to send stolen credit card data and financial information from compromised point-of-sale (POS) systems to attacker-controlled email servers.
  * Tools Used: Custom PowerShell scripts, SMTP libraries (Python, PowerShell), Empire framework modules.
  * Impact: Massive financial losses, compromised customer financial data, and significant reputational harm to victim organizations.
* **ICMP Tunneling Attacks:**
  * Scenario: Attackers used ICMP tunneling to bypass firewall restrictions, encapsulating stolen data within ICMP Echo Requests and Replies.
  * Tools Used: `icmpsh`, `PingTunnel`.
  * Impact: Successful data exfiltration from secured environments, bypassing standard firewall rules and network defenses, resulting in prolonged attacker access and data leakage.
