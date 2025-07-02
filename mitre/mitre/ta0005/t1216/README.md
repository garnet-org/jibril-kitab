---
description: System Script Proxy Execution [T1216]
icon: play
---

# System Script Proxy Execution

## Information

* Name: System Script Proxy Execution
* ID: T1216
* Tactics: [TA0005](../)
* Sub-Technique: [T1216.001](t1216.001.md), T1216.002

## Introduction

System Script Proxy Execution (T1216) is a technique outlined within the MITRE ATT\&CK framework under the Execution tactic. Attackers leverage legitimate scripts or script interpreters already present on targeted systems to execute malicious code, bypass security controls, and evade detection. By exploiting trusted system scripts and utilities, adversaries can execute unauthorized commands, scripts, or payloads without directly invoking suspicious binaries, thereby maintaining stealth and persistence within compromised environments.

## Deep Dive Into Technique

System Script Proxy Execution involves attackers utilizing legitimate system scripts or script interpreters—such as PowerShell, VBScript, JavaScript (JScript), Python, Perl, Bash, or Windows command scripts—to execute malicious commands or payloads. The attacker typically abuses scripts that are inherently trusted by the operating system or security solutions, thus bypassing application whitelisting, antivirus detection, and behavioral analytics.

Common execution methods include:

* **PowerShell Scripts:** Attackers frequently leverage PowerShell due to its powerful scripting capabilities and deep integration with Windows systems. Malicious PowerShell scripts can download payloads, execute commands remotely, and evade antivirus detection through obfuscation and encoding.
* **Windows Script Host (WSH):** WSH supports VBScript and JScript, allowing attackers to execute scripts directly or indirectly to deliver payloads, perform reconnaissance, or maintain persistence.
* **Unix/Linux Shell Scripts:** Attackers exploit Bash, Python, Perl, or other scripting languages available on Unix/Linux systems to execute commands, establish persistence, or pivot within networks.
* **Signed System Scripts:** Attackers abuse legitimate system scripts (such as Microsoft-signed scripts or other trusted vendor scripts) to bypass application control policies and execute malicious code.
* **Living-off-the-Land Binaries and Scripts (LOLBAS):** Attackers exploit legitimate binaries and scripts already present on target systems (such as Certutil.exe, Regsvr32.exe, MSHTA.exe, or Rundll32.exe) to download and execute malicious scripts or binaries.

Real-world procedures include:

* Encoding and obfuscating scripts to evade signature-based antivirus solutions.
* Leveraging scripts to perform lateral movement, privilege escalation, or data exfiltration.
* Embedding malicious scripts within legitimate scheduled tasks, registry keys, or startup scripts for persistence.

## When this Technique is Usually Used

Attackers employ System Script Proxy Execution across multiple stages of the cyber kill chain, including:

* **Initial Access:**
  * Executing malicious scripts via phishing emails containing macro-enabled documents or attachments.
  * Exploiting exposed web applications or remote services to execute scripts remotely.
* **Execution:**
  * Running encoded PowerShell or VBScript payloads directly from the command line or through compromised applications.
  * Utilizing legitimate script interpreters to execute downloaded malware payloads.
* **Persistence:**
  * Embedding malicious scripts within startup folders, scheduled tasks, or registry entries to maintain long-term access.
  * Modifying legitimate scripts or system utilities to execute malicious commands silently at system startup or user login.
* **Privilege Escalation:**
  * Exploiting scripts with elevated permissions or vulnerable scripts to escalate privileges.
* **Defense Evasion:**
  * Using signed or trusted scripts to bypass application whitelisting or antivirus detection.
  * Obfuscating or encoding scripts to evade signature-based detection.
* **Lateral Movement:**
  * Remotely executing scripts on other systems within the compromised network using tools like PowerShell Remoting or WMI.
* **Exfiltration:**
  * Employing scripts to compress, encrypt, and transfer sensitive data to external command-and-control servers.

## How this Technique is Usually Detected

Detection of System Script Proxy Execution involves monitoring and analyzing script execution behaviors and system activities. Effective detection methods include:

* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitoring script interpreter processes (e.g., powershell.exe, cscript.exe, wscript.exe) and flagging abnormal or suspicious script executions.
  * Identifying encoded or obfuscated command-line arguments commonly used by attackers.
