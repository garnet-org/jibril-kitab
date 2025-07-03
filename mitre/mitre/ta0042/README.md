---
description: Resource Development [TA0042]
icon: box
---

# Resource Development

## Information

* ID: TA0042

## Introduction

Resource Development is a tactic within the MITRE ATT\&CK framework that encompasses the preparatory activities adversaries undertake to establish resources necessary for executing cyberattacks. This tactic includes acquiring, configuring, and managing infrastructure, accounts, tools, and capabilities used throughout various stages of an attack lifecycle. Before launching an attack, adversaries carefully build and organize resources to ensure operational security, persistence, and effectiveness of their campaigns.

## Deep Dive Into Technique

Resource Development involves several technical methods and mechanisms adversaries use to prepare and support their operations. These include:

* **Infrastructure Acquisition and Configuration:**
  * Purchasing or renting servers, cloud instances, virtual private servers (VPS), and hosting services from legitimate providers.
  * Compromising legitimate websites or servers (such as web hosting providers) to use as command-and-control (C2) servers or staging platforms.
  * Registering domains and subdomains, often using domain generation algorithms (DGAs), typosquatting, or domain shadowing to evade detection.
* **Account Creation and Management:**
  * Creating email accounts, social media accounts, and messaging platform accounts to facilitate communication, spear-phishing campaigns, and distribution of malicious payloads.
  * Establishing accounts on public cloud platforms (AWS, Azure, Google Cloud) to host malicious infrastructure or payloads.
  * Managing operational security (OPSEC) by anonymizing account creation, using VPNs, proxies, or Tor networks to avoid attribution.
* **Tool Development and Acquisition:**
  * Developing custom malware, exploits, and payloads tailored to specific targets and environments.
  * Modifying and obfuscating publicly available tools (e.g., open-source penetration testing tools like Metasploit, Cobalt Strike, Empire, or Mimikatz) to evade detection.
  * Procuring commercial offensive software, malware-as-a-service, or exploit kits from underground marketplaces.
* **Capabilities Development and Testing:**
  * Conducting reconnaissance and scanning to identify vulnerabilities, misconfigurations, and potential entry points.
  * Testing developed malware, payload delivery methods, and command-and-control infrastructure in controlled environments to ensure reliability, stealth, and effectiveness.
  * Establishing redundant infrastructure to ensure continuity of operations if primary resources are detected or disrupted.

## When this Technique is Usually Used

Resource Development occurs primarily in the early stages of the cyberattack lifecycle and continues throughout operations as needed. Attack scenarios and stages include:

* **Pre-Attack Preparation:**
  * Before initial access, adversaries establish infrastructure, create accounts, and test tools to ensure successful entry into targeted networks.
  * Domain registration and infrastructure procurement happen weeks or months in advance to avoid suspicion.
* **Initial Access and Delivery:**
  * Setting up phishing email accounts, compromised websites, and malicious domains to deliver payloads and initiate infections.
  * Leveraging cloud infrastructure and legitimate services to host malware payloads or redirect victims.
* **Command-and-Control (C2) Establishment:**
  * Deploying servers and infrastructure to facilitate secure, reliable, and stealthy communication with infected hosts.
  * Preparing backup C2 channels and redundant infrastructure to maintain persistent access.
* **Exfiltration and Data Storage:**
  * Establishing cloud storage accounts, FTP servers, or compromised websites to temporarily store and exfiltrate stolen data.
  * Using legitimate cloud services (e.g., Dropbox, Google Drive, AWS S3) to blend into normal network traffic and evade detection.
* **Lateral Movement and Persistence:**
  * Developing and deploying specialized tools and scripts tailored to specific target environments to facilitate lateral movement and persistence.
  * Maintaining repositories of tools and exploits for repeated use across multiple compromised hosts and networks.

## How this Technique is Usually Detected

Detection of Resource Development activities involves monitoring infrastructure, accounts, and tooling used by adversaries. Common detection methods and tools include:

* **Domain and Infrastructure Monitoring:**
  * Monitoring domain registrations for suspicious patterns such as typosquatting, DGAs, or rapid bulk registrations.
  * Using threat intelligence platforms (e.g., VirusTotal, RiskIQ, DomainTools) to identify malicious or suspicious domains and IP addresses.
  * Identifying infrastructure overlap through passive DNS analysis and SSL certificate analysis.
