---
description: Adjust Jibril Cache to avoid Miss Detections
icon: line-columns
---

# Cache Configuration

## <mark style="color:yellow;">Jibril Cache Configuration</mark>

Jibril, utilizes various caches to optimize performance and manage system resources efficiently. The configuration of these caches is crucial for tailoring Jibril to specific operational environments, balancing detection capabilities with resource footprint. As outlined in Jibril's architecture, its flexibility and scalability heavily rely on how these components are configured.

This document details the available cache options in the `config.yaml` file, their purpose, and provides sizing examples for different scenarios.

## <mark style="color:yellow;">Cache Options</mark>

Jibril's caches are designed to store transient data related to system activities, such as tasks, file operations, and network flows. Properly sizing these caches ensures that Jibril can maintain a low resource footprint while providing comprehensive monitoring.

### <mark style="color:yellow;">Task-Related Caches</mark>

These caches store information about running processes and their execution context.

* `jb_tasks`\
  Stores information about OS processes observed by Jibril.
* `jb_cmds`\
  Caches the command lines used to start tasks.
* `jb_args`\
  Stores the arguments passed to commands.
* `jb_rectasks`\
  Holds data for recent tasks for short-term historical analysis.
* `jb_thashcache`\
  A cache for task hashes (to avoid hash calculations).

### <mark style="color:yellow;">File-Related Caches</mark>

These caches manage data related to file system access and modifications.

* `jb_files`\
  Caches information about accessed files.
* `jb_dirs`\
  Stores data related to accessed directories.
* `jb_bases`\
  Caches base paths for files.
* `jb_filetask`\
  Maps files to the tasks that accessed them.
* `jb_taskfile`\
  Maps tasks to the files they accessed.
* `jb_filerefs`\
  Tracks references to files.

### <mark style="color:yellow;">Flow-Related Caches (Network)</mark>

These caches store information about network communications.

* `jb_flows`\
  Caches network flow data.
* `jb_taskflow`\
  Maps tasks to the network flows they are associated with.
* `jb_flowtask`\
  Maps network flows back to the tasks responsible for them.
* `jb_flowrefs`\
  Tracks references to network flows.

### <mark style="color:yellow;">Domain-Related Caches (Network)</mark>

These caches store information related to network domain resolutions and peer connections.

* `jb_domains`\
  Caches resolved domain names.
* `jb_canons`\
  Stores canonical domain names, which helps in normalizing domain representations (e.g., handling CNAMEs).
* `jb_peers`\
  Caches information about network peers (e.g., remote IP addresses).

## <mark style="color:yellow;">Cache Size Examples</mark>

