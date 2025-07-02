---
description: Modify System Image [T1601]
icon: image
---

# Modify System Image

## Information

* Name: Modify System Image
* ID: T1601
* Tactics: [TA0005](../)
* Sub-Technique: [T1601.001](t1601.001.md), [T1601.002](t1601.002.md)

## Introduction

The "Modify System Image" technique (T1601) is categorized under the MITRE ATT\&CK framework as a persistence tactic. Adversaries leverage this method to manipulate system images, including firmware, operating system images, or other critical software components, to maintain persistence, evade detection, and ensure long-term access to compromised systems. By altering legitimate system images, attackers can embed malicious code that survives system reboots, software updates, and even complete reinstallations, making it particularly challenging for defenders to detect and remediate effectively.

## Deep Dive Into Technique

The "Modify System Image" technique involves adversaries making unauthorized modifications to system images or firmware to establish persistent access. These modifications typically occur at a low level, allowing attackers to persist through reboots, firmware updates, and OS reinstalls. Attackers commonly exploit this technique by:

* Modifying boot images, firmware, or OS installation images to embed malicious payloads.
* Injecting malware into system recovery partitions or backup images.
* Altering BIOS or UEFI firmware to execute malicious code at system boot time.
* Tampering with virtual machine disk images or container images to ensure malicious code execution upon deployment.

Technical mechanisms employed include:

* Directly accessing and modifying firmware using specialized tools or exploits targeting firmware vulnerabilities.
* Employing rootkits or bootkits designed specifically to embed themselves into system images or firmware.
* Utilizing legitimate administrative tools or custom scripts to modify system images stored on network shares or update servers.

Real-world procedures often involve initial compromise through phishing, exploitation of vulnerabilities, or supply-chain attacks, followed by lateral movement to infrastructure responsible for system image storage or distribution.

## When this Technique is Usually Used

Attackers typically use the "Modify System Image" technique in various stages and scenarios, including:

* **Persistence Stage:** Ensuring long-term access by embedding malicious code into firmware or OS images.
* **Supply Chain Attacks:** Compromising trusted vendors or third-party software providers to distribute maliciously modified system images to multiple victims.
* **Advanced Persistent Threat (APT) Campaigns:** Nation-state actors embedding stealthy persistence mechanisms to maintain covert access for espionage or sabotage.
* **Pre-Deployment Attacks:** Modifying OS or firmware images prior to deployment in enterprise environments or cloud infrastructure.
* **Virtualization and Container Environments:** Injecting malware into virtual machine templates or container images to propagate malicious code across multiple deployments.

## How this Technique is Usually Detected

Detection of "Modify System Image" is challenging due to its low-level persistence and stealthy nature. However, several methods and tools can aid in identifying this technique:

* **Integrity Checking and Hash Validation:**
  * Regularly verify cryptographic hashes or digital signatures of system images and firmware against trusted baselines.
  * Employ integrity monitoring tools (e.g., Tripwire, OSSEC) to detect unauthorized modifications.
* **Firmware Security Tools:**
  * Utilize firmware scanning tools such as CHIPSEC or Binwalk to analyze firmware images for anomalies or embedded malicious code.
  * Deploy UEFI scanning tools to detect suspicious modifications to boot firmware.
* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitor endpoints for unusual firmware updates, BIOS/UEFI changes, or unexpected modifications to system partitions.
  * Alert on suspicious administrative actions involving firmware or system image manipulation.
* **Behavioral Monitoring and Anomaly Detection:**
  * Monitor network traffic or system logs for unexpected firmware or image downloads/uploads.
  * Detect anomalous user activities or privileged account misuse related to image modification.
* **Indicators of Compromise (IoCs):**
  * Unexplained changes in firmware versioning or unexpected firmware update events.
  * Presence of unknown or unauthorized firmware modules.
  * Detection of known malicious bootkits, rootkits, or firmware implants.
  * Anomalous file hashes or signatures of system images differing from officially distributed versions.

## Why it is Important to Detect This Technique

Early detection of "Modify System Image" attacks is critical due to the severe impacts and persistence this technique can achieve. Key reasons include:

* **Long-Term Persistence:**
  * Malicious modifications to firmware or OS images persist even after reboots, updates, or reinstalls, making remediation difficult and costly.
* **Stealth and Evasion:**
  * Attackers leveraging this technique often evade traditional security controls, antivirus solutions, and endpoint protection products.
* **Supply Chain Risks:**
  * Compromised system images distributed through trusted supply chains can rapidly propagate malicious code across multiple organizations and systems.
* **High-Level Privileges:**
  * Modified firmware or OS images typically run with kernel-level or firmware-level privileges, providing attackers unrestricted access to system resources and sensitive data.
* **Potential for Severe Damage:**
  * Attackers can leverage persistent access for espionage, data exfiltration, sabotage, ransomware deployment, or destructive attacks, causing significant operational disruption and financial loss.

## Examples

Several real-world incidents illustrate the use and impact of the "Modify System Image" technique:

* **ShadowHammer (ASUS Supply Chain Attack, 2019):**
  * Attackers compromised ASUS Live Update utility, embedding malicious code into legitimate firmware updates delivered to thousands of ASUS customers.
  * Malicious updates contained backdoors enabling attackers to target specific users based on MAC addresses.
  * Impact: Large-scale compromise affecting numerous users, demonstrating the wide-reaching consequences of modified system images within trusted supply chains.
* **LoJax UEFI Rootkit (APT28, 2018):**
  * Russian APT group (Fancy Bear/APT28) deployed LoJax, a UEFI rootkit capable of persisting across OS reinstalls and hard drive replacements.
  * Attackers modified UEFI firmware to embed persistent malicious code, providing stealthy and resilient access.
  * Impact: Highlighted the risks associated with firmware-level persistence and the difficulty of remediation, requiring firmware re-flashing or hardware replacement.
* **VPNFilter Malware (2018):**
  * Sophisticated malware infecting network devices by modifying firmware images in routers and network-attached storage devices.
  * Enabled attackers to intercept traffic, exfiltrate data, and render devices inoperable through destructive commands.
  * Impact: Over half a million devices infected worldwide, showcasing the significant threat posed by firmware-level modifications.
* **Operation ShadowPad (Supply Chain Attack, 2017):**
  * Attackers compromised NetSarang software distribution channels, embedding malicious code into legitimate software updates.
  * Modified software images facilitated backdoor access into victim networks.
  * Impact: Demonstrated the capability of attackers to infiltrate enterprise environments through trusted software updates, emphasizing the importance of detecting modified system images.

These examples underline the importance of robust detection, prevention, and response strategies to mitigate the risks associated with the "Modify System Image" technique.
