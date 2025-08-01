---
description: Phishing [T1566]
icon: lock
---

# Phishing

## Information

* Name: Phishing
* ID: T1566
* Tactics: [TA0001](../)
* Sub-Technique: [T1566.002](t1566.002.md), [T1566.001](t1566.001.md), [T1566.004](t1566.004.md), [T1566.003](t1566.003.md)

## Introduction

Phishing (T1566) is a social engineering technique classified within the MITRE ATT\&CK framework under the "Initial Access" tactic. Attackers utilize phishing to deceive users into revealing sensitive information, downloading malware, or granting unauthorized access. This technique typically involves sending carefully crafted emails, messages, or links that appear legitimate, aiming to trick users into performing actions beneficial to attackers. Phishing remains one of the most common and effective initial access vectors used by threat actors.

## Deep Dive Into Technique

Phishing attacks primarily exploit human psychology, trust, and lack of awareness. Attackers typically execute phishing through the following methods:

* **Email Phishing**:
  * Attackers send fraudulent emails impersonating trusted entities such as banks, government agencies, or well-known companies.
  * Emails often contain malicious attachments (e.g., weaponized documents, macros, or executables) or links to malicious websites designed to steal credentials or distribute malware.
  * Techniques include spoofing sender addresses, using similar domain names (typosquatting), and employing urgent or authoritative language to pressure victims into action.
* **Spear Phishing**:
  * Highly targeted phishing attacks directed toward specific individuals, organizations, or roles.
  * Attackers conduct extensive reconnaissance to personalize messages, increasing the likelihood of success.
  * Commonly used in advanced persistent threat (APT) campaigns to gain initial footholds in targeted networks.
* **Whaling**:
  * Specialized spear phishing targeting high-ranking executives or individuals with privileged access.
  * Often involves sophisticated social engineering tactics, leveraging publicly available information to craft highly convincing messages.
* **Smishing and Vishing**:
  * Smishing involves phishing via SMS or text messages, often containing malicious links or requests for sensitive information.
  * Vishing (voice phishing) involves phone calls impersonating legitimate entities to trick victims into providing confidential data or access.

Attackers employ various technical mechanisms to enhance phishing effectiveness, including:

* Using compromised legitimate email accounts or domains to bypass spam filters.
* Implementing URL shortening services to obscure malicious links.
* Employing HTTPS certificates (often free or easily obtained certificates) to appear trustworthy.
* Hosting phishing pages on compromised legitimate websites or cloud services to evade detection.
* Utilizing obfuscation techniques within malicious attachments to bypass antivirus and endpoint detection solutions.

## When this Technique is Usually Used

Phishing can appear across multiple stages and scenarios of an attack lifecycle, most prominently during:

* **Initial Access Stage**:
  * Attackers commonly use phishing to gain initial entry into a victim's network or system.
  * Phishing emails containing malicious attachments or links are frequently the first vector in APT campaigns, ransomware attacks, and credential harvesting operations.
* **Credential Harvesting**:
  * Attackers use phishing websites or forms to trick users into entering credentials, enabling further lateral movement and privilege escalation.
* **Malware Delivery**:
  * Phishing emails often deliver malware payloads such as remote access trojans (RATs), ransomware, or banking trojans.
* **Social Engineering for Further Exploitation**:
  * Attackers may use phishing repeatedly within a campaign to maintain persistence, escalate privileges, or move laterally within a compromised environment.
* **Business Email Compromise (BEC)**:
  * Attackers impersonate executives or trusted partners to request wire transfers or sensitive data.

## How this Technique is Usually Detected

Detection of phishing involves multiple layers of security controls, user awareness, and technical indicators. Common detection methods and tools include:

* **Email Filtering Solutions**:
  * Spam filters, secure email gateways (SEGs), and advanced threat protection platforms analyze email headers, attachments, and embedded links for malicious indicators.
