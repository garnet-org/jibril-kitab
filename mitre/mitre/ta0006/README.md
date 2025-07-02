---
description: Credential Access [TA0006]
icon: door-open
---

# Credential Access [TA0006]

## Information

- ID: TA0006

## Introduction

Credential Access is a critical tactic in the MITRE ATT&CK framework that involves techniques adversaries use to obtain account credentials, such as usernames and passwords, to gain unauthorized access to systems and networks. Attackers frequently target credentials to escalate privileges, maintain persistence, and move laterally within compromised environments. Credential Access techniques include extracting credentials from operating systems, applications, browsers, and network traffic, making it a pivotal step in many cyber-attacks.

## Deep Dive Into Technique

Credential Access encompasses a wide range of methods and procedures adversaries use to extract or compromise credentials. Common execution methods include:

- **Credential Dumping:**

  - Accessing password hashes stored in system memory or files (e.g., SAM database, LSASS process on Windows).
  - Tools commonly used: Mimikatz, Procdump, Windows Credential Editor (WCE).
  - Techniques:
    - Extracting hashes from the Security Account Manager (SAM) database.
    - Dumping credentials from the Local Security Authority Subsystem Service (LSASS) memory.
    - Accessing cached credentials stored on Windows systems.

- **Keylogging:**

  - Capturing keystrokes to obtain credentials as users type them.
  - Tools commonly used: Hardware keyloggers, software-based solutions like Keylogger malware.

- **Brute Force Attacks:**

  - Attempting multiple password combinations to gain access to accounts.
  - Tools commonly used: Hydra, Medusa, CrackMapExec.

- **Credential Theft from Web Browsers:**

  - Extracting stored passwords and session cookies from browsers.
  - Tools commonly used: BrowserPassView, LaZagne.

- **Network Sniffing:**

  - Intercepting network traffic to capture plaintext credentials or hashes.
  - Tools commonly used: Wireshark, tcpdump, Ettercap.

- **Password Spraying:**

  - Attempting common passwords against multiple user accounts to avoid account lockouts.
  - Tools commonly used: Metasploit framework, CrackMapExec.

- **Credential Harvesting via Phishing:**
  - Trick users into providing their credentials through deceptive emails or fake login pages.
  - Tools commonly used: Evilginx, SET (Social Engineering Toolkit).

## When this Technique is Usually Used

Credential Access techniques are typically employed at various stages of an attack lifecycle, including:

- **Initial Access Stage:**

  - Phishing attacks designed to harvest credentials.
  - Password spraying or brute-force attacks against externally accessible services.

- **Execution and Persistence Stages:**

  - Credential dumping to gain higher privileges or maintain persistent access.
  - Keylogging to continuously capture credentials.

- **Privilege Escalation Stage:**

  - Extracting privileged account credentials from memory or configuration files.

- **Lateral Movement Stage:**

  - Using stolen credentials to move across internal systems and networks.
  - Pass-the-hash or pass-the-ticket attacks leveraging compromised credentials.

- **Exfiltration and Impact Stages:**
  - Using credentials to access sensitive data repositories.
  - Deploying ransomware or destructive malware using elevated credentials.

## How this Technique is Usually Detected

Effective detection of Credential Access techniques involves monitoring, logging, and analysis using various tools and methods, including:

- **Endpoint Detection and Response (EDR) Solutions:**

  - Monitoring for suspicious processes accessing credential storage locations (e.g., LSASS).
  - Detecting unusual process injections or memory dumps.

- **Security Information and Event Management (SIEM) Systems:**

  - Alerting on multiple failed login attempts indicative of brute force or password spraying attacks.
  - Correlating suspicious authentication events across multiple systems.

- **Behavioral Analytics:**

  - Identifying abnormal user login patterns, such as logins from unusual locations or times.
  - Detecting anomalies in credential usage, such as privileged account logins from unexpected hosts.

- **Network Traffic Analysis:**

  - Detecting plaintext credential exposure or unusual credential-related network traffic.
  - Identifying communication indicative of credential harvesting or phishing.

- **Honeypots and Deception Technologies:**

  - Deploying decoy credentials or services to detect unauthorized credential usage attempts.

- **Indicators of Compromise (IoCs):**
  - Unusual process execution (e.g., Mimikatz, procdump.exe).
  - Suspicious registry modifications related to credential storage.
  - Presence of credential dumping tools or scripts on endpoints.
  - Unusual authentication logs, failed login attempts, or suspicious account lockouts.
  - Unexpected network traffic, such as SMB or Kerberos traffic anomalies.

## Why it is Important to Detect This Technique

Early detection of Credential Access techniques is critical due to the significant impacts they can have on organizations, including:

- **Privilege Escalation:**

  - Attackers obtaining higher-level privileges, enabling further exploitation and control.

- **Lateral Movement:**

  - Compromised credentials allow attackers to move undetected across multiple systems and networks, significantly expanding the attack surface.

- **Data Exfiltration:**

  - Attackers gaining access to sensitive data repositories, leading to potential data breaches and compliance violations.

- **Persistence and Long-Term Compromise:**

  - Stolen credentials enable attackers to maintain persistent access, complicating remediation and increasing the risk of long-term compromise.

- **Operational Disruption:**

  - Credential compromise can result in unauthorized actions, data destruction, ransomware deployment, and severe disruption to business operations.

- **Reputational and Financial Damage:**
  - Credential theft can lead to severe reputational harm, loss of customer trust, regulatory fines, and significant financial losses.

Early and accurate detection allows organizations to respond rapidly, limit damage, and prevent further compromise.

## Examples

Real-world examples of Credential Access techniques and their impacts include:

- **NotPetya Attack (2017):**

  - Attackers used credential dumping tools (Mimikatz) to extract credentials from infected systems.
  - Leveraged pass-the-hash techniques for rapid lateral movement.
  - Resulted in billions of dollars in damages globally, impacting multiple multinational corporations.

- **Colonial Pipeline Attack (2021):**

  - Attackers gained initial access through compromised VPN credentials.
  - Used stolen credentials to move laterally within the network and deploy ransomware.
  - Caused significant disruption to fuel supply in the United States, leading to widespread economic impact.

- **SolarWinds Supply Chain Attack (2020):**

  - Attackers harvested credentials through advanced credential theft techniques and lateral movement.
  - Compromised numerous government agencies and private sector organizations.
  - Highlighted the critical importance of monitoring credential access and usage.

- **Operation Cloud Hopper (2019):**

  - Threat actors compromised Managed Service Providers (MSPs) using credential theft and lateral movement.
  - Extracted credentials to access client networks, resulting in data exfiltration and espionage.

- **Emotet Malware Campaigns:**
  - Malware deployed credential stealing modules to extract passwords from browsers and email clients.
  - Credentials were subsequently used for further attacks, spam campaigns, and lateral movement.

These examples emphasize the critical role of Credential Access techniques in successful cyber-attacks and underscore the necessity for robust detection and prevention measures.
