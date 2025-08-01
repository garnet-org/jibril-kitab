---
description: Data Manipulation [T1565]
icon: database
---

# Data Manipulation

## Information

* Name: Data Manipulation
* ID: T1565
* Tactics: [TA0040](../)
* Sub-Technique: [T1565.001](t1565.001.md), [T1565.003](t1565.003.md), [T1565.002](t1565.002.md)

## Introduction

Data Manipulation (T1565) is a technique categorized within the MITRE ATT\&CK framework under the Impact tactic. Attackers use data manipulation to alter, damage, or otherwise compromise data integrity, leading to misinformation, disruption of business operations, or loss of trust in data reliability. This technique can involve modifying, deleting, or inserting data to achieve malicious objectives such as sabotage, espionage, or extortion.

## Deep Dive Into Technique

Data Manipulation involves unauthorized actions that alter data stored on disk, databases, or transmitted across networks. Attackers typically execute this technique by:

* **Modifying Data:**
  * Altering database records to corrupt or falsify critical information.
  * Changing configuration files to disrupt service availability.
  * Editing logs to evade detection or cover tracks after an intrusion.
* **Deleting Data:**
  * Removing critical files or database entries to cause service outages.
  * Erasing logs or audit trails to conceal malicious activities.
* **Injecting False Data:**
  * Inserting fraudulent records into databases to mislead decision-making processes.
  * Creating fake log entries to divert forensic investigations.

Technical mechanisms used include:

* Exploiting vulnerabilities in web applications (SQL injection, command injection).
* Gaining unauthorized access to database management systems (MySQL, PostgreSQL, Oracle, Microsoft SQL Server).
* Abusing administrative privileges obtained through credential theft or privilege escalation.
* Leveraging malware or scripts to automate bulk data manipulation.

Real-world procedures attackers might follow:

1. Reconnaissance to identify valuable data assets.
2. Initial compromise using phishing, vulnerability exploitation, or credential theft.
3. Privilege escalation to obtain administrative or database-level permissions.
4. Execution of scripts/tools to manipulate targeted data.
5. Covering tracks by altering or deleting logs and audit records.

## When this Technique is Usually Used

Data Manipulation can appear across multiple stages of an attack lifecycle, particularly:

* **Impact Stage**:
  * To disrupt business operations or cause service outages.
  * To sabotage competitors or adversaries by corrupting critical data.
  * To facilitate ransomware attacks by making recovery more difficult without paying ransom.
* **Defense Evasion**:
  * Altering or deleting logs to hide attacker activities.
  * Modifying timestamps or file metadata to mislead forensic analysis.
* **Persistence and Credential Access**:
  * Modifying user permissions or authentication data to maintain long-term access.
  * Changing configuration files to enable persistent backdoors.

Attack scenarios commonly involving Data Manipulation:

* Cyber espionage campaigns targeting intellectual property or sensitive records.
* Financial fraud schemes that alter transaction data.
* State-sponsored sabotage against critical infrastructure (utilities, healthcare, transportation).
* Ransomware attacks that corrupt backups or critical data to increase leverage.

## How this Technique is Usually Detected

Detection methods and tools commonly used include:

* **File Integrity Monitoring (FIM)**:
  * Tools like Tripwire, OSSEC, and AlienVault detect unauthorized changes to files or configurations.
* **Database Activity Monitoring (DAM)**:
  * Solutions such as Imperva, IBM Guardium, and Oracle Audit Vault monitor and alert on suspicious database queries or modifications.
* **Log Analysis and SIEM Solutions**:
  * Splunk, Elastic Security, IBM QRadar, and ArcSight analyze logs for abnormal patterns indicating data manipulation.
* **Endpoint Detection and Response (EDR)**:
  * CrowdStrike Falcon, Microsoft Defender for Endpoint, and SentinelOne detect malicious scripts or executables performing unauthorized data changes.

Specific Indicators of Compromise (IoCs) include:

* Unusual or unauthorized database queries or transactions.
* Sudden increase in log deletion or modification activities.
* Unexpected changes in file hashes or metadata.
* Anomalous user account modifications (privilege escalations, unauthorized access rights).
* Detection of scripts or tools commonly used for data manipulation (SQLMap, custom PowerShell scripts, database manipulation utilities).

## Why it is Important to Detect This Technique

Detecting Data Manipulation early is critical due to potential severe impacts:

* **Loss of Data Integrity**:
  * Altered data can disrupt business decisions, product quality, and customer trust.
* **Operational Disruption**:
  * Deleted or corrupted data may cause extended downtime, financial loss, and reduced productivity.
* **Compliance and Legal Consequences**:
  * Manipulated data may lead to regulatory fines, legal actions, and reputational damage.
* **Security Posture Compromise**:
  * Data manipulation used to hide attacker activities can prolong attacker dwell time and allow further exploitation.

Early detection helps organizations:

* Minimize operational disruption and reduce financial impact.
* Preserve customer trust and brand reputation.
* Ensure compliance with regulatory requirements and industry standards.
* Strengthen overall cybersecurity posture and resilience against future attacks.

## Examples

Real-world cases demonstrating Data Manipulation include:

* **Stuxnet Attack (2010)**:
  * Scenario: State-sponsored malware designed to sabotage Iranian nuclear enrichment facilities.
  * Tools Used: Custom malware exploiting Siemens SCADA systems.
  * Impact: Manipulated centrifuge rotation speeds, causing physical damage and operational disruption.
* **Sony Pictures Hack (2014)**:
  * Scenario: Attackers infiltrated Sony Pictures' network, modifying and deleting critical business data.
  * Tools Used: Malware variants including Destover.
  * Impact: Severe operational disruption, leaked sensitive data, and significant financial losses.
* **Bangladesh Bank Heist (2016)**:
  * Scenario: Attackers manipulated SWIFT transaction records to transfer funds illegally.
  * Tools Used: Dridex malware, custom scripts, and compromised credentials.
  * Impact: Approximately $81 million stolen, highlighting vulnerabilities in financial transaction systems.
* **NotPetya Ransomware Attack (2017)**:
  * Scenario: Malware designed to irreversibly encrypt and corrupt data, masquerading as ransomware.
  * Tools Used: EternalBlue exploit, Mimikatz credential theft tool, and destructive disk encryption.
  * Impact: Global disruption, billions of dollars in damages, and prolonged operational outages across multiple industries.
* **Ukrainian Power Grid Attack (2015)**:
  * Scenario: Attackers remotely manipulated power distribution control systems, causing widespread outages.
  * Tools Used: BlackEnergy malware, KillDisk data-wiping component.
  * Impact: Temporary power outages for hundreds of thousands of residents, highlighting critical infrastructure vulnerabilities.
