---
description: Compromise Infrastructure [T1584]
icon: lock
---

# Compromise Infrastructure

## Information

* Name: Compromise Infrastructure
* ID: T1584
* Tactics: [TA0042](../)
* Sub-Technique: [T1584.008](t1584.008.md), [T1584.003](t1584.003.md), [T1584.005](t1584.005.md), [T1584.006](t1584.006.md), [T1584.002](t1584.002.md), [T1584.007](t1584.007.md), [T1584.004](t1584.004.md), [T1584.001](t1584.001.md)

## Introduction

Compromise Infrastructure is a technique defined in the MITRE ATT\&CK framework (T1584), referring to adversaries exploiting or compromising third-party infrastructure to facilitate their malicious operations. Attackers commonly leverage compromised infrastructure to mask their identities, blend in with normal traffic, evade detection, and enhance the credibility of their malicious activities. This infrastructure can include compromised servers, domains, hosting providers, or cloud services that attackers use to command and control (C2), host malware, or stage attacks.

## Deep Dive Into Technique

Compromise Infrastructure involves attackers gaining unauthorized access to legitimate infrastructure to support their cyber operations. The following technical details outline common execution methods and mechanisms:

* **Server Exploitation:**
  * Attackers exploit vulnerabilities in web servers, databases, or application servers.
  * Common vulnerabilities exploited include SQL injection, remote code execution (RCE), and misconfigured services.
  * Once compromised, servers may host malware payloads, phishing pages, or act as proxy nodes for C2 communications.
* **Domain Hijacking:**
  * Attackers compromise domain registrar accounts or DNS providers through credential theft, social engineering, or exploiting vulnerabilities.
  * Compromised domains are redirected to attacker-controlled infrastructure, facilitating phishing attacks or malware distribution.
* **Cloud Infrastructure Exploitation:**
  * Attackers exploit misconfigured cloud services, weak credentials, or vulnerabilities in cloud-based applications.
  * Compromised cloud instances or storage buckets are used to host malicious payloads, serve as C2 servers, or exfiltrate data.
* **Content Delivery Networks (CDNs) Abuse:**
  * Attackers leverage compromised CDN accounts to distribute malware payloads or phishing content, benefiting from CDN reliability and trustworthiness.
* **Exploitation of Managed Service Providers (MSPs):**
  * Attackers compromise MSP infrastructure to gain access to multiple downstream client networks.
  * MSP compromise allows attackers to move laterally and distribute malware or ransomware widely.

## When this Technique is Usually Used

Attackers frequently utilize Compromise Infrastructure at various stages and scenarios throughout their cyber operations, including:

* **Initial Access and Delivery:**
  * Hosting malicious files, exploit kits, or phishing pages on compromised infrastructure to lure victims.
  * Delivering malware payloads via legitimate domains or servers to bypass security controls.
* **Command and Control (C2):**
  * Establishing covert communication channels via compromised servers or cloud infrastructure to evade detection.
  * Utilizing legitimate infrastructure to disguise malicious traffic as benign activity.
* **Data Exfiltration:**
  * Leveraging compromised cloud storage or servers to temporarily store stolen data before retrieval.
  * Masking exfiltration activities by routing through legitimate infrastructure.
* **Persistence and Lateral Movement:**
  * Using compromised third-party infrastructure to maintain persistent access to victim networks.
  * Facilitating lateral movement by leveraging trusted relationships with compromised MSPs or cloud providers.

## How this Technique is Usually Detected

Detection of Compromise Infrastructure typically involves a combination of methods, tools, and monitoring practices:

* **Network Traffic Analysis:**
  * Monitoring for unusual outbound communications to previously unknown or suspicious external IP addresses and domains.
  * Identifying anomalous DNS requests, DNS hijacking attempts, or unexpected redirections.
* **Endpoint Detection and Response (EDR):**
  * Detecting unusual processes or binaries downloaded from external compromised infrastructure.
  * Monitoring for abnormal behavior indicative of malware delivered via compromised infrastructure.
