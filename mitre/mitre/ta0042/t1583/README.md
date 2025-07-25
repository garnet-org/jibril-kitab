---
description: Acquire Infrastructure [T1583]
icon: lock
---

# Acquire Infrastructure

## Information

* Name: Acquire Infrastructure
* ID: T1583
* Tactics: [TA0042](../)
* Sub-Technique: [T1583.007](t1583.007.md), [T1583.008](t1583.008.md), [T1583.002](t1583.002.md), [T1583.005](t1583.005.md), [T1583.001](t1583.001.md), [T1583.004](t1583.004.md), [T1583.003](t1583.003.md), [T1583.006](t1583.006.md)

## Introduction

Acquire Infrastructure (T1583) is a technique documented within the MITRE ATT\&CK framework under the Resource Development tactic. It involves adversaries obtaining resources such as virtual private servers (VPS), domains, botnets, or compromised systems to support their malicious operations. These resources allow attackers to host command-and-control (C2) servers, malware payloads, phishing pages, and other infrastructure elements critical to the success of their cyber operations. By acquiring infrastructure, adversaries can mask their identities, increase redundancy, and enhance their operational security.

## Deep Dive Into Technique

Adversaries utilize various methods and mechanisms to acquire infrastructure, including:

* **Domain Registration:**
  * Registering new domains through legitimate registrars, often using false or stolen information, prepaid cards, or cryptocurrency to avoid attribution.
  * Leveraging privacy-protecting services (e.g., WHOIS privacy) to conceal registrant information.
* **Cloud and VPS Hosting:**
  * Purchasing virtual private servers or cloud instances from reputable providers (e.g., AWS, Azure, DigitalOcean, Linode) using stolen or fraudulent payment methods.
  * Utilizing compromised user accounts or credentials to provision cloud infrastructure without direct financial cost.
  * Exploiting free trial periods to establish temporary infrastructure for short-term operations.
* **Compromised Infrastructure:**
  * Gaining unauthorized access to existing servers and services through vulnerabilities, credential theft, or social engineering.
  * Utilizing botnets consisting of compromised hosts to distribute malware, conduct DDoS attacks, or proxy malicious traffic.
* **Bulletproof Hosting Providers:**
  * Engaging hosting providers known for ignoring abuse reports and law enforcement requests, thus ensuring longevity and stability for malicious infrastructure.
* **Proxy and VPN Services:**
  * Acquiring proxy services, VPN subscriptions, or compromised endpoints to mask attacker IP addresses and locations.
  * Using anonymization networks (e.g., Tor, I2P) to protect C2 communications and evade detection.

## When this Technique is Usually Used

Acquire Infrastructure typically occurs early in the adversary operational lifecycle, primarily during the preparation and staging phases. Common scenarios include:

* **Preparation and Reconnaissance:**
  * Establishing infrastructure prior to launching phishing campaigns, malware distribution, or targeted intrusions.
* **Initial Access and Delivery:**
  * Hosting malware payloads, phishing landing pages, or exploit kits on acquired infrastructure to facilitate initial compromise.
* **Command-and-Control (C2):**
  * Deploying C2 servers on acquired infrastructure to maintain persistent communication with compromised hosts.
* **Exfiltration and Data Storage:**
  * Storing exfiltrated data temporarily on acquired infrastructure before transferring it to attacker-controlled long-term storage locations.
* **Redundancy and Resilience:**
  * Establishing multiple redundant infrastructures to ensure operational continuity in case of takedowns or disruptions.

## How this Technique is Usually Detected

Detection involves monitoring, analyzing, and correlating various indicators and behaviors associated with infrastructure acquisition:

* **Domain Monitoring:**
  * Tracking newly registered domains, particularly those using privacy services or suspicious registrant details.
  * Identifying domains with unusual naming conventions or typosquatting patterns.
* **Network Traffic Analysis:**
  * Observing outbound connections to new or previously unknown IP addresses and domains.
  * Detecting traffic to known bulletproof hosting providers or anonymization networks (Tor, VPN endpoints).
* **Cloud Infrastructure Auditing:**
  * Monitoring cloud account activity logs for suspicious resource provisioning or unusual usage patterns.
  * Detecting unauthorized or anomalous access to cloud resources through security information and event management (SIEM) solutions.
* **Payment and Account Fraud Detection:**
  * Identifying fraudulent transactions or stolen payment methods used to acquire hosting services.
  * Correlating suspicious financial activities with infrastructure provisioning events.
* **Threat Intelligence Integration:**
  * Leveraging threat intelligence feeds and platforms to detect known malicious infrastructure or IP addresses.
  * Utilizing open-source intelligence (OSINT) to identify suspicious hosting providers or compromised hosts.

Specific Indicators of Compromise (IoCs) include:

* Newly registered domains with short lifespans or suspicious naming patterns.
* IP addresses and domains associated with known malicious hosting providers.
* Cloud instances provisioned from unusual geographic locations or IP addresses.
* Infrastructure provisioning using stolen or fraudulent payment methods.

## Why it is Important to Detect This Technique

Timely detection of infrastructure acquisition is critical due to several potential impacts:

* **Early Warning and Prevention:**
  * Identifying malicious infrastructure early can prevent subsequent stages of attacks, reducing the likelihood of successful compromises.
* **Reduced Dwell Time:**
  * Early detection and disruption of attacker infrastructure limits adversary dwell time and reduces the potential for lateral movement, data exfiltration, or damage.
* **Improved Incident Response:**
  * Understanding attacker infrastructure allows incident response teams to better respond, contain, and remediate threats effectively.
* **Minimized Operational Impact:**
  * Preventing attackers from establishing stable infrastructure reduces the risk of prolonged operational disruptions, data breaches, and financial losses.
* **Enhanced Threat Intelligence:**
  * Tracking infrastructure acquisition patterns provides valuable insights into adversary tactics, techniques, and procedures (TTPs) for future defense improvements.

## Examples

Real-world examples illustrating the Acquire Infrastructure technique include:

* **APT29 (Cozy Bear):**
  * Utilized legitimate cloud providers and compromised servers to host C2 infrastructure during the SolarWinds supply chain attack.
  * Leveraged multiple domains registered through anonymized services to evade attribution.
* **Emotet Malware Operations:**
  * Regularly acquired VPS hosting and compromised websites to distribute malware payloads and manage command-and-control infrastructure.
  * Frequently rotated domains and IP addresses to evade detection and maintain operational resilience.
* **APT41 (Winnti Group):**
  * Acquired cloud infrastructure using stolen credentials and fraudulent payment methods to support espionage and financially motivated cyber operations.
  * Established extensive infrastructure networks to host malware distribution servers and C2 endpoints.
* **Magecart Groups:**
  * Registered multiple domains and acquired compromised web servers as infrastructure to host malicious JavaScript skimmers targeting e-commerce websites.
  * Utilized bulletproof hosting services to maintain persistent malicious infrastructure despite takedown efforts.
* **FIN7 Cybercrime Operations:**
  * Leveraged compromised cloud accounts and legitimate hosting providers to establish phishing infrastructure and C2 servers.
  * Frequently changed infrastructure to evade detection and disruption by cybersecurity defenders.
