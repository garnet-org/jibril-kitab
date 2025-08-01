---
description: Data from Cloud Storage [T1530]
icon: cloud
---

# Data from Cloud Storage

## Information

* Name: Data from Cloud Storage
* ID: T1530
* Tactics: [TA0009](../)

## Introduction

The "Data from Cloud Storage" technique, identified as T1530 within the MITRE ATT\&CK framework, refers to adversaries leveraging legitimate cloud storage services to retrieve malicious payloads, exfiltrate data, or facilitate command-and-control (C2) communication. Attackers exploit trusted cloud platforms such as Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, Dropbox, Google Drive, and OneDrive to host malicious tools, scripts, or stolen data. By utilizing reputable cloud infrastructure, adversaries can effectively bypass traditional perimeter defenses, evade detection, and maintain persistence within compromised environments.

## Deep Dive Into Technique

Attackers commonly exploit cloud storage services for various malicious purposes, including:

* **Payload Hosting and Distribution**:
  * Attackers host malware binaries, scripts, or malicious documents on cloud storage platforms.
  * Victims are directed or tricked into downloading payloads from legitimate URLs, minimizing suspicion and detection.
  * Legitimate cloud domains bypass URL filters and security gateways, as they are often whitelisted or trusted.
* **Command-and-Control (C2) Infrastructure**:
  * Attackers use cloud storage services to pass commands, instructions, or configuration data to compromised endpoints.
  * Malware periodically polls cloud storage URLs to retrieve updated commands or exfiltrate data.
  * Cloud storage provides attackers with high availability, scalability, and anonymity due to shared infrastructure.
* **Data Exfiltration**:
  * Sensitive or proprietary data stolen from victim networks is uploaded directly to cloud storage services.
  * Attackers leverage encryption and legitimate cloud APIs to evade detection by network monitoring tools.
  * Cloud storage platforms offer substantial bandwidth, storage capacity, and ease of access from anywhere, facilitating large-scale data exfiltration.

Technical mechanisms attackers utilize include:

* **API Access**:
  * Direct use of cloud storage APIs (e.g., AWS S3 APIs, Google Cloud Storage APIs) for automated, stealthy interaction.
  * API keys and tokens are stolen or misused to authenticate and interact with cloud infrastructure.
* **Web Requests via HTTP/HTTPS**:
  * Malware or scripts perform HTTP/HTTPS GET and POST requests to cloud-hosted URLs for payload retrieval, command execution, or data uploads.
  * Encryption (TLS) ensures traffic is difficult to inspect or intercept.
* **Cloud Storage SDKs and Client Tools**:
  * Attackers embed cloud storage SDKs or official command-line tools into malware to simplify interactions and evade suspicion.
  * Using legitimate client software reduces the likelihood of detection by security tools.

## When this Technique is Usually Used

Attackers frequently utilize the "Data from Cloud Storage" technique across multiple stages and scenarios:

* **Initial Access and Delivery**:
  * Phishing campaigns delivering malicious payloads hosted on cloud storage services.
  * Legitimate cloud URLs increase trustworthiness and lower suspicion among targets.
* **Execution and Malware Delivery**:
  * Malware retrieves secondary payloads or additional tools from cloud storage after initial compromise.
  * Attackers dynamically update malware capabilities by uploading new payloads to cloud storage.
* **Persistence and Command-and-Control**:
  * Malware maintains persistence by periodically checking cloud storage URLs for updated instructions or configuration files.
  * Attackers leverage cloud storage to store commands, enabling flexible and stealthy C2 communication.
* **Exfiltration and Data Theft**:
  * Sensitive data is encrypted and directly uploaded to cloud storage services, avoiding detection by traditional network monitoring.
  * Attackers leverage cloud storage to facilitate large-scale exfiltration of sensitive corporate or personal data.

## How this Technique is Usually Detected

Detection of malicious use of cloud storage services involves multiple methods and tools, including:

* **Network Traffic Analysis**:
  * Monitoring network traffic for unusual volume or frequency of requests to cloud storage domains (e.g., AWS S3, Google Cloud Storage, Dropbox).
  * Detecting anomalous data transfers, particularly large uploads or downloads to cloud storage endpoints.
