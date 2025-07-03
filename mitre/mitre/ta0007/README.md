---
description: Discovery [TA0007]
icon: lock
---

# Discovery

## Information

* ID: TA0007

## Introduction

Discovery is a tactic within the MITRE ATT\&CK framework that involves adversaries attempting to gain detailed knowledge about the compromised environment. After initial access or compromise, attackers systematically explore systems, networks, and resources to identify valuable information, vulnerabilities, or potential pivot points. Discovery encompasses various techniques aimed at mapping the environment, enumerating system configurations, discovering user accounts, and understanding network structures. Attackers perform these actions to inform subsequent stages of their operations, such as lateral movement, privilege escalation, or data exfiltration.

## Deep Dive Into Technique

Discovery techniques are diverse and typically involve built-in operating system utilities, custom scripts, or specialized tools. Attackers leverage these techniques to gather information about the target environment, enabling informed decisions on subsequent actions.

Common discovery methods include:

* **Account Discovery:**
  * Enumerating local and domain user accounts using commands such as `net user`, `net group`, `net localgroup`, `dsquery user`, or PowerShell cmdlets like `Get-ADUser`.
  * Extracting account information from Active Directory or LDAP services.
* **Network Discovery:**
  * Scanning networks using tools like `nmap`, `masscan`, or built-in utilities (`ping`, `arp`, `tracert`).
  * Enumerating network shares using `net view`, `net share`, or SMB enumeration scripts.
  * Identifying network connections and open ports using commands such as `netstat`, `ss`, or PowerShell's `Get-NetTCPConnection`.
* **System Information Discovery:**
  * Gathering system details (OS version, patches, installed software) using commands like `systeminfo`, `wmic`, or PowerShell's `Get-ComputerInfo`.
  * Enumerating running processes (`tasklist`, `ps`, `top`) and services (`sc query`, `systemctl`).
* **File and Directory Discovery:**
  * Searching for sensitive files, configuration data, or credentials using commands like `dir`, `ls`, `find`, `grep`, or PowerShell's `Get-ChildItem`.
* **Cloud Infrastructure Discovery:**
  * Enumerating cloud resources, permissions, and configurations using cloud-specific CLI tools (AWS CLI, Azure CLI, Google Cloud CLI).
  * Querying cloud metadata services to identify instance details or credentials.

Attackers often automate discovery processes with custom scripts or frameworks (e.g., PowerSploit, BloodHound, Empire) to rapidly gather and analyze environmental data.

## When this Technique is Usually Used

Discovery techniques appear throughout various stages of the cyber kill chain and are particularly prevalent during:

* **Initial Reconnaissance and Post-Compromise Exploration:**
  * Immediately after gaining initial access to understand the compromised environment and identify potential targets for privilege escalation or lateral movement.
* **Privilege Escalation and Lateral Movement:**
  * Identifying vulnerable systems, services, or privileged accounts within the network to facilitate lateral movement or privilege escalation.
* **Persistence and Maintaining Access:**
  * Continuously monitoring the environment to detect changes, new users, or security measures deployed by defenders.
* **Data Exfiltration Preparation:**
  * Locating sensitive data repositories, file shares, databases, or cloud storage services before exfiltrating data.

Discovery is a foundational tactic that attackers repeatedly use throughout their operations to maintain situational awareness and adjust their strategies dynamically.

## How this Technique is Usually Detected

Detection of discovery techniques involves monitoring and analyzing multiple data sources, including logs, endpoint telemetry, network traffic, and behavioral analytics. Common detection methods include:

* **Endpoint Detection:**
  * Monitoring command-line execution and process creation events for suspicious discovery commands (`net user`, `systeminfo`, `tasklist`, `wmic`).
  * Analyzing PowerShell logs and script-block logging for unusual enumeration activities.
  * Detecting execution of known reconnaissance scripts or binaries (e.g., BloodHound, PowerSploit).
