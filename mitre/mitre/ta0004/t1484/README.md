---
description: Domain or Group Policy Modification [T1484]
icon: globe
---

# Domain or Tenant Policy Modification

## Information

* Name: Domain or Tenant Policy Modification
* ID: T1484
* Tactics: [TA0005](../../ta0005/), [TA0004](../)
* Sub-Technique: [T1484.002](t1484.002.md), [T1484.001](t1484.001.md)

## Introduction

Domain or Group Policy Modification (Technique ID: T1484) is categorized under the MITRE ATT\&CK framework as a persistence, privilege escalation, and defense evasion technique. Attackers manipulate domain or local group policies (GPOs) to modify security settings, deploy malicious payloads, or weaken the overall security posture of a network environment. This technique allows attackers to maintain persistent access, escalate privileges, and evade detection by leveraging legitimate management functionalities inherent in Windows environments.

## Deep Dive Into Technique

Attackers exploiting Domain or Group Policy Modification typically leverage legitimate administrative tools and interfaces such as Group Policy Management Console (GPMC), PowerShell cmdlets, or direct Active Directory (AD) manipulation. The key technical aspects include:

* **Group Policy Objects (GPOs)**: GPOs are collections of settings managed centrally through Active Directory. Attackers modify these objects to enforce malicious configurations across multiple systems simultaneously.
* **Administrative Templates (ADMX/ADM files)**: Attackers may alter or create custom administrative templates to push malicious settings or scripts.
* **Scheduled Tasks and Scripts**: Attackers may utilize GPOs to deploy malicious scripts, scheduled tasks, or startup/shutdown scripts to execute malware persistently.
* **Security Policies**: Modifying password policies, account lockout settings, audit policies, or user rights assignments to weaken defenses and facilitate further lateral movement or privilege escalation.
* **Registry Modifications**: Leveraging GPOs to make registry changes that disable security features, reduce logging, or hide malicious activities.

Typical execution methods include:

* Using built-in Windows tools such as `gpedit.msc`, `gpmc.msc`, or PowerShell (`Set-GPO`, `New-GPO`, and related cmdlets).
* Directly editing policy files stored in the SYSVOL share (`\\<Domain>\SYSVOL`) on domain controllers.
* Leveraging compromised administrative credentials to authenticate and modify policies remotely.

Real-world procedures often involve attackers first obtaining domain administrator privileges, after which they manipulate Group Policy settings to propagate malware, disable endpoint protections, or create backdoors.

## When this Technique is Usually Used

Attackers commonly utilize Domain or Group Policy Modification in the following scenarios and attack stages:

* **Persistence**: Establishing persistent footholds by deploying scripts or scheduled tasks that execute malware at system startup or user logon.
* **Privilege Escalation**: Modifying security policies to grant elevated privileges to compromised accounts or create new privileged accounts.
* **Defense Evasion**: Disabling security controls such as antivirus software, endpoint detection and response (EDR), Windows Defender, or logging/auditing mechanisms.
* **Lateral Movement**: Leveraging GPOs to deploy malware or scripts across multiple systems simultaneously within an Active Directory domain environment.
* **Credential Harvesting**: Adjusting policies to weaken authentication mechanisms, allowing easier credential theft or reuse.
* **Destructive Attacks**: Deploying ransomware or destructive payloads broadly across the organization via modified GPOs.

## How this Technique is Usually Detected

Detection of Domain or Group Policy Modification typically involves monitoring and auditing activities associated with Active Directory and Group Policy management. Effective detection methods include:

* **Monitoring Windows Event Logs**:
  * Security logs (Event IDs: 4662, 5136, 5137, 5138, 5139, and 5141) indicating modifications to Group Policy objects.
  * Directory Service Access logs tracking changes to SYSVOL shares and AD objects.
* **File Integrity Monitoring (FIM)**:
  * Monitoring changes to SYSVOL shares (`\\<Domain>\SYSVOL`) and policy files (`GPT.INI` and Group Policy templates).
* **Endpoint Detection and Response (EDR)**:
  * Alerting on suspicious processes or scripts executed through GPO-deployed scheduled tasks or startup scripts.
* **SIEM Solutions**:
  * Correlation rules to detect anomalous patterns, such as frequent policy changes, policy modifications outside maintenance windows, or unusual administrative behavior.
* **Baselining and Anomaly Detection**:
  * Establishing baseline configurations and detecting deviations from standard GPO settings.
* **Indicators of Compromise (IoCs)**:
  * Unexpected registry modifications (e.g., disabling antivirus or Windows Defender).
  * Unusual scheduled tasks or startup scripts deployed via GPO.
  * Presence of unknown administrative templates or scripts in SYSVOL.
  * Unrecognized privileged accounts or changes in security policies.

## Why it is Important to Detect This Technique

Detecting Domain or Group Policy Modification is critical due to its potential severe impacts on system and network security. The importance of early detection includes:

* **Prevention of Persistence**: Early detection prevents attackers from establishing persistent footholds that are difficult to eradicate.
* **Mitigation of Privilege Escalation**: Timely detection reduces the risk of attackers escalating privileges and gaining further control over sensitive resources.
* **Protection Against Mass Deployment of Malware**: Attackers leveraging GPOs can rapidly propagate malware or ransomware across enterprise environments. Early detection can limit or prevent widespread compromise.
* **Defense Against Security Control Disabling**: Attackers frequently disable antivirus, EDR, firewalls, or logging mechanisms through GPO modifications, leaving organizations blind to further malicious activities.
* **Protection of Sensitive Data**: Early detection prevents attackers from modifying policies that weaken authentication, encryption, or data protection mechanisms, potentially averting data breaches or exfiltration.
* **Reducing Incident Response Costs**: Early detection and containment significantly reduce remediation efforts, downtime, and financial losses associated with large-scale compromises.

## Examples

Real-world examples of Domain or Group Policy Modification include:

1. **NotPetya Ransomware Attack (2017)**:
   * **Scenario**: Attackers compromised domain controllers and modified GPOs to deploy ransomware payloads across entire enterprise environments rapidly.
   * **Tools Used**: Mimikatz (credential harvesting), PsExec, and modified malicious scripts deployed via GPO.
   * **Impact**: Massive operational disruptions, financial losses estimated in billions, and extensive downtime for affected organizations.
2. **Ryuk Ransomware Attacks**:
   * **Scenario**: Attackers utilized compromised domain admin credentials to modify GPOs, disabling antivirus and endpoint protection software before deploying ransomware.
   * **Tools Used**: PowerShell scripts, compromised credentials, and native Windows administrative tools.
   * **Impact**: Significant financial damages, prolonged downtime, and extensive data loss for multiple organizations.
3. **APT29 (Cozy Bear) Intrusions**:
   * **Scenario**: Persistent threat actors modified domain policies to weaken security settings, allowing easier lateral movement and persistent access.
   * **Tools Used**: Custom PowerShell scripts, compromised privileged credentials, built-in administrative tools.
   * **Impact**: Long-term espionage operations, persistent access to sensitive information, and compromised security posture.
4. **FIN7 Cybercrime Group**:
   * **Scenario**: Leveraged GPO modifications to deploy malicious scripts and scheduled tasks, enabling persistent access and lateral movement.
   * **Tools Used**: PowerShell Empire, Cobalt Strike, and native Windows administrative functionalities.
   * **Impact**: Financial theft, data breaches, and persistent compromise of targeted organizations.

These examples illustrate the diversity of threat actors and attack scenarios leveraging Domain or Group Policy Modification, highlighting the critical need for proactive detection and mitigation strategies.
