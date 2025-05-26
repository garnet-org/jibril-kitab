---
description: Execution [TA0002]
icon: play
---

# Execution [TA0002]

## Information

- ID: TA0002

## Introduction

Execution is a critical tactic within the MITRE ATT&CK framework that represents adversary attempts to run malicious code or commands on a targeted system or network. This tactic encompasses various techniques attackers leverage to execute unauthorized software, scripts, or commands, enabling them to achieve their objectives, such as persistence, privilege escalation, data exfiltration, or lateral movement. Understanding execution techniques is essential for defenders to identify, detect, and mitigate attacks early in the attack lifecycle.

## Deep Dive Into Technique

Execution techniques involve methods attackers use to run malicious payloads or code on victim systems. Attackers commonly utilize built-in operating system utilities, scripting languages, legitimate administrative tools, or third-party software to evade detection and blend into normal system operations. Detailed execution methods include:

- **Command and Scripting Interpreter**

  - Attackers use command-line interfaces such as PowerShell, Windows Command Prompt (cmd.exe), Unix shells (bash, sh), and scripting languages (Python, JavaScript, VBScript) to execute malicious scripts or commands.
  - These interpreters are often legitimate tools, making detection challenging.

- **Scheduled Tasks and Cron Jobs**

  - Adversaries schedule malicious executables or scripts to run automatically at specified times or intervals, ensuring persistence and regular execution.

- **Service Execution**

  - Attackers create or modify system services (Windows services, Linux daemons) to execute malicious payloads.
  - This method allows persistent execution with elevated privileges.

- **User Execution**

  - Techniques that rely on user interactions, such as social engineering, phishing emails, or malicious attachments/documents, triggering execution of malicious payloads upon opening or interaction.

- **Inter-Process Communication (IPC)**

  - Attackers leverage IPC mechanisms (pipes, sockets, shared memory) to execute code indirectly or remotely on compromised systems.

- **Exploitation for Client Execution**

  - Exploiting vulnerabilities in client applications (e.g., browsers, email clients, PDF readers) to execute malicious payloads remotely.

- **Native API**
  - Attackers directly invoke Windows or Linux APIs to execute malicious code, bypassing higher-level security controls.

## When this Technique is Usually Used

Execution techniques appear throughout multiple stages of the cyber-attack lifecycle and across various attack scenarios, including:

- **Initial Access**

  - Attackers execute malicious payloads after successful phishing attacks, drive-by downloads, or exploitation of public-facing applications.
  - Examples: Malicious Office macros, malicious scripts via phishing emails.

- **Persistence**

  - Attackers use execution techniques to ensure continued access by scheduling tasks, creating services, or modifying startup items.
  - Examples: Scheduled tasks, cron jobs, malicious services.

- **Privilege Escalation**

  - Execution of scripts, binaries, or commands to exploit vulnerabilities or misconfigurations, elevating user privileges.
  - Examples: Exploiting kernel vulnerabilities, executing scripts with elevated permissions.

- **Defense Evasion**

  - Attackers execute encoded or obfuscated commands and scripts to evade traditional detection mechanisms.
  - Examples: Obfuscated PowerShell scripts, encoded command-line arguments.

- **Lateral Movement**

  - Execution of remote commands and scripts to move laterally across compromised networks.
  - Examples: Remote PowerShell sessions, SSH commands, Windows Management Instrumentation (WMI).

- **Data Exfiltration**
  - Execution of scripts or commands to compress, encrypt, or transfer data out of the victim environment.
  - Examples: Compression tools, FTP/SFTP commands, cloud storage command-line interfaces.

## How this Technique is Usually Detected

Detecting execution techniques requires monitoring and analyzing various system activities, processes, and logs. Common detection methods include:

- **Endpoint Detection and Response (EDR) Tools**

  - Monitoring execution of unusual commands, scripts, or binaries.
  - Detecting suspicious parent-child process relationships (e.g., Word spawning PowerShell).

- **Process Monitoring**

  - Monitoring processes for unusual command-line arguments, encoded commands, or obfuscated scripts.
  - Tools: Sysmon, Process Monitor, EDR solutions.

