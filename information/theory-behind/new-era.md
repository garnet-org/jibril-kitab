---
description: Understand will Jibril is not just another runtime security system.
icon: wreath-laurel
---

# New Paradigm

## <mark style="color:yellow;">Why Jibril Stands Out</mark>

***

IT environments generate vast amounts of logs, with security teams relying on real-time kernel event streaming tools that often falter during high traffic, causing system slowdowns and data loss.

Jibril's query-driven eBPF approach, unlike traditional event-streaming models, collects kernel behavioral data with minimal overhead, eliminating performance bottlenecks while maintaining monitoring integrity.

{% hint style="success" %}
**The result ?**

Experience comprehensive monitoring without ring-buffer overruns, missed events, or CPU bottlenecks. Jibril's low-latency architecture ensures data integrity in high-throughput, security-critical environments.

* **Minimal Overhead, Maximum Insights**
* **Robust Security Model**
* **Uncompromised Data Fidelity**
* **Scalable & Compliant**
{% endhint %}

## <mark style="color:yellow;">Core Innovations</mark> <a href="#id-1-core-innovations-in-jibrils-architecture" id="id-1-core-innovations-in-jibrils-architecture"></a>

***

### **Recent Security Solutions**

Most recent security solutions often rely on event flooding through ring buffers as a means to transfer kernel events to user space efficiently. This mechanism is designed with the intention of providing a seamless flow of event data across the boundary between kernel and user space, which is crucial for maintaining system security. However, this approach can inadvertently lead to significant challenges, especially under heavy loads.

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption><p>2nd Generation Agents: Current eBPF Runtime Security Tools</p></figcaption></figure>

> As the system encounters an increased number of events, ring buffers may struggle to manage the volume effectively, leading to potential data loss or delays. This bottleneck not only hampers performance but can also diminish the responsiveness and reliability of security monitoring systems. Consequently, while event flooding through ring buffers serves its purpose in many scenarios, it necessitates careful consideration and optimization to prevent these performance bottlenecks and ensure robust security monitoring in high-demand environments.

### **Jibril's Innovations**

Jibril utilizes in-kernel maps for efficiently storing events, allowing for on-demand cached data retrieval. This innovative approach addresses common issues associated with ring-buffer overload and potential data loss. By focusing on high performance, even under significant system stress, Jibril's mechanism ensures that critical event data remains both accessible and reliable.&#x20;

<figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption><p>3rd Generation Agent: Jibril Runtime Security</p></figcaption></figure>

#### Minimal Overhead, Maximum Visibility <a href="#id-12-minimal-overhead-maximum-visibility" id="id-12-minimal-overhead-maximum-visibility"></a>

* **Ensured Data Integrity**\
  Maps feature cryptographic hashing to prevent unauthorized key generation or modification. Any tampering renders the system "tainted," ensuring detectability and preserving forensic integrity.\
  (<sup><sub>This feature isn't available in the free version. Contact us for more information).<sub></sup>
* **Kernel-Resident Data Management**\
  Jibril employs interconnected hashed key-value maps with strategic caching to prevent query exhaustion, minimizing context switching and reducing overhead - unlike traditional streaming tools that degrade under load.

#### High-Frequency Event Efficiency <a href="#id-13-high-frequency-event-efficiency" id="id-13-high-frequency-event-efficiency"></a>

* **Resiliency**: Jibril's in-kernel storage delivers reliable monitoring without CPU strain. While standard eBPF tools may drop events at enterprise loads - sometimes exceeding 50,000 events per second - Jibril maintains consistent performance without data loss.
* Cadence and CPU consumption

<figure><img src="../../.gitbook/assets/image (35).png" alt=""><figcaption><p>Deterministic CPU Consumption</p></figcaption></figure>

* Minimal CPU overhead: No Misses

<figure><img src="../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

## <mark style="color:yellow;">From Kernel to Userland</mark> <a href="#id-3-end-to-end-flow-from-kernel-to-userland" id="id-3-end-to-end-flow-from-kernel-to-userland"></a>

***

**Data Collection (Kernel Space)**

* **Uniform Binary Object**\
  Jibril's eBPF code executes consistently across diverse kernel versions without requiring custom modules.
* **Key-Value Map Storage**\
  Process behaviors and events are hashed into eBPF maps, enabling minimal CPU consumption and rapid lookups.

**Userland Daemon**

* **Detection & Pattern Matching**\
  The daemon selectively retrieves kernel data and analyzes it against detection recipes to identify anomalies and suspicious activities.
* **Modular Detection**\
  Jibril's detection logic comes in built-in plugins organized by type (file, network, etc.), each running in an isolated thread to prevent system-wide failures from individual plugin issues.

**Printers & Dashboards**

* **Flexible Output**: Detection events can be routed to multiple destinations including stdout, logs, external dashboards.
* **Secure Submissions**: All data transmission occurs over authenticated channels (HTTPS with API tokens) to maintain confidentiality and integrity.

## <mark style="color:yellow;">Extensibility</mark> <a href="#id-5-extensibility-future-ready" id="id-5-extensibility-future-ready"></a>

***

**Plugins & Extensions**

* **Security-by-Design**\
  Plugins are pre-compiled with well-defined detection recipes, with future versions planned to support runtime extensions via a descriptive language without compromising system stability.
* **Thread-Based Isolation**\
  Self-contained plugins operate independently, ensuring that issues in one monitoring area (like network detection) cannot impact others (such as file monitoring).

**Printers**

* **Built-In Dispatch**\
  Jibril includes various "printers" that forward detection events to logs, dashboards, or external APIs, all easily configured through simple toggles.
* **Optional AI Integrations**\
  For advanced threat analytics, Jibril can transmit summarized data to OpenAI services, leveraging machine learning for intuitive pattern interpretation while protecting raw data.

## <mark style="color:yellow;">Roadmap</mark>

***

* **Enhanced Data Protection**\
  Future updates will implement data anonymization for sensitive information and optional encryption for kernel-collected data.
* **Comprehensive Compliance**\
  Planned enhancements include expanded GDPR and ISO 27001 audit support through detailed access logs, improved documentation, and configurable redaction capabilities.

## <mark style="color:yellow;">Conclusion</mark> <a href="#conclusion-embrace-the-next-generation" id="conclusion-embrace-the-next-generation"></a>

***

Jibril redefines runtime security with its revolutionary approach to kernel event management - collecting, storing, and analyzing system activity with unprecedented efficiency, minimal latency, and tamper-resistant architecture.

Unlike traditional solutions that falter under high event volumes, Jibril's performance actually scales with demand, ensuring:

* Unwavering reliability when you need it most
* Complete visibility across your entire system
* Ironclad security with tamper-evident design

Purpose-built for modern enterprise environments, Jibril combines kernel-level monitoring depth with negligible performance impact and compliance-ready features—delivering the comprehensive protection today's security-conscious organizations demand.

Experience the confidence that comes from truly knowing what's happening in your systems, even at the most critical moments.
