---
description: Boot or Logon Initialization Scripts [T1037]
icon: boot
---

# Boot or Logon Initialization Scripts

## Information

* Name: Boot or Logon Initialization Scripts
* ID: T1037
* Tactics: [TA0003](../), [TA0004](../../ta0004/)
* Sub-Technique: [T1037.002](t1037.002.md), [T1037.005](t1037.005.md), [T1037.003](t1037.003.md), [T1037.004](t1037.004.md), [T1037.001](t1037.001.md)

## Introduction

Boot or Logon Initialization Scripts is a persistence technique categorized under MITRE ATT\&CK (Technique ID: T1037). Attackers leverage scripts that automatically execute during system boot or user logon to maintain persistence, escalate privileges, or execute malicious payloads. These scripts typically run with elevated privileges, making them attractive targets for adversaries seeking long-term footholds within compromised environments.

## Deep Dive Into Technique

Attackers exploit Boot or Logon Initialization Scripts by inserting malicious code into legitimate startup processes. Common scripts include:

* **Windows Environments**:
  * **Group Policy Objects (GPO)**:
    * Attackers inject malicious scripts into startup or logon scripts managed by Active Directory Group Policy.
    *   Scripts stored in:

        ```
        \\<domain>\SYSVOL\<domain>\Policies\<GUID>\MACHINE\Scripts\Startup\
        \\<domain>\SYSVOL\<domain>\Policies\<GUID>\USER\Scripts\Logon\
        ```
  * **Local Group Policy Editor**:
    * Malicious scripts placed directly on endpoints via Local Group Policy Editor (`gpedit.msc`).
  * **Registry Keys**:
    *   Attackers utilize registry keys to configure startup scripts:

        ```
        HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
        HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
        ```
  * **Scheduled Tasks**:
    *   Scripts configured as scheduled tasks to trigger at boot or logon, often via:

        ```
        schtasks.exe /create /sc onlogon /tn "TaskName" /tr "MaliciousScript.bat"
        ```
* **Linux/Unix Environments**:
  * **Init Scripts**:
    * Scripts placed in `/etc/init.d/` or `/etc/rc.d/` directories.
  * **Systemd Services**:
    * Malicious `.service` files placed within `/etc/systemd/system/` or `/usr/lib/systemd/system/`.
  * **User Profile Scripts**:
    * Modifying `.bashrc`, `.bash_profile`, `.profile`, or similar files within user home directories.

Attackers frequently use scripting languages such as PowerShell, batch scripts, VBScript, Bash, Python, and Perl. These scripts enable attackers to execute arbitrary commands, download additional payloads, establish reverse shells, or escalate privileges.

## When this Technique is Usually Used

Attackers commonly utilize Boot or Logon Initialization Scripts during multiple stages of the attack lifecycle, including:

* **Persistence**:
  * Establishing continuous access to compromised systems even after reboot or user logoff.
* **Privilege Escalation**:
  * Leveraging scripts that execute with elevated privileges to escalate attacker permissions.
* **Defense Evasion**:
  * Leveraging legitimate system processes and scripts to evade detection by blending malicious activity with normal system behaviors.
* **Execution**:
  * Automatically executing payloads or commands upon system startup or user logon without manual intervention.

Specific scenarios include:

* Post-exploitation phase to maintain long-term access.
* Advanced Persistent Threat (APT) campaigns targeting enterprises.
* Insider threats embedding malicious scripts within administrative scripts or scheduled tasks.
* Malware campaigns leveraging boot scripts to ensure consistent execution.

## How this Technique is Usually Detected

Detection of malicious Boot or Logon Initialization Scripts involves monitoring system behaviors, analyzing script contents, and tracking configuration changes. Effective detection methods include:

