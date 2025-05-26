---
icon: list-tree
---

# Filesystem Fingerprint

## Quick Explanation

The `filesystem_fingerprint` recipe detects access to files that contain detailed system information. These accesses can range from benign tasks to preparatory steps for malicious actions like data exfiltration or privilege escalation. When detected in CI/CD pipelines, it raises concerns about unnecessary access to low-level system information, potentially introducing security vulnerabilities.

## More Information

### Information

**Description**: Filesystem fingerprint **Category**: Discovery **Method**: System Information Discovery **Importance**: Low

### Analysis of the Event

The `filesystem_fingerprint` detection event is triggered when specific system files related to disk and filesystem configurations are accessed in a manner suggesting an attempt to gather detailed system information. According to the MITRE ATT\&CK framework, this activity falls under the **Discovery category**, specifically System Information Discovery (T1082). The intention behind accessing these files can range from routine system management tasks to preparatory steps for more invasive actions by an adversary, such as data exfiltration or privilege escalation.

The targeted files (`/etc/fstab`, `/proc/diskstats`, `/proc/filesystems`, etc.) are crucial for understanding the layout and usage of filesystems and storage on a Linux system. Accessing these files can reveal information about storage devices, partition configurations, and mounted filesystems, which could be used to tailor further attacks or evade defenses based on system configuration.

Adversaries often use this information-gathering phase to understand the environment before executing more sophisticated attacks like lateral movement (T1021) or credential access (T1078). This reconnaissance activity can also help attackers in evading detection by blending their activities with normal traffic patterns, as seen in network intrusion scenarios where DNS tunneling and covert channels are employed.

### Implications

#### Implications for CI/CD Pipelines

Detecting such an event during a CI/CD pipeline execution raises concerns about why build processes require access to low-level system information. This is generally unnecessary for most build and test operations, and its presence may indicate potential security flaws or vulnerabilities being introduced into the environment. For instance, it could lead to unauthorized disclosure of sensitive information about server configurations in a production environment, potentially aiding attackers in crafting targeted attacks.

#### Implications for Staging

In staging environments, adversarial testing might involve attempts to gather system fingerprints before deploying malicious code. This phase also poses risks such as data leakage due to misconfigured access controls and insider threats from developers or testers with elevated privileges.

#### Implications for Production

In a production environment, the long-term persistence risk is heightened by adversaries who may use this information for lateral movement within the network (T1021) or credential theft (T1078). Data exfiltration becomes more feasible once system configurations are known. Advanced Persistent Threats (APT) often leverage such detailed reconnaissance to maintain a foothold in the network over extended periods.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Review Pipeline Configurations**: Examine the CI/CD pipeline configurations to identify why access to low-level system files is occurring. Ensure that only necessary permissions are granted to the build processes.
2. **Implement Access Controls**: Restrict access to sensitive system files within the CI/CD environment. Ensure that only authorized processes and users can access these files.
3. **Security Training**: Educate the development and operations teams on the importance of minimizing access to sensitive system information during build processes.

#### Actions for Staging

1. **Conduct Security Assessments**: Perform regular security assessments to identify and mitigate any misconfigured access controls that could lead to unauthorized file access.
2. **Limit Privileges**: Ensure that developers and testers have the minimum necessary privileges to perform their tasks, reducing the risk of insider threats.
3. **Test Security Controls**: Regularly test security controls to ensure they effectively prevent unauthorized access to system files.

#### Actions for Production

1. **Strengthen Network Defenses**: Enhance network defenses to detect and prevent lateral movement and credential theft attempts that may follow system information discovery.
2. **Implement Data Loss Prevention (DLP)**: Deploy DLP solutions to monitor and prevent data exfiltration attempts that could exploit known system configurations.
3. **Conduct Threat Hunting**: Engage in proactive threat hunting to identify and mitigate potential APT activities leveraging detailed system reconnaissance.
4. **Regularly Update Security Policies**: Ensure security policies are up-to-date and reflect the latest threat intelligence to protect against evolving attack vectors.