* **Account Creation and Usage Monitoring:**
  * Detecting anomalous account creation patterns (e.g., multiple accounts created from similar IP addresses or unusual geographical locations).
  * Monitoring cloud service usage logs (AWS CloudTrail, Azure Audit Logs, GCP Audit Logs) for unusual account activities, resource provisioning, or rapid infrastructure changes.
  * Identifying suspicious email accounts, social media profiles, or messaging platform accounts through behavioral analytics and threat intelligence feeds.
* **Tool and Malware Detection:**
  * Employing sandbox analysis tools (e.g., Cuckoo Sandbox, Hybrid Analysis) to detect malicious payloads during testing phases.
  * Using endpoint detection and response (EDR) solutions (e.g., CrowdStrike Falcon, Carbon Black, Microsoft Defender ATP) to detect malicious binaries, scripts, or tool usage.
  * Monitoring public code repositories (e.g., GitHub, GitLab) for adversaries publicly hosting or modifying tools and exploits.
* **Indicators of Compromise (IoCs):**
  * Suspicious domain names and IP addresses associated with known threat actors.
  * SSL/TLS certificates reused across multiple malicious domains.
  * File hashes, filenames, or specific strings associated with known malware tools and frameworks.
  * Anomalous cloud infrastructure or hosting providers frequently leveraged by threat actors.

## Why it is Important to Detect This Technique

Early detection of Resource Development activities significantly reduces the risk and potential impact of cyberattacks. Importance includes:

* **Proactive Threat Mitigation:**
  * Identifying adversary infrastructure and tooling before attacks occur enables proactive blocking, blacklisting, or takedown actions.
  * Early detection disrupts adversaries' operational timelines, forcing them to spend additional resources and time rebuilding infrastructure.
* **Reducing Attack Surface:**
  * Detecting and blocking malicious domains, IP addresses, and accounts reduces the available attack surface for initial access and command-and-control activities.
  * Monitoring infrastructure development helps defenders identify potential vulnerabilities and misconfigurations targeted by adversaries.
* **Operational Security (OPSEC) Insight:**
  * Understanding adversaries' resource development methods provides valuable intelligence on their capabilities, intentions, and attribution.
  * Enables organizations to anticipate adversary behavior, improve defenses, and inform threat hunting activities.
* **Minimizing Damage and Loss:**
  * Early disruption of adversary infrastructure prevents successful delivery of malware and reduces the likelihood of successful data exfiltration.
  * Preventing adversaries from establishing persistent access minimizes potential long-term damage to networks and systems.

## Examples

Real-world examples of Resource Development include:

* **APT29 (Cozy Bear) and SolarWinds Supply Chain Attack:**
  * Attackers registered domains mimicking legitimate SolarWinds services months in advance.
  * Used compromised cloud infrastructure and legitimate hosting providers for command-and-control.
  * Leveraged customized malware (SUNBURST) and specialized tooling to evade detection and maintain stealth.
* **Lazarus Group and Cryptocurrency Theft Campaigns:**
  * Created multiple fake cryptocurrency exchange websites and domains to trick users and steal credentials.
  * Leveraged cloud infrastructure and compromised web hosting to distribute malicious payloads and maintain persistence.
  * Developed custom malware and obfuscated publicly available tools to evade detection.
* **FIN7 Cybercrime Group:**
  * Established extensive infrastructure, including multiple domains, email accounts, and cloud hosting services for phishing campaigns and malware delivery.
  * Customized Cobalt Strike payloads and tools for targeted attacks against financial institutions and retail companies.
  * Managed redundant infrastructure to quickly pivot and continue operations after detection and takedowns.
* **Magecart Web Skimming Attacks:**
  * Attackers compromised legitimate e-commerce websites and cloud hosting providers to host malicious JavaScript skimmers.
  * Developed infrastructure to collect and exfiltrate stolen payment card data through legitimate-looking domains and services.
  * Continuously rotated domains and infrastructure to evade detection and maintain operational persistence.
