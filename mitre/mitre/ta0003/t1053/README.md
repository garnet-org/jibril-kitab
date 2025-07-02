---
description: Scheduled Task/Job [T1053]
icon: lock
---

# Scheduled Task/Job

## Information

* Name: Scheduled Task/Job
* ID: T1053
* Tactics: [TA0002](../../ta0002/), [TA0003](../), [TA0004](../../ta0004/)
* Sub-Technique: [T1053.005](t1053.005.md), [T1053.007](t1053.007.md), [T1053.003](t1053.003.md), T1053.001, T1053.004, [T1053.006](t1053.006.md), [T1053.002](t1053.002.md)

## Introduction

Scheduled Task/Job (T1053) is a widely recognized execution technique within the MITRE ATT\&CK framework. Attackers leverage scheduled tasks or jobs within operating systems to execute malicious code at specific times or intervals. Such tasks can be configured using built-in utilities like Task Scheduler on Windows, cron jobs on Linux/Unix systems, or launchd on macOS. Due to their legitimate administrative nature, scheduled tasks/jobs offer attackers a stealthy mechanism for persistence, privilege escalation, and lateral movement, making them a critical element for defenders to monitor and detect.

## Deep Dive Into Technique

Scheduled tasks/jobs allow attackers to automate the execution of malicious payloads or scripts without manual intervention. Attackers commonly exploit native scheduling utilities available across operating systems:

* **Windows Task Scheduler**:
  * Commands typically used:
    * `schtasks.exe`
    * PowerShell cmdlets (`New-ScheduledTask`, `Register-ScheduledTask`)
  * Tasks can be configured to execute binaries, scripts, or commands at system startup, user logon, or at specific intervals.
  * Tasks are stored in `%SystemRoot%\System32\Tasks` or registry locations (`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache`).
* **Linux/Unix Cron Jobs**:
  * Cron jobs are managed through crontab files (`/etc/crontab`, `/etc/cron.*`, or user-specific crontabs).
  * Attackers often insert malicious scripts or binaries into cron directories or user crontabs to execute periodically or at reboot.
  * Commands used:
    * `crontab -e`
    * Direct editing of cron files (`/etc/cron.d/`, `/var/spool/cron/`)
* **macOS Launchd**:
  * Uses Launch Agents (`~/Library/LaunchAgents`) and Launch Daemons (`/Library/LaunchDaemons`, `/System/Library/LaunchDaemons`) to schedule tasks.
  * Attackers create malicious `.plist` files specifying commands or scripts to execute at regular intervals or on system events.
  * Commands typically used:
    * `launchctl load`
    * `launchctl start`

Attackers may leverage scheduled tasks/jobs to:

* Establish and maintain persistence on compromised systems.
* Escalate privileges by scheduling tasks to run with higher privileges.
* Move laterally by scheduling tasks remotely on other systems within the network.
* Automate data exfiltration or command-and-control (C2) communications.

## When this Technique is Usually Used

Scheduled Task/Job usage spans multiple stages within the cyber kill chain and various attack scenarios, including:

* **Persistence**:
  * Attackers commonly schedule tasks to maintain long-term access to compromised systems, ensuring malicious payloads execute after reboots or user logins.
* **Privilege Escalation**:
  * Tasks configured to run as SYSTEM or root can elevate attacker privileges, allowing greater control over systems and networks.
* **Execution**:
  * Automated execution of payloads or scripts at specific intervals, reducing manual intervention and increasing stealth.
* **Lateral Movement**:
  * Attackers schedule tasks remotely on target machines within the network, facilitating lateral movement and further compromise.
* **Data Exfiltration**:
  * Automated data collection and exfiltration tasks run periodically, reducing attacker exposure and enhancing stealth.
* **Command and Control (C2)**:
  * Scheduled tasks periodically beacon to attacker-controlled servers, enabling sustained communication and remote control.

## How this Technique is Usually Detected

Detection of malicious scheduled tasks/jobs involves monitoring, auditing, and analyzing various system artifacts and behaviors:

