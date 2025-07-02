---
description: Boot or Logon Autostart Execution [T1547]
icon: boot
---

# Boot or Logon Autostart Execution

## Information

* Name: Boot or Logon Autostart Execution
* ID: T1547
* Tactics: [TA0003](../../ta0003/), [TA0004](../)
* Sub-Technique: [T1547.014](t1547.014.md), [T1547.012](../../../TA0004/T1547.012.md), [T1547.010](t1547.010.md), [T1547.009](t1547.009.md), [T1547.005](t1547.005.md), [T1547.003](t1547.003.md), [T1547.011](t1547.011.md), [T1547.004](t1547.004.md), [T1547.015](t1547.015.md), [T1547.001](t1547.001.md), [T1547.006](t1547.006.md), [T1547.002](t1547.002.md), [T1547.013](t1547.013.md), [T1547.007](t1547.007.md), [T1547.008](t1547.008.md)

## Introduction

Boot or Logon Autostart Execution is a persistence technique classified under MITRE ATT\&CK Technique ID T1547. It involves adversaries configuring malicious programs or scripts to automatically execute during system boot-up or user logon processes. This approach ensures persistence, allowing attackers to maintain system access even after system restarts or user logouts. Attackers leverage built-in operating system features or third-party software mechanisms to achieve this persistent execution.

## Deep Dive Into Technique

Attackers commonly utilize multiple built-in operating system mechanisms and third-party software to achieve Boot or Logon Autostart Execution. The following technical methods are widely employed by adversaries:

