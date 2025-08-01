---
description: Gather Victim Identity Information [T1589]
icon: user
---

# Gather Victim Identity Information

## Information

* Name: Gather Victim Identity Information
* ID: T1589
* Tactics: [TA0043](../)
* Sub-Technique: [T1589.002](t1589.002.md), [T1589.003](t1589.003.md), [T1589.001](t1589.001.md)

## Introduction

Gather Victim Identity Information (MITRE ATT\&CK ID: T1589) is a reconnaissance technique used by adversaries to collect personal or organizational identity information about potential victims. This information often includes email addresses, employee names, job titles, phone numbers, and other personally identifiable information (PII). Attackers leverage this data to facilitate targeted attacks, such as spear-phishing, social engineering, or impersonation attacks. Within the MITRE ATT\&CK framework, this technique falls under the "Reconnaissance" tactic, emphasizing the adversary's intent to gather preliminary information to support subsequent attack phases.

## Deep Dive Into Technique

Attackers utilize various methods and tools to systematically gather victim identity information. The methods can range from passive reconnaissance to active scanning and enumeration.

Common mechanisms include:

* **Open Source Intelligence (OSINT):**
  * Leveraging publicly available resources such as social media platforms (LinkedIn, Twitter, Facebook).
  * Searching through corporate websites, blogs, press releases, or employee directories.
  * Utilizing professional networking sites to map organizational hierarchies and employee roles.
* **Web Scraping and Crawling:**
  * Automated scripts or bots to extract employee details, emails, and phone numbers from websites.
  * Parsing metadata from documents publicly shared online (PDFs, Word documents) to identify authors, contributors, or internal structures.
* **Social Engineering Techniques:**
  * Engaging employees through email or social media under false pretenses to extract sensitive personal or organizational details.
  * Conducting pretexting operations by impersonating legitimate entities to gain trust and extract identity information.
* **Dark Web and Underground Forums:**
  * Purchasing or trading leaked databases containing employee credentials, emails, phone numbers, or other sensitive identity information.
  * Monitoring data breach dumps to collect victim identity details.
* **Technical Tools and Frameworks:**
  * OSINT frameworks (e.g., Maltego, SpiderFoot, TheHarvester) to automate data collection.
  * Custom scripts and bots written in Python or Bash to scrape and aggregate victim information from multiple sources.

## When this Technique is Usually Used

Adversaries primarily use this technique during the early reconnaissance phase of an attack lifecycle. Scenarios and stages include:

* **Pre-attack Reconnaissance:**
  * Gathering information to prepare targeted phishing or spear-phishing campaigns.
  * Identifying key personnel or executives for Business Email Compromise (BEC) attacks.
* **Initial Access Preparation:**
  * Collecting employee details to craft convincing phishing emails or social engineering attempts.
  * Mapping organizational structures to identify high-value targets or privileged access points.
* **Social Engineering Campaigns:**
  * Leveraging collected identity information to impersonate trusted individuals or entities.
  * Conducting targeted vishing (voice phishing) or smishing (SMS phishing) attacks using accurate victim identity details.
* **Advanced Persistent Threat (APT) Operations:**
  * Identifying critical personnel with privileged access to sensitive data or systems.
  * Conducting long-term reconnaissance to maintain updated victim profiles and organizational structures.

## How this Technique is Usually Detected

Detection of victim identity information gathering activities primarily involves proactive monitoring, behavioral analytics, and threat intelligence. Common detection methods include:

* **Monitoring Web Server Logs and Traffic:**
  * Detecting unusual crawling or scraping patterns indicative of automated reconnaissance.
  * Identifying repeated requests targeting employee directories or contact pages.
* **Behavioral Analytics and Anomaly Detection:**
  * Employing User and Entity Behavior Analytics (UEBA) solutions to detect abnormal access patterns to employee information.
  * Monitoring for abnormal spikes in queries or downloads of personal data from web assets.
* **Threat Intelligence Integration:**
  * Leveraging threat intelligence platforms (TIPs) to identify malicious IP addresses or domains associated with reconnaissance activities.
  * Utilizing external threat feeds to correlate suspicious activity patterns.
* **Email and Social Media Monitoring:**
  * Identifying suspicious social engineering attempts targeting employees.
  * Monitoring social media platforms for signs of targeted reconnaissance against organizational personnel.
* **Indicators of Compromise (IoCs):**
  * Unusual access patterns from known malicious IP addresses or TOR exit nodes.
  * Repeated automated requests to sensitive organizational pages (e.g., "/about-us," "/team," or "/contacts").
  * Detection of known OSINT tools' user agents or signatures (e.g., Maltego, SpiderFoot, TheHarvester).

## Why it is Important to Detect This Technique

Early detection of victim identity information gathering is crucial for several reasons:

* **Prevention of Targeted Attacks:**
  * Identifying reconnaissance activities early can prevent subsequent targeted phishing, spear-phishing, or social engineering attacks.
* **Reduction of Attack Surface:**
  * Early detection allows organizations to proactively secure publicly exposed information and limit the amount of sensitive data available to attackers.
* **Minimizing Reputational Damage:**
  * Preventing identity information leaks protects organizational reputation and maintains customer and employee trust.
* **Protection Against Advanced Threat Actors:**
  * Early identification of reconnaissance activities can disrupt advanced persistent threats (APTs) during initial stages, reducing the risk of prolonged compromise.
* **Compliance and Regulatory Requirements:**
  * Detecting and mitigating unauthorized access to personal data helps organizations adhere to privacy regulations (e.g., GDPR, HIPAA) and avoid potential legal penalties.
* **Resource Optimization:**
  * Early detection reduces the resources required for incident response and remediation, minimizing operational disruptions.

## Examples

Real-world examples of gathering victim identity information include:

* **APT28 (Fancy Bear) Operations:**
  * Utilized OSINT techniques to collect target email addresses, employee names, and job titles from public sources.
  * Leveraged the collected data to launch spear-phishing campaigns against political and military organizations.
* **FIN7 Criminal Group Activities:**
  * Conducted extensive reconnaissance to identify key personnel within targeted financial and hospitality organizations.
  * Used gathered identity information to craft convincing phishing emails and social engineering attacks, resulting in significant financial losses.
* **LinkedIn Scraping Incident (2021):**
  * Attackers scraped publicly available profile information from millions of LinkedIn users, including names, job titles, email addresses, and phone numbers.
  * The collected data was later sold on underground forums, facilitating further targeted attacks and impersonation schemes.
* **Twitter Social Engineering Attack (2020):**
  * Attackers gathered personal identity information of Twitter employees through social engineering techniques.
  * Leveraged this information to conduct a successful spear-phishing attack, gaining access to internal administrative tools and compromising high-profile accounts.
* **Operation Aurora (2010):**
  * Attackers performed extensive reconnaissance, gathering identity information on Google employees.
  * Utilized targeted spear-phishing emails crafted with accurate employee details to compromise internal systems and exfiltrate sensitive data.

In these examples, attackers utilized various techniques and tools, including OSINT frameworks (Maltego, SpiderFoot), automated scraping scripts, and targeted social engineering. The impacts ranged from financial losses and reputational damage to sensitive data breaches and long-term compromise of organizational assets.
