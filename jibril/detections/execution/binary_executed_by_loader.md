---
icon: file-binary
---

# Binary Executed By Loader

## Quick Explanation

The `binary_executed_by_loader` detection recipe identifies when a binary is executed through a loader, such as `ld.so`. This event can indicate an attempt by adversaries to bypass standard execution paths, potentially leading to unauthorized access or control over the system. Such behavior aligns with various attack vectors and evasion techniques documented in the MITRE ATT\&CK framework.

## More Information

### Information

**Description**: Binary executed through loader  
**Tactic**: [Defense Evasion](https://jibril.garnet.ai/mitre/mitre/ta0005)  
**Technique**: [Hijack Execution Flow](https://jibril.garnet.ai/mitre/mitre/ta0005/t1574)  
**Importance**: Critical

### Analysis of the Event

The detection of a binary being executed through a loader, such as `ld.so`, is flagged as suspicious due to its potential use in evading security controls and executing unauthorized actions within the system. This event aligns with the MITRE ATT\&CK framework's Execution category, specifically under System Services techniques (T1543). Adversaries often leverage legitimate system services or loaders to execute malicious payloads, aiming to blend their activities among normal operations and evade detection.

In real-world scenarios, such as the SolarWinds supply chain attack, adversaries used legitimate binaries and loaders to inject malware into trusted software updates. This technique allowed them to maintain persistence and move laterally within victim networks undetected for extended periods. The critical importance of this event underscores its potential to enable significant threats, including unauthorized access, control over system processes, and the execution of malicious payloads.

### Implications

#### Implications for CI/CD Pipelines

Risks related to build process compromise, dependency poisoning, and artifact integrity are heightened when a binary is executed through an unvetted loader. Adversaries could exploit this vector to inject malicious code into builds or modify dependencies to introduce vulnerabilities. This poses significant risks of data breaches, service disruptions, and the propagation of compromised artifacts across the pipeline.

#### Implications for Staging

Adversarial testing, data leakage, insider threats, and unauthorized access risks before production deployment are critical concerns in staging environments. The execution through loaders can be a precursor for lateral movement within the environment, allowing attackers to gather sensitive information or test further exploitation methods without immediate detection.

#### Implications for Production

Long-term persistence risks, lateral movement, credential theft, data exfiltration, and advanced persistent threats (APT) become more pronounced once such behavior is detected in production. Adversaries may use loaders to establish persistent backdoors, enabling continuous access and control over critical systems. This can lead to sustained data breaches and operational disruptions.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Audit and Review Build Processes**: Immediately review and audit all build and deployment scripts to ensure no unauthorized changes have been made. Focus on the integrity of the loaders and any scripts that invoke system services.
2. **Strengthen Artifact Security**: Implement strict controls on artifact repositories to prevent unauthorized access and modifications. Consider using cryptographic signatures to verify the integrity of binaries before deployment.
3. **Enhance Monitoring and Logging**: Increase the logging level around build processes and loader activities. Set up alerts for any unusual loader activity or unexpected binary executions.

#### Actions for Staging

1. **Conduct a Thorough Security Assessment**: Perform a detailed security assessment of the staging environment to identify any potential compromises or vulnerabilities associated with loader activities.
2. **Isolate and Analyze Suspicious Activities**: Isolate environments where suspicious loader activities have been detected. Perform a forensic analysis to understand the scope and impact of the issue.
3. **Update and Harden Security Policies**: Review and update security policies and access controls based on findings from the security assessment. Ensure that loaders and system services are covered by these policies.

#### Actions for Production

1. **Immediate Containment and Mitigation**: Initiate containment measures to prevent any potential spread or escalation of the issue. This may include temporarily suspending affected systems or services.
2. **Root Cause Analysis and Remediation**: Conduct a root cause analysis to determine how and why the unauthorized loader activity occurred. Follow up with comprehensive remediation steps to address the identified issues.
3. **Regular Security Audits and Updates**: Schedule regular security audits to ensure continuous monitoring and updating of security measures in response to emerging threats and vulnerabilities.
