---
icon: key
---

# SSH Auth Keys Modification

## Quick Explanation

The `ssh_authorized_keys_modification` detection recipe identifies unusual write or rename operations targeting the SSH `authorized_keys` file. Such modifications can indicate attempts by attackers to establish persistent access by injecting unauthorized SSH keys, potentially enabling future unauthorized logins and lateral movement within the environment.

## More Information

### Information

**Description**: Unusual write or rename to SSH authorized_keys file  
**Tactic**: [Persistence](https://jibril.garnet.ai/mitre/mitre/ta0007)  
**Technique**: [Account Manipulation](https://jibril.garnet.ai/mitre/mitre/ta0007/t1098)  
**Sub-Technique**: [None](https://jibril.garnet.ai/mitre/mitre/ta0007/t1098/t1098.001)  
**Importance**: Critical

### Analysis of the Event

The `ssh_authorized_keys_modification` detection, flagged by Jibril, highlights a persistence method where attackers attempt to modify or rename the SSH `authorized_keys` file. Attackers commonly target this file to insert their own SSH public keys, allowing them persistent and unauthorized access to compromised systems.

From a security perspective, this tactic aligns with the MITRE ATT&CK framework's Persistence techniques under T1098 (Account Manipulation). Unauthorized modifications to the `authorized_keys` file can enable attackers to maintain long-term access, bypass authentication mechanisms, and facilitate lateral movement across the network.

While legitimate administrative actions may occasionally involve modifying the `authorized_keys` file, unexpected or unauthorized modifications should be immediately investigated.

### Implications

#### Implications for CI/CD Pipelines

Detection of unauthorized modifications to the SSH `authorized_keys` file during CI/CD pipeline execution indicates a potential compromise or unauthorized access attempt. Attackers may leverage this access to inject malicious code, compromise build artifacts, or gain persistent access to sensitive infrastructure. This can lead to unauthorized deployments, data breaches, and persistent threats within the pipeline environment.

#### Implications for Staging

In staging environments, unauthorized modifications to the SSH `authorized_keys` file may indicate adversarial attempts to establish persistent access or escalate privileges. Attackers could leverage compromised SSH keys to gain unauthorized access, exfiltrate sensitive data, or establish persistent footholds. Such activities pose significant risks related to insider threats, unauthorized access, and potential data leakage prior to production deployment.

#### Implications for Production

In production environments, unauthorized modifications to the SSH `authorized_keys` file represent a critical threat, potentially enabling attackers to gain persistent access, escalate privileges, and move laterally within the network. Successful exploitation can lead to severe impacts, including data exfiltration, credential theft, and advanced persistent threats (APTs), compromising the confidentiality, integrity, and availability of critical systems and data.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Audit SSH Key Management**: Immediately review and audit all SSH keys and authorized_keys files within pipeline environments to identify potential compromise or unauthorized modifications.
2. **Enhance Monitoring and Logging**: Implement or enhance monitoring solutions to detect and alert on unauthorized modifications to SSH authorized_keys files during pipeline execution.
3. **Strengthen Access Controls**: Enforce strict access controls and multi-factor authentication (MFA) for pipeline-related accounts and services to mitigate risks associated with unauthorized SSH key modifications.
4. **Regular Security Reviews**: Conduct regular security assessments and penetration tests to proactively identify and remediate vulnerabilities related to SSH key management and authorized_keys file handling.

#### Actions for Staging

1. **Investigate Unauthorized Modifications**: Immediately investigate any detected unauthorized modifications to the SSH authorized_keys file to determine the scope and potential impact.
2. **Isolate Affected Systems**: Quickly isolate systems where unauthorized modifications were detected to prevent further compromise or lateral movement.
3. **Rotate Compromised Keys**: Rotate any potentially compromised SSH keys and enforce strict key management policies to reduce future risks.
4. **Enhance Security Controls**: Implement stricter security measures, including rigorous monitoring, logging, and access controls within the staging environment.

#### Actions for Production

1. **Immediate Incident Response**: Initiate incident response procedures to investigate, contain, and remediate any potential breaches resulting from unauthorized SSH authorized_keys file modifications.
2. **Notify Relevant Stakeholders**: Inform security teams, management, and potentially affected clients or partners about the incident to maintain transparency and trust.
3. **Credential Rotation and Management**: Immediately rotate compromised SSH keys and implement robust credential management practices, including regular rotation and multi-factor authentication.
4. **Continuous Monitoring and Improvement**: Deploy continuous monitoring solutions to detect similar threats in the future and continuously improve defense mechanisms based on the latest threat intelligence.
