---
icon: road
---

# Security Model

## <mark style="color:yellow;">**Behavioral Data Integrity**</mark>

### **Detection Recipe Confidentiality**

Jibril's monitoring system maintains its core detection logic as a secret, even though it provides public detection guidelines. This secrecy hinders attackers from deciphering its detection patterns, thereby minimizing their evasion opportunities.

### **Rate-Limiting**

Jibril utilizes sophisticated internal mechanisms to limit repetitive events, significantly reducing noise and false positives. Moreover, Jibril integrates with advanced AI models, enabling it to block or accurately classify incorrect detections. This dual approach ensures that false positives are quickly and effectively identified, enhancing the system's accuracy and reliability.

## <mark style="color:yellow;">**Kernel/Userland Separation**</mark>

### **Secure Memory Access**

eBPF (extended Berkeley Packet Filter) programs execute safely in the kernel after passing a stringent validation by the Linux kernel verifier. This verifier checks the programs to ensure compliance with memory usage rules, preventing unauthorized memory access. This process enforces security policies, maintains isolation between kernel and user-space memory, and bolsters system integrity.

### **Userland Optimization**

Userland code ensures isolation by executing each process in a separate, controlled environment. Detection recipes operate independently, utilizing distinct logic pathways to avoid interference with other processes. Reactions are executed within their own JavaScript VM contexts, further safeguarding the system by encapsulating execution environments.

## <mark style="color:yellow;">**Access Control and Monitoring**</mark>

### **Privilege Protection**

To load or inspect Jibril's kernel programs, root user access is essential, accompanied by specific permissions such as CAP\_BPF or CAP\_SYS\_ADMIN. These permissions are strictly required to ensure system integrity and security. Any attempt to bypass or manipulate these restrictions is immediately detected and flagged as potential tampering.

### **Userland Privilege Management**

Jibril follows least-privilege principles, dropping unnecessary capabilities after eBPF initialization to prevent privilege exploitation.

## <mark style="color:yellow;">**System Resilience**</mark>

### **Tamper Detection**

Any writes to eBPF maps that have not been verified are detected as tampering events. Similarly, unauthorized or rogue eBPF loads are identified and marked for further investigation. This ensures that the system maintains its integrity by preventing potential malicious activities from unverified executions.

### **Plugin Isolation**

In Jibril, each extension and plugin operates in its own dedicated set of threads. This strategy ensures enhanced reliability and robustness across the entire monitoring system. By isolating each component in individual threads, the system can protect itself against failures that might arise within any single extension or plugin. As a result, if a particular component encounters issues or fails, it will not compromise or disrupt the overall functioning of the monitoring system.

## <mark style="color:yellow;">**Compliance Alignment**</mark>

### **GDPR-Focused**

Jibril tracks only metadata (filenames, PIDs, timestamps)—not content—minimizing personal data processing risks. Future updates will implement anonymization for enhanced compliance requirements.

### **ISO 27001 Ready**

Robust logging, granular access controls, and tamper alerting facilitate compliance with ISO 27001 security framework requirements.
