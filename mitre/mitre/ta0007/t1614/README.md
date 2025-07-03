---
description: System Location Discovery [T1614]
icon: lock
---

# System Location Discovery

## Information

* Name: System Location Discovery
* ID: T1614
* Tactics: [TA0007](../)
* Sub-Technique: [T1614.001](t1614.001.md)

## Introduction

System Location Discovery is a technique categorized under the MITRE ATT\&CK framework (Technique ID: T1614). Attackers leverage this technique to identify geographical or physical location information of targeted systems or networks. This information aids adversaries in strategic targeting, evasion of detection, and tailored exploitation. Understanding and detecting this technique is crucial for proactive cybersecurity defense.

## Deep Dive Into Technique

System Location Discovery involves adversaries determining the physical or geographical location of a compromised system or network. Attackers typically employ various methods to achieve this, including:

* **IP Geolocation Services:**
  * Attackers query external IP geolocation databases or services to map IP addresses to geographic locations.
  * Services like MaxMind GeoIP, IPinfo, or ipgeolocation.io are commonly used.
* **System Configuration Analysis:**
  * Examination of system settings such as timezone, language settings, or regional configurations.
  * Reviewing registry entries on Windows or locale files on Unix/Linux systems.
* **Network Infrastructure Reconnaissance:**
  * Analyzing DNS records, WHOIS databases, and network routing paths to identify geographic locations.
  * Tracing network hops and latency measurements to approximate physical locations.
* **Metadata Extraction:**
  * Analyzing metadata from documents, images, or files residing on compromised systems.
  * Extracting GPS coordinates or other location-related data embedded within files.
* **Wireless Network Analysis:**
  * Leveraging SSID information, MAC addresses, and nearby Wi-Fi access points to deduce physical locations.
  * Utilizing databases like WiGLE.net for mapping wireless networks.

Attackers often automate these methods through scripts, malware modules, or reconnaissance tools to streamline the discovery process.

## When this Technique is Usually Used

System Location Discovery can occur across various stages of an attack lifecycle, particularly during:

* **Initial Reconnaissance:**
  * Attackers gather location-related intelligence before launching targeted attacks to tailor phishing campaigns or exploit vulnerabilities specific to certain regions.
* **Post-Exploitation and Persistence:**
  * After initial compromise, adversaries may verify location details to confirm they have accessed the intended target or to pivot within the network.
* **Targeted Espionage Campaigns:**
  * Nation-state actors and advanced persistent threats (APTs) perform system location discovery to identify sensitive or strategic targets based on geographic criteria.
* **Ransomware Attacks:**
  * Attackers may identify geographic locations to enforce compliance with sanctions, avoid law enforcement attention, or set ransom demands according to regional economic factors.
* **Fraud and Financial Attacks:**
  * Cybercriminals use location discovery to bypass geolocation-based security controls or to tailor fraudulent campaigns to specific regions.

## How this Technique is Usually Detected

Organizations can detect System Location Discovery through multiple methods and tools:

* **Network Traffic Monitoring:**
  * Detecting unusual outbound connections to known IP geolocation services or WHOIS databases.
  * Monitoring DNS queries to known geolocation or metadata extraction services.
* **Endpoint Detection and Response (EDR) Tools:**
  * EDR solutions can identify suspicious processes or scripts accessing system locale, timezone, or registry entries related to location data.
* **Log Analysis and SIEM Solutions:**
  * Correlating logs from firewalls, proxies, DNS servers, and endpoints to detect patterns indicative of location discovery.
  * Identifying repeated attempts to access files or metadata containing location information.
* **Behavioral Analytics:**
  * Machine-learning algorithms that detect anomalies in system or network behavior, such as unusual queries or metadata extraction attempts.
* **Indicators of Compromise (IoCs):**
  * Suspicious IP addresses or domains associated with popular geolocation services.
  * Unexpected access to system files or registry keys related to timezone, locale, or regional settings.
  * Unusual scripts or binaries performing geolocation lookups or metadata extraction.

## Why it is Important to Detect This Technique

Detecting System Location Discovery is crucial for several reasons:

* **Preventing Targeted Attacks:**
  * Early detection can disrupt adversaries' reconnaissance efforts, limiting their ability to launch precise, tailored attacks.
* **Reducing Risk of Data Exfiltration:**
  * Location discovery often precedes data theft or espionage; detecting this activity can prevent further compromise.
* **Compliance and Regulatory Requirements:**
  * Organizations may be subject to data sovereignty laws and regulations; unauthorized location discovery could indicate attempts to violate these rules.
* **Protecting Operational Security (OPSEC):**
  * Location information could compromise physical security or operational secrecy, especially in sensitive industries such as defense, critical infrastructure, or government facilities.
* **Minimizing Financial and Reputational Damage:**
  * Early detection and response reduce potential financial losses, regulatory fines, and reputational harm resulting from targeted attacks or breaches.

## Examples

Real-world examples of System Location Discovery include:

* **APT28 (Fancy Bear):**
  * Russian state-sponsored threat actor known to use IP geolocation services and metadata extraction from target documents to identify the geographic locations of targeted systems, particularly in espionage campaigns against government entities.
* **FIN7 Cybercrime Group:**
  * Known for financial attacks, FIN7 used location discovery techniques to tailor phishing emails and malware campaigns to specific geographic regions, increasing their effectiveness.
* **Equation Group:**
  * Advanced persistent threat linked to the NSA, reportedly leveraging network infrastructure reconnaissance and system settings analysis to identify precise geographic locations of targets, facilitating highly targeted espionage operations.
* **Ransomware Operators (e.g., REvil/Sodinokibi):**
  * Employing IP geolocation and metadata extraction to verify victim location, adjust ransom demands, or avoid targeting entities in jurisdictions that could trigger law enforcement actions.
* **DarkHotel Campaign:**
  * Threat actor targeting hotel Wi-Fi networks, using wireless network analysis and metadata extraction methods to pinpoint locations of high-profile targets, enabling tailored exploitation and espionage.

In these examples, attackers utilized various tools and methodologies, including custom scripts, publicly available geolocation databases, metadata extraction tools (ExifTool, FOCA), and network reconnaissance utilities (traceroute, WHOIS lookups). Impacts ranged from sensitive data exfiltration and financial loss to significant operational disruption and reputational damage.
