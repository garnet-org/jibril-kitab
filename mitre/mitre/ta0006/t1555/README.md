---
description: Credentials from Password Stores [T1555]
icon: key
---

# Credentials from Password Stores

## Information

* Name: Credentials from Password Stores
* ID: T1555
* Tactics: [TA0006](../)
* Sub-Technique: T1555.002, T1555.001, [T1555.005](t1555.005.md), [T1555.003](t1555.003.md), T1555.006, [T1555.004](t1555.004.md)

## Introduction

Credentials from Password Stores (MITRE ATT\&CK Technique ID: T1555) refers to adversaries accessing and extracting credential information from various password storage mechanisms. Password stores include password managers, browsers, operating system credential stores, and other secure storage solutions. Attackers leverage this technique to gain unauthorized access, escalate privileges, and maintain persistence within compromised environments. This technique is categorized under Credential Access tactics in the MITRE ATT\&CK framework, highlighting its role in facilitating deeper intrusion and lateral movement.

## Deep Dive Into Technique

Attackers use several methods and mechanisms to extract credentials from password stores:

* **Browser Credential Extraction:**
  * Modern browsers such as Chrome, Firefox, Edge, and Safari store credentials locally in encrypted databases or keychains.
  * Attackers utilize specialized tools like Mimikatz, LaZagne, WebBrowserPassView, or custom scripts to extract these credentials.
  * Credentials stored in browsers are often encrypted using user-specific keys, but attackers can decrypt them if they have sufficient privileges or user context.
* **Operating System Credential Stores:**
  * Windows Credential Manager, macOS Keychain, and Linux GNOME Keyring store user credentials securely.
  * Attackers may exploit vulnerabilities or misconfigurations to access and decrypt these credential stores.
  * On Windows, tools like Mimikatz, Credential Dumping scripts, or PowerShell modules can extract credentials from Credential Manager.
  * On macOS and Linux, attackers may leverage command-line utilities or scripts to access Keychain or Keyring data.
* **Third-party Password Managers:**
  * Password managers like KeePass, LastPass, 1Password, Dashlane, and Bitwarden securely store credentials in encrypted vaults.
  * Attackers may attempt to compromise vault files directly or intercept master passwords or session tokens.
  * Malware or keyloggers can capture master passwords or clipboard data, allowing attackers to decrypt stored credentials.
* **Memory Dumping and Credential Scraping:**
  * Credentials temporarily stored in memory can be extracted using memory scraping techniques.
  * Tools such as Mimikatz, ProcDump, or custom scripts can dump process memory and extract plaintext or hashed credentials.
* **Cloud and Network-based Credential Stores:**
  * Cloud-based password stores and services may be targeted through phishing, credential stuffing, or API exploitation.
  * Attackers may also intercept network traffic or perform man-in-the-middle attacks to capture credentials transmitted between users and password stores.

## When this Technique is Usually Used

Attackers typically utilize this technique during various stages of the attack lifecycle, including:

* **Initial Access and Reconnaissance:**
  * Early-stage attacks may involve credential theft to escalate privileges or pivot to other systems or services.
  * Phishing attacks or initial malware infections may target password stores to gain initial footholds.
* **Privilege Escalation and Lateral Movement:**
  * Attackers use stolen credentials to escalate privileges or move laterally within a network.
  * Credentials extracted from password stores can grant attackers access to sensitive resources, administrative accounts, or critical infrastructure.
* **Persistence and Long-term Access:**
  * Attackers leverage stolen credentials to maintain persistent access, even after detection and remediation attempts.
  * Credentials from password stores can provide attackers with multiple entry points and methods to regain control if initial footholds are lost.
* **Data Exfiltration and Impact:**
  * Attackers use extracted credentials to access sensitive data, intellectual property, or critical systems.
  * Credential theft can facilitate ransomware deployment, data exfiltration, or sabotage operations.

## How this Technique is Usually Detected

Detection involves monitoring, logging, and analyzing system behaviors and activities related to credential access:

* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitor processes and system activities for suspicious behaviors, such as memory scraping, credential dumping, or unauthorized access to password storage locations.
  * Detect known malicious tools (e.g., Mimikatz, LaZagne, WebBrowserPassView) based on file hashes, signatures, or behavioral patterns.
* **File Access and Audit Logging:**
  * Monitor file access events for password store files, databases, or configuration files (e.g., browser profile directories, KeePass database files, Keychain files).
  * Identify abnormal or unauthorized access attempts, especially from unusual processes or user accounts.
* **Network Traffic Analysis:**
  * Inspect network traffic for unusual patterns or data exfiltration attempts related to credential theft.
  * Detect suspicious outbound connections or data transfers indicative of stolen credential usage.
* **User and Entity Behavior Analytics (UEBA):**
  * Identify anomalous user behaviors, such as login attempts from unusual locations, times, or devices.
  * Correlate credential usage events with other suspicious activities to detect potential credential compromise.
* **Indicators of Compromise (IoCs):**
  * Presence of known credential extraction tools or binaries (e.g., Mimikatz, LaZagne, WebBrowserPassView).
  * Suspicious processes accessing sensitive files or memory regions.
  * Unusual registry modifications related to credential storage mechanisms.
  * Detection of unauthorized or abnormal access to credential databases or password store files.

## Why it is Important to Detect This Technique

Early detection of credential theft from password stores is critical for several reasons:

* **Preventing Privilege Escalation and Lateral Movement:**
  * Early identification prevents attackers from escalating privileges and moving laterally, reducing overall damage and containment complexity.
* **Protecting Sensitive Information:**
  * Credentials grant access to sensitive data, intellectual property, or critical infrastructure. Early detection limits data exposure and breach impact.
* **Reducing Operational and Financial Impact:**
  * Credential theft often precedes significant attacks such as ransomware, sabotage, or data exfiltration. Early detection reduces remediation costs and organizational disruption.
* **Maintaining Compliance and Regulatory Requirements:**
  * Organizations must protect credentials and sensitive data to comply with regulations (e.g., GDPR, HIPAA, PCI-DSS). Detecting credential theft helps maintain compliance and avoid regulatory penalties.
* **Enhancing Incident Response Capabilities:**
  * Early detection provides incident response teams critical insights and indicators to rapidly respond, isolate, and remediate threats.

## Examples

Real-world examples demonstrating credential extraction from password stores include:

* **APT29 (Cozy Bear):**
  * Used credential extraction techniques, such as Mimikatz, to access Windows Credential Manager and browser-stored credentials.
  * Facilitated lateral movement and persistence in targeted networks, including the SolarWinds supply chain attack.
* **TrickBot Malware:**
  * Extracted browser-stored credentials and credentials from password managers.
  * Leveraged stolen credentials for lateral movement, ransomware deployment (Ryuk), and financial fraud activities.
* **RedLine Stealer:**
  * Malware specifically designed to steal browser-stored credentials, cryptocurrency wallets, and credentials from password managers.
  * Widely distributed via phishing campaigns, facilitating credential theft and subsequent unauthorized access.
* **FIN7 Cybercrime Group:**
  * Used credential dumping tools (e.g., LaZagne) to extract credentials from browsers and password managers.
  * Enabled targeted attacks against financial institutions, retail, hospitality, and other sectors for financial gain.
* **DarkHotel APT Group:**
  * Targeted business travelers, extracting credentials stored in browsers and password managers through compromised hotel Wi-Fi networks.
  * Facilitated espionage, intellectual property theft, and targeted attacks against corporate executives and government officials.