* **Threat Intelligence Feeds:**
  * Leveraging regularly updated threat intelligence to identify known compromised IP addresses, domains, and URLs.
  * Correlating network activity logs with threat intelligence indicators of compromise (IoCs).
* **Security Information and Event Management (SIEM):**
  * Aggregating and correlating logs from network devices, endpoints, and applications to detect suspicious infrastructure usage.
  * Alerting on abnormal login patterns, traffic anomalies, or suspicious file downloads.

### Indicators of Compromise (IoCs)

* IP addresses or domains identified by threat intelligence as compromised or malicious.
* Unusual DNS changes or unauthorized modifications to DNS records.
* Suspicious cloud infrastructure usage, such as unauthorized instances or buckets.
* Unexpected network connections to previously unseen external infrastructure.
* Anomalous traffic patterns or spikes in traffic to external cloud services or CDNs.

## Why it is Important to Detect This Technique

Early detection of Compromise Infrastructure is critical due to the significant potential impacts on networks, systems, and organizations:

* **Data Breaches and Exfiltration:**
  * Compromised infrastructure is commonly used to facilitate theft and exfiltration of sensitive or proprietary data.
  * Early detection prevents data loss, regulatory fines, and reputational damage.
* **Malware and Ransomware Delivery:**
  * Attackers frequently use compromised infrastructure to distribute malware or ransomware.
  * Prompt detection helps mitigate infection spread, minimize downtime, and reduce remediation costs.
* **Command and Control (C2) Operations:**
  * Compromised infrastructure enables attackers to maintain persistent and covert communication channels.
  * Detecting and disrupting compromised C2 infrastructure limits attacker persistence and reduces dwell time.
* **Operational and Financial Impact:**
  * Compromise of MSP or cloud infrastructure can disrupt multiple client networks simultaneously, amplifying operational impacts.
  * Early detection prevents widespread disruptions, financial losses, and potential legal liabilities.
* **Reputation and Trust:**
  * Organizations whose infrastructure is compromised may lose customer trust and suffer reputational harm.
  * Timely detection and remediation preserve stakeholder confidence and organizational credibility.

## Examples

Several real-world examples demonstrate the use of Compromise Infrastructure in cyber attacks:

* **SolarWinds Supply Chain Attack (SUNBURST):**
  * Attackers compromised SolarWinds' legitimate infrastructure to insert malicious code into software updates.
  * Malicious updates were distributed to thousands of organizations, enabling widespread espionage and data exfiltration.
  * Impact included significant breaches of government agencies and major enterprises.
* **Operation Cloud Hopper (APT10):**
  * Chinese threat actors compromised MSP infrastructure to infiltrate multiple client networks simultaneously.
  * Attackers leveraged compromised MSP infrastructure to exfiltrate sensitive intellectual property and trade secrets from targeted organizations globally.
  * Resulted in extensive data breaches and significant economic damage.
* **Magecart Attacks:**
  * Attackers compromised third-party web infrastructure, such as CDNs or JavaScript libraries, to inject malicious scripts.
  * Malicious scripts captured payment card details from e-commerce websites, resulting in large-scale data theft.
  * Impacted major retailers and e-commerce platforms, causing financial losses and reputational harm.
* **DNSpionage Campaign:**
  * Attackers compromised DNS infrastructure through registrar vulnerabilities and credential theft.
  * Redirected victim traffic to attacker-controlled servers, enabling espionage and credential harvesting.
  * Targeted government and critical infrastructure organizations, leading to sensitive data compromise.
* **Cloud Infrastructure Abuse (TeamTNT):**
  * Attackers exploited misconfigured cloud services and Docker APIs to deploy cryptomining malware.
  * Compromised cloud infrastructure used to mine cryptocurrencies, causing financial losses and resource exhaustion for victims.
  * Demonstrated the importance of securing cloud configurations and monitoring infrastructure usage.
