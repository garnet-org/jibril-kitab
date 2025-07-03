---
description: Phishing for Information [T1598]
icon: fish-fins
---

# Phishing for Information

## Information

* Name: Phishing for Information
* ID: T1598
* Tactics: [TA0043](../)
* Sub-Technique: [T1598.003](t1598.003.md), [T1598.004](t1598.004.md), [T1598.002](t1598.002.md), [T1598.001](t1598.001.md)

## Introduction

Phishing for Information is a recognized social engineering technique within the MITRE ATT\&CK framework (Technique ID: T1598). Attackers utilize deceptive communication methods, typically email, messaging, or social media platforms, to trick individuals into revealing sensitive information, credentials, or other valuable data. This technique leverages trust, urgency, or familiarity to manipulate targets into performing actions that compromise security.

## Deep Dive Into Technique

Phishing for Information involves attackers crafting convincing communications that appear legitimate and trustworthy. Attackers commonly employ the following methods and mechanisms:

* **Email Phishing:**
  * Attackers send emails appearing to originate from reputable sources, such as banks, service providers, or internal departments.
  * Messages often contain urgent requests, warnings, or enticing offers to prompt immediate action.
  * Embedded links direct victims to malicious websites designed to harvest credentials or personal information.
* **Spear Phishing:**
  * Personalized attacks targeting specific individuals or organizations.
  * Attackers perform reconnaissance to gather details about the victim's role, interests, and contacts, increasing the credibility of the phishing attempt.
  * Highly tailored content increases the likelihood of successful deception.
* **Smishing (SMS Phishing):**
  * Attackers send fraudulent text messages containing malicious links or instructions.
  * Messages may claim to be from trusted entities such as financial institutions, delivery services, or government agencies.
* **Vishing (Voice Phishing):**
  * Attackers conduct phone calls posing as legitimate representatives.
  * They manipulate victims into providing sensitive information verbally, such as account numbers, passwords, or security codes.
* **Social Media Phishing:**
  * Attackers create fake profiles or compromised accounts to send direct messages or posts containing malicious links.
  * Often exploits existing trust relationships within social networks.

Real-world procedures attackers use include:

* Registering domains visually similar to legitimate websites (typosquatting).
* Utilizing URL shortening services to obscure malicious links.
* Employing legitimate cloud services to host phishing pages, evading reputation-based detection.
* Using stolen branding and logos to enhance authenticity.

## When this Technique is Usually Used

Phishing for Information can occur at multiple stages and scenarios within an attack lifecycle:

* **Initial Access:**
  * Attackers use phishing to obtain credentials or sensitive information, enabling initial network entry or account compromise.
* **Credential Harvesting:**
  * Attackers specifically target login credentials for email, VPN, cloud services, or critical internal applications.
* **Reconnaissance:**
  * Attackers employ phishing to gather organizational structure details, contact information, or internal procedures.
* **Privilege Escalation and Lateral Movement:**
  * Attackers leverage obtained credentials or information to escalate privileges or move laterally within networks.
* **Financial Fraud and Extortion:**
  * Attackers use phishing to obtain banking details, facilitate wire transfers, or support ransomware and extortion campaigns.
* **Supply Chain Attacks:**
  * Attackers target third-party vendors or partners via phishing to infiltrate larger organizations indirectly.

## How this Technique is Usually Detected

Detection methods and tools commonly used to identify Phishing for Information include:

* **Email Security Gateways:**
  * Inspect incoming emails for suspicious attachments, URL reputation, sender authenticity, and malicious content.
* **Endpoint Detection and Response (EDR):**
  * Monitor endpoint behavior for unusual activity following email interactions, such as credential theft attempts or malicious website visits.
* **Security Information and Event Management (SIEM):**
  * Aggregate and correlate logs from email servers, web proxies, DNS queries, and endpoint solutions to identify phishing attempts.
* **User Reporting Mechanisms:**
  * Encourage users to report suspicious communications, enabling rapid investigation and response.
* **Threat Intelligence Feeds:**
  * Incorporate real-time intelligence on known phishing campaigns, malicious domains, and attacker infrastructure.

Specific Indicators of Compromise (IoCs) include:

* Suspicious sender email addresses (spoofed or look-alike domains).
* URLs pointing to newly registered or untrusted domains.
* Emails containing urgent language, grammatical errors, or unusual formatting.
* Unsolicited requests for sensitive information or credentials.
* Malicious attachments (e.g., HTML files used for credential harvesting).

## Why it is Important to Detect This Technique

Detecting Phishing for Information early is critical due to its significant potential impacts:

* **Credential Compromise:**
  * Unauthorized access to sensitive accounts, systems, or data repositories.
* **Financial Loss:**
  * Direct monetary theft through fraudulent transactions or indirect costs from incident response and recovery efforts.
* **Data Breaches:**
  * Exposure of confidential, proprietary, or personally identifiable information (PII), resulting in legal, regulatory, and reputational consequences.
* **Operational Disruption:**
  * Attackers leveraging compromised credentials to disrupt business operations, causing downtime and productivity loss.
* **Reputation Damage:**
  * Public disclosure of successful phishing attacks undermines customer trust and damages organizational reputation.
* **Compliance Violations:**
  * Failure to detect and respond to phishing incidents may result in non-compliance with industry standards or regulatory requirements, leading to fines or legal actions.

Early detection enables timely mitigation, reducing the overall impact and preventing attackers from achieving their objectives.

## Examples

Real-world examples demonstrating Phishing for Information include:

* **Google and Facebook Spear Phishing Attack (2013–2015):**
  * Attack Scenario:
    * Attacker impersonated a legitimate hardware supplier (Quanta Computer) by creating fake invoices and emails.
    * Targeted employees responsible for financial transactions.
  * Tools and Techniques:
    * Email spoofing, fake domains, and fraudulent invoices.
  * Impact:
    * Approximately $100 million stolen from both companies combined.
    * Highlighted vulnerabilities in vendor management and invoice verification processes.
* **Twitter Account Compromise (2020):**
  * Attack Scenario:
    * Attackers conducted spear phishing against Twitter employees, gaining access to internal administrative tools.
  * Tools and Techniques:
    * Phone-based social engineering (vishing) combined with phishing emails.
  * Impact:
    * Compromise of high-profile Twitter accounts (e.g., Elon Musk, Barack Obama) used in cryptocurrency scams.
    * Resulted in significant reputational damage and regulatory scrutiny.
* **Operation Aurora (2010):**
  * Attack Scenario:
    * Attackers targeted Google and other large tech firms using spear phishing emails containing malicious links.
  * Tools and Techniques:
    * Emails contained links to malicious websites hosting zero-day exploits.
  * Impact:
    * Theft of intellectual property and sensitive information.
    * Prompted widespread adoption of stronger detection and response measures across the industry.
* **RSA SecurID Breach (2011):**
  * Attack Scenario:
    * Attackers sent phishing emails to RSA employees titled "2011 Recruitment Plan," containing malicious Excel attachments.
  * Tools and Techniques:
    * Malicious attachments exploiting vulnerabilities.
  * Impact:
    * Compromise of RSA's internal network and theft of sensitive data related to SecurID tokens.
    * Resulted in significant financial costs and loss of customer trust.

These examples underscore the effectiveness of phishing techniques and the necessity for robust detection, awareness training, and incident response capabilities.
