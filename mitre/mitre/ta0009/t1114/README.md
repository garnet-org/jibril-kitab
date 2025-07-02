---
description: Email Collection [T1114]
icon: lock
---

# Email Collection

## Information

* Name: Email Collection
* ID: T1114
* Tactics: [TA0009](../)
* Sub-Technique: [T1114.001](t1114.001.md), [T1114.003](t1114.003.md), [T1114.002](t1114.002.md)

## Introduction

Email Collection is a reconnaissance technique recognized within the MITRE ATT\&CK framework (T1114). Attackers use this method to gather email addresses from target organizations or individuals, often as part of initial intelligence gathering phases. Obtaining email addresses helps adversaries craft targeted phishing campaigns, conduct social engineering attacks, or facilitate further reconnaissance activities.

## Deep Dive Into Technique

Attackers use various technical and non-technical methods to gather email addresses belonging to targeted organizations or individuals. Common methods include:

* **Web Scraping and Crawling:**
  * Automated scripts or bots scan public websites, forums, social media platforms, and directories for email addresses.
  * Tools like Scrapy, BeautifulSoup, or custom Python scripts are commonly used.
* **Search Engine Queries (Google Dorking):**
  * Utilizing advanced search operators to discover email addresses indexed by search engines.
  * Example queries:
    * `"@targetdomain.com" site:linkedin.com`
    * `"email" filetype:xls site:target.com`
* **Social Media Harvesting:**
  * Gathering email addresses from publicly available profiles on platforms such as LinkedIn, Facebook, Twitter, and GitHub.
* **Public Data Breaches and Leaks:**
  * Attackers leverage previously breached databases available on dark web marketplaces or forums.
  * Tools like Have I Been Pwned (HIBP) or Dehashed can be misused to access compromised email addresses.
* **WHOIS and DNS Enumeration:**
  * Using WHOIS databases to retrieve administrative or technical contacts for registered domains.
  * DNS enumeration tools (e.g., DNSRecon, dnsenum) to identify associated email addresses.
* **Email Harvesting Tools:**
  * Specialized tools like theHarvester, Hunter.io, or EmailHarvester automate the collection process.

## When this Technique is Usually Used

Attackers typically use Email Collection at the initial stages of cyber-attacks, specifically during reconnaissance and intelligence-gathering phases. Common scenarios include:

* **Initial Reconnaissance Phase:**
  * Gathering email contacts to identify potential targets for spear-phishing campaigns or social engineering attacks.
* **Phishing and Spear-phishing Campaigns:**
  * Identifying employee email addresses to craft personalized and convincing phishing emails.
* **Preparation for Credential Harvesting:**
  * Targeting email accounts for credential theft or account takeover attacks.
* **Business Email Compromise (BEC) Attacks:**
  * Identifying key personnel (executives, finance departments) to impersonate or target in fraudulent email schemes.
* **Further Reconnaissance and Lateral Movement:**
  * Leveraging collected email addresses to enumerate internal structures, identify key personnel, and plan lateral movement within the organization.

## How this Technique is Usually Detected

Detection of Email Collection activities can be challenging, as many methods leverage publicly available information. However, organizations can employ several methods to detect and mitigate such activities:

* **Web Server and Application Logs:**
  * Monitor for unusual crawling patterns or excessive requests from single IP addresses or user agents.
  * Tools like Splunk or ELK stack can help analyze logs for suspicious activities.
* **Email Gateway Monitoring:**
  * Detecting unusual email traffic patterns, phishing attempts, or unsolicited emails can indicate prior email harvesting.
  * Solutions such as Proofpoint, Mimecast, or Cisco IronPort can detect suspicious email patterns or phishing attempts.
* **DNS and WHOIS Monitoring:**
  * Monitor WHOIS lookup activity and DNS enumeration attempts through network monitoring solutions or security analytics platforms.
* **Honeypots and Honeytokens:**
  * Deploying fake email addresses (honeytokens) publicly to detect harvesting attempts when these addresses receive unsolicited emails.
* **Dark Web Monitoring:**
  * Monitoring dark web marketplaces and forums for leaks or sales of organizational email addresses using services like Recorded Future, Digital Shadows, or Intel471.

Indicators of Compromise (IoCs):

* Sudden increase in unsolicited emails or phishing attempts targeting organizational email addresses.
* Detection of automated web scraping or crawling activity from unknown sources.
* Public disclosure of corporate email addresses on unauthorized platforms or forums.

## Why it is Important to Detect This Technique

Early detection of Email Collection is crucial due to the significant risks and potential impacts:

* **Preventing Phishing and Spear-phishing Attacks:**
  * Early detection allows organizations to proactively warn users, implement email filtering, and educate employees.
* **Reducing Risk of Credential Theft:**
  * Identifying email harvesting activities can help prevent subsequent credential harvesting attacks and account compromises.
* **Protecting Against Business Email Compromise (BEC):**
  * Early detection can help secure critical email accounts, implement additional verification processes, and mitigate financial losses.
* **Minimizing Sensitive Information Exposure:**
  * Preventing attackers from mapping organizational structures and identifying key personnel reduces the risk of targeted attacks.
* **Reducing Operational and Financial Impact:**
  * Early detection and mitigation reduce the resources needed for incident response, investigation, and recovery efforts.

## Examples

Real-world examples of Email Collection and its impacts include:

* **LinkedIn Scraping Incident (2021):**
  * Attackers scraped publicly available LinkedIn profiles, collecting email addresses and personal data of millions of users.
  * Tools used: Custom web scraping scripts.
  * Impact:
    * Increased phishing and social engineering risks for affected individuals.
    * Potential credential harvesting and targeted attacks.
* **Facebook Data Leak (2019):**
  * Millions of email addresses and personal details were scraped from publicly accessible Facebook profiles.
  * Tools used: Automated scraping scripts and bots.
  * Impact:
    * Elevated phishing risks, account takeovers, and identity theft.
* **SolarWinds Supply Chain Attack (2020):**
  * Attackers conducted extensive reconnaissance, including email harvesting, to identify key targets and craft highly targeted phishing emails.
  * Tools used: Custom reconnaissance scripts, email harvesting techniques.
  * Impact:
    * Successful compromise of multiple high-profile organizations and government agencies.
    * Significant financial and reputational damages.
* **WHOIS Data Harvesting for BEC Attacks:**
  * Attackers harvested administrative email addresses via WHOIS databases to launch targeted BEC attacks.
  * Tools used: WHOIS enumeration tools, email harvesting scripts.
  * Impact:
    * Financial losses due to fraudulent transfers.
    * Compromise of business-critical email accounts.

By understanding real-world examples, organizations can better grasp the importance of detecting and mitigating Email Collection activities.
