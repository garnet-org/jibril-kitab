---
description: Hide Artifacts [T1564]
icon: lock
---

# Hide Artifacts

## Information

* Name: Hide Artifacts
* ID: T1564
* Tactics: [TA0005](../)
* Sub-Technique: T1564.012, T1564.008, T1564.011, [T1564.002](t1564.002.md), T1564.009, T1564.006, T1564.007, [T1564.003](t1564.003.md), [T1564.005](t1564.005.md), [T1564.001](t1564.001.md), [T1564.004](t1564.004.md), T1564.010

## Introduction

Hide Artifacts is a technique categorized within the MITRE ATT\&CK framework under "Defense Evasion." This tactic involves attackers intentionally concealing malicious artifacts such as files, scripts, processes, or registry entries to evade detection by security tools and analysts. Attackers typically employ this method to maintain persistence, avoid detection, and prolong their access to compromised systems. By obscuring the presence of malicious activities, adversaries can operate covertly, making detection and remediation significantly more challenging.

## Deep Dive Into Technique

The Hide Artifacts technique includes various technical methods attackers utilize to conceal their presence on compromised systems. Common execution methods and mechanisms include:

* **Hidden Files and Directories:**
  * Attackers create files or directories with hidden attributes, making them invisible to standard directory listings.
  * On Windows, attackers might use the "attrib +h" command or NTFS Alternate Data Streams (ADS) to hide malicious files.
  * On Linux/Unix systems, attackers typically prefix filenames with a dot (.) to hide them from default directory listings.
* **Rootkits and Kernel-Level Hiding:**
  * Rootkits are specialized malware designed to conceal processes, files, registry keys, and network connections.
  * Kernel-mode rootkits intercept system calls and modify system behavior, effectively hiding malicious artifacts from user-space detection tools.
* **Process Injection and Memory Manipulation:**
  * Attackers inject malicious code into legitimate processes, effectively hiding malicious activities within trusted applications.
  * Techniques include DLL injection, reflective DLL injection, process hollowing, and thread hijacking.
* **Registry and Configuration Manipulation:**
  * Malicious actors may modify registry entries or configuration files to obscure persistence mechanisms.
  * Techniques include creating hidden registry keys, using obscure registry locations, or modifying legitimate registry entries to blend into normal system behavior.
* **Data Obfuscation and Encryption:**
  * Attackers encode or encrypt malicious payloads and configuration files to bypass signature-based detection systems.
  * Obfuscation methods include Base64 encoding, XOR encryption, and custom encoding schemes.
* **Fileless Malware:**
  * Attackers execute malicious payloads directly in memory without writing files to disk, significantly reducing forensic artifacts.
  * Common methods include PowerShell scripts, WMI commands, or legitimate scripting frameworks.

## When this Technique is Usually Used

The Hide Artifacts technique is commonly employed across various stages and scenarios within a cyber attack lifecycle, including:

* **Initial Access and Execution:**
  * Attackers hide malicious payloads during initial delivery to bypass antivirus and endpoint detection solutions.
* **Persistence and Privilege Escalation:**
  * Attackers conceal persistence mechanisms such as scheduled tasks, startup scripts, registry modifications, or hidden services to maintain long-term access.
* **Defense Evasion and Lateral Movement:**
  * Attackers hide tools, scripts, and binaries used for lateral movement or privilege escalation to avoid detection by endpoint protection and network monitoring solutions.
* **Exfiltration and Command-and-Control (C2):**
  * Attackers disguise or encrypt data exfiltration methods, conceal network communication channels, and hide evidence of data theft activities.
* **Covering Tracks and Cleanup:**
  * Attackers remove or hide logs, system events, or forensic evidence to complicate incident response and forensic analysis.

## How this Technique is Usually Detected

Detecting the Hide Artifacts technique requires a combination of monitoring, behavioral analysis, and proactive threat hunting strategies. Detection methods, tools, and specific indicators of compromise (IoCs) include:

* **Endpoint Detection and Response (EDR) Solutions:**
  * Utilize EDR solutions to detect suspicious process injection, unauthorized memory modifications, and hidden processes.