- **Command-Line Auditing**

  - Logging and analyzing command-line arguments and scripting interpreter usage.
  - Tools: Windows Event Logs, PowerShell logging, Bash history logging.

- **Behavioral Analytics**

  - Identifying abnormal execution patterns, such as processes executing from unusual directories or at unusual times.
  - Tools: SIEM solutions, UEBA platforms.

- **File Integrity Monitoring (FIM)**

  - Detecting unauthorized changes to scheduled tasks, cron jobs, services, or startup items.
  - Tools: Tripwire, OSSEC, built-in OS auditing.

- **Network Monitoring**
  - Detecting unusual outbound connections or data transfers initiated by executed scripts or commands.
  - Tools: IDS/IPS systems, network traffic analyzers (Wireshark, Zeek).

### Specific Indicators of Compromise (IoCs)

- Unusual parent-child process relationships (e.g., Office applications spawning scripting interpreters).
- Execution of encoded or obfuscated commands (e.g., Base64-encoded PowerShell).
- Unexpected scheduled tasks or cron jobs.
- Creation or modification of system services or daemons.
- Unusual network traffic patterns following script or command execution.

## Why it is Important to Detect This Technique

Early detection of execution techniques is crucial due to their significant impact on systems and networks, including:

- **Persistence and Long-Term Access**

  - Attackers leverage execution techniques to maintain persistent footholds, making remediation challenging if not detected early.

- **Privilege Escalation**

  - Execution of malicious code can lead to elevated privileges, enabling attackers to compromise additional system components and sensitive data.

- **Data Exfiltration and Theft**

  - Attackers execute scripts and commands to steal sensitive data, intellectual property, or personal information, causing significant operational and reputational damage.

- **Lateral Movement**

  - Execution techniques facilitate lateral movement across networks, expanding the scope of compromise and complicating containment and remediation efforts.

- **Disruption and Damage**

  - Execution of malicious scripts or commands can lead to system instability, service disruption, or data destruction.

- **Regulatory and Compliance Implications**
  - Failure to detect and respond to malicious execution can lead to regulatory penalties, compliance violations, and loss of customer trust.

Early detection and response reduce the attacker’s ability to achieve their objectives, limit potential damage, and significantly decrease remediation costs.

## Examples

Real-world examples illustrating execution techniques include:

- **Emotet Malware**

  - Attack Scenario: Delivered via phishing emails containing malicious Office macros.
  - Tools Used: Malicious Word documents, PowerShell scripts.
  - Impact: Initial access, persistence, credential theft, lateral movement, deployment of additional malware (e.g., TrickBot, Ryuk ransomware).

- **APT29 (Cozy Bear)**

  - Attack Scenario: Leveraged PowerShell and Windows Management Instrumentation (WMI) for execution and lateral movement.
  - Tools Used: PowerShell scripts, WMI commands, custom malware.
  - Impact: Long-term espionage, data exfiltration, persistent access to sensitive networks.

- **NotPetya Ransomware**

  - Attack Scenario: Exploited SMB vulnerabilities and executed malicious payloads via scheduled tasks and compromised software updates (MeDoc).
  - Tools Used: Scheduled tasks, malicious DLLs, EternalBlue exploit.
  - Impact: Massive operational disruption, global financial damage, data destruction.

- **FIN7 Group**

  - Attack Scenario: Used phishing emails with malicious attachments executing JavaScript, VBScript, and PowerShell scripts.
  - Tools Used: JavaScript-based payloads, PowerShell scripts, Cobalt Strike.
  - Impact: Financial theft, payment card data exfiltration, persistent access to corporate networks.

- **DarkHotel APT**
  - Attack Scenario: Exploited vulnerabilities in hotel Wi-Fi networks, executed malicious payloads via client-side exploits.
  - Tools Used: Browser exploits, malicious executables, scripting languages.
  - Impact: Espionage, credential theft, targeted attacks against executives and government officials.

These examples demonstrate the versatility and potential impact of execution techniques in real-world cyber-attacks, underscoring the importance of detection, monitoring, and mitigation.
