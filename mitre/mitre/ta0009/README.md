---
description: Collection [TA0009]
icon: folder
---

# Collection

## Information

* ID: TA0009

## Introduction

Collection is a tactic within the MITRE ATT\&CK framework that involves adversaries gathering information of interest from targeted systems and networks. During this phase, attackers seek sensitive data, credentials, intellectual property, or other critical information to achieve their objectives, such as espionage, financial gain, or sabotage. Collection typically occurs after initial access and persistence have been established, allowing attackers to identify, locate, and extract valuable data before exfiltration.

## Deep Dive Into Technique

Collection involves multiple techniques and procedures that adversaries use to gather data from compromised hosts or networks. Attackers may leverage various built-in operating system utilities, custom scripts, or specialized malware to locate and extract sensitive information. Key technical details include:

* **Automated Collection**:
  * Attackers deploy automated scripts or malware to scan and harvest data across multiple systems.
  * Tools include custom scripts, PowerShell, batch scripts, and specialized malware like Infostealers.
* **Clipboard Data Collection**:
  * Attackers monitor and collect data copied to the clipboard, often capturing credentials or sensitive information.
  * Malware commonly used includes keyloggers and clipboard hijackers.
* **Screen Capture**:
  * Attackers capture screenshots of user activity, potentially revealing sensitive information, credentials, or internal documents.
  * Tools include built-in OS utilities (e.g., Snipping Tool, screenshot commands) or specialized malware.
* **Input Capture (Keylogging)**:
  * Attackers record keystrokes to capture credentials, confidential communications, or sensitive data.
  * Common tools include keyloggers embedded in malware or standalone utilities.
* **Data from Local System**:
  * Attackers collect files stored locally, including documents, configuration files, logs, or database files.
  * Techniques involve automated file searches, file indexing, and targeted copying.
* **Data from Network Shared Drives**:
  * Attackers enumerate and collect data from accessible network shares.
  * Methods include SMB enumeration, network drive mapping, and automated file scanning tools.
* **Email Collection**:
  * Attackers target email clients or servers to extract sensitive communications.
  * Tools include scripts, malware plugins, or direct access to email storage files (e.g., PST, OST, EML files).
* **Browser Data Collection**:
  * Attackers harvest stored browser data, including passwords, cookies, browsing history, or session tokens.
  * Malware or scripts target browser data storage locations or leverage tools like Mimikatz.

## When this Technique is Usually Used

Adversaries utilize the Collection tactic throughout various stages of an attack lifecycle, primarily after gaining initial access and establishing persistence. Typical attack scenarios include:

* **Reconnaissance and Espionage**:
  * Gathering sensitive documents, intellectual property, or strategic information for intelligence purposes.
* **Credential Theft and Privilege Escalation**:
  * Capturing credentials via keylogging, clipboard monitoring, or browser data harvesting to escalate privileges or move laterally across networks.
* **Financially Motivated Cybercrime**:
  * Collecting financial data, payment card information, banking credentials, or personally identifiable information (PII) for fraudulent activities.
* **Ransomware Attacks**:
  * Extracting sensitive data prior to encryption for double-extortion purposes, threatening data leaks if demands are not met.
* **Supply Chain Attacks**:
  * Harvesting credentials, code repositories, or sensitive documentation to compromise downstream customers or partners.
* **Insider Threat Scenarios**:
  * Malicious insiders collecting proprietary or confidential data for personal gain or competitive advantage.

## How this Technique is Usually Detected

Detecting Collection activities involves a combination of monitoring, logging, and threat hunting techniques. Common detection methods and tools include:

* **Endpoint Detection and Response (EDR)**:
  * Monitoring endpoint processes for suspicious behaviors, such as unusual file access patterns, clipboard monitoring, or keylogging.
  * Tools: CrowdStrike Falcon, Microsoft Defender for Endpoint, Carbon Black.
* **Network Traffic Analysis (NTA)**:
  * Identifying unusual network traffic patterns, data transfers, or connections indicative of data collection and exfiltration.
  * Tools: Zeek (Bro), Cisco Stealthwatch, Darktrace.
