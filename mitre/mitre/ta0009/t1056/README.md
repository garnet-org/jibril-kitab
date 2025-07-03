---
description: Input Capture [T1056]
icon: keyboard
---

# Input Capture

## Information

* Name: Input Capture
* ID: T1056
* Tactics: [TA0009](../), [TA0006](../../ta0006/)
* Sub-Technique: [T1056.001](t1056.001.md), [T1056.003](t1056.003.md), [T1056.002](t1056.002.md), T1056.004

## Introduction

Input Capture (MITRE ATT\&CK ID: T1056) is a technique adversaries utilize to intercept and record user input to obtain credentials, sensitive information, or other valuable data. This technique encompasses various methods, including keylogging, clipboard data extraction, and capturing user input from graphical interfaces or command-line sessions. Attackers commonly use input capture to escalate privileges, perform lateral movement, or gain deeper persistence within compromised environments.

## Deep Dive Into Technique

Input Capture involves intercepting user input through multiple technical approaches and mechanisms, including:

* **Keylogging:**
  * Software-based keyloggers installed on victim machines to record keystrokes.
  * Hardware-based keyloggers physically connected to keyboards or USB ports.
  * Kernel-level or driver-based keyloggers that intercept input at the operating system level.
* **Clipboard Data Capture:**
  * Monitoring and extracting data copied to the clipboard, which may contain sensitive information such as passwords or confidential content.
* **GUI Input Capture:**
  * Capturing input entered into graphical user interfaces (GUIs) by hooking into application processes or intercepting API calls.
  * Utilizing screen-capturing techniques to visually record user interactions and input.
* **Terminal Session Capture:**
  * Recording inputs entered into command-line interfaces or terminal sessions, particularly in Unix/Linux environments.
  * Intercepting SSH or remote desktop sessions to capture sensitive commands or credentials.

Technical mechanisms commonly used for implementing Input Capture include:

* API hooking and injection into legitimate processes.
* Kernel-mode rootkits or drivers to evade detection.
* Malicious browser extensions or plugins designed to intercept browser-based input.
* Exploitation of accessibility features to log keystrokes or GUI interactions.

Real-world adversaries often incorporate Input Capture into malware payloads, backdoors, and persistent implants to continuously harvest sensitive information over extended periods.

## When this Technique is Usually Used

Adversaries commonly use Input Capture techniques throughout various stages of an attack, including:

* **Initial Access and Credential Harvesting:**
  * Capturing user credentials during initial compromise to facilitate deeper network infiltration or lateral movement.
* **Privilege Escalation:**
  * Recording administrative or privileged user inputs to escalate privileges or gain access to additional resources.
* **Persistence and Long-Term Surveillance:**
  * Maintaining ongoing visibility into user activity and sensitive data inputs to sustain persistent access.
* **Lateral Movement:**
  * Capturing credentials and sensitive commands entered by users to pivot between systems and escalate access across the network.
* **Data Exfiltration:**
  * Gathering sensitive data inputs (e.g., passwords, financial information, confidential communications) for exfiltration and exploitation.

Scenarios frequently leveraging Input Capture include:

* Targeted espionage and reconnaissance campaigns.
* Financially motivated cybercrime operations (e.g., banking trojans).
* Insider threat monitoring and surveillance.
* Credential theft and account compromise attacks.

## How this Technique is Usually Detected

Input Capture detection methods typically involve a combination of behavioral analysis, endpoint monitoring, and specific indicators of compromise (IoCs):

* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitoring for suspicious API calls associated with keylogging or input interception.
  * Detecting unusual process injection or hooking behaviors indicative of input capture attempts.
* **Behavioral Analytics and Anomaly Detection:**
  * Identifying abnormal keyboard or clipboard monitoring activities.
  * Detecting processes accessing or logging keystrokes or clipboard data without legitimate justification.
* **System and Network Monitoring:**
  * Monitoring for suspicious outbound network connections from processes that may indicate exfiltration of captured input data.
  * Detecting unusual file creation or modification patterns associated with input logging activities.
* **Indicators of Compromise (IoCs):**
  * Presence of known keylogger binaries or malicious DLLs.
  * Unusual registry modifications or scheduled tasks consistent with input capture persistence mechanisms.
  * Suspicious files or logs containing captured keystrokes or clipboard content.
  * Unexpected hardware devices connected (hardware keyloggers).

Tools commonly used for detection include:

* Endpoint Detection and Response (EDR) platforms (e.g., CrowdStrike, SentinelOne, Carbon Black).
* Host-based intrusion detection systems (HIDS).
* Security Information and Event Management (SIEM) solutions (e.g., Splunk, QRadar, Elastic Security).
* Antivirus and anti-malware solutions with behavioral detection capabilities.

## Why it is Important to Detect This Technique

Early detection of Input Capture is crucial due to its significant potential impacts on organizations, systems, and users:

* **Credential Theft and Account Compromise:**
  * Captured credentials enable adversaries to escalate privileges, access sensitive systems, and propagate across networks.
* **Loss of Sensitive Data and Intellectual Property:**
  * Adversaries intercept sensitive corporate data, trade secrets, financial information, or personally identifiable information (PII), leading to severe financial and reputational damage.
* **Operational Disruption and Business Continuity Risks:**
  * Compromised user accounts and stolen credentials can disrupt critical business operations, causing downtime and productivity loss.
* **Regulatory and Compliance Implications:**
  * Failure to detect and respond to input capture attacks can lead to breaches of regulatory compliance (e.g., GDPR, HIPAA), resulting in legal penalties and fines.
* **Long-Term Persistence and Surveillance:**
  * Input capture allows adversaries to maintain persistent surveillance of user activity, significantly increasing the risk of prolonged, undetected compromise.

Therefore, proactive detection and mitigation of Input Capture techniques are essential to minimize organizational risk, protect sensitive information, and maintain operational integrity.

## Examples

Real-world examples demonstrating the use of Input Capture include:

* **Agent Tesla Malware:**
  * Widely-used information stealer malware capturing keystrokes and clipboard data.
  * Distributed via phishing emails and malicious attachments.
  * Impact: Credential theft, financial fraud, sensitive data exfiltration.
* **HawkEye Keylogger:**
  * Commercially available keylogger malware capturing keystrokes and clipboard content.
  * Typically delivered through phishing campaigns targeting businesses.
  * Impact: Theft of credentials, sensitive business information, financial losses.
* **APT Groups (e.g., APT28/Fancy Bear, APT29/Cozy Bear):**
  * Nation-state actors employing sophisticated input capture techniques within espionage operations.
  * Capturing credentials and sensitive information through keylogging and clipboard monitoring.
  * Impact: Significant breaches of government, defense, and corporate organizations, resulting in national security implications.
* **FIN7 Cybercrime Group:**
  * Financially motivated group deploying keyloggers and input capture tools in attacks on retail, hospitality, and financial sectors.
  * Capturing payment card data, credentials, and sensitive customer information.
  * Impact: Large-scale financial fraud, data breaches, and significant financial and reputational damage.

These examples highlight the prevalence and impact of Input Capture techniques across various threat actors, industries, and attack scenarios, underscoring the importance of effective detection and mitigation strategies.