* **Network Detection:**
  * Identifying anomalous network scans or port enumeration activities through network intrusion detection systems (IDS/IPS) or network traffic analysis tools.
  * Detecting SMB enumeration attempts or unusual LDAP queries against Active Directory.
* **Log Analysis and SIEM Correlation:**
  * Aggregating and correlating logs from endpoints, Active Directory, and network devices to detect abnormal enumeration patterns.
  * Creating detection rules and alerts for specific discovery command usage or unusual user behavior.
* **Behavioral Analytics and Machine Learning:**
  * Leveraging user and entity behavioral analytics (UEBA) solutions to detect deviations from normal activity patterns indicative of discovery activities.

Specific Indicators of Compromise (IoCs) include:

* Execution of enumeration commands (`net user`, `net group`, `systeminfo`, `tasklist`) by unusual users or processes.
* Suspicious LDAP queries or Active Directory enumeration events.
* Network scans or port sweeps originating from internal hosts.
* Execution of known enumeration scripts or binaries (e.g., SharpHound, BloodHound collectors).

## Why it is Important to Detect This Technique

Early detection of discovery techniques is critical because it can significantly limit the adversary's ability to progress further into the attack lifecycle. The importance of detecting discovery includes:

* **Reducing Attacker Dwell Time:**
  * Identifying discovery activities early can reduce the time attackers spend undetected in the environment, limiting their ability to escalate privileges, move laterally, or exfiltrate data.
* **Preventing Privilege Escalation and Lateral Movement:**
  * Discovery is often a precursor to more damaging activities; detecting it early can prevent attackers from identifying vulnerabilities or misconfigurations that facilitate further compromise.
* **Protecting Sensitive Data:**
  * Early detection prevents attackers from locating sensitive information, reducing the risk of data exfiltration and breaches.
* **Improving Incident Response Effectiveness:**
  * Timely detection of discovery activities provides defenders with critical context to respond proactively, isolate compromised assets, and mitigate threats more effectively.
* **Strengthening Security Posture:**
  * Analyzing discovery attempts helps organizations identify weaknesses in their security controls, enabling continuous improvement and hardening of their infrastructure.

## Examples

Real-world examples illustrating discovery techniques, tools used, and impacts include:

* **APT29 (Cozy Bear):**
  * Attack Scenario: After initial access through phishing, APT29 utilized built-in Windows utilities such as `net user`, `net group`, and `systeminfo` to enumerate user accounts, domain groups, and system configurations.
  * Tools Used: Native Windows commands, PowerShell scripts.
  * Impact: Enabled lateral movement and privilege escalation, ultimately leading to sensitive data exfiltration.
* **Ryuk Ransomware:**
  * Attack Scenario: Ryuk operators conducted extensive network discovery using tools such as `nltest`, `net view`, and SMB enumeration scripts to map the network and identify critical assets.
  * Tools Used: Native Windows utilities, custom enumeration scripts.
  * Impact: Identification of critical assets and data repositories, leading to targeted ransomware deployment and significant operational disruption.
* **FIN7 Cybercrime Group:**
  * Attack Scenario: FIN7 leveraged PowerShell scripts and BloodHound to enumerate Active Directory environments, identify privileged user accounts, and map domain trust relationships.
  * Tools Used: BloodHound, PowerSploit, custom enumeration scripts.
  * Impact: Successful lateral movement, privilege escalation, and theft of sensitive data, including financial records and payment card information.
* **Cloud Hopper Campaign (APT10):**
  * Attack Scenario: APT10 conducted cloud infrastructure discovery using AWS CLI and Azure CLI tools to enumerate cloud resources, permissions, and credentials.
  * Tools Used: AWS CLI, Azure CLI, custom enumeration scripts.
  * Impact: Compromise of cloud environments, unauthorized access to sensitive data, and persistence within victim cloud infrastructures.

These examples demonstrate the widespread use of discovery techniques across various threat actor types, emphasizing the importance of robust detection and response capabilities.
