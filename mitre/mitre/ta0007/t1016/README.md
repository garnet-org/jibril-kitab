---
description: System Network Configuration Discovery [T1016]
icon: wrench
---

# System Network Configuration Discovery

## Information

* Name: System Network Configuration Discovery
* ID: T1016
* Tactics: [TA0007](../)
* Sub-Technique: [T1016.001](t1016.001.md), T1016.002

## Introduction

System Network Configuration Discovery is categorized under the MITRE ATT\&CK framework as technique T1016. Attackers utilize this technique to gather detailed information about network configurations, interfaces, routing tables, DNS settings, and other network-related data. This reconnaissance enables adversaries to understand the target environment, identify potential pivot points, and plan subsequent attack stages effectively.

## Deep Dive Into Technique

System Network Configuration Discovery involves adversaries executing commands or scripts on compromised hosts to enumerate network settings and configurations. Attackers typically leverage built-in operating system utilities and commands, reducing the need for additional malicious tools and thus minimizing detection risk.

Common execution methods include:

* **Windows Environments:**
  * `ipconfig /all`: Displays detailed network adapter configurations, DNS servers, DHCP settings.
  * `route print`: Lists routing tables, showing network paths and gateways.
  * `arp -a`: Reveals ARP tables, mapping IP addresses to MAC addresses.
  * `netsh interface show`: Enumerates network interfaces and their configurations.
  * PowerShell commands such as `Get-NetIPConfiguration` or `Get-NetRoute`.
* **Linux/Unix Environments:**
  * `ifconfig` or `ip addr`: Displays IP addresses, subnet masks, and interface details.
  * `route -n` or `ip route`: Lists routing tables and gateway information.
  * `cat /etc/resolv.conf`: Provides DNS configuration settings.
  * `arp -a`: Lists ARP cache entries.
  * Commands such as `netstat -r` to display network routing tables.

Attackers may also use scripting languages such as Python, Bash, or PowerShell scripts to automate network discovery and exfiltrate configuration data quietly.

## When this Technique is Usually Used

System Network Configuration Discovery typically occurs in various attack scenarios and stages, including:

* **Initial Access and Reconnaissance:**
  * Immediately after gaining initial foothold to map the network environment.
  * Identifying valuable assets, servers, and network segments.
* **Lateral Movement:**
  * Discovering network routes, gateways, and reachable hosts to pivot internally.
  * Identifying internal DNS servers and network topology.
* **Privilege Escalation:**
  * Gathering network information to locate and exploit misconfigurations or vulnerable services.
  * Identifying network services running with elevated privileges.
* **Persistence and Command and Control (C2):**
  * Determining outbound network paths and firewall rules to establish persistent communications.
  * Understanding DNS configurations for domain fronting or DNS tunneling.
* **Data Exfiltration:**
  * Mapping network routes and configurations to identify optimal exfiltration paths.
  * Understanding firewall and proxy configurations to bypass network defenses.

## How this Technique is Usually Detected

Detection of System Network Configuration Discovery typically involves a combination of endpoint monitoring, log analysis, and network anomaly detection:

* **Endpoint Monitoring and EDR (Endpoint Detection and Response):**
  * Monitoring execution of unusual or suspicious system commands (`ipconfig`, `ifconfig`, `route`, `arp`).
  * Detecting PowerShell scripts or other scripting languages executing network enumeration commands.
  * Monitoring processes and command-line arguments that enumerate network configurations.
* **SIEM (Security Information and Event Management) and Log Analysis:**
  * Collecting and analyzing logs for unusual volume or frequency of network-related commands.
  * Identifying unexpected processes querying network configuration files (`/etc/resolv.conf`, Windows registry keys related to network settings).
* **Behavioral Analysis and Anomaly Detection:**
  * Detecting unusual patterns of command execution or abnormal enumeration activities.
  * Alerting on unexpected enumeration commands across multiple systems in short timeframes.
* **Network Monitoring and IDS/IPS (Intrusion Detection/Prevention Systems):**
  * Detecting network scanning or enumeration attempts that may follow network configuration discovery.
  * Identifying unusual DNS queries or ARP requests indicative of reconnaissance.

Specific Indicators of Compromise (IoCs) include:

* Execution of commands such as:
  * `ipconfig /all`
  * `route print`
  * `arp -a`
  * `ifconfig`
  * `netsh interface`
* Scripts or binaries performing repeated or scripted network enumeration.
* Suspicious or anomalous access to network configuration files or registry keys.

## Why it is Important to Detect This Technique

Early detection of System Network Configuration Discovery is crucial due to several potential impacts:

* **Facilitates Lateral Movement:**
  * Attackers use discovered network routes and configurations to pivot internally, compromising additional assets.
* **Enables Privilege Escalation:**
  * Misconfigurations or vulnerable network services identified during enumeration may enable attackers to escalate privileges.
* **Supports Data Exfiltration:**
  * Detailed network knowledge helps attackers identify optimal paths to exfiltrate sensitive data while evading detection.
* **Increases Attack Efficiency:**
  * Accurate network mapping reduces attacker dwell time and increases the speed and effectiveness of subsequent attacks.
* **Compromises Network Security:**
  * Understanding network defenses, firewall configurations, and DNS settings allows attackers to bypass security measures.

Early detection allows security teams to:

* Interrupt attacker reconnaissance before further compromise.
* Implement defensive measures proactively, such as network segmentation, access restrictions, and firewall rule adjustments.
* Investigate and remediate compromised hosts quickly, reducing overall attack impact.

## Examples

Real-world examples of System Network Configuration Discovery include:

* **APT28 (Fancy Bear):**
  * During intrusions, utilized commands such as `ipconfig /all`, `route print`, and `arp -a` to enumerate network configurations and plan lateral movement strategies.
  * Leveraged PowerShell scripts for automated network enumeration across multiple compromised hosts.
* **APT29 (Cozy Bear):**
  * Used native Linux commands (`ifconfig`, `route -n`, `cat /etc/resolv.conf`) after initial compromise to map out internal network infrastructure.
  * Conducted network reconnaissance to identify DNS configurations and internal network routes for command-and-control communications.
* **FIN7 Cybercrime Group:**
  * Executed automated scripts and batch files to enumerate network details (`netsh`, `ipconfig`) on compromised Windows endpoints.
  * Leveraged gathered network information to identify sensitive systems such as payment processing servers, leading to targeted data exfiltration.
* **WannaCry Ransomware:**
  * After initial infection, executed network enumeration commands (`ipconfig`, `arp`, `route`) to identify additional vulnerable hosts within the local subnet.
  * Used gathered network information to propagate laterally, significantly increasing attack impact and propagation speed.
* **TrickBot Malware:**
  * Performed detailed network configuration discovery to identify DNS servers, DHCP settings, and network routes.
  * Utilized this information to facilitate lateral movement, credential harvesting, and subsequent ransomware deployment (e.g., Ryuk ransomware).

In these examples, attackers primarily leveraged built-in operating system tools and commands, highlighting the importance of monitoring native system utilities and command execution patterns closely.