* **Endpoint Detection and Response (EDR)**:
  * Monitoring system processes for unusual HTTP/HTTPS requests or API calls to cloud storage services.
  * Identifying suspicious binaries or scripts downloading payloads from cloud storage URLs.
* **Cloud Access Security Brokers (CASB)**:
  * CASB solutions monitor and analyze cloud service usage patterns, identifying unauthorized or suspicious cloud storage interactions.
  * Detection of abnormal API usage, unusual user-agent strings, or atypical access patterns.
* **Security Information and Event Management (SIEM)**:
  * Aggregation and correlation of logs from network devices, endpoints, and cloud services to detect suspicious cloud storage interactions.
  * Alerting based on predefined rules or anomaly detection algorithms.
* **Indicators of Compromise (IoCs)**:
  * Known malicious cloud storage URLs or domains identified from threat intelligence feeds.
  * Suspicious user-agent strings or headers commonly used by malware interacting with cloud storage.
  * Unusual or unauthorized API keys or tokens used to access cloud storage services.
  * Detection of encrypted or obfuscated payloads downloaded from cloud storage URLs.

## Why it is Important to Detect This Technique

Detecting malicious use of cloud storage services is critical due to significant impacts and risks posed to organizations:

* **Data Loss and Theft**:
  * Attackers frequently use cloud storage for exfiltration of sensitive corporate, intellectual property, or customer data, leading to financial and reputational damage.
* **Malware Delivery and Propagation**:
  * Cloud storage services facilitate the distribution of malware payloads, enabling attackers to rapidly scale and propagate attacks across enterprise networks.
* **Evasion of Traditional Security Controls**:
  * Legitimate cloud storage domains often bypass traditional URL filtering, firewall, and proxy rules, allowing attackers to evade detection and defenses.
* **Persistent and Stealthy Command-and-Control**:
  * Attackers leverage cloud storage for stealthy C2 communications, making detection and remediation challenging for security teams.
* **Regulatory and Compliance Risks**:
  * Unauthorized data exfiltration to cloud storage services can lead to compliance violations (e.g., GDPR, HIPAA), resulting in legal and financial consequences.

Early detection enables:

* Rapid containment and mitigation of threats before significant damage occurs.
* Prevention of large-scale data breaches and associated costs.
* Maintenance of regulatory compliance and avoidance of legal penalties.
* Protection of organizational reputation and customer trust.

## Examples

Real-world examples of attacks leveraging the "Data from Cloud Storage" technique include:

* **APT29 (Cozy Bear)**:
  * Utilized legitimate cloud storage services, including Dropbox and Google Drive, to host malicious payloads and exfiltrate stolen data.
  * Attackers leveraged cloud storage URLs for initial malware delivery and subsequent C2 operations, evading traditional security defenses.
* **Menlo Security's Discovery of "Duri" Campaign**:
  * Attackers hosted malicious payloads on cloud storage services to deliver malware through phishing emails.
  * Victims received legitimate-looking emails directing them to cloud-hosted malicious documents, bypassing URL filtering and email gateway protections.
* **FIN7 Cybercrime Group**:
  * Leveraged cloud storage services such as AWS S3 buckets to distribute malware payloads and exfiltrate stolen payment card data from compromised retail and hospitality networks.
  * Attackers encrypted exfiltrated data before uploading it to cloud storage, evading detection by network monitoring.
* **Lazarus Group (North Korea)**:
  * Frequently used cloud storage platforms (e.g., Dropbox, OneDrive) for malware distribution and data exfiltration.
  * Attackers stored malicious scripts and payloads on legitimate cloud storage URLs, complicating detection by endpoint and network monitoring tools.
* **Operation Cloud Hopper (APT10)**:
  * Chinese threat actors extensively leveraged cloud storage services to host malware payloads and exfiltrate sensitive data from managed service providers (MSPs) and their customers.
  * Attackers used legitimate cloud storage APIs and encrypted communications to evade detection and maintain persistence.

In these scenarios, attackers benefited from the trusted reputation of cloud storage services, significantly complicating detection and response efforts.
