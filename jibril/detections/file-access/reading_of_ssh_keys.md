---
icon: key
---

# Reading of SSH Keys

## Quick Explanation

The `reading_of_ssh_keys` detection recipe identifies instances where processes attempt to read SSH key files. This behavior can indicate attempts by attackers to access sensitive credentials stored in SSH keys, potentially leading to unauthorized access, privilege escalation, or lateral movement within the environment.

## More Information

### Information

**Description**: Reading of SSH keys  
**Tactic**: [Credential Access](https://jibril.garnet.ai/mitre/mitre/ta0006)  
**Technique**: [Unsecured Credentials](https://jibril.garnet.ai/mitre/mitre/ta0006/t1552)  
**Sub-Technique**: [Credentials in Files](https://jibril.garnet.ai/mitre/mitre/ta0006/t1552/t1552.001)  
**Importance**: Medium

### Analysis of the Event

The `reading_of_ssh_keys` detection, flagged by Jibril, highlights a credential access method where processes attempt to read SSH key files such as `id_rsa`, `id_dsa`, `authorized_keys`, and SSH configuration files. Attackers commonly target these files to obtain sensitive credentials, enabling unauthorized access to systems and facilitating further malicious activities.

From a security perspective, this tactic aligns with the MITRE ATT&CK framework's Credential Access techniques under T1552 (Unsecured Credentials). Attackers frequently leverage stolen SSH keys to gain persistent access, escalate privileges, or move laterally across networks, increasing the risk of compromise.

While legitimate processes such as SSH daemons (`sshd`) or container runtimes (`containerd`) may access these files as part of normal operations, unexpected or unauthorized processes reading SSH keys should be thoroughly investigated.

### Implications

#### Implications for CI/CD Pipelines

Detection of SSH key reading during CI/CD pipeline execution indicates a potential compromise or unauthorized access attempt. Attackers may exploit pipeline credentials to inject malicious code, compromise build artifacts, or gain unauthorized access to sensitive infrastructure. This can lead to significant consequences, including unauthorized deployments, data breaches, and persistent threats within the pipeline environment.

#### Implications for Staging

In staging environments, unauthorized reading of SSH keys may indicate adversarial reconnaissance or attempts to escalate privileges. Attackers could leverage compromised SSH keys to gain unauthorized access, exfiltrate sensitive data, or establish persistent footholds. Such activities pose notable risks related to insider threats, unauthorized access, and potential data leakage prior to production deployment.

#### Implications for Production

In production environments, unauthorized access to SSH keys represents a serious threat, potentially enabling attackers to gain persistent access, escalate privileges, and move laterally within the network. Successful exploitation can lead to significant impacts, including data exfiltration, credential theft, and advanced persistent threats (APTs), compromising the confidentiality, integrity, and availability of critical systems and data.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Audit Pipeline Credentials**: Immediately review and audit all pipeline credentials and SSH keys to identify potential compromise or unauthorized access attempts.
2. **Enhance Monitoring and Logging**: Implement or enhance monitoring solutions to detect and alert on unauthorized access to SSH keys during pipeline execution.
3. **Strengthen Access Controls**: Enforce strict access controls and multi-factor authentication (MFA) for pipeline-related accounts and services to mitigate credential compromise risks.
4. **Regular Security Reviews**: Conduct regular security assessments and penetration tests to proactively identify and remediate vulnerabilities related to credential management and SSH key handling.

#### Actions for Staging

1. **Investigate Unauthorized Access**: Immediately investigate any detected unauthorized SSH key access to determine the scope and potential impact.
2. **Isolate Affected Systems**: Quickly isolate systems where unauthorized SSH key access was detected to prevent further compromise or lateral movement.
3. **Rotate Compromised Keys**: Rotate any potentially compromised SSH keys and enforce strict key management policies to reduce future risks.
4. **Enhance Security Controls**: Implement stricter security measures, including rigorous monitoring, logging, and access controls within the staging environment.

#### Actions for Production

1. **Immediate Incident Response**: Initiate incident response procedures to investigate, contain, and remediate any potential breaches resulting from unauthorized SSH key access.
2. **Notify Relevant Stakeholders**: Inform security teams, management, and potentially affected clients or partners about the incident to maintain transparency and trust.
3. **Credential Rotation and Management**: Immediately rotate compromised SSH keys and implement robust credential management practices, including regular rotation and multi-factor authentication.
4. **Continuous Monitoring and Improvement**: Deploy continuous monitoring solutions to detect similar threats in the future and continuously improve defense mechanisms based on the latest threat intelligence.
