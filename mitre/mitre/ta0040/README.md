---
description: Impact [TA0040]
icon: burst
---

# Impact

## Information

* ID: TA0040

## Introduction

Impact is a tactic within the MITRE ATT\&CK framework that focuses on techniques adversaries use to disrupt availability, integrity, or confidentiality of systems and data. Unlike tactics aimed at gaining initial access or persistence, Impact techniques explicitly aim to harm the target organization by destroying, corrupting, manipulating, or interrupting the normal functioning of systems and data. Common objectives include service disruption, data destruction or encryption, defacement, and denial of service (DoS).

## Deep Dive Into Technique

Impact techniques can manifest in various forms, each with distinct execution methods and mechanisms:

* **Data Destruction:**
  * Overwriting or deleting critical files and data.
  * Utilizing tools like wipers (e.g., Shamoon, NotPetya) to render data irrecoverable.
  * Executing destructive scripts or commands (e.g., "rm -rf" in Unix/Linux systems, or "del /f /s /q" in Windows).
* **Data Encryption (Ransomware):**
  * Encrypting files using strong cryptographic algorithms (AES, RSA).
  * Delivering ransomware payloads via phishing emails, malicious websites, or compromised software updates.
  * Demanding ransom payments in cryptocurrency to provide decryption keys.
* **Denial of Service (DoS/DDoS):**
  * Flooding networks or servers with excessive traffic (UDP floods, SYN floods, HTTP floods).
  * Exploiting vulnerabilities or misconfigurations (e.g., amplification attacks using DNS or NTP servers).
  * Leveraging botnets to scale attack traffic volumes (e.g., Mirai botnet).
* **Resource Hijacking:**
  * Unauthorized use of system resources for cryptocurrency mining ("cryptojacking").
  * Deploying mining software on compromised hosts to consume CPU/GPU resources.
* **Defacement:**
  * Unauthorized modification of websites or public-facing resources.
  * Injecting malicious scripts or offensive content onto websites.
* **Account Access Removal:**
  * Deleting or disabling user accounts to impede legitimate access.
  * Modifying authentication mechanisms or credentials to lock out legitimate users.
* **Disk Wipe:**
  * Employing bootkits or malware to overwrite disk sectors, including Master Boot Record (MBR) or partition tables.
  * Using low-level disk manipulation tools to render systems unbootable or unrecoverable.

## When this Technique is Usually Used

Impact techniques commonly appear during specific stages and scenarios in cyberattacks, including:

* **Final Stages of Cyber Attacks:**
  * When adversaries have already extracted valuable data and seek to cover their tracks.
  * Retaliatory or destructive attacks aimed at damaging the victim organization's infrastructure.
* **Extortion and Financial Gain:**
  * Ransomware attacks designed to extort money through encrypted data.
  * Threatening denial-of-service attacks to demand ransom payments.
* **Hacktivism and Ideological Motivations:**
  * Defacement or disruption attacks to spread political or ideological messages.
  * Targeted resource hijacking or denial-of-service attacks against organizations perceived as adversaries.
* **State-Sponsored Cyber Warfare:**
  * Destructive attacks to cripple critical infrastructure (e.g., power grids, financial systems).
  * Coordinated cyber operations aimed at destabilizing or disrupting adversary nations or organizations.
* **Competitive Sabotage:**
  * Attacks aimed at disrupting business operations of competitors.
  * Data destruction or denial of service to harm reputation or operational capability.

## How this Technique is Usually Detected

Detection of Impact techniques involves multiple layers of monitoring and analysis, including:

* **Endpoint Detection and Response (EDR) Tools:**
  * Monitoring file system activities for mass deletions, modifications, or encryption.
  * Detecting suspicious processes or scripts indicative of ransomware or wiper malware.
* **Network Monitoring and Intrusion Detection Systems (IDS):**
  * Identifying unusual traffic patterns, such as large-scale outbound requests or abnormal spikes in network activity.
  * Detecting known denial-of-service attack signatures (e.g., SYN flood, UDP amplification).