* **File Integrity Monitoring (FIM)**:
  * Monitoring critical directories and files for unauthorized modifications, including:
    * Windows:
      * `%SystemRoot%\System32\GroupPolicy\Machine\Scripts\`
      * `%SystemRoot%\System32\GroupPolicy\User\Scripts\`
      * `%SystemRoot%\SYSVOL\domain\Policies\`
    * Linux:
      * `/etc/init.d/`
      * `/etc/rc.d/`
      * `/etc/systemd/system/`
      * User home directories (e.g., `.bashrc`, `.profile`)
* **Registry Monitoring**:
  *   Monitoring registry keys related to startup scripts, such as:

      ```
      HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\
      HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\
      ```
* **Log Analysis and Auditing**:
  * Analyzing Windows Event Logs, especially events related to Group Policy changes (Event IDs: 5136, 5137, 5138, 5139, 5141).
  * Reviewing audit logs for suspicious script executions and scheduled task creations.
* **Endpoint Detection and Response (EDR) Tools**:
  * Detecting anomalous script executions, command-line parameters, and suspicious parent-child process relationships.
* **Behavioral Analytics and SIEM Solutions**:
  * Correlating multiple events and behaviors indicating malicious persistence mechanisms.

Indicators of Compromise (IoCs):

* Unrecognized scripts in startup directories or user profiles.
* Scheduled tasks created with suspicious parameters.
* Registry keys referencing unknown scripts or executables.
* Unusual outbound connections initiated by scripts at boot or logon.

## Why it is Important to Detect This Technique

Detecting malicious Boot or Logon Initialization Scripts is crucial due to significant potential impacts, including:

* **Persistence of Threat Actors**:
  * Attackers maintain long-term access, enabling continuous data exfiltration, reconnaissance, or lateral movement.
* **Privilege Escalation Risks**:
  * Scripts often run with elevated privileges, allowing attackers to escalate permissions and gain administrative control.
* **Stealth and Evasion**:
  * Malicious scripts embedded within legitimate startup processes can evade detection, prolonging attacker presence.
* **Operational Disruption**:
  * Malicious scripts may degrade system performance, alter system configurations, or cause service disruptions.
* **Data Exfiltration and Espionage**:
  * Persistent scripts facilitate continuous data theft, intellectual property compromise, or espionage activities.

Early detection and mitigation significantly reduce attacker dwell time, limit damage, and prevent further exploitation within networks and systems.

## Examples

Real-world examples of Boot or Logon Initialization Scripts being exploited include:

* **FIN7 Group**:
  * Leveraged Group Policy Objects (GPO) startup scripts to deploy malicious payloads across compromised Windows domains.
  * Attackers placed malicious scripts within the SYSVOL share, enabling automated execution on domain-connected endpoints.
* **APT29 (Cozy Bear)**:
  * Utilized scheduled tasks and registry-based logon scripts for persistence in targeted networks.
  * Scripts executed PowerShell commands to download and execute additional payloads, enabling espionage and data theft.
* **TrickBot Malware**:
  * Employed scheduled tasks and registry keys to execute persistence scripts at system startup, ensuring continuous malware execution and command-and-control (C2) communication.
* **Carbanak Group**:
  * Leveraged malicious startup scripts and scheduled tasks within financial institutions to maintain persistence, escalate privileges, and facilitate lateral movement.
* **Operation Cloud Hopper (APT10)**:
  * Used malicious Linux init scripts and systemd services to maintain persistence on compromised cloud infrastructure and managed service providers (MSPs).

Common tools and scripts observed:

* PowerShell scripts executing encoded commands or downloading payloads.
* Batch scripts (`.bat`, `.cmd`) configuring scheduled tasks or registry keys.
* VBScript (`.vbs`) and JavaScript (`.js`) scripts embedded within user logon scripts.
* Linux Bash scripts placed within `/etc/init.d/` or systemd service files executing reverse shells or downloading secondary payloads.

Impacts observed in these scenarios include:

* Persistent attacker access and prolonged data exfiltration.
* Privilege escalation and administrative control over compromised environments.
* Significant financial losses and reputational damage for targeted organizations.
* Operational disruptions, service outages, and reduced productivity due to malicious script activities.
