---
icon: sliders-up
---

# Configuration File

## <mark style="color:yellow;">Defaults: /etc/jibril/config.yaml</mark>

```yaml
#### Jibril Configuration File.

#### Basic configuration.

log-level: info
stdout: stdout
stderr: stderr
chop-lines: false
no-health: false
profiler: false
cardinal: true
daemon: false
notify: false

#### Extensions, plugins and printers.

extension:
  #### Enable extensions here
  # - example
  # - simple
  - config
  - data
  - jibril
plugin:
  #### Enable plugins here
  # - example:helloworld
  # - simple:printers
  - jibril:hold
  - jibril:procfs
  - jibril:printers
  # - jibril:jbconfig
  # - jibril:pause
  # - jibril:attenuator:enabled=true:model=gpt-4o:temperature=0.3:mode=reason
  - jibril:detect
  - jibril:netpolicy:file=/etc/jibril/netpolicy.yaml
  # - jibril:github
printer:
  #### Enable printers here
  # - simple:printers:voidprinter
  # - jibril:printers:stdout
  # - jibril:printers:stdout:raw=true
  - jibril:printers:varlog
  # - jibril:printers:garnet
  # - jibril:printers:garnet:error_log_rate=30s
  # - jibril:github:listendev
  # - jibril:github:listendevdebug

#### Event configuration.

event:
  #### Informational events about network policy applied
  # - jibril:netpolicy:dropip
  # - jibril:netpolicy:dropdomain
  #### Informational events about network flows
  - jibril:detect:flow
  #### Detection recipes for file access patterns
  - jibril:detect:file_example
  - jibril:detect:capabilities_modification
  - jibril:detect:code_modification_through_procfs
  - jibril:detect:core_pattern_access
  - jibril:detect:cpu_fingerprint
  - jibril:detect:credentials_files_access
  - jibril:detect:filesystem_fingerprint
  - jibril:detect:java_debug_lib_load
  - jibril:detect:java_instrument_lib_load
  - jibril:detect:machine_fingerprint
  - jibril:detect:os_fingerprint
  - jibril:detect:os_network_fingerprint
  - jibril:detect:os_status_fingerprint
  - jibril:detect:package_repo_config_modification
  - jibril:detect:pam_config_modification
  - jibril:detect:sched_debug_access
  - jibril:detect:shell_config_modification
  - jibril:detect:ssl_certificate_access
  - jibril:detect:sudoers_modification
  - jibril:detect:sysrq_access
  - jibril:detect:unprivileged_bpf_config_access
  - jibril:detect:global_shlib_modification
  - jibril:detect:environ_read_from_procfs
  - jibril:detect:binary_self_deletion
  - jibril:detect:crypto_miner_files
  - jibril:detect:auth_logs_tamper
  ##### Detection recipes for execution patterns
  - jibril:detect:exec_example
  - jibril:detect:binary_executed_by_loader
  - jibril:detect:code_on_the_fly
  - jibril:detect:credentials_text_lookup
  - jibril:detect:data_encoder_exec
  - jibril:detect:denial_of_service_tools
  - jibril:detect:exec_from_unusual_dir
  - jibril:detect:file_attribute_change
  - jibril:detect:hidden_elf_exec
  - jibril:detect:interpreter_shell_spawn
  - jibril:detect:net_filecopy_tool_exec
  - jibril:detect:net_mitm_tool_exec
  - jibril:detect:net_scan_tool_exec
  - jibril:detect:net_sniff_tool_exec
  - jibril:detect:net_suspicious_tool_exec
  - jibril:detect:net_suspicious_tool_shell
  - jibril:detect:passwd_usage
  - jibril:detect:runc_suspicious_exec
  - jibril:detect:webserver_exec
  - jibril:detect:webserver_shell_exec
  - jibril:detect:crypto_miner_execution
  ##### Detection recipes for network peers patterns
  - jibril:detect:peer_example
  - jibril:detect:adult_domain_access
  - jibril:detect:algorithmic_domains
  - jibril:detect:algorithmic_domains_light
  - jibril:detect:badware_domain_access
  - jibril:detect:cloud_metadata_access
  - jibril:detect:dyndns_domain_access
  - jibril:detect:fake_domain_access
  - jibril:detect:gambling_domain_access
  - jibril:detect:gambling_domain_access_light
  - jibril:detect:general_new_domains
  - jibril:detect:general_new_domains_light
  - jibril:detect:phishing_domains
  - jibril:detect:phishing_domains_light
  - jibril:detect:piracy_domain_access
  - jibril:detect:plaintext_communication
  - jibril:detect:threat_domain_access
  - jibril:detect:threat_domain_access_light
  - jibril:detect:threat_domain_access_medium
  - jibril:detect:tracking_domain_access
  - jibril:detect:vpnlike_domain_access

#### Advanced configuration.

#
# Cadence configuration.
#
# Note: The cadence interval determines how often behavioral patterns are evaluated, not
# the detection accuracy itself. All monitored resources maintain cached behavioral state
# that gets analyzed at each cadence interval. Shorter intervals may increase CPU usage
# and require larger cache sizes to avoid losing behavioral data. Detection accuracy
# depends on the combination of evaluation frequency, the rate of behavioral changes
# between intervals, and cache capacity.
#

cadences:
  file_access: 9 # 9 sec interval in between file access patterns check.
  network_peers: 9 # 9 sec interval in between network peers patterns check.
  network_flows: 9 # 9 sec interval in between network flows patterns check.

#
# Cache configuration.
#
# Note: The cache size determines how much behavioral data is stored for each monitored
# resource. Larger caches can improve detection accuracy by providing more context for
# pattern analysis, but require bigger memory footprint. The cache size should be adjusted
# based on the expected rate of behavioral changes and the desired detection accuracy.
#

#### Average:
#### Average memory consumption.
#### Reasonable file-access miss-detection.
caches:
  #### Tasks.
  jb_tasks: 65536 # Tasks.
  jb_cmds: 32768 # Commands.
  jb_args: 32768 # Arguments.
  jb_rectasks: 4096 # Recent tasks.
  jb_thashcache: 4096 # Task hash cache.
  #### Files.
  jb_files: 32768 # Files.
  jb_dirs: 8192 # Directories.
  jb_bases: 16384 # Bases.
  #### Files references.
  jb_filetask: 32768 # File + Task.
  jb_taskfile: 32768 # Task + File.
  jb_filerefs: 32768 # File references.
  #### Flows.
  jb_flows: 32768 # Flows.
  #### Flows references.
  jb_taskflow: 32768 # Task + Flow.
  jb_flowtask: 32768 # Flow + Task.
  jb_flowrefs: 32768 # Flow references.
  #### Domains.
  jb_domains: 16384 # Domains.
  jb_canons: 16384 # Canonical domains.
  jb_peers: 16384 # Peers.

#### Heavy I/O:
#### Bigger memory consumption.
#### Lower miss-detection.
# caches:
#   #### Tasks.
#   jb_tasks: 65536
#   jb_cmds: 32768
#   jb_args: 32768
#   jb_rectasks: 32768
#   jb_thashcache: 8192
#   #### Files.
#   jb_files: 32768
#   jb_dirs: 32768
#   jb_bases: 32768
#   #### Files references.
#   jb_filetask: 524288
#   jb_taskfile: 524288
#   jb_filerefs: 524288
#   #### Flows.
#   jb_flows: 32768
#   #### Flows references.
#   jb_taskflow: 131072
#   jb_flowtask: 131072
#   jb_flowrefs: 131072
#   #### Domains.
#   jb_domains: 32768
#   jb_canons: 32768
#   jb_peers: 32768

#### Low Footprint:
#### Small memory consumption.
#### Possible file-access miss-detection.
# caches:
#   #### Tasks.
#   jb_tasks: 16384
#   jb_cmds: 8192
#   jb_args: 8192
#   jb_rectasks: 8192
#   jb_thashcache: 4096
#   #### Files.
#   jb_files: 8192
#   jb_dirs: 8192
#   jb_bases: 8192
#   #### Files references.
#   jb_filetask: 16384
#   jb_taskfile: 16384
#   jb_filerefs: 16384
#   #### Flows.
#   jb_flows: 8192
#   #### Flows references.
#   jb_taskflow: 16384
#   jb_flowtask: 16384
#   jb_flowrefs: 16384
#   # Domains.
#   jb_domains: 8192
#   jb_canons: 8192
#   jb_peers: 8192
```

## <mark style="color:yellow;">Run Jibril</mark>

```
sudo -E ./build/loader --config ~/config/default.yaml
```
