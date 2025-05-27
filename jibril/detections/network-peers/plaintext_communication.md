---
icon: line-height
---

# Plaintext Communication

## Quick Explanation

The `plaintext_communication` event detects communication with specific domains associated with pastebin services. This detection is critical as it may indicate malicious activities like code injection, command and control (C2) communications, or data exfiltration. During CI/CD operations, such external communications could compromise the integrity of the build process and potentially introduce vulnerabilities into production environments.

## More Information

### Information

**Description**: Access to pastebin services  
**Tactic**: [Command And Control](https://jibril.garnet.ai/mitre/mitre/ta0011)  
**Technique**: [Application Layer Protocol](https://jibril.garnet.ai/mitre/mitre/ta0011/t1071)  
**Sub-Technique**: [Web Protocols](https://jibril.garnet.ai/mitre/mitre/ta0011/t1071/t1071.001)  
**Importance**: Critical

### Analysis of the Event

The `plaintext_communication` detection is a critical component of Jibril's network monitoring capabilities, specifically designed to identify communications with domains associated with pastebin services. These activities can serve multiple malicious purposes:

* **Data Exfiltration:** Pastebin services may be used as conduits for exfiltrating sensitive data from compromised systems. Attackers might upload stolen credentials, intellectual property, or other confidential information to these platforms, where it can later be accessed remotely.
* **Command and Control (C2):** Malware often utilizes pastebin domains as a means of receiving commands and updates. This technique allows attackers to maintain control over infected machines by embedding C2 instructions within publicly accessible content.
* **Code Injection:** Attackers may leverage these services for storing malicious code or scripts, which can be retrieved and executed on target systems without raising immediate suspicion from traditional security measures.

This detection is tagged with critical importance due to the high risk of unauthorized data handling or security breaches. The event leverages network peer monitoring to identify connections that deviate from expected application behavior, particularly within CI/CD pipelines where all network interactions should be tightly controlled and predictable.

### Implications

#### Implications for CI/CD Pipelines

Detection of plaintext communication with known pastebin services during a CI/CD pipeline run can indicate significant security flaws in new code changes. These communications may stem from legitimate but misconfigured features or intentional malicious activities, both of which pose risks such as data leakage and system compromise.

* **Build Process Compromise:** Attackers might inject malicious code into the build process, leading to the creation of compromised artifacts that could be deployed across multiple environments.
* **Dependency Poisoning:** Malicious actors can exploit dependencies by modifying open-source packages or libraries used in builds, thereby introducing vulnerabilities that can be exploited post-deployment.

#### Implications for Staging

In a staging environment, plaintext communication with pastebin services poses risks such as:

* **Adversarial Testing:** Attackers may use these communications to test and refine their malicious activities before they are deployed in production.
* **Data Leakage:** Sensitive data could inadvertently leak through the staging environment if proper access controls are not enforced.
* **Insider Threats:** Unauthorized access by insiders can be facilitated through these channels, allowing for both exfiltration of sensitive information and introduction of malware.

#### Implications for Production

In a production environment, plaintext communication with pastebin services represents severe risks:

* **Long-term Persistence Risks:** Attackers may establish long-term persistence mechanisms that allow them to maintain control over systems even after initial compromise.
* **Lateral Movement:** Compromised hosts can be used as stepping stones for moving laterally within the network, increasing the scope of potential damage.
* **Credential Theft:** Data exfiltration through pastebin services can include sensitive credentials, enabling further attacks and amplifying the impact of breaches.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Immediate Investigation:** Review recent code changes and build logs to identify any unauthorized or suspicious activities. Look for unexpected scripts or dependencies that may have been introduced.
2. **Access Control Review:** Ensure that access controls are properly configured to prevent unauthorized communication with external services. Implement stricter network policies to block such communications.
3. **Dependency Audit:** Perform a comprehensive audit of all dependencies used in the build process to detect any tampered or malicious packages.

#### Actions for Staging

1. **Environment Isolation:** Ensure that the staging environment is isolated from production and other sensitive networks to prevent potential data leakage.
2. **Security Testing:** Conduct security testing to identify and mitigate vulnerabilities that could be exploited via pastebin communications.
3. **Data Handling Policies:** Review and enforce data handling policies to ensure that sensitive information is not exposed or transmitted insecurely.

#### Actions for Production

1. **Incident Response Activation:** Activate your incident response plan to address potential breaches. This includes identifying compromised systems and isolating them from the network.
2. **Comprehensive Threat Hunt:** Conduct a thorough threat hunt to identify any signs of long-term persistence mechanisms or lateral movement within the network.
3. **Credential Security:** Immediately change and secure any credentials that may have been exposed. Implement multi-factor authentication to enhance security.
