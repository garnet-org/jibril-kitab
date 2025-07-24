---
icon: bee
---

# Bigger eBPF Logic

## What is eBPF in Jibril?

eBPF (extended Berkeley Packet Filter) serves as the foundation for Jibril's runtime detection capabilities. This powerful technology allows Jibril to run sandboxed bytecode directly in the Linux kernel without modifying kernel source code or loading kernel modules. By leveraging eBPF, Jibril can observe and analyze system behavior in real-time, detecting security vulnerabilities as they're being exploited.

## How does Jibril use eBPF for pattern detection?

Jibril implements sophisticated detection logic through eBPF programs written in a restricted C-like language and compiled into eBPF bytecode. After verification by the eBPF verifier (ensuring kernel safety), these programs are strategically attached to various kernel hooks to monitor system activities:

1. **Multi-point Event Collection:** Jibril attaches eBPF programs to diverse kernel hooks including syscall entry points, network interfaces, file operations, and process creation events.
2. **In-kernel Data Storage:** Collected events and their metadata are efficiently stored within kernel space using eBPF maps, creating a rich repository of behavioral data that persists without continuous userland communication.
3. **Intelligent Data Retrieval:** Jibril's Golang-based analysis engine queries these kernel-side data structures at strategic intervals, pulling only the necessary information for analysis while minimizing system overhead.
4. **Pattern Matching:** Using the retrieved data, Jibril correlates events across time and system components to identify complex attack patterns from its database of known attack signatures and suspicious behavior patterns.
5. **Anomaly Detection:** Beyond known patterns, Jibril can identify deviations from normal system behavior that might indicate novel exploitation techniques.

For example, when detecting a privilege escalation attempt, Jibril might analyze a sequence of file access operations, unusual syscalls, and process spawning events that individually seem benign but together match the pattern of a known exploit—all while maintaining the data within kernel space until analysis is required.

## Where does Jibril's eBPF detection operate?

Jibril's eBPF programs operate within the Linux kernel while being managed by its Golang components in user space. The detection hooks are strategically placed at:

* System call interfaces (capturing process creation, file operations, network activity)
* Network stack entry and exit points (for detecting network-based attacks)
* Security-related kernel functions (for monitoring permission changes)
* Memory management operations (to detect memory corruption exploits)
* Container boundaries (for monitoring container escapes)

This comprehensive coverage ensures that Jibril can observe the full attack surface of a Linux system, leaving minimal blind spots for attackers.

## Why is eBPF-based pattern detection effective?

Jibril's approach to security monitoring through eBPF offers several advantages:

1. **Comprehensive Visibility:** By monitoring multiple system components simultaneously, Jibril can detect sophisticated attacks that operate across different system layers.
2. **Real-time Detection:** The kernel-side data collection and storage model allows for immediate event capture, while the strategic retrieval approach enables timely threat analysis without constant kernel-userspace communication overhead.
3. **Low False Positives:** The ability to correlate multiple events reduces false positives compared to single-point detection systems, as malicious activities often require multiple suspicious actions in sequence.
4. **Performance Efficiency:** By keeping data within kernel space until needed and minimizing context switches, Jibril achieves exceptional monitoring performance with minimal impact on system resources.
5. **Evasion Resistance:** Since Jibril monitors at the kernel level and stores detection data within the kernel itself, it's significantly more difficult for attackers to evade detection or tamper with security telemetry.

## Conclusion

Jibril leverages eBPF's powerful capabilities to implement sophisticated pattern detection logic that can identify security vulnerabilities being exploited at runtime. By maintaining critical security data within kernel space and retrieving it strategically for analysis, Jibril provides comprehensive protection against both known and novel threats while maximizing system performance. This approach represents a significant advancement in Linux runtime security monitoring, offering deeper visibility and more effective threat detection than traditional security tools.
