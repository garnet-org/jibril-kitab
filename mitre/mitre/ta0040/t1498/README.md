---
description: Network Denial of Service [T1498]
icon: house-water
---

# Network Denial of Service

## Information

* Name: Network Denial of Service
* ID: T1498
* Tactics: [TA0040](../)
* Sub-Technique: [T1498.001](t1498.001.md), [T1498.002](t1498.002.md)

## Introduction

Network Denial of Service (DoS) is a technique categorized under MITRE ATT\&CK Framework as tactic ID T1498. It involves overwhelming targeted networks or systems with excessive traffic or requests, causing service disruption, downtime, or degraded performance. Attackers commonly employ this technique to disrupt business operations, distract defenders, or mask other malicious activities occurring concurrently.

## Deep Dive Into Technique

Network Denial of Service attacks aim to exhaust system resources such as bandwidth, CPU cycles, memory, or storage capacity. Attackers typically employ one or more of the following methods:

* **Volumetric Attacks**: Flooding the targeted network with massive amounts of traffic to overwhelm bandwidth and network infrastructure. Common protocols exploited include UDP, ICMP, DNS amplification, and NTP amplification.
* **Protocol Attacks**: Exploiting vulnerabilities or weaknesses in network protocols to consume server resources. Examples include SYN flood attacks, TCP connection exhaustion, and fragmented packet attacks.
* **Application-Layer Attacks**: Targeting specific applications or services (e.g., HTTP, DNS, SMTP) with seemingly legitimate requests to exhaust server resources and degrade performance.

Attackers frequently leverage botnets—networks of compromised devices—to amplify the scale and impact of the attack. Botnets enable attackers to generate large volumes of malicious traffic from distributed sources, complicating detection and mitigation efforts.

## When this Technique is Usually Used

Network Denial of Service attacks are commonly utilized in various attack scenarios and stages, including:

* **Initial Access and Reconnaissance**:
  * Attackers may perform DoS attacks to test network resilience and response capabilities of targeted organizations.
* **Disruption and Sabotage**:
  * Politically motivated attackers or hacktivists employ DoS attacks to disrupt operations, damage reputation, or cause financial losses.
  * Nation-state actors may use DoS to disrupt critical infrastructure or communication channels during cyber warfare or espionage campaigns.
* **Diversionary Tactics**:
  * Attackers may launch DoS attacks as a smokescreen to divert attention away from simultaneous, more sophisticated attacks (e.g., data exfiltration, lateral movement, or malware deployment).
* **Extortion and Ransom**:
  * Cybercriminals may threaten or execute DoS attacks against organizations to demand ransom payments for cessation of attacks or future protection.

## How this Technique is Usually Detected

Effective detection methods for Network Denial of Service attacks include:

* **Traffic Analysis and Monitoring**:
  * Network monitoring tools (e.g., Wireshark, tcpdump, NetFlow analyzers) identify abnormal spikes in traffic volume or unusual patterns indicative of DoS activity.
  * Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) detect protocol anomalies, malformed packets, and known attack signatures.
* **Performance Monitoring**:
  * System and application performance metrics (CPU, memory utilization, network latency, response time) can indicate resource exhaustion or degradation due to DoS attacks.
* **Security Information and Event Management (SIEM)**:
  * Aggregation and correlation of system logs, firewall events, and network device alerts help identify coordinated attack patterns and suspicious traffic sources.
* **Specific Indicators of Compromise (IoCs)**:
  * Sudden unexplained bandwidth consumption or traffic spikes
  * Excessive connection attempts from single or multiple IP addresses
  * High volume of SYN packets without completion of TCP handshakes
  * Unusual DNS or NTP request volumes indicative of amplification attacks
  * Repeated HTTP requests targeting specific resource-intensive pages or APIs

## Why it is Important to Detect This Technique

Timely detection and mitigation of Network Denial of Service attacks are critical due to their significant impacts, including:

* **Operational Disruption**:
  * Prolonged downtime or degraded service availability negatively affects business continuity, productivity, and customer satisfaction.
* **Financial Losses**:
  * Direct financial impacts due to lost revenue, recovery costs, remediation expenses, and potential ransom payments.
* **Reputational Damage**:
  * Service outages or disruptions can severely damage an organization's reputation and customer trust.
* **Security Risks**:
  * DoS attacks may serve as a diversionary tactic, masking other malicious activities such as data exfiltration, malware deployment, or lateral movement.
* **Regulatory and Compliance Implications**:
  * Organizations may face regulatory penalties or legal consequences due to failure to maintain service availability or protect sensitive data during a DoS attack.

Early detection enables rapid response, minimizing potential damage, preserving business continuity, and maintaining stakeholder confidence.

## Examples

Real-world examples of Network Denial of Service attacks include:

* **Mirai Botnet Attack (2016)**:
  * **Scenario**: Attackers leveraged a botnet composed of compromised IoT devices to conduct massive DDoS attacks against DNS provider Dyn.
  * **Tools Used**: Mirai malware, compromised IoT devices (cameras, routers).
  * **Impact**: Major internet services (Twitter, Netflix, Reddit, GitHub) experienced significant outages and disruptions, highlighting IoT vulnerabilities.
* **GitHub DDoS Attack (2018)**:
  * **Scenario**: Attackers executed a volumetric attack via memcached amplification, generating approximately 1.35 Tbps of traffic directed at GitHub infrastructure.
  * **Tools Used**: Memcached servers exploited for amplification, spoofed UDP packets.
  * **Impact**: GitHub services temporarily disrupted; mitigated quickly through traffic filtering and DDoS protection services.
* **Estonian Cyberattacks (2007)**:
  * **Scenario**: Politically motivated attackers launched coordinated DoS attacks against Estonian government websites, banks, and media organizations.
  * **Tools Used**: Botnets, ICMP floods, SYN floods, HTTP floods.
  * **Impact**: Extended disruption of critical online services, significant economic and political consequences, and increased awareness of cyber warfare threats.
* **Cloudflare Mitigation of Record DDoS Attack (2022)**:
  * **Scenario**: Cloudflare mitigated a record-breaking HTTPS DDoS attack peaking at 26 million requests per second.
  * **Tools Used**: Distributed botnet, HTTP/HTTPS request floods.
  * **Impact**: Demonstrated increasing scale of attacks and importance of strong DDoS mitigation strategies and infrastructure.

These examples illustrate the diverse motivations, attack methods, and potential impacts associated with Network Denial of Service attacks, emphasizing the importance of proactive detection and mitigation strategies.
