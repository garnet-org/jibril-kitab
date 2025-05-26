---
icon: bitcoin
---

# Crypto Miner Execution

## Quick Explanation

This Jibril detection recipe targets suspicious files and commands related to cryptocurrency mining. It highlights newly introduced or executed miner binaries, libraries, and scripts within the CI/CD pipeline. By flagging these occurrences, the goal is to prevent malicious exploitation of resources, unauthorized access, or embedding of miner code in production artifacts.

## More Information

### Information

**Description**: Crypto miner execution **Category**: Resource Development **Method**: Establish Account **Importance**: High

### Analysis of the Event

The `crypto_miner_execution` event covers a wide range of executables, libraries, and scripts commonly associated with crypto mining operations. In legitimate scenarios, some of these tools could appear in testing or research environments. However that is unusual for overall workloads and may suggest unauthorized activities.

Attackers often embed miners into container images or inject them via scripts to hijack computing resources. If successful, they could remain undetected for extended periods, leveraging the pipeline’s infrastructure to mine cryptocurrency.

This also opens the door to broader exploitation strategies, such as creating new accounts (T1098: Account Manipulation) or pivoting to more critical systems through lateral movement techniques (T1021: Remote Services), all while hiding behind seemingly legitimate CI processes.

Additionally, attackers may use DNS tunneling (T1047: Ingress/Egress Tools) and covert channels (T1097: Covert Channel) to exfiltrate data or communicate with command-and-control servers.

Compromised builds can also threaten downstream environments if the malicious artifacts are deployed to staging or production. This risk extends to potential data leaks, financial fraud, and further infiltration of corporate networks through supply chain attacks (T1098: Supply Chain Compromise).

### Implications

#### Implications for CI/CD Pipelines

* **Drain Resources**: Miners consume significant CPU/GPU cycles, slowing builds and increasing operational costs. This can lead to delayed deployments and increased cloud resource utilization charges.
* **Threaten Build Integrity**: Malicious scripts or code injected into build artifacts can propagate to production, impacting reliability and trust. Such malicious payloads could include trojans (T1056: T1218: Exploitation for Privilege Escalation) that further compromise systems.
* **Enable Persistence**: Attackers may establish hidden accounts or backdoor services (T1098: Account Manipulation, T1003: Automated Exfiltration), persisting across future builds and deployments. These mechanisms can be used to maintain long-term access to the CI/CD environment.
* **Exfiltrate Sensitive Data**: While running with elevated privileges, miners or scripts might collect credentials (T1216: Credential Access via API) and critical information, exposing the broader infrastructure.

Should these components become part of the merged codebase, production systems may be compromised, resulting in costly downtime, data breaches, or reputational harm.

#### Implications for Staging

* **Malicious Artifacts**: Malware-infected binaries can be introduced into staging environments, leading to potential lateral movement and further compromise.
* **Data Leakage**: Covert channels (T1097: Covert Channel) could allow for the exfiltration of sensitive data from staging systems.

#### Implications for Production

* **Operational Disruption**: Compromised production systems can suffer from reduced performance due to resource-intensive mining operations, leading to service outages.
* **Data Breaches**: Exfiltrated sensitive information can result in regulatory penalties and loss of customer trust.
* **Reputation Damage**: Public disclosure of a security breach can severely impact the organization’s reputation.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Conduct a Thorough Investigation**: Immediately initiate a detailed forensic analysis to determine the origin, scope, and method of the crypto miner's introduction into the CI/CD pipeline. Check recent changes, commit logs, and access logs for any anomalies or unauthorized access.
2. **Strengthen Security Measures**: Implement stricter security controls, including more robust code review processes, multi-factor authentication for access, and automated security scanning of code and dependencies.
3. **Update and Patch Systems**: Ensure that all systems and software in the CI/CD pipeline are up-to-date with the latest security patches to prevent exploitation of known vulnerabilities.
4. **Educate and Train Staff**: Conduct security awareness training for all team members involved in the CI/CD process to recognize and prevent security threats like crypto miner injections.

#### Actions for Staging

1. **Isolate and Analyze Affected Systems**: Isolate any systems suspected of being compromised. Perform a comprehensive security audit and malware scan to identify and remove any malicious artifacts.
2. **Validate All Artifacts Before Promotion**: Implement automated tools to scan and validate all binaries, libraries, and scripts before they are promoted from staging to production.
3. **Regular Snapshot and Backup**: Maintain regular snapshots and backups of the staging environment, which can be restored in case of contamination by crypto miners or other malware.

#### Actions for Production

1. **Immediate Containment and Remediation**: If crypto mining activity is detected in production, prioritize containing the threat and remediating affected systems. This may involve taking services offline temporarily to prevent further damage.
2. **Monitor Network Traffic**: Increase monitoring of network traffic for unusual patterns that may indicate data exfiltration or command and control communications associated with the crypto miner.
3. **Review and Revise Incident Response Plans**: Post-incident, review and update incident response plans to incorporate lessons learned from the event to better handle similar incidents in the future.
4. **Communicate Transparently with Stakeholders**: Inform stakeholders, including customers and partners, about the breach responsibly and transparently, detailing what measures are being taken to address the issue and prevent future occurrences.
