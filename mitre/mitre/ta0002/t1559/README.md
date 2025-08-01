---
description: Inter-Process Communication [T1559]
icon: link
---

# Inter-Process Communication

## Information

* Name: Inter-Process Communication
* ID: T1559
* Tactics: [TA0002](../)
* Sub-Technique: [T1559.002](t1559.002.md), [T1559.001](t1559.001.md), [T1559.003](t1559.003.md)

## Introduction

Inter-Process Communication (IPC), as defined in the MITRE ATT\&CK framework (Technique ID: T1559), refers to adversaries abusing mechanisms designed for communication between processes to execute malicious activities. IPC enables processes to exchange data and synchronize their actions, often through shared memory, named pipes, sockets, message queues, or other OS-provided methods. Attackers exploit IPC mechanisms to evade detection, escalate privileges, or maintain persistence while blending in with legitimate system operations.

## Deep Dive Into Technique

Inter-Process Communication is fundamental to modern operating systems, facilitating data exchange and synchronization between processes. Attackers exploit IPC mechanisms by leveraging legitimate OS functionalities, making detection challenging.

Common IPC mechanisms exploited include:

* **Named Pipes:**
  * Attackers create or hijack existing named pipes to communicate between malware components or compromised processes.
  * Named pipes can facilitate lateral movement, privilege escalation, or data exfiltration, often bypassing traditional detection methods.
* **Sockets:**
  * Local sockets (Unix domain sockets, Windows sockets) allow attackers to perform covert communications between malicious processes on the same host.
  * Attackers can create hidden sockets to tunnel data, evade network-based monitoring, or transmit commands.
* **Shared Memory:**
  * Attackers use shared memory segments to transfer data or inject malicious payloads directly into legitimate processes.
  * Shared memory can be leveraged to evade traditional file-based detection mechanisms.
* **Message Queues and Mail Slots:**
  * Attackers may misuse message queues or mail slots to facilitate asynchronous communication between processes, enabling stealthy command-and-control (C2) channels on compromised hosts.

Technical execution methods include:

* Injecting malicious payloads into legitimate processes via IPC mechanisms (e.g., process injection through shared memory).
* Leveraging legitimate IPC channels to communicate between malware components, reducing suspicious network traffic.
* Hijacking existing IPC endpoints to blend malicious activities with normal system operations.

Real-world procedures observed include:

* Malware families such as Cobalt Strike and Metasploit leveraging named pipes for lateral movement and command execution.
* Advanced Persistent Threat (APT) groups utilizing sockets and shared memory to evade detection during espionage campaigns.

## When this Technique is Usually Used

Attackers utilize IPC mechanisms across multiple attack stages and scenarios, including:

* **Privilege Escalation:**
  * Exploiting IPC channels to inject payloads into higher-privileged processes, escalating attacker privileges.
* **Defense Evasion:**
  * Using IPC to bypass file-based detection, antivirus solutions, and endpoint monitoring tools by avoiding writing malicious payloads to disk.
* **Lateral Movement:**
  * Leveraging named pipes and sockets to communicate between compromised hosts or processes within the network, facilitating lateral movement without generating network alerts.
* **Command and Control (C2):**
  * Establishing covert communication channels between malware components or compromised processes within the same host, reducing external network visibility.
* **Persistence:**
  * Maintaining persistent communication channels between malicious processes and legitimate system services to ensure long-term access.

## How this Technique is Usually Detected

Detecting malicious IPC use requires specialized monitoring and analysis techniques, including:

* **Endpoint Detection and Response (EDR) Tools:**
  * Monitoring process interactions and IPC activities at the system level.
  * Detecting anomalous named pipe creations, socket connections, or shared memory segments.
* **Sysmon and OS-Level Logging:**
  * Utilizing tools such as Sysinternals Sysmon to log named pipe events, socket creations, and shared memory operations.
  * Analyzing logs for suspicious IPC endpoint names or unusual process interactions.
* **Behavioral Analysis and Anomaly Detection:**
  * Establishing baseline IPC activity patterns and alerting on deviations or uncommon IPC usage scenarios.
* **Memory Forensics:**
  * Analyzing memory dumps to detect injected payloads or anomalous shared memory segments.

Indicators of Compromise (IoCs) specific to IPC abuse include:

* Suspicious or randomly named IPC endpoints (named pipes, sockets, shared memory segments).
* Unexpected IPC communications between unrelated processes.
* Anomalous process injection events correlated with IPC activities.
* Known malicious IPC endpoint names associated with tools like Cobalt Strike or Metasploit.

## Why it is Important to Detect This Technique

Early detection of malicious IPC usage is critical due to significant potential impacts on systems and networks, including:

* **Privilege Escalation:**
  * Attackers leveraging IPC to inject payloads into privileged processes, leading to unauthorized administrative access.
* **Persistence and Stealth:**
  * IPC allows attackers to maintain covert, persistent communication channels, making detection and remediation challenging.
* **Defense Evasion:**
  * IPC abuse bypasses traditional file-based antivirus and endpoint security tools, enabling attackers to operate undetected for extended periods.
* **Lateral Movement Facilitation:**
  * Attackers use IPC mechanisms such as named pipes and sockets to move laterally within networks quietly, increasing the scale and severity of breaches.
* **Data Exfiltration and Espionage:**
  * Malicious IPC channels can facilitate stealthy data exfiltration or espionage activities, resulting in significant data loss or compromise of sensitive information.

Detecting IPC misuse early enables rapid containment, reduces the severity of breaches, and limits attackers' ability to escalate privileges or maintain persistence.

## Examples

Real-world examples of IPC abuse in cyberattacks include:

* **Cobalt Strike Framework:**
  * Attack Scenario:
    * Utilizes named pipes to facilitate lateral movement and command execution between compromised hosts.
  * Tools Used:
    * Cobalt Strike beacon payloads communicating via named pipes.
  * Impacts:
    * Successful lateral movement, privilege escalation, and persistent access within enterprise networks.
* **Metasploit Framework:**
  * Attack Scenario:
    * Employs named pipes and sockets for local communication between payloads and compromised processes.
  * Tools Used:
    * Metasploit Meterpreter payloads leveraging IPC for stealthy communication.
  * Impacts:
    * Persistent remote access, evasion of endpoint detection tools, and covert lateral movement.
* **Duqu Malware:**
  * Attack Scenario:
    * Utilizes shared memory segments for process injection and stealthy communication between malware components.
  * Tools Used:
    * Custom malware payloads exploiting shared memory IPC.
  * Impacts:
    * Espionage activities, persistent access, and defense evasion in targeted cyberattacks.
* **APT28 (Fancy Bear):**
  * Attack Scenario:
    * Uses named pipes and sockets to facilitate stealthy command-and-control operations within compromised systems.
  * Tools Used:
    * Custom implants leveraging IPC mechanisms for covert communication.
  * Impacts:
    * Persistent espionage capabilities, lateral movement facilitation, and evasion of traditional detection mechanisms.
