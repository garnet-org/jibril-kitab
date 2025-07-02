---
description: Encrypted Channel [T1573]
icon: lock
---

# Encrypted Channel

## Information

* Name: Encrypted Channel
* ID: T1573
* Tactics: [TA0011](../)
* Sub-Technique: [T1573.001](t1573.001.md), [T1573.002](t1573.002.md)

## Introduction

Encrypted Channel (MITRE ATT\&CK ID: T1573) refers to adversaries leveraging encrypted communication channels to conceal command and control (C2) traffic, data exfiltration, or lateral movement within compromised networks. By using encryption, attackers aim to evade detection, bypass security controls, and maintain persistent, covert access to target environments. This technique is categorized under the Command and Control tactic within the MITRE ATT\&CK framework and is commonly utilized by sophisticated threat actors.

## Deep Dive Into Technique

Attackers often establish encrypted channels using standard protocols, custom encryption schemes, or legitimate encryption tools to mask malicious traffic. The following are common execution methods and mechanisms:

* **Standard Encrypted Protocols:**
  * HTTPS (TLS/SSL): Attackers commonly use HTTPS to blend malicious traffic with legitimate web traffic.
  * SSH: Secure Shell protocol is frequently abused for remote command execution, tunneling, or lateral movement.
  * VPNs: Attackers may leverage VPN connections to hide C2 traffic or exfiltrate sensitive data.
* **Custom Encryption Schemes:**
  * Proprietary encryption methods or obfuscation techniques may be employed to evade detection by traditional security solutions.
  * Attackers might use symmetric or asymmetric encryption algorithms (AES, RSA, ECC) to secure communications.
* **Encrypted Tunnels:**
  * Tunneling tools (e.g., stunnel, OpenVPN, DNS-over-HTTPS, DNS-over-TLS) can encapsulate malicious traffic within legitimate encrypted protocols.
  * Encrypted DNS protocols are increasingly exploited to hide malicious DNS queries and responses.
* **Encryption in Malware:**
  * Malware payloads often embed encryption routines to encrypt C2 communications, making traffic analysis difficult.
  * Malware families such as TrickBot, Emotet, and Cobalt Strike commonly implement encrypted channels for stealth.

Attackers may also leverage legitimate cloud services (e.g., cloud storage providers, messaging platforms) that inherently use encryption to mask malicious communications.

## When this Technique is Usually Used

Encrypted channel techniques are prevalent across multiple stages of cyber-attacks, including:

* **Initial Access and Delivery:**
  * Malware delivery via encrypted channels (e.g., HTTPS downloads, encrypted email attachments).
* **Command and Control (C2):**
  * Establishing encrypted C2 channels to evade detection and monitoring tools.
  * Maintaining persistent and covert communication with compromised systems.
* **Lateral Movement:**
  * Utilizing encrypted protocols (e.g., SSH, RDP with TLS) to move laterally within networks without detection.
* **Data Exfiltration:**
  * Exfiltrating sensitive data through encrypted channels (HTTPS, SFTP, encrypted cloud storage) to avoid detection by network monitoring tools.

Encrypted channel techniques are particularly favored by advanced persistent threats (APTs), cybercriminal groups, and state-sponsored actors to maintain stealth and evade defensive measures.

## How this Technique is Usually Detected

Detection of encrypted channel usage requires specialized monitoring tools and proactive security measures, including:

* **Traffic Analysis and Network Monitoring:**
  * Monitoring network traffic for unusual patterns, anomalous encrypted sessions, or unexpected protocol usage.
  * Analyzing TLS/SSL handshake metadata (certificate anomalies, unusual cipher suites, or unexpected certificate issuers).
* **Endpoint Detection and Response (EDR):**
  * Identifying suspicious processes initiating encrypted connections.
  * Monitoring for unusual usage of encryption libraries, suspicious binaries, or unexpected encryption tool installations.
* **Deep Packet Inspection (DPI):**
  * Utilizing SSL/TLS decryption appliances or proxies to inspect encrypted traffic (where permitted).
  * Detecting suspicious payloads or malicious behaviors within decrypted traffic.
* **Behavioral Analytics and Machine Learning:**
  * Leveraging behavioral analytics to detect anomalies in encrypted traffic patterns, data flows, or protocol misuse.
  * Machine learning algorithms trained to identify malicious encrypted traffic based on known indicators.
* **Indicators of Compromise (IoCs):**
  * Suspicious digital certificates (self-signed, expired, unusual issuers).
  * Known malicious domains or IP addresses associated with encrypted C2 channels.
  * Abnormal use of encryption tools (stunnel, OpenVPN, SSH tunnels) on endpoints.
  * Unusual port and protocol combinations (e.g., HTTPS traffic on non-standard ports).

## Why it is Important to Detect This Technique

Early detection of encrypted channel usage is critical due to the following impacts and risks:

* **Stealthy Persistence:**
  * Attackers may remain undetected within networks for extended periods, increasing the risk of data theft, espionage, or sabotage.
* **Data Exfiltration:**
  * Sensitive data can be exfiltrated securely, potentially leading to significant financial losses, regulatory penalties, and reputational damage.
* **Command and Control Evasion:**
  * Encrypted channels allow attackers to bypass traditional security controls, complicating incident response and forensic investigations.
* **Increased Incident Response Complexity:**
  * Late detection of encrypted channel usage significantly complicates remediation efforts, increasing response time and associated costs.
* **Regulatory and Compliance Risks:**
  * Failure to detect encrypted exfiltration channels may result in compliance violations (e.g., GDPR, HIPAA), fines, and legal consequences.

Early and accurate detection of encrypted channel activity enables rapid containment, reduces damage, and improves overall security posture.

## Examples

Real-world examples of encrypted channel usage include:

* **APT29 (Cozy Bear):**
  * Utilized encrypted HTTPS channels and custom encryption mechanisms to communicate with C2 servers during the SolarWinds supply chain attack.
  * Leveraged encrypted DNS protocols for covert communications.
* **Emotet Malware:**
  * Employed HTTPS communication channels with encrypted payloads to evade network detection.
  * Frequently rotated encryption keys and domains to further obfuscate activity.
* **TrickBot Trojan:**
  * Used encrypted communications over HTTPS to securely deliver payloads, receive commands, and exfiltrate stolen data.
  * Implemented robust encryption routines to evade inspection and detection.
* **FIN7 Cybercriminal Group:**
  * Leveraged encrypted SSH tunnels and VPN connections to maintain covert access, move laterally, and exfiltrate payment card data from compromised retail networks.
* **Cobalt Strike Framework:**
  * Widely used by threat actors to establish encrypted HTTPS channels for command and control, lateral movement, and data exfiltration.
  * Offers flexible encryption options, making detection challenging.

These examples highlight the widespread and effective use of encrypted channels by sophisticated attackers to evade detection, maintain persistent access, and achieve malicious objectives.
