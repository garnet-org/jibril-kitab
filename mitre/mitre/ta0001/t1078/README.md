---
description: Valid Accounts [T1078]
icon: users
---

# Valid Accounts

## Information

* Name: Valid Accounts
* ID: T1078
* Tactics: [TA0005](../../ta0005/), [TA0003](../../ta0003/), [TA0004](../../ta0004/), [TA0001](../)
* Sub-Technique: [T1078.001](t1078.001.md), [T1078.002](t1078.002.md), [T1078.004](t1078.004.md), [T1078.003](t1078.003.md)

## Introduction

The Valid Accounts technique (MITRE ATT\&CK ID: T1078) refers to adversaries leveraging legitimate user credentials to gain unauthorized access, maintain persistence, escalate privileges, or perform lateral movement within targeted environments. In the MITRE ATT\&CK framework, this technique falls under the tactic categories of Initial Access, Persistence, Privilege Escalation, and Defense Evasion. By utilizing valid credentials, attackers blend seamlessly into normal user activity, significantly complicating detection and response efforts.

## Deep Dive Into Technique

Attackers employing the Valid Accounts technique exploit legitimate authentication mechanisms by using stolen, compromised, or otherwise illicitly obtained credentials. This approach can circumvent traditional security defenses, as the activity appears as normal user behavior.

Technical execution methods and mechanisms include:

* **Credential Theft**:
  * Phishing attacks targeting user credentials.
  * Credential dumping from compromised systems (e.g., using Mimikatz or LSASS memory extraction).
  * Keylogging malware capturing credentials from user input.
  * Credential harvesting through social engineering.
* **Reuse of Stolen Credentials**:
  * Credential stuffing attacks using previously leaked credentials.
  * Password spraying attacks to identify weak or commonly used passwords.
* **Exploitation of Trusted Relationships**:
  * Leveraging credentials from third-party vendors or contractors to access target networks.
* **Account Manipulation**:
  * Modifying user account permissions to maintain persistence or elevate privileges.
  * Creating additional valid accounts to ensure continued access.

Real-world procedures attackers commonly employ include:

* Remote Desktop Protocol (RDP) or Secure Shell (SSH) logins with valid credentials.
* Web application logins using stolen credentials to access sensitive data.
* Leveraging VPN access with compromised credentials to infiltrate internal networks.
* Use of cloud service credentials to access cloud infrastructure and applications (e.g., AWS, Azure, Google Cloud).

## When this Technique is Usually Used

Attackers utilize the Valid Accounts technique across various attack scenarios and stages, including:

* **Initial Access**:
  * Gaining initial foothold through stolen user credentials obtained via phishing or credential reuse.
* **Persistence**:
  * Maintaining long-term access by periodically logging into compromised accounts.
  * Creating new accounts or modifying existing accounts to ensure continued access after initial compromise.
* **Privilege Escalation**:
  * Using valid administrative or privileged credentials to escalate privileges within the environment.
* **Defense Evasion**:
  * Avoiding detection by blending malicious activities with legitimate user account activities.
* **Lateral Movement**:
  * Using valid credentials to access additional systems across the network, expanding the scope of compromise.
* **Exfiltration**:
  * Leveraging valid accounts to access sensitive data repositories and facilitate data extraction.

## How this Technique is Usually Detected

Detection of the Valid Accounts technique typically involves monitoring and analyzing authentication logs, user behavior analytics, and activity patterns. Effective detection methods and tools include:

* **Behavioral Analysis**:
  * Identifying anomalous login times, locations, or patterns inconsistent with normal user behavior.
  * Detecting unusual volume or frequency of login attempts.
* **Monitoring Authentication Logs**:
  * Reviewing logs for suspicious login failures followed by successful logins.
  * Detecting logins from unusual IP addresses or geographic locations.
* **Endpoint Detection and Response (EDR)**:
  * Monitoring endpoint activities for signs of credential dumping tools (e.g., Mimikatz, ProcDump).
  * Detecting suspicious processes accessing credential stores.
* **Network Traffic Analysis**:
  * Identifying abnormal traffic patterns indicative of lateral movement using valid credentials.
  * Detecting unusual remote access protocols or VPN sessions.
* **Multi-Factor Authentication (MFA) Monitoring**:
  * Tracking failed MFA attempts or unusual MFA bypass scenarios.

Specific Indicators of Compromise (IoCs) include:

* Unusual login times or locations (e.g., logins from geographically distant locations within short periods).
* Repeated login failures followed by successful logins.
* Presence of credential dumping tools or scripts on endpoints.
* Sudden changes to account permissions or creation of new user accounts.
* Anomalous VPN or remote desktop connections outside typical user behavior.

## Why it is Important to Detect This Technique

Timely detection of the Valid Accounts technique is critical due to the significant potential impacts on organizational systems and networks, including:

* **Data Breach and Exfiltration**:
  * Attackers gaining access to sensitive information, intellectual property, or personal data.
  * Financial and reputational damage resulting from unauthorized disclosure.
* **Privilege Escalation**:
  * Attackers escalating privileges to administrative levels, enabling further compromise of critical systems and infrastructure.
* **Persistence and Lateral Movement**:
  * Attackers maintaining long-term, undetected access, allowing continuous reconnaissance and exploitation of network resources.
* **Operational Disruption**:
  * Potential sabotage or disruption of critical business operations through unauthorized access to key systems or infrastructure.
* **Compliance and Regulatory Implications**:
  * Failure to detect unauthorized access may lead to violations of regulatory standards (e.g., GDPR, HIPAA, PCI DSS), resulting in fines and legal consequences.

Early detection is essential to:

* Minimize damage and limit the scope of compromise.
* Quickly contain and remediate incidents.
* Reduce financial, operational, and reputational risks associated with prolonged unauthorized access.

## Examples

Real-world examples illustrating the Valid Accounts technique include:

1. **APT29 (Cozy Bear) Attacks**:
   * **Attack Scenario**: Leveraged stolen user credentials obtained through phishing and credential harvesting to infiltrate government and private sector organizations.
   * **Tools Used**: Spear-phishing emails, credential harvesting websites, legitimate VPN and remote desktop connections.
   * **Impacts**: Extensive espionage operations, theft of sensitive government and corporate information, prolonged undetected access within targeted networks.
2. **Colonial Pipeline Attack (DarkSide Ransomware)**:
   * **Attack Scenario**: Attackers gained initial access via compromised VPN credentials obtained from leaked credentials on dark web forums.
   * **Tools Used**: VPN access using valid credentials, ransomware deployment tools.
   * **Impacts**: Major operational disruption, temporary shutdown of fuel distribution, significant financial and reputational damage.
3. **Uber Data Breach (2016)**:
   * **Attack Scenario**: Attackers utilized compromised cloud infrastructure credentials obtained through credential stuffing attacks.
   * **Tools Used**: Credential stuffing scripts, cloud service (AWS) access using valid credentials.
   * **Impacts**: Exposure of personal data for millions of users and drivers, regulatory investigations, substantial financial penalties and reputational harm.
4. **SolarWinds Supply Chain Attack**:
   * **Attack Scenario**: Attackers leveraged stolen credentials to access internal development environments and inject malicious code into software updates.
   * **Tools Used**: Valid administrative credentials, access to software build environments, sophisticated malware implants.
   * **Impacts**: Compromise of multiple government agencies and private sector organizations, significant national security implications, widespread operational and reputational damage.
