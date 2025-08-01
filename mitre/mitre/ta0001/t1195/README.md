---
description: Supply Chain Compromise [T1195]
icon: lock
---

# Supply Chain Compromise

## Information

* Name: Supply Chain Compromise
* ID: T1195
* Tactics: [TA0001](../)
* Sub-Technique: [T1195.001](t1195.001.md), [T1195.003](t1195.003.md), [T1195.002](t1195.002.md)

## Introduction

Supply Chain Compromise (T1195) is a critical adversarial technique categorized under the MITRE ATT\&CK framework. This technique involves attackers infiltrating organizations indirectly through suppliers, vendors, or third-party services. Attackers exploit the implicit trust relationship between organizations and their suppliers to gain unauthorized access, introduce malicious components, or compromise software/hardware products during their development, manufacturing, or distribution stages. Such compromises allow attackers to bypass traditional security measures, making them challenging to detect and mitigate.

## Deep Dive Into Technique

Supply Chain Compromise can occur at various stages within the supply chain lifecycle, including software development, hardware manufacturing, software distribution, and third-party service provision. Attackers leverage several technical methods and mechanisms to execute this technique:

* **Software Development Compromise:**
  * Injecting malicious code into legitimate software repositories, build systems, or libraries.
  * Compromising developer accounts or version control systems (e.g., GitHub, GitLab).
  * Manipulating Continuous Integration/Continuous Deployment (CI/CD) pipelines to insert malicious artifacts.
* **Hardware Supply Chain Compromise:**
  * Introducing compromised or counterfeit hardware components during manufacturing.
  * Embedding malicious firmware or microcode into hardware devices during production.
  * Tampering with hardware during shipping or storage to insert malicious implants.
* **Distribution and Update Mechanism Compromise:**
  * Hijacking legitimate software update channels to distribute malware or backdoors.
  * Compromising software distribution platforms and package managers (e.g., npm, PyPI, Maven) to deliver malicious packages.
* **Third-party Service Provider Compromise:**
  * Breaching managed service providers (MSPs) or cloud service providers to access multiple downstream customers.
  * Exploiting trust relationships between organizations and third-party vendors to pivot into target networks.

Attackers often utilize advanced persistent threat (APT) methodologies, combining stealth, persistence, and lateral movement techniques to maximize the effectiveness of the compromise.

## When this Technique is Usually Used

Attackers typically employ Supply Chain Compromise in scenarios where direct attacks against a target organization are challenging, costly, or less likely to succeed. This technique is frequently used at various attack stages and scenarios:

* **Initial Access Phase:**
  * Gaining initial footholds into otherwise secure organizations through trusted third-party software or hardware.
  * Leveraging compromised software updates to deliver malware payloads directly into protected environments.
* **Persistence and Lateral Movement:**
  * Maintaining long-term persistence through compromised hardware or software components.
  * Using trusted third-party connections and credentials to move laterally and escalate privileges within victim networks.
* **Espionage and Intelligence Gathering:**
  * Targeting software developers, hardware manufacturers, or service providers to infiltrate multiple related targets simultaneously.
  * Conducting espionage activities by embedding hidden backdoors or implants into widely adopted software/hardware.
* **Sabotage and Disruption:**
  * Introducing malicious modifications into critical infrastructure components.
  * Executing destructive payloads delivered through compromised supply chain channels to disrupt operations or cause physical damage.

## How this Technique is Usually Detected

Detecting Supply Chain Compromise requires vigilance, proactive monitoring, and specialized detection strategies. Common detection methods, tools, and indicators of compromise (IoCs) include:

* **Software Integrity and Code Auditing:**
  * Regularly auditing and verifying source code repositories and build processes.
  * Comparing software binaries against known-good hashes and signatures.
* **Behavioral Monitoring and Anomaly Detection:**
  * Using Endpoint Detection and Response (EDR) and Security Information and Event Management (SIEM) solutions to detect unusual software behavior or unauthorized network connections.
  * Monitoring software update processes and distribution channels for unexpected changes or deviations.
* **Threat Intelligence and IoC Feeds:**
  * Leveraging threat intelligence platforms to identify compromised software packages, domains, IP addresses, or malicious certificates.
  * Monitoring public advisories and security bulletins regarding compromised third-party software or hardware.
* **Network Traffic Analysis and DNS Monitoring:**
  * Analyzing outbound network traffic for connections to suspicious domains or IP addresses.
  * Monitoring DNS requests for unusual or newly registered domains associated with known threat actors.
