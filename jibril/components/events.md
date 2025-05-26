---
description: Enable or disable events at will.
icon: equals
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Events

<figure><img src="../../.gitbook/assets/image (15).png" alt="" width="128"><figcaption></figcaption></figure>

## <mark style="color:yellow;">Jibril Extension Network Policy (netpolicy) Plugin</mark> <a href="#jibril-netpolicy" id="jibril-netpolicy"></a>

<table><thead><tr><th width="161.34375">Event</th><th>Description</th></tr></thead><tbody><tr><td><strong>dropip</strong></td><td>Alerts when network flows are dropped by existing policy due to CIDR or domain name restrictions</td></tr><tr><td><strong>dropdomain</strong></td><td>Alerts when domain resolutions are dropped by existing policy due to domain name restrictions</td></tr></tbody></table>

## <mark style="color:yellow;">Jibril Extension Detect (detect) Plugin</mark> <a href="#jibril-detect" id="jibril-detect"></a>

### Flow Events (detect all the network flows)

<table><thead><tr><th width="156.98046875">Event</th><th>Description</th></tr></thead><tbody><tr><td><strong>flow</strong></td><td>Captures and logs network flow data, including source and destination addresses, ports, and protocols</td></tr></tbody></table>

### File Access (detection mechanism)

<table><thead><tr><th width="290.9453125">Event</th><th>Description</th></tr></thead><tbody><tr><td>capabilities_modification</td><td>Detects changes to file capabilities</td></tr><tr><td>code_modification_through_procfs</td><td>Detects code modifications via /proc</td></tr><tr><td>core_pattern_access</td><td>Monitors access to core pattern configurations</td></tr><tr><td>cpu_fingerprint</td><td>Identifies unique CPU fingerprints for anomaly detection</td></tr><tr><td>credentials_files_access</td><td>Tracks access to credential files</td></tr><tr><td>filesystem_fingerprint</td><td>Detects changes in filesystem signatures</td></tr><tr><td>java_debug_lib_load</td><td>Monitors loading of Java debug libraries</td></tr><tr><td>java_instrument_lib_load</td><td>Tracks loading of Java instrumentation libraries</td></tr><tr><td>machine_fingerprint</td><td>Identifies unique machine fingerprints</td></tr><tr><td>os_fingerprint</td><td>Detects changes in OS signatures</td></tr><tr><td>os_network_fingerprint</td><td>Monitors OS network-related fingerprints</td></tr><tr><td>os_status_fingerprint</td><td>Tracks OS status changes</td></tr><tr><td>package_repo_config_modification</td><td>Detects modifications in package repository configurations</td></tr><tr><td>pam_config_modification</td><td>Monitors changes to PAM configurations</td></tr><tr><td>sched_debug_access</td><td>Detects access to scheduler debug interfaces</td></tr><tr><td>shell_config_modification</td><td>Tracks changes to shell configurations</td></tr><tr><td>ssl_certificate_access</td><td>Monitors access to SSL certificates</td></tr><tr><td>sudoers_modification</td><td>Detects changes to sudoers files</td></tr><tr><td>sysrq_access</td><td>Tracks access to sysrq functionalities</td></tr><tr><td>unprivileged_bpf_config_access</td><td>Detects access to unprivileged BPF configurations</td></tr><tr><td>global_shlib_modification</td><td>Monitors modifications to global shared libraries</td></tr><tr><td>environ_read_from_procfs</td><td>Detects environment variables reading from procfs</td></tr><tr><td>binary_self_deletion</td><td>Detects executable self-deletion</td></tr><tr><td>crypto_miner_files</td><td>Detects access to files related to crypto mining</td></tr><tr><td>auth_logs_tamper</td><td>Detects authentication log files tampering</td></tr></tbody></table>

### Execution (detection mechanism)

<table><thead><tr><th width="292.265625">Event</th><th>Description</th></tr></thead><tbody><tr><td>binary_executed_by_loader</td><td>Detects binaries executed via the ELF loader</td></tr><tr><td>code_on_the_fly</td><td>Monitors dynamic code execution</td></tr><tr><td>denial_of_service_tools</td><td>Detects the use of denial-of-service tools</td></tr><tr><td>exec_from_unusual_dir</td><td>Tracks executions from non-standard directories</td></tr><tr><td>file_attribute_change</td><td>Detects changes to file attributes</td></tr><tr><td>hidden_elf_exec</td><td>Identifies hidden ELF executions</td></tr><tr><td>interpreter_shell_spawn</td><td>Monitors the spawning of interpreter shells</td></tr><tr><td>net_filecopy_tool_exec</td><td>Detects the execution of network file copy tools</td></tr><tr><td>net_mitm_tool_exec</td><td>Identifies man-in-the-middle network tool executions</td></tr><tr><td>net_scan_tool_exec</td><td>Detects network scanning tool executions</td></tr><tr><td>net_sniff_tool_exec</td><td>Monitors the use of network sniffing tools</td></tr><tr><td>net_suspicious_tool_exec</td><td>Detects suspicious network tool executions</td></tr><tr><td>net_suspicious_tool_shell</td><td>Identifies suspicious tool shells in network contexts</td></tr><tr><td>passwd_usage</td><td>Tracks the usage of the passwd command</td></tr><tr><td>runc_suspicious_exec</td><td>Detects suspicious executions related to runc</td></tr><tr><td>webserver_exec</td><td>Detects web server daemon startup</td></tr><tr><td>webserver_shell_exec</td><td>Detects shell spawned by webserver</td></tr><tr><td>crypto_miner_execution</td><td>Detects execution of crypto miners</td></tr></tbody></table>

### Network Peers (detection mechanism)

<table><thead><tr><th width="292.265625">Event</th><th>Description</th></tr></thead><tbody><tr><td>adult_domain_access</td><td>Detects access to adult content domains</td></tr><tr><td>badware_domain_access</td><td>Detects access to known malware or suspicious domains</td></tr><tr><td>dyndns_domain_access</td><td>Detects access to dynamic DNS services</td></tr><tr><td>fake_domain_access</td><td>Detects access to fake or spoofed domains</td></tr><tr><td>gambling_domain_access</td><td>Detects access to gambling-related domains</td></tr><tr><td>piracy_domain_access</td><td>Detects access to piracy-related domains</td></tr><tr><td>plaintext_communication</td><td>Detects unencrypted network communications</td></tr><tr><td>threat_domain_access</td><td>Detects access to known threat domains</td></tr><tr><td>tracking_domain_access</td><td>Detects access to tracking and analytics domains</td></tr><tr><td>vpnlike_domain_access</td><td>Detects access to VPN-like service domains</td></tr></tbody></table>
