---
description: Supported Platforms & Requirements
icon: hand
---

# Requirements

## <mark style="color:yellow;">Linux Distributions</mark>

<div align="center"><figure><img src="../../.gitbook/assets/Debian.png" alt="" width="64"><figcaption><p>Debian</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Ubuntu.png" alt="" width="64"><figcaption><p>Ubuntu</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Arch-Linux.png" alt="" width="64"><figcaption><p>Arch</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Fedora.png" alt="" width="64"><figcaption><p>Fedora</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Raspberry-Pi.png" alt="" width="64"><figcaption><p>Raspbian</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Red-Hat.png" alt="" width="64"><figcaption><p>RedHat</p></figcaption></figure> <figure><img src="../../.gitbook/assets/openSUSE.png" alt="" width="64"><figcaption><p>SuSe</p></figcaption></figure></div>

## <mark style="color:yellow;">Virtual Environments</mark>

<div><figure><img src="../../.gitbook/assets/OpenStack.png" alt="" width="64"><figcaption><p>OpenStack</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Docker.png" alt="" width="64"><figcaption><p>Docker</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Composer.png" alt="" width="64"><figcaption><p>Composer</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Red-Hat.png" alt="" width="64"><figcaption><p>RedHat<br>Ent Virt</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Incus.png" alt="" width="63"><figcaption><p>Incus<br>or LXD</p></figcaption></figure> <figure><img src="../../.gitbook/assets/KVM.png" alt="" width="63"><figcaption><p>KVM</p></figcaption></figure></div>

## <mark style="color:yellow;">Cloud Providers</mark>

<div><figure><img src="../../.gitbook/assets/Kubernetes (1).png" alt="" width="63"><figcaption><p>Kubernetes</p></figcaption></figure> <figure><img src="../../.gitbook/assets/AWS.png" alt="" width="64"><figcaption><p>AWS</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Digital-Ocean.png" alt="" width="64"><figcaption><p>Digital<br>Ocean</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Google-Cloud.png" alt="" width="64"><figcaption><p>Google<br>Cloud</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Oracle.png" alt="" width="64"><figcaption><p>Oracle<br>Cloud</p></figcaption></figure> <figure><img src="../../.gitbook/assets/IBM.png" alt="" width="64"><figcaption><p>IBM<br>Cloud</p></figcaption></figure></div>

and many others (consult).

## <mark style="color:yellow;">CI/CD plugins</mark>

<div><figure><img src="../../.gitbook/assets/GitHub.png" alt="" width="63"><figcaption><p>GitHub</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Jenkins.png" alt="" width="64"><figcaption><p>Jenkins</p></figcaption></figure></div>

## <mark style="color:yellow;">Linux Requirements</mark>

* Linux Kernel ≥ v6.2 recommended (works with ≥ 5.10)
* x64 Linux OS with eBPF (most current distributions)
* Root privileges with the following capabilities:
  * CAP\_BPF (or CAP\_SYS\_ADMIN if not available)
  * CAP\_PERFMON
  * CAP\_NET\_ADMIN

## <mark style="color:yellow;">Kubernetes Requirements</mark>

* Kubernetes cluster with version 1.16+
* Command `kubectl` configured to communicate with your cluster