* **Registry Run Keys / Startup Folder (Windows):**
  * Attackers place malicious executables or scripts in Windows registry keys such as:
    * `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
    * `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  * Malicious payloads placed in the Windows Startup folder:
    * `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
    * `%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup`
* **Scheduled Tasks (Windows):**
  * Attackers create scheduled tasks configured to run at system boot or user logon using the Windows Task Scheduler.
  *   Example command to create a malicious task:

      ```
      schtasks /create /sc onlogon /tn "malicious_task" /tr "C:\malicious.exe"
      ```
* **Startup Items and LaunchAgents/LaunchDaemons (macOS):**
  * Attackers exploit macOS startup mechanisms such as LaunchAgents and LaunchDaemons located in:
    * `/Library/LaunchAgents/`
    * `/Library/LaunchDaemons/`
    * `~/Library/LaunchAgents/`
* **Linux Cron Jobs and Init Scripts:**
  * Attackers place malicious scripts or executables in Linux system directories or user cron jobs:
    * `/etc/init.d/`
    * `/etc/rc.local`
    * User cron tabs (`crontab -e`)
* **Bootkits and Rootkits:**
  * Advanced attackers may install bootkits or rootkits that execute prior to the operating system loading, making detection and removal significantly more difficult.
* **Modification of System Initialization Files:**
  * Attackers alter system initialization files such as Windows Boot Configuration Data (BCD), Linux GRUB configuration, or macOS boot files to execute malicious payloads during boot.

## When this Technique is Usually Used

Attackers typically employ Boot or Logon Autostart Execution during the persistence stage of the cyber kill chain. This technique is commonly observed in various attack scenarios, including:

* **Initial compromise:**
  * After gaining initial access, attackers quickly establish persistence to maintain access.
* **Privilege escalation:**
  * Attackers leverage elevated privileges to embed persistent backdoors or malicious scripts.
* **Lateral movement:**
  * Attackers establish persistence on multiple systems within the network to ensure ongoing access even if one system is compromised or remediated.
* **Long-term espionage campaigns:**
  * Advanced Persistent Threat (APT) groups utilize this technique extensively to maintain covert access over extended periods.
* **Ransomware and malware infections:**
  * Malware authors frequently use autostart execution to ensure ransomware or malware executes after reboots or logoffs.

## How this Technique is Usually Detected

Detection of Boot or Logon Autostart Execution involves various methods, tools, and indicators of compromise (IoCs):

* **Endpoint Detection and Response (EDR) Tools:**
  * EDR solutions monitor system events, registry changes, scheduled tasks, and startup folder modifications in real-time.
* **Log Analysis and Monitoring:**
  * Regular monitoring and analysis of Windows Event Logs, Sysmon logs, and audit logs for suspicious registry modifications, file creations, and scheduled task creations.
* **File Integrity Monitoring (FIM):**
  * Tools like Tripwire or OSSEC detect unauthorized changes to critical system files, configuration files, and startup directories.
* **Registry Monitoring:**
  * Monitor registry keys associated with autostart locations for unauthorized modifications using tools like Autoruns, Sysinternals Suite, or custom scripts.
* **Behavioral Analysis and Anomaly Detection:**
  * Behavioral detection systems identify unusual startup behaviors, malicious scheduled task creations, or abnormal boot processes.
* **Threat Hunting:**
  * Proactive threat hunting activities identify suspicious startup scripts, executables, and scheduled tasks through manual inspection or automated hunting queries.
* **Indicators of Compromise (IoCs):**
  * Suspicious executables/scripts placed in startup directories.
  * Unfamiliar scheduled tasks or cron jobs.
  * Unauthorized modifications to registry keys.
  * Unusual entries in boot configuration files or initialization scripts.

## Why it is Important to Detect This Technique

Early detection of Boot or Logon Autostart Execution is crucial due to the following impacts and considerations:

* **Persistent Access:**
  * Attackers maintain long-term access to systems, enabling continuous data exfiltration, espionage, or repeated compromises.
* **Stealth and Evasion:**
  * Autostart mechanisms often evade detection by standard antivirus tools, allowing attackers to remain undetected for extended periods.
* **Privilege Escalation:**
  * Attackers may leverage autostart mechanisms to elevate privileges or maintain administrative access.
* **Data Theft and Exfiltration:**
  * Persistent malware can continuously steal sensitive information, intellectual property, or credentials.
* **System Stability and Integrity:**
  * Malicious persistent scripts or executables can degrade system performance, stability, and reliability over time.
* **Increased Remediation Complexity:**
  * Persistent threats embedded in boot or startup processes are significantly more challenging and resource-intensive to remediate.
* **Compliance and Regulatory Risks:**
  * Undetected persistent threats pose significant compliance, regulatory, and reputational risks to organizations.
* **Facilitation of Further Attacks:**
  * Persistent access provides a foothold for attackers to conduct lateral movement, privilege escalation, and further exploitation within the network.

## Examples

Real-world examples illustrating the use of Boot or Logon Autostart Execution:

* **TrickBot Malware:**
  * TrickBot leverages Windows scheduled tasks and registry run keys to maintain persistence, allowing it to survive system reboots and continue stealing credentials and banking information.
* **APT29 (Cozy Bear):**
  * APT29 uses registry Run keys and scheduled tasks extensively to maintain persistent access during espionage campaigns targeting government and enterprise networks.
* **NotPetya Ransomware:**
  * NotPetya creates scheduled tasks and modifies registry keys to ensure ransomware payload executes upon reboot, causing rapid and widespread damage.
* **Emotet Malware:**
  * Emotet leverages Windows registry keys and scheduled tasks to maintain persistent access, enabling further malware deployment and lateral movement within networks.
* **OSX/Shlayer Malware (macOS):**
  * OSX/Shlayer malware utilizes LaunchAgents and LaunchDaemons to persistently execute malicious payloads on macOS systems, leading to adware and potentially unwanted software installations.
* **CronRAT (Linux):**
  * CronRAT malware hides malicious payloads in Linux cron jobs scheduled to execute at unconventional times, ensuring stealthy persistent access to compromised web servers.

These examples demonstrate the widespread adoption of Boot or Logon Autostart Execution across diverse threat actors, malware families, and operating systems, underscoring the importance of detecting and mitigating this persistence technique.
