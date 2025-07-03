---
description: Gather Victim Network Information [T1590]
icon: gun
---

# Gather Victim Network Information

## Information

* Name: Gather Victim Network Information
* ID: T1590
* Tactics: [TA0043](../)
* Sub-Technique: [T1590.005](t1590.005.md), [T1590.002](t1590.002.md), [T1590.004](t1590.004.md), [T1590.003](t1590.003.md), [T1590.006](t1590.006.md), [T1590.001](t1590.001.md)

## Introduction

Gathering victim network information is categorized under the MITRE ATT\&CK framework as a reconnaissance and discovery technique (T1590). Attackers leverage this technique to collect detailed information about the victim's network infrastructure, including IP addresses, network topology, domain information, subnet information, and network services. This information gathering phase is crucial for attackers to understand the victim's environment, identify potential vulnerabilities, and plan subsequent attack stages effectively.

## Deep Dive Into Technique

Attackers employ various technical methods and tools to gather detailed information about victim networks. This reconnaissance technique typically involves passive and active enumeration methods:

### Passive Enumeration Methods

* **WHOIS Queries**: Attackers query WHOIS databases to obtain domain registration details, administrative contacts, IP address ranges, and DNS server information.
* **DNS Enumeration**: Attackers use tools such as DNSdumpster, DNSRecon, or Dig to enumerate DNS records (A, MX, NS, TXT, PTR) to map the network infrastructure.
* **Publicly Available Sources**: Leveraging search engines, social media platforms, job postings, and company websites to identify network details, internal IP schemes, network architecture, and technologies in use.
* **Certificate Transparency Logs**: Attackers analyze publicly available certificate transparency logs to discover subdomains and internal services.

### Active Enumeration Methods

* **Network Scanning**: Tools like Nmap, Masscan, and Zmap actively probe IP ranges to identify live hosts, open ports, services, and operating systems.
* **Traceroute and Path Discovery**: Attackers use traceroute utilities to map network paths, identify network devices, and understand network topology.
* **SNMP Enumeration**: Exploiting Simple Network Management Protocol (SNMP) vulnerabilities or misconfigurations to gather network device information, configurations, and topology.
* **Banner Grabbing**: Using tools like Netcat, Telnet, or automated scripts to connect to services and extract banner information revealing service versions, operating systems, and configurations.

Attackers often combine passive and active enumeration techniques to create a comprehensive understanding of the victim's network infrastructure, enabling targeted and effective follow-up attacks.

## When this Technique is Usually Used

Attackers utilize network information gathering techniques across various attack stages and scenarios:

* **Reconnaissance Phase**: Primary use-case during initial reconnaissance to identify targets, understand network architecture, and discover vulnerabilities.
* **Initial Access and Exploitation**: Gathering detailed network information to identify vulnerable services, misconfigurations, and weak points for exploitation.
* **Lateral Movement**: Attackers use network information to identify internal hosts, subnets, and network paths, facilitating lateral movement through the victim's network.
* **Persistence and Privilege Escalation**: Leveraging network details to identify critical infrastructure, administrative systems, and high-value targets for privilege escalation and persistence.
* **Data Exfiltration**: Understanding network topology and security controls to plan stealthy data exfiltration paths and evade detection mechanisms.

## How this Technique is Usually Detected

Detection of network information gathering activities requires a combination of network monitoring, logging, and proactive security measures:

### Detection Methods

* **Network Traffic Monitoring**:
  * Monitoring unusual network scanning activities (e.g., multiple connection attempts, SYN scans, port sweeps).
  * Detecting suspicious DNS queries (high volume of DNS enumeration requests).
  * Identifying abnormal traceroute attempts or ICMP traffic patterns.
* **Intrusion Detection Systems (IDS)**:
  * Signature-based detection of known scanning tools (e.g., Nmap, Masscan).
  * Behavioral-based detection to identify anomalous network enumeration behaviors.
