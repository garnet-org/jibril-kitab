---
description: Active Scanning [T1595]
icon: barcode-read
---

# Active Scanning

## Information

* Name: Active Scanning
* ID: T1595
* Tactics: [TA0043](../)
* Sub-Technique: [T1595.002](t1595.002.md), [T1595.003](t1595.003.md), [T1595.001](t1595.001.md)

## Introduction

Active Scanning (T1595) in the MITRE ATT\&CK framework refers to the adversary's use of scanning techniques to gather information about target systems, networks, and services. Attackers actively probe networks to discover vulnerabilities, open ports, running services, and available resources. This technique helps attackers map the target environment and identify potential points of exploitation, facilitating subsequent attack stages like initial access, lateral movement, and privilege escalation.

## Deep Dive Into Technique

Active Scanning involves sending crafted network packets or queries to targeted systems and analyzing their responses to identify services, vulnerabilities, and network configurations. The scanning process can involve multiple technical approaches:

* **Port Scanning:**
  * Identifies open TCP and UDP ports.
  * Common tools include Nmap, Masscan, and Zmap.
  * Techniques include TCP SYN scans, TCP Connect scans, UDP scans, and ACK scans.
* **Vulnerability Scanning:**
  * Uses automated tools to detect known vulnerabilities.
  * Common vulnerability scanners include Nessus, OpenVAS, Qualys, and Rapid7 Nexpose.
  * Scanners rely on vulnerability databases, CVE identifiers, and exploit scripts to detect weaknesses.
* **Service Enumeration:**
  * Identifies running services and their versions.
  * Banner grabbing and fingerprinting techniques determine service details.
  * Tools such as Nmap, Metasploit auxiliary modules, and custom scripts are commonly used.
* **Network Mapping:**
  * Discovers network topology, subnets, and hosts.
  * Techniques include ICMP echo requests, traceroute, and ARP scanning.
  * Tools like Nmap, traceroute, and Ping sweeps facilitate this process.
* **Web Application Scanning:**
  * Detects vulnerabilities in web applications such as SQL injection, Cross-Site Scripting (XSS), and directory traversal.
  * Tools include OWASP ZAP, Burp Suite, Nikto, and Acunetix.

Real-world procedures may involve combining multiple scanning methods to achieve comprehensive reconnaissance. Attackers typically automate these scans using scripts or specialized software, allowing them to quickly gather extensive information about their targets.

## When this Technique is Usually Used

Active Scanning can appear in multiple attack stages and scenarios, including:

* **Reconnaissance Stage:**
  * Early-stage information gathering to identify potential targets, vulnerabilities, and attack vectors.
  * Used extensively by attackers to select promising targets before launching attacks.
* **Initial Access Stage:**
  * Attackers actively scan external-facing systems to identify vulnerabilities or misconfigurations that can be exploited to gain initial foothold.
* **Lateral Movement Stage:**
  * Internal network scanning to identify additional vulnerable hosts, privileges, and services for lateral movement.
* **Privilege Escalation Stage:**
  * Scanning internal hosts and services to identify misconfigurations or vulnerabilities that can be exploited to escalate privileges.
* **Persistence and Post-Exploitation Stages:**
  * Continuous scanning to maintain awareness of the environment and identify new potential targets or vulnerable services.

Active Scanning is commonly employed by various threat actors, including:

* Cybercriminals conducting ransomware campaigns.
* Advanced Persistent Threat (APT) groups performing targeted attacks.
* Penetration testers and red teams during security assessments.

## How this Technique is Usually Detected

Detection of Active Scanning involves monitoring network traffic, analyzing logs, and identifying abnormal scanning patterns. Detection methods include:

* **Network Intrusion Detection Systems (NIDS):**
  * Tools such as Snort, Suricata, Zeek (Bro), and Security Onion detect scanning patterns based on predefined signatures or behavioral rules.
  * Detection of excessive SYN packets, unusual port access patterns, and repeated connection attempts.
* **Firewall and IPS Logs:**
  * Analysis of firewall and Intrusion Prevention System logs for blocked or allowed connection attempts to multiple ports or hosts.
  * Identification of repeated failed connection attempts and unusual traffic patterns.
* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitoring host-level activities for unusual network connections or scanning-related processes.
  * Detection of scanning tools execution on endpoints.
* **SIEM and Log Analysis:**
  * Aggregation and correlation of logs from network devices, servers, and endpoints.
  * Detection of anomalies such as rapid sequential connection attempts, unusual traffic spikes, and abnormal service enumeration.

Specific Indicators of Compromise (IoCs) include:

* Multiple connection attempts from a single source IP address to various ports or hosts.
* Unusual network traffic patterns such as sequential port access or rapid scanning behaviors.
* Detection of known scanning tool signatures (e.g., Nmap user-agent strings, default scan payloads).
* Presence of scanning software executables or scripts on compromised endpoints.

## Why it is Important to Detect This Technique

Early detection of Active Scanning is critical due to its significant implications for system and network security:

* **Early Warning of Potential Attacks:**
  * Detecting Active Scanning can provide an early indication of attacker interest and intent, allowing security teams to proactively mitigate threats before exploitation occurs.
* **Preventing Exploitation of Vulnerabilities:**
  * Timely detection and response can prevent attackers from identifying vulnerabilities and reduce the risk of successful exploitation.
* **Reducing Attack Surface:**
  * Identifying scanning activities enables organizations to understand their exposed services and proactively secure or restrict access to vulnerable assets.
* **Minimizing Damage and Impact:**
  * Early detection helps limit potential damage, reduce downtime, and prevent data breaches or unauthorized access.
* **Compliance and Regulatory Requirements:**
  * Organizations may be required by regulatory frameworks to detect and respond to scanning activities promptly to maintain compliance and avoid penalties.

## Examples

Real-world examples of Active Scanning include:

* **WannaCry Ransomware Attack (2017):**
  * Attack Scenario: Attackers actively scanned the internet for vulnerable SMB services (port 445) to exploit the EternalBlue vulnerability.
  * Tools Used: Custom scanning scripts and automated exploitation tools.
  * Impact: Massive global disruption, affecting hundreds of thousands of computers, including critical infrastructure systems.
* **Mirai Botnet (2016):**
  * Attack Scenario: Mirai malware actively scanned the internet for IoT devices with default credentials or vulnerabilities.
  * Tools Used: Automated scripts embedded in Mirai malware to scan IP ranges and attempt login with common credentials.
  * Impact: Large-scale Distributed Denial of Service (DDoS) attacks, impacting major internet services and websites.
* **Equifax Data Breach (2017):**
  * Attack Scenario: Attackers actively scanned web servers to identify vulnerable Apache Struts installations.
  * Tools Used: Vulnerability scanning tools and scripts to detect and exploit CVE-2017-5638.
  * Impact: Compromise of personal data of approximately 147 million individuals, significant financial and reputational damage.
* **Operation Aurora (2010):**
  * Attack Scenario: APT groups conducted active scanning and reconnaissance to identify vulnerable services and hosts within targeted organizations.
  * Tools Used: Nmap, custom scanning scripts, and vulnerability scanners.
  * Impact: Compromise of intellectual property, sensitive data theft, and significant reputational impact on affected organizations.

These examples illustrate the widespread use of Active Scanning techniques by cyber adversaries, highlighting the importance of robust detection, monitoring, and defensive measures.
