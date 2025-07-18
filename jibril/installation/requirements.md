---
description: Supported Platforms & Requirements
icon: hand
---

# Requirements

## Linux

### 1. Kernel Version

- **Minimum:** Linux kernel v5.2  
- **Recommended:** v6.2 or higher (only v6.2+ is officially tested and supported)
- **Check your kernel:**

  ```sh
  uname -r
  ```

### 2. Architecture and eBPF Support

- **Required:** x86_64 architecture
- **eBPF support:**
  - Modern distributions (Ubuntu 22.04+, RHEL 9+, etc.) usually provide full eBPF support out of the box.
  - To verify, check if the following kernel configs are enabled:  
    `CONFIG_BPF=y`, `CONFIG_BPF_SYSCALL=y`, `CONFIG_HAVE_EBPF_JIT=y`

    ```sh
    zcat /proc/config.gz | grep BPF
    ```

  - Alternatively, run:

    ```sh
    bpftool feature probe
    ```

  - Look for BPF and JIT features marked as “available”.

### 3. Privileges & Capabilities

- **Root access required.**
- **Capabilities:**
  - `CAP_BPF` (primary, present in kernel 5.8+)
  - `CAP_SYS_ADMIN` (fallback for older kernels or tools)
  - `CAP_PERFMON` (performance monitoring)
  - `CAP_NET_ADMIN` (network observability)
- **How to verify:**
  - Check current capabilities:

    ```sh
    capsh --print | grep cap_
    ```

  - For containerized environments, ensure capabilities are not dropped (see [Kubernetes docs](https://kubernetes.io/docs/) or [Docker docs](https://docs.docker.com/)).

### 4. Distribution Compatibility

- **Tested on:** Recent Ubuntu, Debian, CentOS/RHEL, Fedora.
- **Note:** Custom kernels or minimal distributions may require enabling/configuring eBPF-related options.

---

## Kubernetes

### 1. Cluster Version

- **Minimum:** Kubernetes 1.16+
- **Check version:**

  ```sh
  kubectl version --short
  ```

### 2. kubectl Access

- Ensure `kubectl` is installed and configured to communicate with the target cluster:

  ```sh
  kubectl cluster-info
  ```

- You should receive cluster details, not errors.

### 3. Cluster Capabilities

- For cluster-wide deployments, confirm permission to create privileged DaemonSets and grant required Linux capabilities.
- If using managed services (EKS, GKE, AKS), ensure nodes support eBPF and required kernel capabilities (see cloud provider documentation).

---

## Troubleshooting & Validation

- **Check eBPF runtime support:**

  ```sh
  bpftool prog list
  ```

  - Lists loaded eBPF programs; command should succeed without errors.

- **Validate capabilities in containers:**
  - Review `securityContext.capabilities` in Pod specs for necessary capabilities.
  - For troubleshooting, check container logs and system logs (`dmesg`, `/var/log/messages`).
