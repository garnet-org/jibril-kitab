---
description: Unsecured Credentials [T1552]
icon: key
---

# Unsecured Credentials

## Information

* Name: Unsecured Credentials
* ID: T1552
* Tactics: [TA0006](../)
* Sub-Technique: T1552.005, [T1552.002](t1552.002.md), T1552.004, [T1552.003](t1552.003.md), [T1552.001](t1552.001.md), [T1552.006](t1552.006.md), T1552.008, T1552.007

## Introduction

Unsecured Credentials (MITRE ATT\&CK Technique ID: T1552) refers to adversaries exploiting credentials that are stored or transmitted insecurely. Attackers leverage credentials found in plaintext, weakly encrypted, or improperly stored locations to gain unauthorized access to systems, networks, or sensitive data. This technique falls under the Credential Access tactic within the MITRE ATT\&CK framework, highlighting its role in acquiring legitimate credentials to further compromise the target infrastructure.

## Deep Dive Into Technique

Adversaries commonly exploit unsecured credentials due to improper storage, transmission, or configuration practices. Technical details include:

* **Plaintext Storage**: Credentials found in configuration files, scripts, source code repositories, or documentation that are stored in plaintext.
* **Weak Encryption or Encoding**: Credentials stored using easily reversible encryption methods (e.g., base64 encoding, ROT13) or weak cryptographic algorithms.
* **Misconfigured Services**: Services such as FTP, SMB, databases, or web applications that store or transmit credentials insecurely.
* **System Memory and Logs**: Credentials temporarily stored in memory dumps, system logs, debug files, or crash reports.
* **Network Traffic**: Credentials transmitted over unsecured channels (e.g., HTTP, FTP, Telnet) without encryption.
* **Cloud Environments**: Credentials or API keys stored insecurely in cloud storage buckets, repositories, or publicly accessible locations.

Real-world procedures involve adversaries performing reconnaissance to identify insecure credential storage locations, extracting these credentials, and using them to escalate privileges, pivot laterally, and maintain persistence.

## When this Technique is Usually Used

Attackers typically use unsecured credentials at various stages and scenarios throughout an attack lifecycle, including:

* **Initial Access**:
  * Exploiting publicly accessible repositories or cloud storage containing plaintext credentials.
  * Intercepting unencrypted network traffic to obtain valid credentials.
* **Privilege Escalation**:
  * Leveraging credentials found in plaintext configuration files to escalate privileges within compromised systems.
* **Lateral Movement**:
  * Using unsecured credentials to authenticate to other systems within the network, facilitating lateral movement.
* **Persistence**:
  * Continuously using improperly stored credentials to maintain persistent access without triggering security alerts.
* **Data Exfiltration and Impact**:
  * Utilizing compromised credentials to access sensitive data stores or applications, leading to data theft, ransomware deployment, or disruption of services.

## How this Technique is Usually Detected

Detection methods for unsecured credentials typically involve proactive and reactive measures, including:

* **Proactive Auditing and Scanning**:
  * Regular scans of filesystems, repositories, and cloud storage for plaintext or weakly encrypted credentials.
  * Configuration audits to identify insecure storage or transmission methods.
* **Network Monitoring and Analysis**:
  * Monitoring network traffic for clear-text credential transmissions using tools such as Wireshark, Zeek, or Snort.
  * Implementing Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) to detect credential leaks.
* **Endpoint Detection and Response (EDR)**:
  * Monitoring endpoints for suspicious access to credential files or memory dumps.
  * Detection of anomalous processes accessing known credential storage locations.
* **File Integrity Monitoring (FIM)**:
  * Detecting unauthorized access or changes to sensitive files containing credentials.
* **Log Analysis and SIEM Solutions**:
  * Analyzing logs for unusual access patterns, failed authentication attempts, or suspicious processes accessing credential stores.
  * Correlation of events from multiple sources to identify credential compromise.
* **Indicators of Compromise (IoCs)**:
  * Presence of plaintext credentials in unexpected locations (e.g., scripts, configuration files, logs).
  * Unusual authentication events from unknown IP addresses or user agents.
  * Detection of credential harvesting tools or scripts (e.g., Mimikatz, LaZagne).

## Why it is Important to Detect This Technique

Early detection of unsecured credentials is critical due to the following potential impacts:

* **Unauthorized Access and Privilege Escalation**:
  * Attackers can quickly escalate privileges and gain administrative control over critical systems.
* **Lateral Movement and Persistence**:
  * Attackers may use compromised credentials to spread through networks, increasing the scope and severity of the breach.
* **Data Breaches and Exfiltration**:
  * Unauthorized access to sensitive information can lead to severe data breaches, compliance violations, and financial losses.
* **Operational Disruption and System Downtime**:
  * Attackers leveraging unsecured credentials can disrupt business operations, deploy ransomware, or cause system outages.
* **Reputation and Regulatory Impact**:
  * Failure to detect credential compromise promptly may lead to reputational damage and regulatory penalties due to inadequate security controls.

Early detection allows organizations to promptly respond, mitigate the threat, limit damage, and enhance overall security posture.

## Examples

Real-world examples of unsecured credential exploitation include:

* **Uber (2016 Data Breach)**:
  * Attackers discovered plaintext AWS credentials stored in GitHub repositories.
  * Leveraged credentials to access AWS infrastructure, leading to the exposure of personal data belonging to millions of users and drivers.
  * Impact: Massive data breach, regulatory fines, significant reputational damage.
* **Capital One Breach (2019)**:
  * Attacker exploited misconfigured AWS S3 buckets and IAM roles containing unsecured credentials.
  * Gained access to sensitive personal and financial information of over 100 million individuals.
  * Impact: Severe financial penalties, regulatory scrutiny, and reputational harm.
* **Mirai Botnet (2016)**:
  * Exploited unsecured credentials (default usernames/passwords) on IoT devices.
  * Gained control of thousands of IoT devices, launching massive Distributed Denial-of-Service (DDoS) attacks.
  * Impact: Major disruption of internet services, highlighting risks of unsecured credential storage and default passwords.
* **TeamViewer Credential Leak (2016)**:
  * Attackers leveraged credentials stored insecurely or reused across multiple platforms.
  * Unauthorized remote access to user systems, leading to financial fraud and data theft.
  * Impact: Financial losses, compromised user privacy, and reduced trust in remote access solutions.
* **Equifax Data Breach (2017)**:
  * Attackers exploited plaintext credentials stored in configuration files accessible via web application vulnerabilities.
  * Gained access to sensitive personal data of approximately 147 million individuals.
  * Impact: Massive data breach, extensive legal settlements, regulatory fines, and reputational damage.

These examples underscore the critical importance of securely storing and transmitting credentials, as well as proactively detecting and mitigating unsecured credential vulnerabilities.
