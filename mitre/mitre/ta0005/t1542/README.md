---
description: Pre-OS Boot [T1542]
icon: boot
---

# Pre-OS Boot

## Information

* Name: Pre-OS Boot
* ID: T1542
* Tactics: [TA0005](../), [TA0003](../../ta0003/)
* Sub-Technique: [T1542.001](t1542.001.md), [T1542.003](t1542.003.md), [T1542.005](t1542.005.md), [T1542.002](t1542.002.md), [T1542.004](t1542.004.md)

## Introduction

Pre-OS Boot techniques, as classified under MITRE ATT\&CK (T1542), involve adversaries executing malicious code or modifying system components before the operating system fully boots. Such methods allow attackers to maintain persistence, evade detection, and establish deep-rooted control over compromised systems. These techniques primarily target firmware, bootloaders, and other pre-operating system components to ensure malicious code execution at the earliest stages of system startup.

## Deep Dive Into Technique

Pre-OS Boot attacks exploit vulnerabilities or weaknesses in the system boot process, firmware, or hardware initialization routines. Attackers typically leverage the following methods:

* **Firmware Modification:**
  * Manipulating BIOS or UEFI firmware to embed malicious code.
  * Utilizing firmware rootkits to persistently infect systems, surviving OS reinstallations or disk replacements.
* **Bootloader Manipulation:**
  * Altering bootloader code (e.g., GRUB, Windows Boot Manager) to execute malicious payloads before the OS loads.
  * Injecting code into boot sectors or EFI partitions.
* **Hardware-Level Attacks:**
  * Exploiting vulnerabilities in hardware components (chipsets, TPM, storage controllers) to execute malicious instructions pre-boot.
  * Using compromised hardware or firmware implants to subvert system security.
* **Secure Boot Bypass:**
  * Exploiting vulnerabilities or misconfigurations to bypass secure boot mechanisms, enabling unauthorized code execution at boot time.
  * Employing stolen or compromised signing keys to sign malicious bootloaders or firmware.

Real-world procedures typically involve:

* Gaining initial system access through phishing, supply chain compromise, or physical access.
* Escalating privileges to modify firmware or bootloader components.
* Installing persistent implants or rootkits to ensure stealth and longevity.

## When this Technique is Usually Used

Attackers commonly employ Pre-OS Boot techniques in the following scenarios and stages of an attack:

* **Persistence Stage:**
  * To maintain long-term, stealthy persistence that survives OS reinstallation, system updates, and security software scans.
* **Privilege Escalation:**
  * To escalate privileges by controlling system boot processes and firmware-level operations, enabling attackers to bypass OS-level security controls.
* **Defense Evasion:**
  * To evade detection by security solutions that typically operate at OS-level, as pre-OS boot code executes before security tools are active.
* **Supply Chain Attacks:**
  * Embedding malicious firmware or bootloader modifications during hardware manufacturing or software distribution processes.
* **Advanced Persistent Threat (APT) Operations:**
  * Leveraging pre-OS malware to maintain persistent access in high-value targets, including government agencies, critical infrastructure, and large enterprises.
* **Physical Access Scenarios:**
  * Exploiting systems where an attacker has temporary physical access, enabling direct firmware manipulation or bootloader tampering.

## How this Technique is Usually Detected

Detection of Pre-OS Boot compromises typically requires specialized methods, tools, and indicators of compromise (IoCs):

* **Firmware Integrity Checks:**
  * Regularly verifying firmware integrity through cryptographic hashes, secure boot procedures, and firmware attestation tools.
* **Bootloader Monitoring:**
  * Analyzing bootloader configurations, boot sectors, EFI partitions, and monitoring for unauthorized modifications or anomalies.
* **Hardware Security Modules (HSM) and TPMs:**
  * Utilizing Trusted Platform Modules (TPMs) or hardware security modules to detect deviations from expected boot measurements and firmware states.
* **UEFI Scanning Tools:**
  * Employing specialized tools such as CHIPSEC, UEFITool, or ESET UEFI Scanner to detect malicious firmware implants or unauthorized code injections.
* **Behavioral Indicators:**
  * Unexpected system crashes or boot failures.
  * Unusual boot times or delays.
  * Unrecognized firmware version numbers or unexpected firmware updates.
* **Specific Indicators of Compromise (IoCs):**
  * Unknown or unsigned firmware images.
  * Suspicious EFI binaries or bootloader files.
  * Unusual firmware or bootloader configurations detected in logs.

## Why it is Important to Detect This Technique

Detecting Pre-OS Boot techniques is critical due to their severe impact on systems and networks:

* **High-Level Persistence:**
  * Malicious firmware implants or bootloader modifications persist across OS reinstallation, disk replacement, and routine security updates, making remediation challenging.
* **Stealth and Evasion:**
  * Pre-OS malware executes before OS-level security controls are active, significantly reducing detection chances and allowing attackers prolonged undetected presence.
* **Privilege Escalation and Control:**
  * Attackers gain comprehensive control over system initialization, enabling high-level privilege escalation and potential system compromise at the deepest hardware and firmware levels.
* **Integrity and Availability Risks:**
  * Malicious pre-OS code can compromise system integrity, causing instability, data corruption, or denial-of-service conditions.
* **Supply Chain Risks:**
  * Pre-OS attacks embedded during manufacturing or distribution can affect large-scale deployments, impacting numerous systems simultaneously.

Early detection and mitigation of Pre-OS Boot compromises are essential to prevent long-term damage, reduce remediation costs, and maintain system integrity and trustworthiness.

## Examples

Real-world examples of Pre-OS Boot attacks include:

* **LoJax UEFI Rootkit (APT28):**
  * **Attack Scenario:** Russian-linked threat actor APT28 compromised UEFI firmware to install LoJax, establishing persistent access on targeted systems.
  * **Tools Used:** LoJax malware, firmware flashing tools, compromised legitimate utilities.
  * **Impact:** Persistent, stealthy infection surviving OS reinstallations, enabling long-term espionage operations.
* **MosaicRegressor UEFI Malware (APT41):**
  * **Attack Scenario:** Chinese-linked APT41 utilized MosaicRegressor, a malicious UEFI implant, to target diplomatic entities.
  * **Tools Used:** MosaicRegressor malware, firmware exploitation, and modification tools.
  * **Impact:** Persistent espionage campaigns with deep system-level access, difficult to detect and remediate.
* **TrickBoot Module (TrickBot Malware):**
  * **Attack Scenario:** TrickBot operators developed TrickBoot to inspect UEFI firmware vulnerabilities, potentially enabling firmware-level persistence.
  * **Tools Used:** TrickBot malware framework, TrickBoot module.
  * **Impact:** Potential for firmware-level persistence, significantly complicating remediation and detection efforts.
* **Sednit Group (APT28) Secure Boot Bypass:**
  * **Attack Scenario:** Exploiting vulnerabilities in Secure Boot implementations to load unsigned malicious bootloaders.
  * **Tools Used:** Custom bootloader modifications, exploitation of Secure Boot vulnerabilities.
  * **Impact:** Complete bypass of fundamental security controls, enabling persistent, stealthy malware execution.

These examples illustrate the severity and persistence potential of Pre-OS Boot attacks, highlighting the necessity for robust detection and mitigation strategies.