The [config.yaml](./) file provides options that allows Jibril to be adapted to various environments, from resource-constrained devices to high-traffic servers. By not information those options, Jibril will use the [default values](cache-configuration.md#id-1.-average-default).

### <mark style="color:yellow;">1. Average (Default)</mark>

This is the default set of values and good for most of the use cases.

```yaml
caches:
  # Tasks.
  jb_tasks: 65536    # Tasks.
  jb_cmds: 32768     # Commands.
  jb_args: 32768     # Arguments.
  jb_rectasks: 4096  # Recent tasks.
  jb_thashcache: 4096 # Task hash cache.

  # Files.
  jb_files: 32768    # Files.
  jb_dirs: 8192      # Directories.
  jb_bases: 16384    # Bases.
  # Files references.
  jb_filetask: 32768 # File + Task.
  jb_taskfile: 32768 # Task + File.
  jb_filerefs: 32768 # File references.

  # Flows.
  jb_flows: 32768    # Flows.
  # Flows references.
  jb_taskflow: 32768 # Task + Flow.
  jb_flowtask: 32768 # Flow + Task.
  jb_flowrefs: 32768 # Flow references.

  # Domains.
  jb_domains: 16384  # Domains.
  jb_canons: 16384   # Canonical domains.
  jb_peers: 16384    # Peers.
```

{% hint style="success" %}
The "Average" configuration provides ample cache space for common system activities. It can handle a moderate number of concurrent processes, file operations, and network flows without excessive memory consumption. Under heavy workloads, missed detections might occur for detection recipes that depend on file accesses (but this can be mitigated by fine-tuning these parameters). This aligns with Jibril's goal of maintaining efficiency by using eBPF for kernel-level data collection and a structured userland execution model.
{% endhint %}

### <mark style="color:yellow;">2. Small Devices</mark>

This configuration significantly reduces cache sizes to minimize Jibril's memory footprint, making it suitable for embedded systems or environments with limited resources.

```yaml
caches:
  # Tasks.
  jb_tasks: 16384    # Tasks.
  jb_cmds: 8192      # Commands.
  jb_args: 8192      # Arguments.
  jb_rectasks: 8192  # Recent tasks.
  jb_thashcache: 4096 # Task hash cache.

  # Files.
  jb_files: 8192     # Files.
  jb_dirs: 8192      # Directories.
  jb_bases: 8192     # Bases.
  # Files references.
  jb_filetask: 16384 # File + Task.
  jb_taskfile: 16384 # Task + File.
  jb_filerefs: 16384 # File references.

  # Flows.
  jb_flows: 8192     # Flows.
  # Flows references.
  jb_taskflow: 16384 # Task + Flow.
  jb_flowtask: 16384 # Flow + Task.
  jb_flowrefs: 16384 # Flow references.

  # Domains.
  jb_domains: 8192   # Domains.
  jb_canons: 8192    # Canonical domains.
  jb_peers: 8192     # Peers.
```

{% hint style="success" %}
For small devices, minimizing memory usage is paramount. While smaller caches might lead to more cache misses and some missed detections, the trade-off is acceptable if other detection recipes come into play. This demonstrates Jibril's adaptability to different deployment scales.
{% endhint %}

### <mark style="color:yellow;">3. Heavy I/O</mark>

This configuration increases cache sizes, particularly for file and flow-related data, to reduce miss-detections and improve performance on systems with high disk and network activity.

```yaml
caches:
  # Tasks.
  jb_tasks: 65536     # Tasks.
  jb_cmds: 32768      # Commands.
  jb_args: 32768      # Arguments.
  jb_rectasks: 32768  # Recent tasks.
  jb_thashcache: 8192   # Task hash cache.

  # Files.
  jb_files: 32768     # Files.
  jb_dirs: 32768      # Directories.
  jb_bases: 32768     # Bases.
  # Files references.
  jb_filetask: 524288 # File + Task.
  jb_taskfile: 524288 # Task + File.
  jb_filerefs: 524288 # File references.

  # Flows.
  jb_flows: 32768     # Flows.
  # Flows references.
  jb_taskflow: 131072 # Task + Flow.
  jb_flowtask: 131072 # Flow + Task.
  jb_flowrefs: 131072 # Flow references.

  # Domains.
  jb_domains: 32768   # Domains.
  jb_canons: 32768    # Canonical domains.
  jb_peers: 32768     # Peers.
```

{% hint style="warning" %}
On systems with heavy I/O (thousands of different file creations or modifications per second), larger caches are beneficial. Increasing cache sizes makes Jibril practically infallible in terms of losing detections, at the cost of consuming more memory. This quid-pro-quo is unavoidable if missing file access-related detections is unacceptable. Unlike other projects, Jibril allows you to choose (instead of quietly dropping events like most, if not all, other eBPF-based tools). This configuration prioritizes comprehensive monitoring and detection accuracy in demanding environments, aligning with Jibril's capability to handle large-scale deployments.
{% endhint %}

### Conclusion

Configuring Jibril's caches appropriately is a key aspect of deploying the agent effectively. By understanding the purpose of each cache and selecting a sizing strategy that matches the system's workload and resource availability, users can ensure optimal performance and robust runtime detection. Jibril's eBPF-based architecture, combined with this configurable caching mechanism, allows for deep visibility into system behavior while maintaining efficiency.