* **Log Analysis and SIEM Solutions:**
  * Correlating logs from operating systems, applications, and security solutions to identify anomalies.
  * Detecting unauthorized account modifications, deletions, or privilege escalation attempts.
* **Integrity Monitoring Solutions:**
  * Monitoring file integrity for unauthorized changes or deletions.
  * Alerting on unexpected modifications to critical system files or configurations.
* **Threat Intelligence and IoCs:**
  * Leveraging known indicators of compromise, including:
    * Hashes of known ransomware or destructive malware.
    * Suspicious IP addresses or domains associated with command-and-control servers.
    * Registry keys or scheduled tasks indicative of persistence or destructive activities.
* **Behavioral Analytics:**
  * Identifying anomalous user or system behaviors, such as sudden spikes in resource usage (CPU, GPU, network bandwidth).
  * Detecting unusual account access patterns or authentication failures.

## Why it is Important to Detect This Technique

Early detection of Impact techniques is critical due to the severe consequences associated with these attacks, including:

* **Operational Downtime and Loss of Productivity:**
  * Service disruptions from denial-of-service or destructive attacks can halt critical business operations, causing significant financial losses.
* **Data Loss and Irrecoverable Damage:**
  * Data destruction or encryption without reliable backups can lead to permanent loss of critical business information and intellectual property.
* **Financial Losses and Extortion:**
  * Ransomware attacks often result in direct financial losses due to ransom payments, recovery costs, and potential fines or penalties.
* **Reputational Damage:**
  * Public-facing impacts, such as defacement or prolonged service outages, can seriously damage an organization's reputation and trust among customers, partners, and stakeholders.
* **Legal and Regulatory Consequences:**
  * Data breaches and disruptions may result in non-compliance with regulations (GDPR, HIPAA), leading to substantial legal penalties and fines.
* **National Security Risks:**
  * In critical infrastructure or governmental contexts, Impact techniques can threaten national security and public safety.

Early detection allows organizations to contain and mitigate these threats swiftly, minimizing damage and facilitating rapid recovery.

## Examples

Real-world examples illustrating Impact techniques include:

* **NotPetya Attack (2017):**
  * **Scenario:** State-sponsored attack targeting Ukraine, spreading globally.
  * **Tools Used:** NotPetya malware employing EternalBlue exploit, Mimikatz, and disk encryption/wiping techniques.
  * **Impact:** Over $10 billion in damages, widespread disruption of global enterprises, permanent data loss.
* **Shamoon Attack (2012, 2016, 2018):**
  * **Scenario:** Targeted attacks against Saudi Arabian oil and gas sectors.
  * **Tools Used:** Shamoon malware with disk wiping capabilities, overwriting MBR and data files.
  * **Impact:** Destruction of tens of thousands of workstations, severe disruption of operations.
* **WannaCry Ransomware (2017):**
  * **Scenario:** Global ransomware attack exploiting EternalBlue vulnerability.
  * **Tools Used:** WannaCry ransomware encrypting data and demanding Bitcoin ransom payments.
  * **Impact:** Over 200,000 systems affected globally, significant disruptions in healthcare, manufacturing, and government sectors.
* **Mirai Botnet DDoS Attack (2016):**
  * **Scenario:** IoT devices compromised to launch massive DDoS attacks.
  * **Tools Used:** Mirai malware infecting IoT devices, orchestrating large-scale DDoS attacks.
  * **Impact:** Major internet outages affecting services like Twitter, Netflix, and Amazon, highlighting vulnerabilities in IoT security.
* **Sony Pictures Hack (2014):**
  * **Scenario:** Destructive cyberattack attributed to nation-state actors.
  * **Tools Used:** Malware designed to erase data, disable systems, and leak sensitive information.
  * **Impact:** Extensive operational disruption, data leaks, reputational damage, and significant financial losses.

These examples emphasize the severity and broad applicability of Impact techniques, underscoring the necessity for proactive detection and response capabilities.
