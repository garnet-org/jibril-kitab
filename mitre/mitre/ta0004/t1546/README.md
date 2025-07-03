---
description: Event Triggered Execution [T1546]
icon: play
---

# Event Triggered Execution

## Information

* Name: Event Triggered Execution
* ID: T1546
* Tactics: [TA0004](../), [TA0003](../../ta0003/)
* Sub-Technique: [T1546.013](t1546.013.md), [T1546.006](t1546.006.md), [T1546.011](t1546.011.md), [T1546.005](t1546.005.md), [T1546.012](t1546.012.md), [T1546.008](t1546.008.md), [T1546.009](t1546.009.md), [T1546.003](t1546.003.md), [T1546.001](t1546.001.md), [T1546.014](t1546.014.md), [T1546.004](t1546.004.md), [T1546.015](t1546.015.md), [T1546.010](t1546.010.md), [T1546.002](t1546.002.md), [T1546.016](t1546.016.md), [T1546.017](t1546.017.md), [T1546.007](t1546.007.md)

## Introduction

Event Triggered Execution is categorized under the MITRE ATT\&CK framework as technique T1546, specifically under the Persistence tactic. Attackers leverage built-in system functionality to execute malicious payloads in response to specific events or conditions. Events triggering execution may include system startup, user logon, scheduled tasks, or hardware and software events. This technique allows adversaries to maintain persistence, escalate privileges, or evade detection by ensuring malware executes automatically under predefined circumstances.

## Deep Dive Into Technique

Event Triggered Execution involves configuring legitimate system features, tools, or mechanisms to trigger malicious commands or scripts based on specific events. Attackers commonly exploit the following mechanisms:

* **Scheduled Tasks/Jobs (T1053)**:
  * Windows Task Scheduler or Linux cron jobs.
  * Malicious scripts or commands scheduled to execute at specific intervals or system events.
* **Windows Management Instrumentation (WMI) Event Subscription (T1546.003)**:
  * Attackers create WMI event subscriptions to trigger execution upon certain system events, such as user logon, process creation, or hardware changes.
  * Often implemented via PowerShell or VBScript.
* **Unix Shell Configuration Modification (T1546.004)**:
  * Alterations to shell initialization files (.bash\_profile, .bashrc, .zshrc) to execute malicious commands upon user login or shell startup.
* **Accessibility Features (T1546.008)**:
  * Modifying Windows accessibility utilities (e.g., Sticky Keys, Utility Manager) to execute malicious payloads when triggered via specific keyboard shortcuts or user interactions.
* **Screensaver Triggered Execution (T1546.002)**:
  * Replacing legitimate screensaver executables or altering registry keys to execute malicious code upon screensaver activation.
* **Component Object Model (COM) Hijacking (T1546.015)**:
  * Modifying COM object registry entries to execute malicious payloads when legitimate applications invoke specific COM objects.

Typical procedures attackers follow:

1. Identify suitable event triggers available on the target system.
2. Configure the trigger to execute malicious payloads or scripts.
3. Ensure stealth by blending malicious activity with legitimate system behavior.
4. Maintain persistence or escalate privileges through triggered execution.

## When this Technique is Usually Used

Attackers commonly employ Event Triggered Execution in various attack scenarios and stages, including:

* **Persistence Stage**:
  * Maintaining long-term access to compromised systems by triggering malicious payloads automatically upon system reboot, user login, or scheduled intervals.
* **Privilege Escalation Stage**:
  * Exploiting event-triggered mechanisms that execute with elevated privileges, enabling attackers to escalate privileges on targeted systems.
* **Defense Evasion Stage**:
  * Utilizing legitimate system features and mechanisms to blend malicious actions with normal system operations, complicating detection and investigation efforts.
* **Lateral Movement Stage**:
  * Leveraging event-driven execution mechanisms to propagate malware or scripts across networked systems, triggered by specific network or user events.
* **Initial Access Stage (less common)**:
  * Occasionally, attackers use event-triggered payloads delivered via phishing or malicious downloads, activating upon specific user actions or events.

## How this Technique is Usually Detected

Detection of Event Triggered Execution typically involves monitoring and analyzing system configurations, logs, and events. Common detection methods and tools include:

* **Monitoring Scheduled Tasks**:
  * Regularly auditing Windows Task Scheduler or cron jobs for anomalous or new tasks.
  * Tools: Sysinternals Autoruns, PowerShell scripts, OSQuery, EDR solutions.
