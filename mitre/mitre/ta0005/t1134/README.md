---
description: Access Token Manipulation [T1134]
icon: door-open
---

# Access Token Manipulation

## Information

* Name: Access Token Manipulation
* ID: T1134
* Tactics: [TA0005](../), [TA0004](../../ta0004/)
* Sub-Technique: [T1134.002](t1134.002.md), [T1134.001](t1134.001.md), [T1134.003](t1134.003.md), [T1134.004](t1134.004.md), [T1134.005](t1134.005.md)

## Introduction

Access Token Manipulation is categorized under MITRE ATT\&CK technique T1134, which attackers use to impersonate users or escalate privileges within a compromised environment. Attackers leverage tokens—security objects created by operating systems—to authenticate and authorize user actions. By stealing, generating, or manipulating these tokens, threat actors can execute processes under different user contexts, enabling lateral movement, privilege escalation, and persistence within compromised systems.

## Deep Dive Into Technique

Access Token Manipulation involves exploiting the way operating systems handle authentication tokens. Detailed technical insights include:

* **Token Types:**
  * **Primary Tokens:** Assigned to processes during user logon, defining user security context.
  * **Impersonation Tokens:** Allow threads to temporarily adopt the security context of another user or process.
* **Execution Methods:**
  * **Token Theft:** Attackers steal tokens from running processes using tools such as Mimikatz or Meterpreter.
  * **Token Impersonation:** Attackers impersonate users by duplicating tokens and assigning them to malicious processes.
  * **Token Creation:** Attackers generate new tokens with elevated privileges, often requiring administrative access.
* **Mechanisms:**
  * Windows APIs such as `DuplicateTokenEx`, `SetThreadToken`, and `ImpersonateLoggedOnUser` are commonly exploited.
  * Manipulation of token privileges (e.g., `SeDebugPrivilege`, `SeImpersonatePrivilege`) to escalate permissions.
* **Real-world Procedures:**
  * Attackers typically inject code into legitimate processes or spawn new processes using stolen tokens.
  * Exploitation of privileged processes (e.g., SYSTEM-level processes) to gain elevated privileges.
  * Usage of known exploits like RottenPotato or JuicyPotato to escalate privileges by token impersonation.

## When this Technique is Usually Used

Access Token Manipulation is commonly employed in various stages of a cyberattack lifecycle, including:

* **Privilege Escalation:**
  * After initial compromise, attackers use token manipulation to escalate from limited user privileges to administrative or SYSTEM-level privileges.
* **Lateral Movement:**
  * Attackers impersonate tokens of authenticated users to move laterally across networked systems without detection.
* **Persistence:**
  * Manipulated tokens can help attackers maintain long-term access within compromised environments by continuously impersonating legitimate users.
* **Credential Access:**
  * Attackers exploit tokens to authenticate to remote resources without needing plaintext credentials.
* **Defense Evasion:**
  * Manipulating tokens allows attackers to evade detection by blending malicious activities within legitimate user contexts.

## How this Technique is Usually Detected

Detection of Access Token Manipulation involves monitoring and analyzing system activities, authentication events, and suspicious behaviors:

* **Event Logs and Monitoring:**
  * Analyzing Windows Security Event Logs (e.g., Event ID 4624 for logon events, Event ID 4672 for special privileges assignment).
  * Monitoring process creation events and correlating them with unusual token privileges or impersonation activities.
* **Endpoint Detection and Response (EDR) Tools:**
  * Tools such as CrowdStrike Falcon, Carbon Black, Microsoft Defender for Endpoint, and SentinelOne can detect token manipulation through behavioral analysis and anomaly detection.
* **Monitoring API Calls:**
  * Monitoring suspicious API calls such as `DuplicateTokenEx`, `SetThreadToken`, or `ImpersonateLoggedOnUser` from unexpected processes or contexts.
* **Indicators of Compromise (IoCs):**
  * Unusual processes running under different user contexts.
  * Processes exhibiting abnormal privileges (e.g., SeDebugPrivilege, SeAssignPrimaryTokenPrivilege).
  * Presence of known token manipulation tools (Mimikatz, RottenPotato, JuicyPotato, Meterpreter) on endpoints.
  * Detection of code injection or process hollowing techniques associated with token manipulation.

## Why it is Important to Detect This Technique

Early detection of Access Token Manipulation is critical due to its significant impact on security and operational integrity:

* **Privilege Escalation:**
  * Allows attackers to escalate privileges rapidly, gaining administrative or SYSTEM-level control, which significantly increases the potential damage.
* **Lateral Movement:**
  * Enables attackers to move undetected across multiple systems, expanding the attack surface and potentially compromising sensitive data and critical infrastructure.
* **Persistence:**
  * Attackers can maintain persistent access, making remediation and eradication difficult and costly.
* **Credential Theft and Abuse:**
  * Attackers can bypass authentication mechanisms, leading to unauthorized access to sensitive resources and data breaches.
* **Detection Evasion:**
  * Attackers use legitimate user contexts to mask malicious activities, complicating detection, response, and forensic analysis.
* **Operational and Reputational Impact:**
  * Undetected token manipulation can lead to prolonged compromise, resulting in significant financial loss, regulatory penalties, and damage to organizational reputation.

## Examples

Real-world examples of Access Token Manipulation include:

* **APT29 (Cozy Bear):**
  * Utilized token impersonation techniques to escalate privileges and move laterally within targeted networks, notably during the SolarWinds supply chain attack.
  * Tools used: Cobalt Strike, Mimikatz, custom implants.
  * Impact: Persistent access, sensitive data exfiltration, significant damage to reputation and security posture.
* **FIN7 Group:**
  * Leveraged token impersonation and theft to escalate privileges and facilitate lateral movement within victim networks.
  * Tools used: Carbanak malware, Cobalt Strike, Meterpreter.
  * Impact: Large-scale financial fraud, theft of payment card data, significant monetary losses.
* **TrickBot Malware:**
  * Employed token manipulation techniques to escalate privileges, evade detection, and spread ransomware payloads such as Ryuk.
  * Tools used: TrickBot loader, PowerShell scripts, Mimikatz.
  * Impact: Ransomware deployment, operational disruption, financial loss, and data breaches.
* **WannaCry Ransomware:**
  * Exploited token manipulation techniques alongside EternalBlue exploit to escalate privileges and propagate rapidly across networks.
  * Tools used: EternalBlue exploit, custom ransomware payload.
  * Impact: Global disruption, significant financial and operational losses, widespread damage across multiple sectors.
* **RottenPotato and JuicyPotato Exploits:**
  * Privilege escalation exploits leveraging token impersonation vulnerabilities in Windows environments.
  * Tools used: RottenPotato, JuicyPotato.
  * Impact: Privilege escalation to SYSTEM-level, enabling attackers to compromise entire systems, gain persistence, and evade detection.
