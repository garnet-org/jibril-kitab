# We are not the same

<figure><img src="../../.gitbook/assets/image.png" alt="" width="250"><figcaption></figcaption></figure>

## Not All eBPF Sensors are Created Equal

{% hint style="info" %}
### Why neglect-able performance impact, low false positives, being production ready, having the biggest amount of detection recipes available matters.&#x20;
{% endhint %}

## Why Jibril’s Query‑Driven Depth Matters Even More

Runtime security solutions have traditionally fallen into two problematic categories: superficial event collection leading to excessive noise, or cumbersome, fragile application-level tracing requiring extensive setup and maintenance.

> Some vendors claim deep application visibility using debug symbols and function-level instrumentation, but these approaches bring complexity, fragility, and operational overhead.

Jibril bypasses these limitations entirely with its innovative query-driven, kernel-state architecture, complemented by a rich set of detection recipes, dynamic Alchemies, and AI-driven noise reduction. It's not just different—it's fundamentally better.

***

## Understanding the Limitations of Current eBPF Tools

### Pitfalls of Traditional eBPF Monitoring

Traditional kernel-level eBPF monitoring often relies on capturing every syscall event, leading to critical problems:

* **Massive Noise and Alert Fatigue**: Millions of unfiltered events overwhelm analysts.
* **High Performance Overhead**: Continuous syscall streaming severely degrades system performance.
* **Risk of Data Loss**: Heavy loads can cause crucial events to drop due to buffer overflows and resource constraints.

Jibril rejects this inefficient model, providing instead focused, context-rich, and actionable insights.

### The False Promise of Application-Level Debug Tracing

Vendors promoting deep application tracing often overlook substantial issues:

* **Dependency Hell**: Debug symbols, frame pointer availability, non-stripped binaries, and external symbol sources create impossible or impractical deployment conditions.
* **Fragility and Complexity**: Minor application updates can break instrumentation, creating gaps or downtime in visibility.
* **Incompatibility with Static Binaries**: Static binaries, containerized applications, and modern deployments frequently lack necessary instrumentation points.

Jibril sidesteps these challenges, offering deep, reliable visibility through intelligent syscall metadata and robust kernel-state monitoring without fragile dependencies.

***

## Introducing Jibril’s Advanced Security

### Efficiency, Scalability, and Reliability by Design

Jibril emphasizes robustness, scalability, and simplicity:

* **Ultra-Lightweight Footprint**: Consumes less than 10% CPU, ideal for resource-constrained production environments and containers.
* **Flexible Deployment**: Deploys as user-space binary, Docker container, systemd service, or Kubernetes DaemonSet—no kernel modules or complex infrastructure required.
* **Kernel Safety Guaranteed**: Fully verified by Linux kernel, ensuring system stability and resilience.

### Deep Visibility Without Compromise

Jibril provides comprehensive insights without fragile complexity:

* Complete process ancestry, file interactions, and network visibility (including DNS context).
* Integrated CVE data and software package metadata for enriched detection context.

***

## Unmatched Detection Capabilities

### The Largest Free Library of Detection Recipes

Jibril ships with over **80 built-in detection recipes** across key threat categories:

* **File Access**: Detects auth-log tampering, SSL cert reads, credential file access, crypto-miner artifacts, environment leaks, shell config modifications, sudoers changes, and more.
* **Execution**: Covers hidden ELF execution, code hot patching, suspicious exec paths, network tool invocations, crypto-miner executions, shell spawns, runc anomalies, and webserver abuses.
* **Network Peers**: Monitors malicious domains, dynamic DNS usage, VPN connections, plaintext communications—fully context-aware.

This library represents the most comprehensive free set of detections available in runtime EDR solutions, covering numerous MITRE ATT\&CK TTPs at no cost.

### Alchemies: DIY Detection Recipes with YAML Simplicity

Jibril further empowers users with **Alchemies**, allowing easy creation of detection logic using simple, human-readable YAML:

* **Simple YAML syntax** for defining detection patterns.
* **Hot-reloading**: Update detection logic dynamically.
* **Built-in Validation**: Ensures your Alchemies are error-free and effective.
* **Versatile Coverage**: Applicable across file, execution, and network detection scenarios.

Your team can rapidly craft unlimited custom detections, greatly outperforming traditional instrumentation methods.

***

## AI-Powered Noise Reduction with Attenuator

Jibril addresses alert fatigue with **Attenuator**, an intelligent system leveraging heuristics and AI:

* **Suppression of repetitive patterns** (e.g., routine cron job activity).
* **Context-aware filtering**: Distinguishes benign from malicious behaviors.
* **Customizable thresholds**: Combine with Alchemies to fine-tune sensitivity.

Attenuator ensures meaningful alerts without overwhelming analysts, significantly improving operational efficiency.

***

## How Jibril Works at the Kernel Level

Jibril leverages a powerful, stateful, and query-driven approach:

* **Stateful, Query-Driven Engine**: Continuously maintains system state—processes, files, networks, privileges—evaluating queries rather than streaming every syscall.
* **Embedded Query Language**: Detection logic runs securely at syscall entry/exit points, serving as the primary policy enforcement mechanism.
* **Real-Time Enforcement**: Blocks malicious activities directly at syscall boundaries before execution.
* **Alert Generation and Attenuation**: Filters alerts through Attenuator to provide actionable intelligence only.
* **YAML-Based Extensions with Hot-Reload**: Dynamically loads, validates, and applies detection recipes without downtime.

***

## Why Jibril’s Model Triumphs

Jibril uniquely combines deep visibility, efficiency, and ease of use:

* **Largest library of free detection recipes**.
* **Unlimited customizable detection** through YAML Alchemies.
* **AI-driven alert quality improvement** via Attenuator.
* **Robust kernel-level enforcement** without fragile instrumentation.
* **Simplicity and production readiness**: lightweight, eBPF-safe, container-ready, and CI/CD-friendly.

***

## TL;DR

Jibril transcends traditional eBPF-based monitoring. It’s a comprehensive, production-grade runtime security platform that uniquely combines extensive detection capabilities, dynamic YAML-based customizations, and AI-driven noise reduction, ensuring maximum protection, minimal overhead, and effortless operational management.

{% hint style="info" %}
Explore Jibril today—see Alchemies and Attenuator in action, or learn how easily you can integrate advanced runtime security into your Kubernetes or CI workflows.
{% endhint %}
