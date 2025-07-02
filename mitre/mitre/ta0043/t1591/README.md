---
description: Gather Victim Org Information [T1591]
icon: scalpel
---

# Gather Victim Org Information

## Information

* Name: Gather Victim Org Information
* ID: T1591
* Tactics: [TA0043](../)
* Sub-Technique: [T1591.003](t1591.003.md), [T1591.002](t1591.002.md), [T1591.004](t1591.004.md), [T1591.001](t1591.001.md)

## Introduction

Gather Victim Org Information (MITRE ATT\&CK technique ID: T1591) is a reconnaissance tactic used by adversaries to collect detailed information about targeted organizations. This technique involves identifying critical organizational details such as employee names, roles, contact information, physical locations, organizational structure, business relationships, and technical infrastructure. Adversaries leverage this information to plan and execute targeted attacks, including spear-phishing, social engineering, and network intrusions.

## Deep Dive Into Technique

Adversaries perform extensive reconnaissance to gather detailed information about targeted organizations. This information collection typically involves both passive and active methods:

* **Passive Collection Methods:**
  * Searching publicly available sources such as corporate websites, social media profiles (LinkedIn, Twitter, Facebook), and online directories.
  * Leveraging search engines (Google Dorking) to discover sensitive documents, organizational charts, or employee contact information.
  * Analyzing job postings to understand technical infrastructure, software used, and internal processes.
  * Monitoring press releases and news articles to identify key personnel, recent changes, mergers, or acquisitions.
* **Active Collection Methods:**
  * Initiating direct communication (emails, phone calls, or social media interactions) to employees under false pretenses.
  * Sending phishing emails or messages designed to extract information or credentials.
  * Interacting with customer support or help desk to gain insight into internal procedures and technical details.
  * Utilizing WHOIS lookups and DNS enumeration to map out the organization's network infrastructure.

Real-world adversaries often combine passive and active methods to maximize the accuracy and depth of gathered information.

## When this Technique is Usually Used

Gathering victim organization information typically occurs in the early stages of the cyber attack lifecycle. Specific scenarios include:

* **Pre-attack Reconnaissance:**
  * Adversaries commonly perform this technique before initiating attacks to identify high-value targets, organizational vulnerabilities, and entry points.
  * Preparing for spear-phishing campaigns by identifying suitable targets and crafting highly personalized messages.
* **Initial Access Stage:**
  * Leveraging collected information to improve social engineering attacks, increasing the likelihood of success in phishing or vishing campaigns.
* **Lateral Movement and Privilege Escalation:**
  * After initial compromise, attackers may continue gathering organizational information to identify key assets, critical systems, or privileged accounts for lateral movement and escalation.
* **Persistent Threat Scenarios:**
  * Advanced Persistent Threat (APT) groups use continuous information gathering to maintain updated intelligence on victim organizations, enabling long-term persistence and sustained exploitation.

## How this Technique is Usually Detected

Detection of this reconnaissance technique focuses on identifying suspicious information-gathering activities, both externally and internally:

* **External Monitoring:**
  * Monitor web server logs and network perimeter devices for unusual scanning activity, directory enumeration, or WHOIS queries originating from suspicious IP addresses.
  * Employ threat intelligence platforms and open-source intelligence (OSINT) monitoring tools to detect adversaries actively gathering information about your organization online.
  * Utilize services that identify suspicious domain registrations or phishing infrastructure that references your organization's name or branding.
* **Internal Monitoring and Detection:**
  * Implement email filtering and detection systems to identify phishing or spear-phishing attempts designed to extract sensitive organizational information.
  * Deploy internal SIEM (Security Information and Event Management) solutions to correlate suspicious user behavior indicative of reconnaissance activities.
  * Train employees to recognize and report suspicious social engineering attempts through awareness training programs.
* **Indicators of Compromise (IoCs):**
  * Unusual spikes in traffic to corporate websites or employee profile pages.
  * Suspicious emails or social media interactions requesting sensitive organizational details.
  * DNS enumeration attempts or repeated WHOIS lookups from known malicious IP addresses or domains.
  * Detection of cloned or spoofed organizational websites used for credential harvesting or information gathering.

## Why it is Important to Detect This Technique

Early detection of adversaries gathering organizational information is critical due to the following potential impacts:

* **Enhanced Attack Precision:**
  * Detailed organizational information enables adversaries to craft highly targeted spear-phishing campaigns, significantly increasing the likelihood of successful compromise.
* **Increased Risk of Social Engineering Attacks:**
  * Employees unaware of reconnaissance activities may inadvertently disclose sensitive information, facilitating further attacks and exploitation.
* **Exposure of Sensitive Information:**
  * Unchecked reconnaissance can lead to inadvertent exposure of critical business data, intellectual property, or sensitive personnel information.
* **Preparation for Advanced Attacks:**
  * Adversaries utilize gathered intelligence to plan sophisticated cyber attacks, including ransomware deployment, data breaches, or supply chain attacks.
* **Long-term Persistence and Damage:**
  * Failure to detect early reconnaissance activities can allow attackers time to establish persistence within an organization, making detection and remediation significantly more challenging and costly.

## Examples

* **APT29 (Cozy Bear):**
  * Utilized extensive reconnaissance techniques, including gathering employee information from social media profiles, to conduct targeted spear-phishing campaigns against government and private sector organizations.
  * Leveraged harvested information to craft highly credible phishing emails, resulting in the compromise of email accounts and sensitive data exfiltration.
* **FIN7 Cybercrime Group:**
  * Conducted detailed reconnaissance of targeted retail and hospitality organizations by analyzing publicly available information, employee roles, and internal processes.
  * Crafted highly customized spear-phishing emails targeting specific roles (e.g., finance or HR departments), resulting in successful malware deployment, financial theft, and long-term damage.
* **Operation Aurora:**
  * Attackers performed extensive reconnaissance of victim organizations, including Google and other high-profile companies, identifying key personnel and infrastructure details.
  * Used this intelligence to execute targeted spear-phishing attacks, ultimately leading to significant intellectual property theft and compromise of corporate networks.
* **Social Engineering Toolkit (SET):**
  * Attackers frequently use SET to automate reconnaissance and phishing attacks. By leveraging publicly available organizational information, attackers create convincing phishing campaigns tailored to specific employees and departments.
* **LinkedIn Data Scraping Incident (2021):**
  * Attackers scraped publicly available LinkedIn profiles to compile extensive datasets on employees from various organizations.
  * This data was subsequently used in targeted phishing campaigns, identity theft, and social engineering attacks against multiple enterprises.
