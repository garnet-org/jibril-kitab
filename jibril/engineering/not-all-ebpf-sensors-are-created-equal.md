# Not All eBPF Sensors Are Created Equal

## Not All eBPF Sensors Are Created Equal: Why Jibril’s Query‑Driven Depth Matters Even More

Runtime security has traditionally meant one of two things: superficial event collection leading to excessive noise or cumbersome, fragile application-level tracing that requires extensive setup and maintenance.&#x20;

While some vendors promote "deep" application tracing—leveraging debug symbols and function-level instrumentation—they introduce complexity, brittleness, and operational overhead.

Jibril bypasses these limitations with its query-based kernel‑state architecture. Now, with the richest free set of detection recipes, dynamic Alchemies, and AI-powered noise suppression, it’s not just different—it’s better.

***

### <mark style="color:red;">The Pitfalls of Traditional eBPF Monitoring</mark>

Traditional kernel-level eBPF monitoring often relies on capturing every syscall event, resulting in significant issues:

* **Massive Noise and Alert Fatigue**: Millions of unfiltered events overwhelm analysts.
* **High Performance Overhead**: Excessive syscall event streaming can severely degrade system performance.
* **Risk of Data Loss**: Under heavy loads, crucial events may be dropped due to buffer overflows and resource constraints.

In contrast, Jibril rejects this inefficient model, instead providing focused, context-rich, and actionable insights.

***

### <mark style="color:red;">The False Promise of Application-Level Debug Tracing</mark>

Competitors advocating for deep application context often gloss over substantial drawbacks:

* **Dependency Hell**: Application-level tracing depends heavily on debug symbols, frame pointer availability, non-stripped binaries, and external symbol sources—requirements often impossible or impractical in production environments.
* **Fragility and Complexity**: Even minor application updates or changes can break instrumentation, causing gaps or downtime in security visibility.
* **Incompatibility with Static Binaries**: Modern static binaries, containerized applications, and production-grade deployments rarely have the necessary instrumentation points, making such tracing impractical.

Jibril sidesteps these challenges entirely, delivering reliable, deep visibility through rich syscall metadata and intelligent kernel-state monitoring without fragile dependencies.

***

### <mark style="color:green;">Efficiency, Scalability, and Reliability by Design</mark>

Jibril’s design emphasizes robustness, scalability, and operational simplicity:

* **Ultra-Lightweight Footprint**: Consuming less than 5% CPU, Jibril is ideal for production environments and resource-constrained containers.
* **Flexible Deployment**: Easily deployable as a user-space binary, Docker container, systemd service, or Kubernetes DaemonSet—without kernel modules or complex infrastructure.
* **Safety Guaranteed by Kernel Verifier**: Jibril’s kernel-side logic is fully verified by the Linux kernel, ensuring system stability and resilience against crashes.

***

### <mark style="color:green;">Deep Visibility Without Compromise</mark>

Jibril delivers rich, meaningful insights:

* Full process ancestry, detailed file system interactions, and comprehensive network visibility, including DNS context.
* Integration with vulnerability management databases (CVEs) and software package metadata provides critical context directly within detections.

This powerful visibility is achieved without the fragile complexity inherent in application-level instrumentation.

***

### <mark style="color:green;">The Largest Free Library of Detection Recipes</mark>

Jibril ships with over 80 built-in detection recipes across three major categories:

1. File Access — from auth-log tampering to SSL cert reads, credential file access, crypto-miner artifacts, environment leaks, shell config modifications, sudoers changes, and more.
2. Execution — including hidden ELF execution, code hot patching (“Code On the Fly”), suspicious exec paths, network tool invocations, crypto-miner execution, shell spawns, runc anomalies, and webserver abuses  .
3. Network Peers — covering access to malicious/adult/fake/gambling/domains, dynamic DNS, VPNs, plaintext communications—fully context-aware with domain-level policy.&#x20;

That’s the most comprehensive set of free detection recipes in any open runtime EDR, covering a wide swath of MITRE TTPs out of the box. Great depth, zero cost.

***

### <mark style="color:green;">Alchemies: DIY Detection Recipes with YAML Simplicity</mark>

Jibril goes even further with Alchemies, a powerful feature that lets users author detection logic in intuitive, human-readable YAML, dynamically loaded and validated at runtime  . Highlights include:

* Simple YAML syntax — define patterns for file, execution, and network anomalies.
* Hot-reloading — update your detection logic on the fly; Jibril auto-refreshes recipes.
* Recipe validation — your Alchemies are validated before activation, avoiding typos or config drift.
* Multiple types supported — whether you’re watching for file access, exec anomalies, or network patterns, Alchemies covers it.

This means you’re not limited to built-in recipes; your team can create unlimited custom detections—faster and safer than app-level instrumentation.

***

### <mark style="color:green;">Attenuator: Smooth and Focused Alerts with AI</mark>

Developers can quickly overwhelm detection systems with false positives. Jibril tackles alert fatigue head-on with Attenuator, leveraging heuristics and lightweight AI to reduce noise  . Features include:

* Suppression of repeated patterns — e.g., constant cron job noise suppressed after a “learned” count.
* Context-aware filtering — recognize benign behavior vs. genuine threats.
* Customization via Alchemies — combine with recipe thresholds (times, limits) to finely tune detection sensitivity.

Attenuator ensures you get meaningful alerts—without being buried.

***

## How It All Works at the Kernel Level

1.  Stateful, Query-Driven Engine

    Jibril continuously maintains key system state—process trees, open files, network peers, privilege levels. Unlike stream-heavy designs, it evaluates queries on state—not every syscall .
2.  Embedded Query Language

    Detection logic (built-in or via Alchemies) runs as kernel-verified eBPF filters at syscall entry/exit—the source of truth and policy enforcement  .
3.  Real-Time Enforcement

    When policy is triggered, Jibril can block suspicious activity at the syscall boundary—stopping malicious behavior before it executes  .
4.  Alert Generation + Attenuation

    Alerts go through Attenuator logic before reaching your logs or integrations—ensuring only actionable detections appear.
5.  Yaml-Based Extensions + Hot-Reload

    At any time, you can drop in a new Alchemy recipe, Jibril will validate, compile, load it—and start enforcing rules without restart dead-time  .

***

## Why Jibril’s Model Triumphs

* Most free detection recipes across file, exec, and network TTPs.
* Customizable detection at no extra cost—via Alchemies.
* Alert quality through AI with Attenuator; fewer false positives means faster response.
* Robust kernel-level enforcement—no sidecar, no kernel module, no fragile instrumentation.
* Designer simplicity meets production rigor—lightweight, eBPF-safe, container and CI/CD ready.

***

## TL;DR

Jibril isn’t just another eBPF monitor—it’s a complete, production-grade runtime security platform. With the largest free recipe library, dynamic YAML-based detection, and AI-powered noise suppression, it delivers depth, flexibility, and clarity—all at the kernel level, with real-time blocking and minimal overhead.

Let me know if you’d like to preview code examples for Alchemies, see attenuation in action, or walk through deploying these detectors in Kubernetes or CI.
