---
description: Command and Scripting Interpreter [T1059]
icon: terminal
---

# Command and Scripting Interpreter

## Information

* Name: Command and Scripting Interpreter
* ID: T1059
* Tactics: [TA0002](../)
* Sub-Technique: [T1059.007](t1059.007.md), [T1059.002](t1059.002.md), [T1059.010](t1059.010.md), [T1059.009](t1059.009.md), [T1059.008](t1059.008.md), [T1059.001](t1059.001.md), [T1059.004](t1059.004.md), [T1059.011](t1059.011.md), [T1059.006](t1059.006.md), [T1059.003](t1059.003.md), [T1059.005](t1059.005.md)

## Introduction

Command and Scripting Interpreter (MITRE ATT\&CK ID: T1059) refers to adversaries leveraging built-in command-line interfaces, scripting languages, and interpreters to execute commands, scripts, or binaries on compromised hosts. These interpreters include Windows Command Shell (cmd.exe), PowerShell, Unix shells (bash, sh), Python, JavaScript, and others. Attackers use these interpreters because they are typically native to operating systems, making their activities harder to distinguish from legitimate administrative operations.

## Deep Dive Into Technique

Attackers use command and scripting interpreters to execute arbitrary commands, automate malicious tasks, and navigate compromised systems. Common interpreters include:

* **Windows Command Shell (cmd.exe):**
  * Executes Windows commands and batch scripts (.bat, .cmd).
  * Often used to initiate malicious binaries or scripts, manipulate files, or enumerate system information.
* **PowerShell:**
  * Native Windows scripting language providing extensive access to system internals.
  * Frequently used due to its robust features, such as obfuscation, remote execution, and advanced script execution capabilities.
* **Unix/Linux Shells (bash, sh, zsh):**
  * Standard command interpreters for Unix/Linux systems.
  * Attackers commonly leverage shell scripts to automate reconnaissance, lateral movement, privilege escalation, and data exfiltration.
* **Python Interpreter:**
  * Widely installed scripting language across multiple platforms.
  * Enables attackers to execute cross-platform scripts, exploit vulnerabilities, or load additional modules dynamically.
* **JavaScript Interpreter (JScript, Node.js):**
  * Commonly employed in Windows for executing scripts via Windows Script Host (WSH).
  * Used by adversaries to execute encoded or obfuscated payloads and bypass traditional defenses.

Execution mechanisms include:

* Direct invocation of interpreters via command line or scripts.
* Embedding scripts within legitimate documents (macros, embedded scripts).
* Utilizing scheduled tasks, cron jobs, or service execution to automate malicious scripts.
* Employing obfuscation and encoding techniques to evade detection and analysis.

Real-world procedures often involve:

* Initial access via phishing emails with malicious scripts attached.
* Execution of PowerShell commands to download additional payloads.
* Use of cmd.exe to enumerate system information or perform lateral movement.
* Leveraging bash scripts to automate data exfiltration on compromised Linux servers.

## When this Technique is Usually Used

Attackers leverage command and scripting interpreters across multiple stages of the cyber kill chain:

* **Initial Access:**
  * Malicious scripts embedded in phishing emails or attachments.
  * Exploitation of web vulnerabilities leading to interpreter execution.
* **Execution:**
  * Direct invocation of interpreters to run malicious payloads or scripts.
  * Automated execution via scheduled tasks or cron jobs.
* **Persistence:**
  * Establishing persistent scheduled tasks or cron jobs executing malicious scripts periodically.
  * Modifying startup scripts or registry entries to invoke interpreters at system boot.
* **Privilege Escalation:**
  * Scripts designed to exploit vulnerabilities or misconfigurations to elevate privileges.
* **Defense Evasion:**
  * Obfuscating scripts or commands to evade detection by antivirus and endpoint detection systems.
  * Using legitimate interpreters to blend malicious activity with normal administrative tasks.
* **Discovery:**
  * Leveraging built-in commands and scripts to enumerate system configurations, installed software, network connections, and user accounts.
* **Lateral Movement:**
  * Scripts executed remotely via PowerShell Remoting, SSH, or remote command execution tools.
* **Exfiltration:**
  * Automating data collection and transfer through scripting interpreters.

## How this Technique is Usually Detected

