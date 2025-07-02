---
icon: shield
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# New Era

## <mark style="color:yellow;">Why Jibril Stands Out</mark>

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

***

### <mark style="color:yellow;">Core Innovations</mark> <a href="#id-1-core-innovations-in-jibrils-architecture" id="id-1-core-innovations-in-jibrils-architecture"></a>

#### Event-Less, Query-Driven Monitoring <a href="#id-11-event-less-query-driven-monitoring" id="id-11-event-less-query-driven-monitoring"></a>

*   **Jibril's Innovation**

    Jibril stores events in in-kernel eBPF maps and retrieves them on-demand, eliminating ring-buffer overload and data loss while maintaining performance under system stress.
*   **Traditional Tools**

    Traditional solutions depend on event flooding via ring buffers to transfer kernel events to user space, creating bottlenecks under load.

{% tabs %}
{% tab title="Jibril Runtime Security" %}
<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption><p>3rd Generation Agent: Jibril Runtime Security</p></figcaption></figure>
{% endtab %}

{% tab title="Current eBPF Runtime Tools" %}
<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption><p>2nd Generation Agents: Current eBPF Runtime Security Tools</p></figcaption></figure>
{% endtab %}
{% endtabs %}

#### Minimal Overhead, Maximum Visibility <a href="#id-12-minimal-overhead-maximum-visibility" id="id-12-minimal-overhead-maximum-visibility"></a>

* **Ensured Data Integrity**\
  Maps feature cryptographic hashing to prevent unauthorized key generation or modification. Any tampering renders the system "tainted," ensuring detectability and preserving forensic integrity.
* **Kernel-Resident Data Management**\
  Jibril employs interconnected hashed key-value maps with strategic caching to prevent query exhaustion, minimizing context switching and reducing overhead—unlike traditional streaming tools that degrade under load.

#### High-Frequency Event Efficiency <a href="#id-13-high-frequency-event-efficiency" id="id-13-high-frequency-event-efficiency"></a>

* **Resiliency**: Jibril's in-kernel storage delivers reliable monitoring without CPU strain. While standard eBPF tools may drop events at enterprise loads - sometimes exceeding 50,000 events per second - Jibril maintains consistent performance without data loss.

{% tabs %}
{% tab title="Cadence and CPU Consumption" %}
<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption><p>Deterministic CPU Consumption</p></figcaption></figure>
{% endtab %}

{% tab title="Minimal CPU Overhead, No Misses" %}
<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

***

### <mark style="color:yellow;">Jibril Security Model</mark> <a href="#id-2-jibril-security-model-the-technical-deep-dive" id="id-2-jibril-security-model-the-technical-deep-dive"></a>

**Behavioral Data Integrity**

* **Detection Recipe Confidentiality**\
  The logic behind Jibril's monitoring is kept secret, preventing attackers from understanding detection patterns and reducing their chances of evasion.
* **Rate-Limiting**\
  Jibril can impose limits on repetitive events globally, per binary, or per process, ensuring your system isn't overwhelmed.

**Kernel/Userland Separation**

* **Secure Memory Access**\
  All eBPF programs undergo validation by the Linux kernel verifier, preventing unauthorized memory access.
* **Low-Latency Interactions**\
  On-demand queries replace constant event "firehoses" between kernel and user space, minimizing overhead.

**Access Control and Monitoring**

* **Privilege Protection**\
  Only root users with CAP\_BPF or CAP\_SYS\_ADMIN permissions can load or inspect Jibril's kernel programs, with unauthorized attempts automatically flagged as tampering.
* **Userland Privilege Management**\
  Jibril follows least-privilege principles, dropping unnecessary capabilities after eBPF initialization to prevent privilege exploitation.

**System Resilience**

* **Tamper Detection**\
  Any unverified writes to eBPF maps or rogue eBPF loads are caught and flagged.
* **Plugin Isolation**\
  Each detection plugin operates in a dedicated thread, preventing individual failures from compromising the entire monitoring system.

**Compliance Alignment**

* **GDPR-Focused**\
  Jibril tracks only metadata (filenames, PIDs, timestamps)—not content—minimizing personal data processing risks. Future updates will implement anonymization for enhanced compliance requirements.
* **ISO 27001 Ready**\
  Robust logging, granular access controls, and tamper alerting facilitate compliance with ISO 27001 security framework requirements.

***

### <mark style="color:yellow;">From Kernel to Userland</mark> <a href="#id-3-end-to-end-flow-from-kernel-to-userland" id="id-3-end-to-end-flow-from-kernel-to-userland"></a>

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

***

### <mark style="color:yellow;">Extensibility</mark> <a href="#id-5-extensibility-future-ready" id="id-5-extensibility-future-ready"></a>

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

***

## <mark style="color:yellow;">Roadmap</mark>

* **Enhanced Data Protection**\
  Future updates will implement data anonymization for sensitive information and optional encryption for kernel-collected data.
* **Comprehensive Compliance**\
  Planned enhancements include expanded GDPR and ISO 27001 audit support through detailed access logs, improved documentation, and configurable redaction capabilities.

***

## <mark style="color:yellow;">Conclusion</mark> <a href="#conclusion-embrace-the-next-generation" id="conclusion-embrace-the-next-generation"></a>

**Jibril redefines runtime security with its revolutionary approach to kernel event management—collecting, storing, and analyzing system activity with unprecedented efficiency, minimal latency, and tamper-resistant architecture.**

Unlike traditional solutions that falter under high event volumes, Jibril's performance actually scales with demand, ensuring:

* **Unwavering reliability** when you need it most
* **Complete visibility** across your entire system
* **Ironclad security** with tamper-evident design

Purpose-built for modern enterprise environments, Jibril combines kernel-level monitoring depth with negligible performance impact and compliance-ready features—delivering the comprehensive protection today's security-conscious organizations demand.

**Experience the confidence that comes from truly knowing what's happening in your systems, even at the most critical moments.**
