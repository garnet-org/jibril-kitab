---
icon: bitcoin
---

# Crypto Miner Files

## Quick Explanation

This Jibril detection recipe targets suspicious files related to cryptocurrency mining. It highlights newly introduced miner-related files, libraries, and scripts within the CI/CD pipeline. By flagging these occurrences, the goal is to prevent malicious exploitation of resources, unauthorized access, or embedding of miner code in production artifacts.

## More Information

### Information

**Description**: Crypto miner execution **Category**: Resource Development **Method**: Establish Account **Importance**: Critical

### Analysis of the Event

The `crypto_miner_files` event covers a wide range of filenames, library files, and scripts commonly associated with crypto mining operations. Jibril’s tracing mechanism, powered by eBPF (Extended Berkeley Packet Filter), looks for file access actions and checks these files against a curated miner-related list.

In legitimate scenarios, some of these tools could appear in testing or research environments but their presence within a CI pipeline is highly unusual and may suggest unauthorized activities. Attackers often embed miners into container images or inject them via scripts to hijack computing resources. If successful, they could remain undetected for extended periods, leveraging the pipeline’s infrastructure to mine cryptocurrency.

This also opens the door to broader exploitation strategies, such as creating new accounts (MITRE ATT\&CK T1098 - Account Manipulation) or pivoting to more critical systems, all while hiding behind seemingly legitimate CI processes. Adversaries may use covert channels like DNS tunneling (T1048 - Exfiltration Over Alternative Protocol) and supply chain risks to bypass security controls.

Compromised builds can also threaten downstream environments if the malicious artifacts are deployed to staging or production. This risk extends to potential data leaks, financial fraud, and further infiltration of corporate networks through lateral movement techniques like T1027 - Recreate File or Directory from Memory (MITRE ATT\&CK technique).

### Implications

#### Implications for CI/CD Pipelines

* **Drain Resources**: Cryptominer binaries consume significant CPU/GPU cycles, slowing builds and increasing operational costs. This can be detected through network analysis tools that monitor unusual traffic patterns or high resource utilization.
* **Threaten Build Integrity**: Malicious scripts or code injected into build artifacts can propagate to production, impacting reliability and trust. Detection strategies include behavior-based detection systems (e.g., SIEM) and anomaly identification techniques that flag unexpected changes in the artifact integrity.
* **Enable Persistence**: Attackers may establish hidden accounts or backdoor services, persisting across future builds and deployments. This can be mitigated by implementing strict access controls and monitoring for unauthorized account creation using tools like Jibril’s eBPF-based detectors.
* **Exfiltrate Sensitive Data**: While running with elevated privileges, miners or scripts might collect credentials, tokens, or other critical information, exposing the broader infrastructure. Threat intelligence insights can help identify known attack patterns and forensic investigation methods can be used to trace data exfiltration attempts.

#### Implications for Staging

* **Adversarial Testing**: Testing environments may be targeted for adversarial testing where attackers attempt to exploit vulnerabilities in staging environments before deploying attacks on production systems. Monitoring tools like SIEM can detect unusual activity indicative of such testing.
* **Unauthorized Access**: Unauthorized access to staging environments can lead to the deployment of malicious code into production. Implementing strict access controls and monitoring for unauthorized access attempts is crucial.

#### Implications for Production

* **Resource Hijacking**: Cryptominers deployed in production can significantly reduce system performance, leading to costly downtime and potential data breaches. Resource quotas (e.g., Kubernetes resource limits) can help mitigate the impact of cryptomining on system resources.
* **Data Breaches**: Compromised systems can lead to unauthorized access to sensitive data. Implementing strong encryption and monitoring for exfiltration attempts using tools like DNS anomaly detection can help prevent data breaches.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Audit and Review Build Logs**: Regularly audit your CI/CD pipeline logs for any unusual activity or unauthorized changes to the build configurations and scripts. Look specifically for the introduction of new, unexpected files or alterations to existing scripts.
2. **Enhance Monitoring and Alerting**: Implement or enhance monitoring tools to detect unusual CPU/GPU usage or network traffic patterns that could indicate the presence of crypto mining activities. Set up alerts for these metrics to catch anomalies early.
3. **Strengthen Access Controls**: Review and tighten access controls around your CI/CD environments. Ensure that only authorized personnel have the necessary permissions, and use multi-factor authentication to secure access points.
4. **Conduct Regular Security Audits and Penetration Testing**: Regularly perform security audits and penetration tests to identify and mitigate vulnerabilities in your CI/CD pipeline that could be exploited to inject malicious code or scripts.

#### Actions for Staging

1. **Implement Strict Access Controls**: Ensure that access to staging environments is strictly controlled and monitored. Use role-based access controls to limit who can deploy and make changes to these environments.
2. **Regularly Update and Patch Systems**: Keep all systems and applications in the staging environment updated and patched to prevent exploitation of known vulnerabilities.
3. **Use Segregation of Duties (SoD) Principles**: Apply segregation of duties principles to separate roles and responsibilities, which can help prevent unauthorized changes and reduce the risk of insider threats.
4. **Monitor for Anomalous Behavior**: Deploy monitoring tools that can detect and alert on suspicious activity or deviations from normal baseline behavior in the staging environment.

#### Actions for Production

1. **Implement Resource Quotas and Limits**: Use resource quotas and limits in your production environment, especially in containerized deployments like Kubernetes, to mitigate the impact of any potential crypto mining activities.
2. **Continuous Monitoring for Data Exfiltration**: Deploy tools that continuously monitor for data exfiltration attempts, particularly focusing on unusual outbound traffic patterns and DNS queries.
3. **Regular Security Assessments**: Conduct regular security assessments to identify and address security gaps that could be exploited to install crypto miners or other malicious software.
4. **Incident Response Plan**: Develop and regularly update an incident response plan that includes procedures for responding to crypto mining and other security incidents to minimize damage and recover operations quickly.
