---
icon: arrows-to-circle
---

# Core Pattern Access

## Quick Explanation

The `core_pattern_access` recipe detects unauthorized modifications to the system's core dump pattern configuration file. This file is essential for debugging and forensic analysis as it dictates how the kernel manages core dumps, including their formatting and output destination. Unauthorized changes can redirect or manipulate core dumps to evade detection or conceal malicious activities, leading to inaccurate system state information during crashes, which may be induced by exploits.

## More Information

### Information

**Description**: Core pattern config file access  
**Tactic**: [Defense Evasion](https://jibril.garnet.ai/mitre/mitre/ta0005)  
**Technique**: [Impair Defenses](https://jibril.garnet.ai/mitre/mitre/ta0005/t1562)  
**Sub-Technique**: [Disable Or Modify System Firewall](https://jibril.garnet.ai/mitre/mitre/ta0005/t1562/t1562.004)  
**Importance**: Critical

### Analysis of the Event

The `core_pattern_access` detection event is triggered when there are attempts to modify the system's core dump pattern, typically found at `/proc/sys/kernel/core_pattern`. This configuration file is crucial for managing how the kernel handles core dumps—files generated during a program crash that contain valuable information about the state of the process at the time of failure. By altering this setting, adversaries can redirect or manipulate these core dumps to evade detection or obscure malicious activity, which aligns with the MITRE ATT\&CK framework's tactics for defense evasion and impairment of defensive measures.

In practical terms, such modifications can prevent system administrators and security tools from obtaining accurate information about the system’s state during a crash. This could be particularly problematic if the crash was caused by an exploit or other malicious activities. Attackers might alter core dump handling to remove traces of their presence or activity, thereby making forensic analysis more challenging.

### Implications

#### Implications for CI/CD Pipelines

Risks related to build process compromise, dependency poisoning, and artifact integrity include attempts to modify `/proc/sys/kernel/core_pattern` during a CI/CD pipeline execution. Such changes might introduce vulnerabilities or backdoors intended to manipulate system behavior during error handling. If such modifications were merged into production, it could lead to compromised systems where forensic data is unreliable or misleading, significantly hampering incident response and recovery efforts in a live environment.

#### Implications for Staging

Adversarial testing may involve manipulating `/proc/sys/kernel/core_pattern` to test the resilience of staging environments against core dump redirection attacks. Data leakage risks arise if attackers can access sensitive information through manipulated core dumps. Insider threats are also heightened as unauthorized personnel might exploit this vector to exfiltrate data or cover their tracks before production deployment.

#### Implications for Production

In a production environment, long-term persistence risks increase due to the potential for malicious actors to redirect core dump outputs to locations under their control, facilitating lateral movement and credential theft. Data exfiltration becomes feasible through manipulated core dumps that contain sensitive information. Advanced persistent threats (APT) can leverage these techniques to maintain stealthy footholds within systems.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Review and Audit**: Immediately review recent changes in the CI/CD pipeline configuration and scripts to identify unauthorized modifications to`/proc/sys/kernel/core_pattern`. Ensure that only authorized personnel have access to modify these settings.
2. **Secure Access Controls**: Strengthen access controls and permissions around CI/CD tools and environments to prevent unauthorized modifications. Consider implementing role-based access controls (RBAC) and multi-factor authentication (MFA).
3. **Conduct a Security Assessment**: Perform a thorough security assessment of the CI/CD pipeline to identify and mitigate potential vulnerabilities that could be exploited to alter core dump settings.

#### Actions for Staging

1. **Validate Configuration Integrity**: Check the integrity of the core pattern configuration in the staging environment and ensure it matches the expected secure configuration.
2. **Simulate Attacks**: Conduct security testing, such as penetration testing or red team exercises, to simulate core dump manipulation attacks and assess the environment's resilience.
3. **Restrict Access**: Limit access to the staging environment to only essential personnel and ensure that all changes are logged and reviewed.
4. **Data Protection Measures**: Implement data protection measures to prevent sensitive information leakage through core dumps, such as encryption and access logging.

#### Actions for Production

1. **Immediate Investigation**: Investigate any unauthorized changes to the core pattern configuration in the production environment to determine if there has been a security breach.
2. **Restore Secure Settings**: Revert any unauthorized changes to the core pattern configuration and ensure it is set to a secure state.
3. **Incident Response Plan**: Update and test the incident response plan to ensure it includes procedures for handling core pattern access events and potential data exfil
