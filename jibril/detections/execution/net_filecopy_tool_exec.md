---
icon: paste
---

# Net Filecopy Tool Exec

## Quick Explanation

The `net_filecopy_tool_exec` recipe identifies the execution of network file copy tools, which is crucial for detecting potential unauthorized data transfers and exfiltration attempts. This event has significant implications for the CI/CD pipeline, as it suggests that recent changes in a pull request might introduce or modify scripts using these tools, posing a risk of sensitive information leakage.

## More Information

### Information

**Description**: Network file copy tool execution  
**Tactic**: [Exfiltration](../../mitre/tactics/TA0010.md)  
**Technique**: [Exfiltration Over Other Network Medium](../../mitre/techniques/T1011.md)  
**Importance**: Critical

### Analysis of the Event

This detection event is triggered when a network file copy tool is executed within the monitored environment. The tools identified include popular utilities such as `scp`,`rsync`, `sftp`, and others used for transferring files over a network. The detection mechanism relies on monitoring file execution events, specifically targeting commands known for their capability to exfiltrate data across different network mediums.

According to the MITRE ATT\&CK framework, this falls under the Exfiltration tactic (T1048), with the technique being "Exfiltration Over Other Network Medium". This technique involves adversaries using non-standard protocols or tools to transfer data out of a compromised environment, often bypassing traditional security controls that monitor standard data transfer methods. Adversaries might leverage DNS tunneling, covert channels, or other obfuscation techniques to evade detection.

The implications of such an event are significant, as it indicates potential unauthorized data transfers that could lead to sensitive information leakage. This detection helps identify attempts to move data out of the organization through less monitored paths, thereby providing an opportunity to mitigate potential data breaches. Historical attack patterns show that attackers often use these tools in conjunction with other techniques like living off the land (LotL) and persistence mechanisms.

### Implications

#### Implications for CI/CD Pipelines

Risks related to build process compromise, dependency poisoning, and artifact integrity are heightened when network file copy tools are detected. Attackers may exploit these tools during the build process to inject malicious payloads or exfiltrate sensitive data from the build artifacts themselves. Dependency poisoning can introduce backdoors into the software supply chain, while compromised artifact integrity could result in unauthorized modifications being pushed through.

#### Implications for Staging

Adversarial testing, data leakage, insider threats, and unauthorized access risks before production deployment are critical concerns. During staging, adversaries might use network file copy tools to test exfiltration methods or to steal sensitive information from the pre-production environment. This can lead to significant data breaches if not detected early.

#### Implications for Production

Long-term persistence risks, lateral movement, credential theft, data exfiltration, and advanced persistent threats (APT) are all potential consequences of using network file copy tools in production environments. APT actors often use these tools to maintain a foothold within the organization's infrastructure, moving laterally across systems and stealing credentials or sensitive information over extended periods.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Review Recent Changes**: Inspect recent pull requests and code changes for unauthorized modifications or the introduction of network file copy tools. Focus on scripts and configuration files.
2. **Audit Build Scripts**: Conduct a thorough audit of all build scripts and related processes to ensure they do not contain calls to network file copy tools unless explicitly required and approved.
3. **Educate Developers**: Provide training for developers on secure coding practices and the risks associated with using network file copy tools in the software development lifecycle.

#### Actions for Staging

1. **Conduct Security Assessments**: Regularly perform security assessments and penetration testing in the staging environment to identify and mitigate unauthorized use of file copy tools.
2. **Implement Strict Access Controls**: Ensure that access to the staging environment is restricted based on roles, and audit these controls frequently.
3. **Log and Monitor**: Increase logging and monitoring capabilities to capture all executions of network file copy tools and review logs regularly for suspicious activity.

#### Actions for Production

1. **Forensic Analysis**: If network file copy tools are detected, perform a forensic analysis to understand the scope of the potential breach and identify the source.
2. **Regular Security Audits**: Schedule regular security audits of the production environment to check for vulnerabilities that might be exploited by attackers using file copy tools.
3. **Update Incident Response Plan**: Ensure that the incident response plan includes specific procedures for dealing with unauthorized data transfers and the use of network file copy tools.
