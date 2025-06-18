---
icon: shield
layout:
  title:
    visible: false
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Jibril

<figure><img src=".gitbook/assets/jibril-logo-batuta-trans.png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">**Use Cases**</mark>

<figure><img src=".gitbook/assets/quadrandt.png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">What is it ?</mark>

Jibril is a cutting-edge runtime monitoring and threat detection engine, designed to deliver real-time insights with minimal impact on system performance. Powered by eBPF, it remains efficient even under heavy event loads exceeding hundreds of thousands of events per second–delivering real-time protection for modern environments from dev to prod.

### <mark style="color:yellow;">Mission</mark>

* Ensure the security and integrity of your systems at **runtime.**
* Deliver clear and actionable insights

### <mark style="color:yellow;">Insights</mark>

<figure><img src=".gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption><p>Deep Visibility on Root Causes</p></figcaption></figure>

{% hint style="info" %}
<mark style="color:yellow;">**Key Benefits**</mark>

* **High Performance**: Maintains efficiency with extensive event loads.
* **Full Visibility**: Tracks all system resources comprehensively.
* **Security**: Ensures robust security and tamper-evident data integrity.
* **Seamless Integration**: Easily integrates with existing infrastructure.
{% endhint %}

***

### <mark style="color:yellow;">Jibril in less than 5 Minutes</mark>

{% embed url="https://www.youtube.com/watch?v=xGT3yiXBC3E" %}
Install and Configure Jibril in Less than 5 Minutes
{% endembed %}

***

### <mark style="color:yellow;">Main Features</mark>

Navigate the tabs for the main features.

{% tabs %}
{% tab title="Detailed Info" %}
<mark style="color:yellow;">**Detailed Security Event Information**</mark>

Jibril provides comprehensive tracking across all system resources, including users, processes, files, and network connections. Its query-driven architecture ensures complete visibility and actionable intelligence into system behavior.

<div><figure><img src=".gitbook/assets/image (2) (1) (1).png" alt=""><figcaption><p>Context Information<br>(OS Package Versions)</p></figcaption></figure> <figure><img src=".gitbook/assets/image (3) (1) (1).png" alt=""><figcaption><p>Triggerer Ancestry Visibility<br>FULL File Access History</p></figcaption></figure> <figure><img src=".gitbook/assets/image (4) (1) (1).png" alt=""><figcaption><p>Track OS Package Dependencies Versions<br>Detection FULL Context<br>On Demand CVE Warnings</p></figcaption></figure></div>
{% endtab %}

{% tab title="Noise Filtering" %}
<mark style="color:yellow;">**Prioritized Detections with Noise Filtering**</mark>

Jibril has an automatic mechanism to reduce noise. Repetitive alerts are filtered by its nature. Some detections are limited by amount of times they happened on the same parent process, some others are limited by amount of times they happened by the same executable path, and so on.

{% include ".gitbook/includes/untitled.md" %}
{% endtab %}

{% tab title="Network Visibility" %}
<mark style="color:yellow;">**Inbound and Outbound connections tied to Security Events**</mark>

<figure><img src=".gitbook/assets/image (6) (1) (1).png" alt=""><figcaption><p>Complete View of Remote Peers Per Process<br>Detections are Linked With Corresponding Remote Peer<br>Full DNS Resolution Path per Peer and Flow</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (10).png" alt=""><figcaption><p>All Processes Communicating with the same Remote Node Are Grouped<br>All Detections are Flagged on Each Entry (linked with Detections Feature)</p></figcaption></figure>
{% endtab %}

{% tab title="Block Traffic" %}
<mark style="color:yellow;">**Network Policy Enforcement**</mark>

<figure><img src=".gitbook/assets/image (11).png" alt=""><figcaption><p>Block Network Connections Using Domains or IP CIDRs.<br>Get Bad Reputation Domains Alerts Realtime.</p></figcaption></figure>
{% endtab %}
{% endtabs %}
