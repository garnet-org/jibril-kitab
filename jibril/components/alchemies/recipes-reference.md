---
description: Learn All Options and Values of Detection Recipes
icon: object-group
---

# Recipes Reference

## <mark style="color:yellow;">Required Fields</mark>

* `kind`: Unique identifier for the recipe type
* `name`: Name of the specific recipe instance
* `version`: Recipe version (numeric)
* `description`: Brief description
* `mechanism`: Detection mechanism type
* `breed`: Detection category
* `tactic`: MITRE ATTACK tactic
* `technique`: MITRE ATTACK technique
* `subtechnique`: MITRE ATTACK sub-technique
* `importance`: Severity level

## <mark style="color:yellow;">File Action Values</mark>

### **Individual Actions**:

* `fasync`: File asynchronous operations
* `flock`: File locking operations
* `fsync`: File synchronization
* `llseek`: Low-level seek operations
* `mmap`: Memory mapping operations
* `open`: File open operations
* `read`: File read operations
* `write`: File write operations
* `rename`: File rename operations
* `truncate`: File truncation operations
* `unlink`: File deletion operations
* `create`: File creation operations
* `close`: File close operations
* `link`: Hard link operations
* `execve`: Executable file operations

### **Action Matching**:

* `how`: Specifies how actions should match
  * `any`: Any action matches
  * `all`: All actions must match

## <mark style="color:yellow;">**Macros**</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">(expanded automatically):</mark>

<table><thead><tr><th width="223.8046875"> Macro vs Actions</th><th width="81.0859375">fasync</th><th width="64.4375">flock</th><th width="54.14453125">fsync</th><th width="73.75">llseek</th><th width="79.046875">mmap</th><th width="68.32421875">open</th><th width="60.73828125">read</th><th width="66.4921875">write</th><th width="81.0078125">rename</th><th width="82.91796875">truncate</th><th width="74.73828125">unlink</th><th width="74.12109375">create</th><th width="65.32421875">close</th><th width="59.83984375">link</th><th width="75.4375">execve</th></tr></thead><tbody><tr><td>any</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>open_related</td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td></tr><tr><td>read_related</td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>modify_related</td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td></tr><tr><td>access_related</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td></td></tr><tr><td>access_no_mmap_related</td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td></td></tr><tr><td>tamper_related</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td></td><td></td><td>✅</td><td></td></tr></tbody></table>

## <mark style="color:yellow;">Times Kind Values</mark>

<table><thead><tr><th width="306.9765625">Limit Type</th><th>Scope Description</th></tr></thead><tbody><tr><td>times_per_proc</td><td>Per process</td></tr><tr><td>times_per_exe</td><td>Per executable</td></tr><tr><td>times_per_parent_proc</td><td>Per parent process</td></tr><tr><td>times_per_parent_exe</td><td>Per parent executable</td></tr><tr><td>times_per_full_ancestry</td><td>Per full process tree</td></tr><tr><td>times_per_hostname</td><td>Per hostname</td></tr><tr><td>times_per_host</td><td>Global limit</td></tr></tbody></table>

## <mark style="color:yellow;">Classification Values</mark>

### **Mechanism**:

* `file_access`
* `execution`
* `network_peers`
* `baseline`

### **Breed**:

* `file_access`
* `execution`
* `remote_domains`
* `remote_ips`
* `local_domains`
* `local_ips`

### **Importance**:

* `low`
* `medium`
* `high`
* `critical`
