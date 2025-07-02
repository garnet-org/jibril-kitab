---
description: Create or Modify System Process [T1543]
icon: lock
---

# Create or Modify System Process

## Information

* Name: Create or Modify System Process
* ID: T1543
* Tactics: [TA0003](../), [TA0004](../../ta0004/)
* Sub-Technique: [T1543.003](t1543.003.md), [T1543.004](t1543.004.md), [T1543.005](t1543.005.md), [T1543.001](t1543.001.md), [T1543.002](t1543.002.md)

## Introduction

"Create or Modify System Process" is categorized under the MITRE ATT\&CK framework as a technique (ID: T1543) within the "Persistence" and "Privilege Escalation" tactics. Attackers leverage this technique to create or alter system-level processes or services, enabling persistent and elevated access to compromised systems. By manipulating legitimate system processes, adversaries can effectively conceal their activities, maintain long-term footholds, and escalate privileges within targeted environments.

## Deep Dive Into Technique

Attackers employing the "Create or Modify System Process" technique typically manipulate legitimate operating system components to establish persistence or escalate privileges. Technical execution methods include:

* **Windows Systems:**
  * Creation or modification of Windows services using tools like `sc.exe`, PowerShell cmdlets (`New-Service`, `Set-Service`), or direct registry edits.
  * Manipulation of scheduled tasks via Task Scheduler (`schtasks.exe`) to execute malicious payloads periodically.
  * Modification of system binaries or DLL files, such as those located in `%SystemRoot%\System32`, to inject malicious code or redirect legitimate processes to malicious payloads.
  * Abuse of Windows Management Instrumentation (WMI) to create persistent event consumers and filters.
* **Unix/Linux Systems:**
  * Creation or modification of systemd services by placing malicious unit files in `/etc/systemd/system/`.
  * Modification of init scripts (`/etc/init.d/`) or cron jobs (`/etc/crontab`, `/etc/cron.*`) for persistent execution.
  * Replacement or alteration of legitimate system binaries in standard system paths (e.g., `/bin`, `/usr/bin`) with malicious counterparts.
  * Leveraging dynamic linker configurations (`ld.so.preload`) to inject malicious shared libraries into legitimate processes.

Real-world procedures often involve attackers initially gaining administrative or root-level privileges to effectively modify system processes. Once established, attackers use these compromised processes for continuous access, data exfiltration, lateral movement, or further exploitation activities.

## When this Technique is Usually Used

This technique commonly appears across multiple attack scenarios and stages, including:

* **Persistence Stage:**
  * Attackers establish long-term presence by embedding malicious processes or services that automatically execute at system startup or at regular intervals.
  * Ensuring continued access even after system reboots or administrator interventions.
* **Privilege Escalation Stage:**
  * Attackers manipulate system processes running with elevated privileges to escalate their own privileges on the compromised host.
  * Exploiting misconfigured permissions or vulnerabilities in system binaries to achieve administrative or root-level access.
* **Defense Evasion Stage:**
  * Modifying legitimate system processes allows attackers to blend malicious activities with normal system operations, reducing suspicion and detection likelihood.
  * Camouflaging malicious code within trusted processes or services.

## How this Technique is Usually Detected

Detection methods and indicators of compromise (IoCs) for this technique include:

* **System Integrity Monitoring:**
  * File integrity monitoring (FIM) tools (e.g., Tripwire, OSSEC) detecting unauthorized changes to critical system binaries or configuration files.
  * Regular comparison of system binaries and configuration files against known-good baselines or hash databases.
* **Endpoint Detection and Response (EDR) Tools:**
  * Monitoring process creation events and service registrations to detect abnormal or unauthorized system process creation.
  * Behavioral analytics detecting unusual parent-child process relationships, unexpected DLL injections, or suspicious command-line parameters.
* **Event Log Analysis:**
  * Windows Event Logs (e.g., Event ID 7045 for service creation, Event IDs 4697, 4698 for scheduled tasks) indicating unauthorized or unexpected service/task creation.
  * Linux audit logs (`auditd`) capturing system calls related to file modifications, service creation, or cron job alterations.
* **Specific Indicators of Compromise (IoCs):**
  * Unrecognized or suspicious services/processes running persistently.
  * Newly created or modified system files with unusual timestamps or file permissions.
  * Presence of unusual scheduled tasks or cron jobs executing unknown scripts or binaries.
  * Altered registry keys related to service definitions (e.g., `HKLM\SYSTEM\CurrentControlSet\Services\`).

## Why it is Important to Detect This Technique

Early detection of the "Create or Modify System Process" technique is critical due to its significant potential impacts:

* **Persistence and Long-Term Access:**
  * Attackers establishing persistent footholds can repeatedly compromise systems, exfiltrate sensitive data, and maintain continuous unauthorized access.
* **Privilege Escalation:**
  * Manipulating system processes enables attackers to elevate privileges, granting them unrestricted access and control over critical system resources.
* **Data Exfiltration and Espionage:**
  * Persistent malicious processes facilitate sustained data exfiltration activities, potentially leading to significant data breaches or intellectual property theft.
* **System Stability and Integrity:**
  * Unauthorized modification of critical system processes can degrade system stability, performance, or cause unexpected downtime or disruptions.
* **Defense Evasion and Detection Difficulty:**
  * Attackers leveraging legitimate system processes complicate detection and attribution efforts, increasing the complexity and cost of incident response and remediation.

Detecting this technique early limits attackers' capabilities, reduces potential damage, and enables prompt containment and remediation.

## Examples

Real-world incidents involving the "Create or Modify System Process" technique include:

* **NotPetya Ransomware Attack (2017):**
  * Attackers modified legitimate Windows binaries and services (e.g., using compromised "MeDoc" software updates) to execute destructive payloads.
  * Impact: Significant global disruption, billions of dollars in damages, and widespread operational outages.
* **APT29 ("Cozy Bear") Operations:**
  * Utilized persistent WMI event subscriptions and scheduled tasks to maintain long-term access and evade detection.
  * Impact: Sustained espionage activities, theft of sensitive government and organizational data.
* **Turla Group Attacks:**
  * Created malicious systemd services on Linux systems to maintain persistence and execute espionage tools.
  * Impact: Long-term espionage campaigns targeting government and diplomatic entities, enabling continuous data exfiltration.
* **Operation Cloud Hopper (APT10):**
  * Attackers leveraged scheduled tasks and modified system services to establish persistent backdoors in managed service provider (MSP) environments.
  * Impact: Extensive data breaches across multiple global enterprises, intellectual property theft, and compromised supply chain security.

These examples highlight the diverse scenarios, tools, and impacts associated with the "Create or Modify System Process" technique, emphasizing the importance of proactive detection and mitigation strategies.