* **Hardware Inspection and Firmware Analysis:**
  * Physically inspecting hardware components for signs of tampering, unauthorized modifications, or counterfeit components.
  * Conducting firmware analysis and reverse engineering to detect unauthorized implants or malicious code.

Indicators of compromise (IoCs) specific to Supply Chain Compromise include:

* Unexpected or undocumented software updates.
* Unauthorized changes in software binaries or hardware firmware.
* Suspicious outbound network connections from trusted software or hardware devices.
* Use of compromised digital certificates or code-signing keys.
* Unusual build artifacts or anomalies in CI/CD pipelines.

## Why it is Important to Detect This Technique

Early detection of Supply Chain Compromise is critical due to the severe and widespread impacts it can have on organizations, systems, and networks. Key reasons for prioritizing detection include:

* **Widespread Impact and Scale:**
  * Supply chain attacks can simultaneously affect multiple organizations, industries, and critical infrastructure, amplifying their overall impact.
  * Compromise of widely adopted software or hardware can rapidly propagate malware across numerous organizations globally.
* **Difficulty of Remediation:**
  * Once compromised components are deployed, remediation can be complex, costly, and time-consuming.
  * Organizations may need to replace hardware, rebuild systems, or extensively audit software codebases to ensure safety.
* **Increased Risk of Persistence and Stealth:**
  * Supply chain compromises often remain undetected for extended periods due to implicit trust in suppliers and third-party components.
  * Attackers can maintain persistent, stealthy access to sensitive systems and data, increasing the risk of data breaches, espionage, or sabotage.
* **Operational and Financial Impacts:**
  * Supply chain compromises can lead to significant operational disruptions, downtime, and financial losses.
  * Organizations may face regulatory fines, legal liabilities, reputational damage, and loss of customer trust.
* **National Security Concerns:**
  * Supply chain attacks targeting critical infrastructure or government entities pose significant risks to national security.
  * Malicious actors can disrupt essential services, steal sensitive information, or carry out espionage activities against government agencies.

## Examples

Several real-world examples illustrate the severity and complexity of Supply Chain Compromise attacks:

* **SolarWinds Orion Attack (2020):**
  * Attack Scenario: Attackers compromised SolarWinds' software build system and injected malicious code into legitimate Orion software updates.
  * Tools Used: SUNBURST backdoor, TEARDROP malware, custom implants.
  * Impacts: Approximately 18,000 organizations downloaded compromised updates, including U.S. government agencies, Fortune 500 companies, and critical infrastructure providers. Attackers gained persistent, stealthy access to sensitive networks.
* **NotPetya Attack via M.E.Doc Software (2017):**
  * Attack Scenario: Attackers compromised Ukrainian tax software M.E.Doc and distributed malicious software updates containing the NotPetya ransomware/wiper.
  * Tools Used: NotPetya malware, EternalBlue exploit, Mimikatz credential harvesting tool.
  * Impacts: Massive global disruption affecting organizations worldwide, causing billions of dollars in financial losses and operational downtime.
* **ASUS Live Update Attack (Operation ShadowHammer, 2018-2019):**
  * Attack Scenario: Attackers compromised ASUS software update servers to distribute malicious updates to targeted ASUS laptop users.
  * Tools Used: Trojanized ASUS Live Update utility, customized malware payloads.
  * Impacts: Hundreds of thousands of ASUS users downloaded compromised updates, allowing attackers to target specific high-value individuals with precision.
* **CCleaner Supply Chain Attack (2017):**
  * Attack Scenario: Attackers infiltrated Piriform's software development environment and embedded malicious code into legitimate CCleaner software updates.
  * Tools Used: Backdoored CCleaner installer, secondary-stage malware payloads.
  * Impacts: Approximately 2.27 million users downloaded compromised versions, with attackers selectively targeting technology companies for further exploitation.
* **Dependency Confusion Attacks (2021):**
  * Attack Scenario: Security researchers demonstrated the possibility of compromising software supply chains by uploading malicious packages to public repositories with names matching internal private packages.
  * Tools Used: Malicious npm, PyPI, RubyGems packages.
  * Impacts: Potential for widespread compromise across numerous organizations relying on package managers, highlighting critical vulnerabilities in software dependency management.

These examples underscore the importance of comprehensive detection, prevention, and response strategies to mitigate the severe risks posed by Supply Chain Compromise attacks.