* **Security Information and Event Management (SIEM)**:
  * Correlation of logs from firewalls, routers, DNS servers, and other network devices to detect enumeration attempts.
  * Alerting on failed SNMP authentication attempts or unauthorized SNMP queries.
* **Endpoint Detection and Response (EDR)**:
  * Detecting unauthorized use of enumeration tools on endpoints.
  * Monitoring suspicious network enumeration scripts or programs executed on compromised hosts.

### Tools for Detection

* Intrusion Detection Systems (IDS) such as Snort, Suricata, Zeek (Bro)
* Security Information and Event Management (SIEM) solutions such as Splunk, QRadar, Elastic Security
* Endpoint Detection and Response (EDR) tools like CrowdStrike Falcon, Microsoft Defender for Endpoint, Carbon Black
* Network monitoring solutions like Wireshark, tcpdump, Zeek (Bro)

### Indicators of Compromise (IoCs)

* Unusual spikes in DNS queries to internal/external DNS servers.
* High volume of ICMP traffic indicative of traceroute or ping sweeps.
* Multiple failed SNMP authentication attempts.
* Extensive connection attempts to sequential IP addresses or ports indicative of scanning activity.
* Known enumeration tool signatures and user-agent strings appearing in network traffic.

## Why it is Important to Detect This Technique

Early detection of victim network information gathering is crucial for preventing severe impacts and mitigating security risks:

* **Preventing Initial Compromise**: Detecting reconnaissance activities can help organizations block attackers before they exploit vulnerabilities and gain initial access.
* **Reducing Attack Surface**: Early detection allows organizations to identify and remediate exposed services, misconfigurations, and vulnerabilities, reducing opportunities for attackers.
* **Minimizing Lateral Movement**: Detecting enumeration attempts within internal networks can prevent attackers from moving laterally, limiting potential damage and data exposure.
* **Protecting Sensitive Data**: Early detection and mitigation reduce the risk of sensitive data exfiltration and unauthorized access to critical systems.
* **Maintaining Operational Continuity**: Preventing attackers from mapping and compromising critical infrastructure ensures business continuity and reduces downtime and remediation costs.
* **Compliance and Regulatory Requirements**: Early detection and incident response capabilities help maintain compliance with regulatory frameworks and industry standards.

## Examples

Real-world examples of victim network information gathering incidents, attack scenarios, and impacts include:

* **APT29 (Cozy Bear) Attacks**:
  * Scenario: Utilized extensive DNS enumeration and network scanning to map victim networks before launching targeted spear-phishing and exploitation attacks.
  * Tools Used: Custom scripts, Nmap, DNSRecon.
  * Impact: Successfully compromised government and private sector networks, leading to espionage and data exfiltration.
* **Mirai Botnet**:
  * Scenario: Conducted large-scale network scanning and banner grabbing to identify vulnerable IoT devices with default credentials.
  * Tools Used: Masscan, custom scanning scripts.
  * Impact: Massive Distributed Denial of Service (DDoS) attacks affecting critical internet infrastructure and services.
* **FIN7 Cybercrime Group**:
  * Scenario: Performed detailed network reconnaissance to identify point-of-sale (POS) systems and administrative networks within retail and hospitality sectors.
  * Tools Used: Cobalt Strike, Nmap, custom enumeration scripts.
  * Impact: Millions of customer payment card records compromised, causing financial losses for affected businesses.
* **Operation Aurora (Google Attack)**:
  * Scenario: Attackers conducted network scanning and reconnaissance to identify vulnerable web servers and internal systems.
  * Tools Used: Nmap, custom enumeration tools.
  * Impact: Intellectual property theft, compromise of internal systems, and unauthorized access to sensitive corporate data.

Understanding these real-world examples highlights the critical importance of detecting and responding to victim network information gathering techniques promptly to minimize potential impacts and strengthen overall cybersecurity posture.