* **Behavioral Analytics and Anomaly Detection:**
  * Detecting unusual script execution patterns or unexpected script interpreter usage on systems.
  * Alerting on scripts executed from unusual locations or by unauthorized users.
* **Application Whitelisting and Integrity Controls:**
  * Enforcing strict whitelisting policies to limit script execution to authorized directories and scripts.
  * Detecting attempts to execute unauthorized or modified legitimate system scripts.
* **Logging and Event Monitoring:**
  * Enabling PowerShell logging (Script Block Logging, Module Logging, and Transcription Logging) to capture detailed script execution data.
  * Monitoring Windows Event Logs (Sysmon, Security logs) for suspicious script execution events or command-line arguments.
* **Network Monitoring and IDS/IPS:**
  * Identifying suspicious network connections initiated by scripts, particularly those reaching out to unknown or malicious IP addresses or domains.

Indicators of compromise (IoCs) include:

* Unusual or encoded command-line parameters associated with script interpreters.
* Execution of scripts from temporary folders, user directories, or unusual system locations.
* Unexpected or abnormal script interpreter processes spawning child processes or network connections.
* Presence of suspicious scripts or files in startup folders, scheduled tasks, or registry autoruns.
* Network traffic from scripts to known malicious IP addresses, URLs, or domains.

## Why it is Important to Detect This Technique

Early detection and response to System Script Proxy Execution is critical due to the following potential impacts and risks:

* **Bypassing Security Controls:**
  * Attackers leverage legitimate tools and scripts to bypass antivirus, application whitelisting, and other traditional security measures, making detection challenging.
* **Persistence and Stealth:**
  * Malicious scripts can maintain stealthy persistence within compromised environments, allowing attackers prolonged access and control over systems.
* **Privilege Escalation and Lateral Movement:**
  * Attackers frequently use scripts to escalate privileges, pivot across networks, and compromise additional systems, significantly increasing the scope and severity of breaches.
* **Data Exfiltration and Data Loss:**
  * Scripts can automate data theft, enabling attackers to rapidly exfiltrate sensitive information, intellectual property, or personal data, resulting in financial and reputational damage.
* **System and Network Disruption:**
  * Malicious scripts can disrupt critical operations, degrade system performance, or facilitate destructive attacks such as ransomware deployment.

Detecting and mitigating System Script Proxy Execution early in the attack lifecycle significantly reduces the risk of widespread compromise, data loss, and operational disruption.

## Examples

Real-world examples of System Script Proxy Execution include:

* **Emotet Malware:**
  * Attackers used malicious PowerShell scripts embedded within macro-enabled Microsoft Office documents delivered via phishing emails. Once executed, these scripts downloaded and executed additional payloads, enabling lateral movement and data exfiltration.
* **FIN7 Group Attacks:**
  * Utilized JavaScript and VBScript files executed through Windows Script Host (WSH) to deliver payloads such as Carbanak malware. These scripts enabled attackers to maintain stealthy persistence, escalate privileges, and move laterally within targeted financial institutions.
* **APT29 (Cozy Bear) Activities:**
  * Leveraged PowerShell scripts for command-and-control communication, lateral movement, and data exfiltration. Attackers often encoded and obfuscated scripts to evade detection and executed them via legitimate system utilities.
* **TrickBot Malware:**
  * Used PowerShell scripts executed via scheduled tasks or registry autoruns to maintain persistence, download additional payloads, and facilitate lateral movement within compromised networks.
* **OilRig (APT34) Campaigns:**
  * Employed malicious VBScript and PowerShell scripts executed through legitimate Windows utilities like MSHTA.exe and Regsvr32.exe to bypass application whitelisting, establish persistence, and exfiltrate sensitive data from targeted organizations.

Tools commonly used by attackers include:

* PowerShell Empire
* Cobalt Strike
* Metasploit Framework
* Nishang (PowerShell-based offensive security scripts)
* Invoke-Obfuscation (PowerShell obfuscation tool)
* Certutil.exe, MSHTA.exe, Regsvr32.exe, Rundll32.exe (LOLBAS techniques)

Impacts observed in real-world attacks:

* Financial losses due to data breaches and fraud.
* Intellectual property theft and espionage.
* Operational disruptions and downtime.
* Regulatory penalties and reputational damage.
