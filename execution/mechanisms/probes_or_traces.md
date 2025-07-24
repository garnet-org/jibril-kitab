---
icon: play-pause
---

# Probes and Traces

## What is Probes or Traces Monitoring?

**Jibril** is a runtime detection tool designed to monitor and analyze advanced system manipulation techniques that might evade other detection mechanisms. Building upon the [Bigger eBPF Logic](bigger_ebpf_logic.md) foundation, Jibril specifically tracks the usage of kernel introspection and modification tools including eBPF (extended Berkeley Packet Filter), perf (performance counters), ftrace (function tracer), and other related hooking mechanisms. While these technologies serve legitimate purposes for performance monitoring and debugging, they can also be weaponized by sophisticated attackers to implement rootkits, hide malicious activities, and tamper with kernel structures.

## How Does Probes or Traces Monitoring Work?

1. **Kernel Structure Integrity Verification**:
   * **Syscall Table Monitoring**: Jibril continuously verifies the integrity of system call tables to detect unauthorized modifications that could redirect legitimate system calls to malicious handlers.
   * **Kernel Function Hooking Detection**: Identifies attempts to patch or redirect core kernel functions through techniques like function pointer manipulation or code patching.
   * **VFS Layer Tampering**: Monitors for modifications to Virtual File System structures that might be used to hide files or directories from standard system utilities.
2. **Introspection Tool Surveillance**:
   * **eBPF Program Validation**: Tracks all eBPF programs loaded into the kernel, analyzing their purpose, permissions, and behavior patterns to identify potentially malicious usage.
   * **Perf Subsystem Monitoring**: Observes access to performance monitoring interfaces that could be exploited for side-channel attacks or information gathering.
   * **Ftrace/Kprobe Auditing**: Maintains a comprehensive inventory of all active kernel tracing mechanisms to detect unauthorized debugging or information collection.
3. **Advanced Rootkit Detection**:
   * **Hidden Process Identification**: Uses kernel-level visibility to identify processes that have been unlinked from standard process lists but remain active in the system.
   * **Memory-resident Malware Detection**: Scans for code execution from unusual memory regions that might indicate fileless malware or advanced persistent threats.
   * **Kernel Module Verification**: Validates the authenticity and integrity of loaded kernel modules against known-good signatures and behaviors.
4. **Correlation Engine**:
   * Leverages Jibril's eBPF-based data collection to correlate suspicious kernel modifications with other system activities, establishing a complete picture of potential attacks.
   * Maintains historical records of kernel structure states to identify subtle, incremental changes that might indicate a sophisticated attack.

## Where Does Probes or Traces Monitoring Operate?

Jibril's Probes or Traces monitoring operates at the deepest levels of the Linux system:

* **Kernel Memory Space**: Directly monitors critical kernel structures and memory regions
* **System Call Interface**: Verifies the integrity of the boundary between user and kernel space
* **Kernel Module Loading Paths**: Observes the introduction of new code into the kernel
* **Debug and Tracing Subsystems**: Monitors legitimate kernel introspection mechanisms for abuse
* **Memory Management Structures**: Identifies unauthorized modifications to memory mappings and permissions

## Why is Probes or Traces Monitoring Important?

1. **Advanced Threat Detection**: By focusing on kernel-level manipulation techniques, Jibril can detect sophisticated attacks that specifically attempt to evade traditional security monitoring.
2. **Rootkit Identification**: The comprehensive monitoring of kernel structures enables detection of modern rootkits designed to maintain persistence while hiding their presence from the operating system.
3. **Zero-Day Exploitation Detection**: Even when attackers use previously unknown techniques, the monitoring of fundamental kernel structures can reveal unauthorized modifications indicative of exploitation.
4. **Complete Attack Surface Coverage**: This monitoring approach addresses a critical blind spot in many security solutions that focus primarily on user-space activities while neglecting kernel-level manipulations.
5. **Forensic Value**: The detailed records of kernel structure modifications provide invaluable evidence for incident response teams investigating sophisticated breaches.

## Conclusion

Probes or Traces monitoring represents Jibril's capability to detect the most sophisticated kernel tampering techniques used by advanced attackers. By leveraging its eBPF foundation to monitor critical kernel structures and introspection mechanisms, Jibril can identify malicious activities that specifically attempt to evade detection by modifying the kernel itself. This capability is essential for detecting modern rootkits, advanced persistent threats, and sophisticated malware that operates at the kernel level to hide its presence and maintain persistence on compromised systems.
