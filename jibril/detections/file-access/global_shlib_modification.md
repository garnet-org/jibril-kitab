---
icon: books
---

# Global Shlib Modification

## Quick Explanation

The `global_shlib_modification` recipe detects modifications to the `/etc/ld.so.preload` file, which is used by the dynamic linker to preload shared libraries during system startup. Such modifications are a critical persistence technique that enables unauthorized code execution covertly during boot or logon processes. Detected in a CI/CD pipeline pull request, this event suggests potential malicious code injection, posing significant risks to both CI and production environments. If left undetected, it could lead to persistent unauthorized access, severely compromising system integrity.

## More Information

### Information

**Description**: Global shared library injection  
**Tactic**: [Persistence](../../mitre/tactics/TA0003.md)  
**Technique**: [Boot Or Logon Autostart Execution](../../mitre/techniques/T1547.md)  
**Sub-Technique**: [Kernel Modules And Extensions](../../mitre/techniques/T1547.006.md)  
**Importance**: Critical

### Analysis of the Event

This security event involves detecting a shared library injection through the modification of the `ld.so.preload` file located in the `/etc` directory. The `ld.so.preload` file is used by the dynamic linker to preload shared libraries during system startup, making it a prime target for persistence mechanisms. Malicious actors can exploit this technique to load unauthorized code early in the system’s startup sequence. This method is often employed for stealthy and persistent attacks, allowing malicious code to execute without direct user or administrator interaction.

In this instance, the Jibril runtime tracing tool identified an attempt to modify the`ld.so.preload` file, classified under the persistence category. The "boot\_or\_logon\_autostart\_execution" method is a common persistence technique that exploits system autostart mechanisms. According to the MITRE ATT\&CK framework, this behavior falls under the T1547.006 tactic (Persistence: Boot or Logon Autostart Execution - Ld.so Preload), where attackers modify critical configuration files to maintain unauthorized access.

The attack vector in this event is specifically related to file access and execution, as modifying a key configuration file like `ld.so.preload` can trigger the loading of malicious shared libraries. This could result in covert channels for data exfiltration or DNS tunneling, allowing attackers to bypass network security controls. The introduction of such modifications during the CI/CD pipeline likely indicates a deliberate injection of malicious code that would persist across reboots if undetected.

### Implications

#### Implications for CI/CD Pipelines

The detection of this event during a pull request suggests that malicious code was either introduced or triggered during the CI testing process. This poses significant risks to both CI and production environments, as the modified `ld.so.preload` file would preload shared libraries containing unauthorized or malicious functionality. If merged into the main branch and deployed, it could result in long-term persistence for attackers, granting them continuous access every time the system boots. Furthermore, this could compromise the integrity of the CI/CD pipeline by tampering with test results, introducing false positives or negatives, and potentially masking other vulnerabilities.

#### Implications for Staging

In a staging environment, adversarial testing might reveal data leakage or unauthorized access risks before production deployment. Malicious actors could leverage these environments to gain insights into system configurations and potential vulnerabilities, preparing for attacks on the actual production systems. This could include exploiting misconfigurations in shared libraries or leveraging known vulnerabilities within preloaded modules.

#### Implications for Production

Deployed systems with compromised `ld.so.preload` files are at high risk of backdoor access and unauthorized control over critical processes. Such a breach can lead to severe security breaches, including data exfiltration, system compromise, and potential lateral movement across the network. Additionally, attackers could use these entry points for further exploitation or to establish persistent footholds within the infrastructure.

### Recommended Actions

#### Actions for CI/CD Pipelines

1. **Audit and Review Code Changes**: Immediately review the pull request that triggered the detection, focusing on changes made to the `/etc/ld.so.preload` file. Identify the contributor and the source of the changes to ascertain if they were intentional or malicious.
2. **Enhance Security Checks**: Integrate additional security scanning tools into the CI/CD pipeline to detect similar attempts in the future. Consider tools that perform more in-depth analysis of file modifications and their implications on system security.
3. **Educate Developers**: Conduct training sessions for developers on secure coding practices, emphasizing the importance of understanding changes to system-critical files and the potential security risks associated with these changes.
4. **Isolate and Test Changes**: Isolate the changes in a controlled environment and perform thorough testing, including behavior analysis and backtracking, to understand the full impact of the modification on the system.

#### Actions for Staging

1. **Perform Comprehensive Security Audits**: Before moving any code from staging to production, ensure that comprehensive security audits are conducted. This includes reviewing all modifications to critical system files like `/etc/ld.so.preload`.
2. **Simulate Attack Scenarios**: Use the staging environment to simulate potential attack scenarios that could arise from the modification of the `ld.so.preload` file. This helps in understanding the potential impacts and preparing appropriate mitigation strategies.
3. **Verify Integrity of Shared Libraries**: Check the integrity and authenticity of all shared libraries that are preloaded as part of the system startup. Ensure they are from trusted sources and have not been tampered with.

#### Actions for Production

1. **Immediate Rollback and Containment**: If the compromised code has been deployed to production, initiate an immediate rollback to a previous known safe state. Isolate affected systems to prevent further unauthorized access or damage.
2. **Patch and Harden Systems**: After addressing the immediate threat, focus on patching the vulnerability and hardening systems against similar attacks. This might include revising system permissions, enhancing file integrity monitoring, and updating security protocols.
