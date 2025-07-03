---
description: Office Application Startup [T1137]
icon: lock
---

# Office Application Startup

## Information

* Name: Office Application Startup
* ID: T1137
* Tactics: [TA0003](../)
* Sub-Technique: [T1137.006](t1137.006.md), [T1137.005](t1137.005.md), [T1137.001](t1137.001.md), [T1137.003](t1137.003.md), [T1137.004](t1137.004.md), [T1137.002](t1137.002.md)

## Introduction

Office Application Startup is a technique categorized under MITRE ATT\&CK's Persistence (T1137) and Execution tactics. Attackers exploit Microsoft Office applications' built-in features and functionalities to execute malicious payloads automatically upon application startup. This technique leverages legitimate Office mechanisms, helping attackers bypass traditional security controls and remain persistent on compromised systems.

## Deep Dive Into Technique

Attackers utilize various built-in Microsoft Office functionalities to launch malicious code automatically when an Office application starts. Commonly targeted Office applications include Microsoft Word, Excel, PowerPoint, Outlook, and Access.

Key execution methods and mechanisms include:

* **Office Application Startup Folders:**
  * Attackers can place malicious templates or add-ins in specific startup paths, causing Office applications to load these files automatically upon startup.
  * Default startup locations for Office applications (examples):
    * Word: `%APPDATA%\Microsoft\Word\STARTUP\`
    * Excel: `%APPDATA%\Microsoft\Excel\XLSTART\`
    * PowerPoint: `%APPDATA%\Microsoft\PowerPoint\STARTUP\`
* **Registry Keys for Office Add-ins:**
  * Attackers manipulate registry keys to register malicious COM add-ins or macros.
  * Common registry locations include:
    * `HKCU\Software\Microsoft\Office\[Version]\[Application]\Addins`
    * `HKLM\Software\Microsoft\Office\[Version]\[Application]\Addins`
* **Macros and VBA Scripts:**
  * Attackers embed malicious VBA macros within Office documents or templates, executing automatically upon opening or startup.
  * Macros can download and execute additional payloads, establish persistence, or exfiltrate data.
* **COM Add-ins and DLL Loading:**
  * Attackers utilize COM add-ins (.dll files) registered within Office applications, allowing malicious code execution during application initialization.
  * DLL side-loading attacks exploit legitimate Office executables to load malicious DLLs from the same directory.

Real-world procedures typically involve:

* Crafting malicious Office templates or add-ins.
* Social engineering or phishing campaigns delivering malicious documents.
* Exploiting trusted Office functionalities to evade antivirus and endpoint detection solutions.

## When this Technique is Usually Used

Attackers commonly use Office Application Startup in the following scenarios and attack stages:

* **Initial Access and Execution:**
  * Phishing campaigns delivering malicious Office documents or templates to users.
  * Users unknowingly executing macros or add-ins embedded within documents.
* **Persistence:**
  * Establishing persistent footholds on compromised endpoints by ensuring malicious payloads execute each time Office applications start.
  * Maintaining long-term access to victim systems for lateral movement or data exfiltration.
* **Privilege Escalation and Credential Theft:**
  * Leveraging Office macros or add-ins to execute scripts that escalate privileges or steal sensitive credentials.
* **Data Exfiltration:**
  * Embedding macros or add-ins capable of collecting and sending sensitive data to attacker-controlled servers.

## How this Technique is Usually Detected

Detection methods for Office Application Startup include:

* **Endpoint Monitoring and EDR Tools:**
  * Monitoring file system changes in Office startup directories (e.g., `%APPDATA%\Microsoft\[OfficeApp]\STARTUP`).
  * Detecting suspicious DLL or COM add-in registrations within Office-related registry keys.
* **Registry Monitoring:**
  * Monitoring registry keys for suspicious COM add-ins or macros registrations:
    * `HKCU\Software\Microsoft\Office\[Version]\[Application]\Addins`
    * `HKLM\Software\Microsoft\Office\[Version]\[Application]\Addins`
* **Behavioral Analysis:**
  * Detecting abnormal Office application behavior, such as unusual network connections initiated by Office processes.
  * Monitoring Office applications launching unexpected child processes (e.g., PowerShell, cmd.exe).
* **Security Tools and Solutions:**
  * Antivirus and endpoint protection solutions capable of detecting malicious macros and DLL injections.
  * Application whitelisting policies restricting unauthorized Office add-ins and macros.
* **Indicators of Compromise (IoCs):**
  * Suspicious files placed in Office startup folders.
  * Unexpected COM add-ins registered in Office registry keys.
  * Unusual network traffic originating from Office applications.
  * Suspicious Office documents containing macros or scripts executing upon startup.

## Why it is Important to Detect This Technique

Detecting Office Application Startup exploitation is critical due to the following impacts on systems and networks:

* **Persistence and Long-term Access:**
  * Attackers achieve persistent footholds, allowing continuous access, data exfiltration, and lateral movement within the network.
* **Credential Theft and Privilege Escalation:**
  * Malicious macros and scripts executed via Office startup can steal credentials, escalate privileges, and compromise critical accounts.
* **Data Loss and Exfiltration:**
  * Malicious Office payloads can silently exfiltrate sensitive data, intellectual property, or confidential information.
* **Evasion of Traditional Security Controls:**
  * Leveraging legitimate Office functionalities helps attackers bypass antivirus and endpoint detection systems, making detection challenging.

Early detection and response to Office Application Startup techniques help mitigate potential damage, prevent lateral movement, and reduce the risk of prolonged compromise.

## Examples

Real-world examples demonstrating Office Application Startup exploitation include:

* **APT28 (Fancy Bear):**
  * Utilized malicious Office documents with embedded macros delivered via spear-phishing campaigns.
  * Macros executed payload downloads and established persistent backdoors on compromised systems.
* **FIN7 Attack Group:**
  * Distributed malicious Word and Excel documents containing macros via phishing emails targeting financial institutions.
  * Macros executed PowerShell scripts, establishing persistent access and exfiltrating sensitive financial data.
* **Emotet Malware:**
  * Delivered via malicious Office documents containing macros through widespread phishing campaigns.
  * Macros executed PowerShell commands to download additional malware payloads, enabling persistence and lateral movement.
* **TrickBot Malware:**
  * Leveraged malicious Excel documents containing macros to execute payloads upon document opening.
  * Established persistent footholds, enabling credential theft, lateral movement, and ransomware deployment.

In these examples, attackers leveraged Office Application Startup techniques through macros, add-ins, and registry manipulations, resulting in significant operational impacts, data breaches, and financial losses.
