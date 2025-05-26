---
icon: reply
---

# Valkyrie Response

## Introduction

Runtime detection systems for cyberattacks, particularly time-progressive attacks such as micro-architectural exploits, rowhammer, ransomware, and cryptominers, face a persistent challenge due to false positives.

These attacks, characterized by their incremental progression over time, leverage system resources to achieve malicious objectives, making them amenable to real-time monitoring. However, false positives in these systems—where benign processes are misclassified as malicious—can disrupt legitimate operations, leading to reduced system productivity.

Traditional countermeasures employ advanced machine learning (ML) and artificial intelligence (AI) techniques, such as deep learning models or multi-level expert systems, to enhance detection accuracy.

Despite these efforts, false positives persist, with reported rates ranging from 3% to 7% in state-of-the-art detectors. The paper "Valkyrie: A Response Framework to Augment Runtime Detection of Time-Progressive Attacks" proposes a novel strategy that shifts focus from eliminating false positives to mitigating their impact.

It introduces Valkyrie, a post-detection response framework designed to augment existing runtime detectors by throttling resource allocation to suspected processes, thereby balancing security and operational continuity.

## Study Summary

Valkyrie operates as an enhancement to any runtime detector, targeting time-progressive attacks by integrating a configurable response mechanism that leverages two key observations: detection efficacy improves with additional runtime measurements, and attack progress is resource-dependent.

The framework allows users to define a desired detection efficacy (e.g., F1-score or false positive rate), which dictates the number of measurement epochs required before decisive action.

During these epochs, Valkyrie computes a _threat index_ for each process, ranging from 0 (benign) to 100 (highly malicious), based on the detector’s periodic inferences. This index is derived from penalty and compensation metrics, adjusted via configurable functions, such as incremental or exponential growth models.

System resources—CPU time, memory, network bandwidth, and filesystem access—are throttled proportionally to the threat index using an actuator function, implemented via Linux kernel features like Cgroups or the Completely Fair Scheduler (CFS).

For instance, CPU time allocation is adjusted by modifying process weights in CFS, reducing time slices for suspected processes. Once\
𝑁∗ is reached, processes are terminated if classified malicious or restored if benign.

{% hint style="info" %}
Case studies on micro-architectural attacks (e.g., Prime+Probe, CJAG), rowhammer, ransomware, and cryptominers demonstrate Valkyrie’s efficacy, achieving significant attack slowdowns (e.g., 79.6% for a sample attack, 100% for rowhammer) while limiting benign process slowdowns to 1% (single-threaded) and 6.7% (multi-threaded).
{% endhint %}

## Conclusions

Valkyrie’s evaluation across diverse platforms (Intel i7-7700, i9-11900, i7-3770) and attack types reveals its robustness in throttling time-progressive attacks while minimizing disruptions from false positives.

Unlike traditional methods that risk premature termination (e.g., a 3% false positive rate implies 3/100 processes halted), Valkyrie’s resource-throttling approach `ensures benign processes recover with minimal overhead`—average slowdowns of less than 1% for single-threaded and 6.7% for multi-threaded SPEC benchmarks, compared to 1.5X–4X overheads from migration-based responses.

Its configurability, allowing trade-offs between security (attack throttling) and performance (slowdown tolerance), enhances applicability across domains, from critical systems needing rapid termination to general-purpose systems prioritizing usability.

By decoupling response from detection accuracy, Valkyrie enables lightweight detectors, suitable for resource-constrained environments, and outperforms conventional strategies that rely solely on complex ML models.

This paradigm shift toward post-detection response mechanisms opens new research avenues for practical cybersecurity, addressing the inherent limitations of detection efficacy and offering a scalable, generalizable solution to the false positive dilemma in runtime attack mitigation.

{% file src="../../.gitbook/assets/valkyrie-a-response-framework-to-augment-runtime-detection.pdf" %}