* **File Integrity Monitoring (FIM):**
  * Monitoring file system changes, especially hidden or system files, can help identify unauthorized modifications or hidden files and directories.
* **Rootkit Detection Tools:**
  * Specialized anti-rootkit tools such as GMER, RootkitRevealer, chkrootkit, and rkhunter can identify hidden kernel-level artifacts.
* **Behavioral Analysis and Anomaly Detection:**
  * Employ behavioral analytics to detect anomalous process behaviors, unusual registry modifications, and suspicious memory activities.
* **Network Monitoring and IDS/IPS:**
  * Network-based intrusion detection systems (IDS) or intrusion prevention systems (IPS) can detect covert communication channels and data exfiltration attempts.
* **Threat Hunting and Forensics:**
  * Proactively search for hidden files, registry entries, alternate data streams (ADS), and encoded or encrypted scripts.
  * Employ memory forensics tools (e.g., Volatility Framework) to detect injected code and hidden processes in memory.

Specific IoCs to look for include:

* Hidden files or directories with unusual naming conventions or attributes.
* Suspicious alternate data streams (ADS) on NTFS file systems.
* Unauthorized registry keys or unusual registry modifications.
* Unexpected network connections or encrypted outbound traffic.
* Suspicious PowerShell scripts or encoded commands executed in memory.

## Why it is Important to Detect This Technique

Detecting the Hide Artifacts technique is critical due to its potential impact on system and network security, including:

* **Prolonged Attacker Presence:**
  * Hidden artifacts enable attackers to maintain persistence and remain undetected for extended periods, increasing the risk of long-term compromise.
* **Increased Damage Potential:**
  * Undetected attackers can escalate privileges, move laterally, and conduct data exfiltration, resulting in significant data breaches, intellectual property theft, or financial loss.
* **Difficulty in Incident Response:**
  * Concealed artifacts complicate forensic analysis, incident response, and remediation efforts, increasing the time and resources required to resolve incidents.
* **Reduced Visibility and Control:**
  * Hidden malicious activities reduce visibility into system operations, undermining the effectiveness of security monitoring tools and processes.
* **Regulatory and Compliance Risks:**
  * Undetected malicious activities can lead to compliance violations, regulatory penalties, and reputational damage for affected organizations.

Early detection of hidden artifacts significantly reduces attacker dwell time, limits damage, facilitates effective incident response, and preserves organizational reputation and compliance.

## Examples

Real-world examples of attacks employing the Hide Artifacts technique include:

* **Sony Pictures Hack (2014):**
  * Attackers utilized kernel-level rootkits and hidden files to evade detection and maintain persistence within Sony's infrastructure.
  * Impact included significant data exfiltration, intellectual property theft, and widespread operational disruption.
* **Equation Group Malware:**
  * Advanced persistent threat (APT) group known as the Equation Group employed sophisticated rootkits and firmware-level malware to conceal malicious artifacts.
  * Malware such as DoubleFantasy and GrayFish utilized hidden partitions, encrypted payloads, and advanced obfuscation techniques.
* **Turla APT Group:**
  * Turla used rootkits, process injection, and hidden file systems to evade detection and maintain long-term persistence in targeted networks.
  * Utilized advanced techniques such as kernel-mode rootkits and memory-resident malware to hide artifacts from endpoint detection.
* **APT29 (Cozy Bear) and Operation Ghost:**
  * APT29 leveraged fileless malware techniques, PowerShell scripts, and reflective DLL injection to hide malicious activities and evade endpoint detection solutions.
  * Attackers successfully compromised government and diplomatic organizations, exfiltrating sensitive information while remaining undetected for extended periods.
* **FIN7 Group Attacks:**
  * Cybercriminal group FIN7 used encoded PowerShell scripts, hidden registry keys, and memory-resident malware to evade detection and persist within compromised retail and hospitality environments.
  * Resulted in large-scale data breaches and financial losses for affected organizations.

These examples illustrate the diverse methods attackers utilize to hide artifacts, emphasizing the importance of robust detection capabilities and proactive threat hunting practices.
