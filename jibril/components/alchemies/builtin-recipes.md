---
description: Jibril ships with numerous built-in detection recipes
icon: arrows-to-circle
---

# Builtin Recipes

<figure><img src="../../../.gitbook/assets/image (28).png" alt="" width="128"><figcaption></figcaption></figure>

## <mark style="color:yellow;">Public Detection Recipes</mark>

* [binary\_self\_deletion](../../detections/file-access/binary_self_deletion.md)
* [capabilities\_modification](../../detections/file-access/capabilities_modification.md)
* [code\_modification\_through\_procfs](../../detections/file-access/code_modification_through_procfs.md)
* [core\_pattern\_access](../../detections/file-access/core_pattern_access.md)
* [cpu\_fingerprint](../../detections/file-access/cpu_fingerprint.md)
* [data\_encoder\_exec](../../detections/execution/data_encoder_exec.md)
* [filesystem\_fingerprint](../../detections/file-access/filesystem_fingerprint.md)
* [global\_shlib\_modification](../../detections/file-access/global_shlib_modification.md)
* [hidden\_elf\_exec](../../detections/execution/hidden_elf_exec.md)
* [java\_debug\_lib\_load](../../detections/file-access/java_debug_lib_load.md)
* [java\_instrument\_lib\_load](../../detections/file-access/java_instrument_lib_load.md)
* [machine\_fingerprint](../../detections/file-access/machine_fingerprint.md)
* [os\_fingerprint](../../detections/file-access/os_fingerprint.md)
* [os\_network\_fingerprint](../../detections/file-access/os_network_fingerprint.md)
* [os\_status\_fingerprint](../../detections/file-access/os_status_fingerprint.md)
* [package\_repo\_config\_modification](../../detections/file-access/package_repo_config_modification.md)
* [pam\_config\_modification](../../detections/file-access/pam_config_modification.md)
* [passwd\_usage](../../detections/execution/passwd_usage.md)
* [sched\_debug\_access](../../detections/file-access/sched_debug_access.md)
* [shell\_config\_modification](../../detections/file-access/shell_config_modification.md)
* [sysrq\_access](../../detections/file-access/sysrq_access.md)
* [unprivileged\_bpf\_config\_access](../../detections/file-access/unprivileged_bpf_config_access.md)

> Public Detection Recipes Repository: [https://github.com/garnet-org/jibril-wahy](https://github.com/garnet-org/jibril-wahy)

{% hint style="info" %}
You may use public detection recipes as examples to create your own recipe.
{% endhint %}

{% hint style="success" %}
The public recipes include a few (to be completed) recipes translate from open-source projects.
{% endhint %}

## <mark style="color:yellow;">Private Recipes</mark>

* [adult\_domain\_access](../../detections/network-peers/adult_domain_access.md)
* [auth\_logs\_tamper](../../detections/file-access/auth_logs_tamper.md)
* [badware\_domain\_access](../../detections/network-peers/badware_domain_access.md)
* [binary\_executed\_by\_loader](../../detections/execution/binary_executed_by_loader.md)
* [cloud\_metadata\_access](../../detections/network-peers/cloud_metadata_access.md)
* [code\_on\_the\_fly](../../detections/execution/code_on_the_fly.md)
* [credentials\_files\_access](../../detections/file-access/credentials_files_access.md)
* [credentials\_text\_lookup](../../detections/execution/credentials_text_lookup.md)
* [crypto\_miner\_execution](../../detections/execution/crypto_miner_execution.md)
* [crypto\_miner\_files](../../detections/file-access/crypto_miner_files.md)
* [denial\_of\_service\_tools](../../detections/execution/denial_of_service_tools.md)
* [dyndns\_domain\_access](../../detections/network-peers/dyndns_domain_access.md)
* [environ\_read\_from\_procfs](../../detections/file-access/environ_read_from_procfs.md)
* [exec\_from\_unusual\_dir](../../detections/execution/exec_from_unusual_dir.md)
* [fake\_domain\_access](../../detections/network-peers/fake_domain_access.md)
* [file\_attribute\_change](../../detections/execution/file_attribute_change.md)
* [gambling\_domain\_access](../../detections/network-peers/gambling_domain_access.md)
* [interpreter\_shell\_spawn](../../detections/execution/interpreter_shell_spawn.md)
* [net\_filecopy\_tool\_exec](../../detections/execution/net_filecopy_tool_exec.md)
* [net\_mitm\_tool\_exec](../../detections/execution/net_mitm_tool_exec.md)
* [net\_scan\_tool\_exec](../../detections/execution/net_scan_tool_exec.md)
* [net\_sniff\_tool\_exec](../../detections/execution/net_sniff_tool_exec.md)
* [net\_suspicious\_tool\_exec](../../detections/execution/net_suspicious_tool_exec.md)
* [net\_suspicious\_tool\_shell](../../detections/execution/net_suspicious_tool_shell.md)
* [piracy\_domain\_access](../../detections/network-peers/piracy_domain_access.md)
* [plaintext\_communication](../../detections/network-peers/plaintext_communication.md)
* [runc\_suspicious\_exec](../../detections/execution/runc_suspicious_exec.md)
* [ssl\_certificate\_access](../../detections/file-access/ssl_certificate_access.md)
* [sudoers\_modification](../../detections/file-access/sudoers_modification.md)
* [threat\_domain\_access](../../detections/network-peers/threat_domain_access.md)
* [tracking\_domain\_access](../../detections/network-peers/tracking_domain_access.md)
* [vpnlike\_domain\_access](../../detections/network-peers/vpnlike_domain_access.md)
* [webserver\_exec](../../detections/execution/webserver_exec.md)
* [webserver\_shell\_exec](../../detections/execution/webserver_shell_exec.md)

{% hint style="info" %}
Some signatures are private-only for now.
{% endhint %}