* **Endpoint Detection and Response (EDR)**:
  * Detects suspicious behavior or malicious attachments executed on endpoints, such as macro execution, suspicious script behavior, or unusual file downloads.
* **Network Monitoring and Intrusion Detection Systems (IDS)**:
  * Identifies anomalous network traffic patterns, unusual DNS queries, access to known malicious domains, or command-and-control (C2) communications.
* **User Reporting and Security Awareness Training**:
  * Employees trained to recognize phishing indicators (poor grammar, unexpected attachments, suspicious sender addresses) can report suspicious emails for further analysis.
* **Domain Monitoring and Threat Intelligence Feeds**:
  * Monitoring newly registered domains, typosquatting domains, and incorporating external threat intelligence (e.g., phishing URLs, IP addresses, malicious hashes) into security tools.

Specific indicators of compromise (IoCs) include:

* Suspicious email sender addresses (e.g., slight misspellings, unfamiliar domains).
* Malicious attachments (e.g., documents containing macros, scripts, executables).
* URLs pointing to domains with typos or unusual characters.
* HTTP/HTTPS requests to known phishing domains or IP addresses.
* Unexpected user credential exposure or login attempts from unfamiliar locations.

## Why it is Important to Detect This Technique

Early detection of phishing is critical due to its substantial impacts on systems, networks, and organizations, including:

* **Credential Theft and Unauthorized Access**:
  * Phishing attacks often lead to compromised credentials, enabling attackers to gain unauthorized access, escalate privileges, and move laterally within the network.
* **Malware Infection**:
  * Phishing emails frequently distribute malware, including ransomware, which can cause significant operational disruption, data loss, and financial damage.
* **Financial Loss**:
  * Phishing attacks, especially BEC campaigns, can result in direct financial losses through fraudulent wire transfers or unauthorized transactions.
* **Reputational Damage**:
  * Successful phishing compromises can lead to data breaches, exposing sensitive customer data and negatively impacting an organization's reputation and customer trust.
* **Compliance and Legal Consequences**:
  * Data breaches resulting from phishing attacks may result in regulatory fines and legal liabilities, particularly in heavily regulated industries (e.g., healthcare, finance).
* **Operational Disruption**:
  * Phishing-related malware infections or credential compromises can disrupt critical business operations and services, causing downtime and productivity loss.

Early detection and mitigation of phishing attempts significantly reduce these risks, protecting organizational assets, sensitive data, and reputation.

## Examples

Real-world examples of phishing attacks illustrate the diverse scenarios, tools, and impacts involved:

* **2016 Democratic National Committee (DNC) Hack**:
  * Attackers (APT28/Fancy Bear) used spear phishing emails containing malicious links to gain initial access.
  * Attackers stole sensitive emails and documents, causing significant reputational damage and political impact.
* **Google and Facebook BEC Attack (2013–2015)**:
  * Attackers impersonated a legitimate hardware supplier via phishing emails, tricking employees into transferring millions of dollars to fraudulent accounts.
  * Total losses exceeded $100 million, highlighting severe financial consequences.
* **Colonial Pipeline Ransomware Attack (2021)**:
  * Attackers gained initial access through a compromised VPN credential, likely obtained via phishing.
  * Resulted in ransomware deployment, operational disruption, and fuel shortages across the U.S. East Coast.
* **Emotet Malware Campaigns (2014–Present)**:
  * Emotet botnet distributed malware via widespread phishing emails containing malicious attachments or links.
  * Enabled secondary infections (e.g., TrickBot, Ryuk ransomware), causing massive financial and operational impacts globally.
* **COVID-19 Themed Phishing Campaigns (2020–2021)**:
  * Attackers exploited public fear and urgency around COVID-19, sending phishing emails impersonating health organizations, government entities, and vaccine providers.
  * Resulted in credential theft, malware infections, and financial fraud across multiple industries and regions.

These examples demonstrate the broad applicability, effectiveness, and severe impacts associated with phishing attacks, underscoring the importance of effective detection, prevention, and user awareness strategies.