* **Security Information and Event Management (SIEM)**:
  * Correlating events from multiple sources (endpoint logs, network logs, authentication logs) to detect anomalous behaviors.
  * Tools: Splunk, QRadar, LogRhythm.
* **File Integrity Monitoring (FIM)**:
  * Detecting unauthorized access, modification, or copying of sensitive files and folders.
  * Tools: Tripwire, OSSEC, Qualys FIM.
* **User and Entity Behavior Analytics (UEBA)**:
  * Identifying abnormal user behaviors, such as unusual access to sensitive data or sudden increases in data collection activities.
  * Tools: Exabeam, Microsoft Sentinel UEBA, Splunk UBA.

Specific Indicators of Compromise (IoCs):

* Unusual processes accessing sensitive files or folders.
* Unexpected screen capture utilities or clipboard-monitoring processes running.
* Suspicious scripts or binaries performing automated file searches and indexing.
* Anomalous network connections or data transfers to unknown external IP addresses.
* Presence of unfamiliar tools or malware associated with data harvesting (e.g., Mimikatz, keyloggers, Infostealers).

## Why it is Important to Detect This Technique

Early detection of Collection activities is critical due to the significant risks and impacts associated with data theft and unauthorized access. Potential impacts include:

* **Data Breaches**:
  * Loss of sensitive or confidential data, resulting in financial loss, regulatory penalties, or reputational damage.
* **Espionage and Intellectual Property Theft**:
  * Theft of proprietary information, trade secrets, or strategic plans, threatening competitive advantage and organizational security.
* **Credential Theft and Further Exploitation**:
  * Captured credentials enable attackers to escalate privileges, move laterally, and maintain persistence, increasing the severity and duration of compromise.
* **Financial Loss and Fraud**:
  * Theft of financial information, payment card data, or personally identifiable information (PII) leading to identity theft, fraud, and financial damages.
* **Operational Disruption**:
  * Attackers leveraging collected data to disrupt operations, sabotage systems, or extort organizations (e.g., ransomware double-extortion attacks).

Early detection helps organizations:

* Limit the extent of data loss and associated damages.
* Respond quickly to contain and remediate threats.
* Maintain compliance with regulatory requirements and avoid penalties.
* Preserve organizational reputation and customer trust.

## Examples

Real-world examples of Collection tactics in cyber-attacks include:

* **APT28 (Fancy Bear)**:
  * Attack Scenario: Espionage campaigns targeting government and defense sectors.
  * Tools Used: Custom malware, keyloggers, screenshot capture utilities.
  * Impact: Theft of sensitive diplomatic, military, and political documents.
* **FIN7 Cybercrime Group**:
  * Attack Scenario: Financially motivated attacks targeting retail, hospitality, and financial sectors.
  * Tools Used: Carbanak malware to collect payment card data, credentials, and sensitive information.
  * Impact: Millions of dollars in financial losses due to stolen payment card data.
* **DarkSide Ransomware Group**:
  * Attack Scenario: Double-extortion ransomware attacks involving data collection prior to encryption.
  * Tools Used: Scripts and malware to collect sensitive data from compromised systems.
  * Impact: Data exfiltration and ransom demands, operational disruption, reputational damage.
* **SolarWinds Supply Chain Attack**:
  * Attack Scenario: Supply chain compromise leading to widespread infiltration of multiple organizations.
  * Tools Used: Sunburst malware for data collection and credential harvesting.
  * Impact: Compromise of sensitive government and private-sector data, significant disruption, and reputational harm.
* **Agent Tesla Infostealer**:
  * Attack Scenario: Mass-distributed malware campaigns targeting credentials, browser data, and clipboard content.
  * Tools Used: Agent Tesla malware capable of keylogging, clipboard monitoring, and browser data harvesting.
  * Impact: Credential theft, financial fraud, identity theft, and unauthorized access to sensitive systems.