Detection of command and scripting interpreter misuse involves a combination of monitoring techniques, tools, and indicators:

* **Endpoint Detection and Response (EDR):**
  * Monitoring interpreter processes (cmd.exe, powershell.exe, bash, python.exe) for abnormal behaviors.
  * Detecting unusual parent-child process relationships (e.g., office documents spawning cmd.exe or powershell.exe).
* **Logging and Monitoring:**
  * Windows Event Logs (Security, PowerShell Operational logs, Sysmon logs) capturing command-line arguments, script execution, and process creation events.
  * Linux auditd logs for tracking shell command execution and cron job modifications.
* **Behavioral Analysis:**
  * Identifying anomalous scripting interpreter usage patterns, such as execution from non-standard directories, unusual command-line parameters, or encoded/obfuscated commands.
* **Threat Hunting:**
  * Proactive searches for suspicious interpreter executions, such as encoded PowerShell commands (base64 encoding), obfuscated JavaScript payloads, or scripts executed from temporary directories.
* **Network Detection:**
  * Network traffic analysis identifying downloads of malicious scripts or executables initiated by interpreter commands.
  * Detection of outbound connections initiated by interpreter processes to known malicious IP addresses or domains.
* **Specific Indicators of Compromise (IoCs):**
  * Suspicious command-line arguments (e.g., encoded PowerShell commands like "-EncodedCommand").
  * Scripts stored or executed from temporary or unusual directories.
  * Unusual scheduled tasks or cron jobs invoking scripting interpreters.
  * Abnormal process trees (e.g., Microsoft Office applications spawning cmd.exe or powershell.exe).

## Why it is Important to Detect This Technique

Early detection of malicious use of command and scripting interpreters is crucial due to the following impacts:

* **System Compromise and Loss of Confidentiality:**
  * Attackers can execute arbitrary commands, access sensitive information, or exfiltrate critical data.
* **Privilege Escalation and Persistence:**
  * Malicious scripts can escalate privileges, establish persistent footholds, and maintain long-term access.
* **Stealth and Defense Evasion:**
  * Legitimate interpreters allow attackers to blend in with normal administrative activities, evading traditional antivirus and signature-based defenses.
* **Lateral Movement and Network Propagation:**
  * Scripts and commands facilitate lateral movement within networks, rapidly escalating the scope and severity of a breach.
* **Operational Disruption and Data Integrity Issues:**
  * Malicious scripts can disrupt system operations, delete or corrupt critical data, and impact business continuity.

Early detection allows security teams to:

* Contain and remediate breaches quickly, minimizing damage and operational disruption.
* Gain visibility into attacker tactics, techniques, and procedures (TTPs), aiding future defense improvements.
* Limit the spread of compromise within the network, preserving critical assets and sensitive data.

## Examples

Real-world examples illustrating the use of command and scripting interpreters include:

* **TrickBot Malware:**
  * Uses PowerShell commands executed via cmd.exe to download and execute additional malware payloads.
  * Employs obfuscated PowerShell scripts to evade antivirus detection.
* **Emotet Malware:**
  * Utilizes malicious macros embedded in Microsoft Office documents to execute cmd.exe or PowerShell scripts, downloading further payloads onto victim systems.
* **FIN7 Group Attacks:**
  * Executes JavaScript payloads via Windows Script Host (WSH) to achieve initial access, persistence, and lateral movement within compromised networks.
* **APT32 (OceanLotus):**
  * Leverages obfuscated PowerShell scripts to execute reconnaissance commands, lateral movement, and data exfiltration tasks.
* **Lazarus Group:**
  * Uses bash scripts on Linux servers to automate reconnaissance, privilege escalation, and data exfiltration activities.
* **NotPetya Ransomware Attack:**
  * Leveraged cmd.exe and PowerShell scripts to propagate across internal networks, encrypting data and causing extensive operational disruption.

In these examples, attackers frequently employed:

* Obfuscation and encoding techniques (base64 encoding, character substitution).
* Execution via legitimate interpreter binaries (powershell.exe, cmd.exe, bash).
* Automated scripts for rapid lateral movement, privilege escalation, and data exfiltration.

The impacts of these attacks included:

* Significant data loss and leakage of sensitive information.
* Extended downtime and operational disruption.
* Significant financial and reputational damage to victim organizations.
