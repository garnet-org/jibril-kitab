---
icon: globe
---

# Network Peers

## What is Network Peer Monitoring?

Network Peer Monitoring is a specialized extension of Jibril's [Network eBPF Logic](network_ebpf_logic.md) that focuses on comprehensive tracking and analysis of all network connections and their associated endpoints. By maintaining a complete graph of network relationships, Jibril creates a detailed map of which processes communicate with which remote peers, how these communications occur, and the complete context surrounding each connection. This capability enables sophisticated detection of anomalous or malicious network behavior by analyzing the relationships between network peers and correlating them with process behavior, DNS resolution paths, and system activities.

## How Does Network Peer Monitoring Work?

1. **Comprehensive Flow Tracking**: Jibril leverages its cgroup/skb eBPF programs to maintain a complete record of all network flows in the system:
   * Every socket operation (connect, accept, bind) is captured and logged
   * Both ingress (incoming) and egress (outgoing) traffic is monitored
   * Local peer-to-peer communications are tracked alongside external connections
   * Complete socket lifecycle monitoring from creation to closure
2. **DNS Resolution Chain Mapping**: Jibril's in-kernel DNS processing capabilities are extended to maintain the complete resolution path for each connection:
   * All DNS queries associated with a particular flow are recorded
   * CNAME chains are preserved, showing the complete resolution path
   * Each A/AAAA record is linked to the flows that resulted from its resolution
   * Historical resolution data is maintained for correlation and analysis
3. **Relationship Graph Construction**: Using eBPF maps, Jibril builds and maintains a sophisticated relationship graph that connects:
   * Processes to their network connections
   * Connections to their remote endpoints
   * DNS resolutions to the resulting connections
   * Parent-child process relationships that initiated connections
   * Temporal sequences of connection establishment
4. **Contextual Correlation Engine**: Network peer data is enriched with additional system context:
   * Binary execution information for processes establishing connections
   * File access patterns associated with networked processes
   * User context and permission levels for connection operations
   * Container and namespace boundaries for precise isolation mapping
5. **Pattern Analysis and Anomaly Detection**: Jibril analyzes the network peer relationship graph to identify:
   * Unusual connection patterns between peers
   * Unexpected communication channels
   * Anomalous data transfer volumes or frequencies
   * Suspicious DNS resolution chains that may indicate domain generation algorithms

## Where Does Network Peer Monitoring Operate?

Jibril's Network Peer Monitoring capabilities operate as an extension of its core Network eBPF Logic:

* **Kernel-level Socket Operations**: Monitoring occurs directly at the socket interface level
* **Protocol Stack Integration**: Visibility across all network protocols (TCP, UDP, ICMP, etc.)
* **Cross-namespace Awareness**: Connections are tracked across container and namespace boundaries
* **System-wide Coverage**: All network peer relationships throughout the system are captured and analyzed

## Why is Network Peer Monitoring Important?

1. **Advanced Threat Detection**: By understanding the complete network relationship graph, Jibril can identify sophisticated attack patterns that might be missed when examining individual connections in isolation.
2. **Lateral Movement Detection**: The comprehensive peer relationship tracking enables detection of lateral movement attempts where compromised systems attempt to connect to other internal resources.
3. **Data Exfiltration Prevention**: By correlating file access with network peer connections, Jibril can identify potential data exfiltration attempts where sensitive files are accessed before unusual external connections.
4. **Command and Control Identification**: The DNS resolution chain mapping helps identify evasive command and control techniques that leverage multiple redirections or domain generation algorithms.
5. **Forensic Investigation Support**: The detailed historical record of all network peer relationships provides invaluable context for security investigations, allowing analysts to trace the complete path of an attack through the network.

## Conclusion

Network Peer Monitoring represents a powerful extension of Jibril's core Network eBPF Logic capabilities. By maintaining a comprehensive graph of all network relationships—including processes, connections, DNS resolutions, and system context—Jibril enables sophisticated detection of network-based threats. This approach provides security teams with unprecedented visibility into how applications communicate, with whom they communicate, and under what circumstances these communications occur. The result is a detection system capable of identifying complex attack patterns by analyzing the relationships between network peers and correlating them with the broader system context.