* **Windows Detection Methods**:
  * Monitor creation or modification of tasks via Windows Event Logs:
    * Event ID 4698 (Scheduled Task created)
    * Event ID 4702 (Scheduled Task updated)
  * Inspect Task Scheduler libraries and registry locations:
    * `%SystemRoot%\System32\Tasks`
    * Registry keys under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache`
  * Use Endpoint Detection and Response (EDR) tools to alert on suspicious `schtasks.exe` executions or unusual PowerShell cmdlets.
* **Linux/Unix Detection Methods**:
  * Audit cron-related file modifications:
    * Monitor `/etc/crontab`, `/etc/cron.*`, `/var/spool/cron/`
  * Utilize file integrity monitoring tools (e.g., AIDE, Tripwire) to detect unauthorized cron file changes.
  * Review system logs (`/var/log/cron`, `/var/log/syslog`) for suspicious cron job creations or executions.
* **macOS Detection Methods**:
  * Monitor Launch Agent/Daemon directories for suspicious `.plist` files:
    * `/Library/LaunchDaemons`
    * `/Library/LaunchAgents`
    * `~/Library/LaunchAgents`
  * Use endpoint monitoring solutions to detect `launchctl` command usage and suspicious file creations.
* **General Indicators of Compromise (IoCs)**:
  * Unrecognized or unusual scheduled tasks/jobs executing binaries/scripts from temporary directories or user profiles.
  * Tasks configured to run with elevated privileges or at unusual intervals.
  * Scheduled tasks calling scripts or binaries with obfuscated or encoded commands.
  * Tasks performing network connections to unknown external IP addresses or domains.

## Why it is Important to Detect This Technique

Early detection of malicious scheduled tasks/jobs is vital due to their significant impact on system security and integrity. Undetected scheduled tasks can lead to:

* **Persistent Compromise**:
  * Attackers maintain long-term access, enabling continuous exploitation and data exfiltration.
* **Privilege Escalation**:
  * Malicious tasks running with elevated privileges can compromise entire systems or networks.
* **Stealthy Operations**:
  * Automated execution reduces attacker exposure, making detection and attribution more challenging.
* **Data Exfiltration and Espionage**:
  * Scheduled tasks can automate sensitive data extraction, causing severe data breaches and privacy violations.
* **Lateral Movement and Network Compromise**:
  * Attackers leverage scheduled tasks for lateral movement, expanding their foothold across the network.

Early detection and mitigation minimize the risk of prolonged compromise, reduce potential data loss, and limit the overall damage to organizational assets, reputation, and operations.

## Examples

Real-world examples of Scheduled Task/Job exploitation illustrate the technique's prevalence and impact:

* **APT29 (Cozy Bear)**:
  * Utilized scheduled tasks for persistence and lateral movement during the SolarWinds supply chain attack.
  * Scheduled tasks executed malicious payloads and PowerShell scripts for C2 communications and data exfiltration.
  * Impact: Compromise of multiple high-profile organizations, government entities, and significant data breaches.
* **FIN7 Cybercrime Group**:
  * Employed scheduled tasks to establish persistence and automate execution of custom malware tools (e.g., Carbanak, Cobalt Strike payloads).
  * Attackers scheduled tasks to run malicious scripts periodically, facilitating ongoing data theft and financial fraud.
  * Impact: Millions of dollars stolen from financial institutions, hospitality organizations, and retail companies.
* **TrickBot Malware**:
  * Commonly schedules tasks to maintain persistence and execute malicious payloads after system reboot or user logon.
  * Tasks typically execute scripts or binaries stored in hidden directories or temporary folders.
  * Impact: Credential theft, ransomware deployment (e.g., Ryuk, Conti), and significant operational disruptions.
* **WannaCry Ransomware**:
  * Scheduled tasks used to propagate ransomware payloads and execute encryption routines on compromised systems.
  * Tasks executed malicious binaries periodically, escalating the impact and spread of ransomware attacks.
  * Impact: Global ransomware outbreak causing billions in financial losses and operational disruptions.

These examples demonstrate the critical importance of monitoring scheduled tasks/jobs, highlighting their role in significant cyber incidents, high-impact breaches, and persistent threats.