* **WMI Event Subscription Auditing**:
  * Monitoring creation or modification of WMI subscriptions.
  * Tools: Sysmon event logging (Event ID 19, 20, 21), WMI Explorer, EDR/SIEM solutions.
* **Registry Monitoring**:
  * Tracking changes to registry keys associated with accessibility features, screensavers, COM objects, and other event-triggered execution points.
  * Tools: Sysmon registry event logging (Event ID 12, 13, 14), Registry auditing, EDR solutions.
* **File Integrity Monitoring (FIM)**:
  * Detecting modifications or replacements of legitimate system binaries or scripts.
  * Tools: Tripwire, OSSEC, Windows Defender ATP, CrowdStrike Falcon.
* **Log Analysis and Alerting**:
  * Analyzing logs for suspicious event-triggered activities, unusual user logins, or abnormal execution patterns.
  * Tools: SIEM solutions (Splunk, Elastic Security), Windows Event Logs, Linux auditd.

Specific Indicators of Compromise (IoCs):

* Creation or modification of suspicious scheduled tasks or cron jobs.
* Unusual WMI event subscriptions referencing suspicious scripts or executables.
* Registry modifications for accessibility utilities, screensavers, or COM objects.
* Unexpected scripts or binaries in shell initialization files (.bashrc, .zshrc).
* Suspicious binaries or scripts executed upon system startup or user logon.

## Why it is Important to Detect This Technique

Detecting Event Triggered Execution is critical because it significantly impacts system and network security by enabling attackers to:

* **Maintain Persistent Access**:
  * Attackers establish long-term footholds on compromised systems, leading to prolonged unauthorized access.
* **Privilege Escalation**:
  * Malicious scripts or payloads triggered by events often execute with elevated privileges, enabling attackers to escalate privileges and gain administrative control.
* **Stealth and Defense Evasion**:
  * Leveraging legitimate system functions and events allows attackers to evade traditional detection methods, complicating incident response and forensic analysis.
* **Lateral Movement and Propagation**:
  * Event-triggered mechanisms facilitate malware propagation across networked systems, increasing the scope and severity of security incidents.
* **Potential Data Exfiltration and System Damage**:
  * Persistent, stealthy execution of malicious payloads can lead to data theft, system corruption, or disruption of critical services.

Early detection helps organizations:

* Contain and remediate threats before significant damage occurs.
* Prevent attackers from escalating privileges or moving laterally.
* Reduce the risk of data breaches, operational disruptions, and reputational damage.
* Enhance overall security posture by identifying and mitigating vulnerabilities exploited by attackers.

## Examples

Real-world examples of Event Triggered Execution include:

* **APT29 (Cozy Bear)**:
  * Utilized WMI event subscriptions to execute malicious payloads upon system boot or user logon, maintaining stealthy persistence within compromised networks.
  * Tools: PowerShell scripts, custom backdoors.
  * Impact: Persistent espionage activities, data exfiltration, prolonged stealthy access.
* **FIN7**:
  * Created scheduled tasks and registry modifications to execute malicious payloads automatically, facilitating payment card theft operations.
  * Tools: Carbanak malware, PowerShell scripts, custom payloads.
  * Impact: Financial fraud, theft of sensitive financial data, significant monetary losses.
* **Turla Group**:
  * Modified Unix shell configuration files (.bashrc, .zshrc) to execute malicious scripts upon user logins, ensuring persistent access to compromised Linux systems.
  * Tools: Custom Linux backdoors, malicious shell scripts.
  * Impact: Cyber espionage, persistent unauthorized access, data theft.
* **DarkHotel**:
  * Exploited accessibility features by altering Windows utility binaries (e.g., Sticky Keys) to execute malicious payloads upon specific user interactions.
  * Tools: Custom malware payloads, modified system binaries.
  * Impact: Targeted espionage against high-profile individuals, data exfiltration, prolonged stealthy access.
* **Stuxnet**:
  * Employed scheduled tasks and event-triggered execution mechanisms to propagate and execute payloads automatically, targeting Iranian nuclear facilities.
  * Tools: Custom worm payload, malicious scheduled tasks.
  * Impact: Physical damage to industrial control systems, operational disruption, geopolitical implications.

These examples demonstrate attackers' diverse use of event-triggered execution to maintain persistence, escalate privileges, evade detection, and achieve strategic objectives.
