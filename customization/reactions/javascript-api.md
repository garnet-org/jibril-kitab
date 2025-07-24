---
description: The bridge between Jibril and a detection reaction
icon: code
---

# JavaScript API

This document provides a complete reference for all JavaScript helper functions available within reaction code. These functions provide controlled access to system resources and security operations.

## <mark style="color:yellow;">Global Variables</mark>

Every reaction has access to these global variables:

* **`kind`** (string): The type of detection event (e.g., "file\_access", "execution", "network\_peer")
* **`name`** (string): The name of the detection recipe that triggered this reaction
* **`uuid`** (string): Unique identifier for the specific event instance
* **`data`** (object): Complete JSON object containing all event details and context

## <mark style="color:yellow;">Logging Functions</mark>

### `Info(message)`

Logs an informational message to the Jibril log system.

**Parameters:**

* `message` (string): The message to log

**Returns:** `undefined`

**Example:**

```javascript
Info("Reaction executed successfully");
Info("Processing event: " + data.metadata.name);
```

### `Warn(message)`

Logs a warning message to the Jibril log system.

**Parameters:**

* `message` (string): The warning message to log

**Returns:** `undefined`

**Example:**

```javascript
Warn("Suspicious activity detected in: " + data.file.file);
```

### `Error(message)`

Logs an error message to the Jibril log system.

**Parameters:**

* `message` (string): The error message to log

**Returns:** `undefined`

**Example:**

```javascript
Error("Failed to block malicious IP address");
```

## <mark style="color:yellow;">Network Policy Functions</mark>

{% hint style="warning" %}
**Network policy functions require the netpolicy plugin to be enabled. If the plugin is not available, these functions will return error codes.**
{% endhint %}

### `NetBlockIp([ipAddress])`

Blocks network traffic to/from specified IP addresses.

**Parameters:**

* `ipAddress` (string, optional): Specific IP address to block. If omitted, blocks all remote IPs from the current event context.

**Returns:**

* `0`: Success (IP blocked)
* `1`: All IPs were already blocked
* `-1`: Error occurred (use `Errno()` for details)

**Example:**

```javascript
// Block a specific IP
let result = NetBlockIp("192.168.1.100");
if (result === 0) {
    Info("IP blocked successfully");
} else if (result === 1) {
    Info("IP was already blocked");
} else {
    Error("Failed to block IP: " + Errno());
}

// Block all remote IPs from the event
let result = NetBlockIp();
if (result === 0) {
    Info("All remote IPs blocked successfully");
}
```

### `NetUnblockIp(ipAddress)`

Unblocks network traffic to/from a specific IP address.

**Parameters:**

* `ipAddress` (string, required): The IP address to unblock

**Returns:**

* `0`: Success (IP unblocked)
* `1`: IP was already unblocked
* `-1`: Error occurred (use `Errno()` for details)

**Example:**

```javascript
let result = NetUnblockIp("192.168.1.100");
if (result === 0) {
    Info("IP unblocked successfully");
} else if (result === 1) {
    Info("IP was already unblocked");
} else {
    Error("Failed to unblock IP: " + Errno());
}
```

### `NetBlockIpTimer(ipAddress, durationSeconds)`

Blocks an IP address for a specific duration in seconds.

**Parameters:**

* `ipAddress` (string, required): The IP address to block
* `durationSeconds` (number, required): Duration in seconds to block the IP

**Returns:**

* `0`: Success (IP blocked with timer)
* `1`: IP was already blocked
* `-1`: Error occurred (use `Errno()` for details)

**Example:**

```javascript
// Block IP for 30 seconds
let result = NetBlockIpTimer("192.168.1.100", 30);
if (result === 0) {
    Info("IP blocked for 30 seconds");
} else {
    Error("Failed to block IP with timer: " + Errno());
}
```

### `NetBlockDomain([domain])`

Blocks network traffic to specified domains.

**Parameters:**

* `domain` (string, optional): Specific domain to block. If omitted, blocks all remote domains from the current event context.

**Returns:**

* `0`: Success (domain blocked)
* `1`: All domains were already blocked
* `-1`: Error occurred (use `Errno()` for details)

**Example:**

```javascript
// Block a specific domain
let result = NetBlockDomain("malicious-site.com");
if (result === 0) {
    Info("Domain blocked successfully");
}

// Block all domains from the event
let result = NetBlockDomain();
if (result === 0) {
    Info("All remote domains blocked successfully");
}
```

## <mark style="color:yellow;">Process Management Functions</mark>

### `KillCurrent()`

Terminates the current process (the one that triggered the detection).

**Parameters:** None

**Returns:**

* `0`: Success (process terminated)
* `1`: Process already exited
* `-1`: Error occurred (use `Errno()` for details)

**Example:**

```javascript
let result = KillCurrent();
if (result === 0) {
    Info("Malicious process terminated");
} else if (result === 1) {
    Info("Process already exited");
} else {
    Error("Failed to terminate process: " + Errno());
}
```

### `KillParent()`

Terminates the parent process of the current process.

**Parameters:** None

**Returns:**

* `0`: Success (parent process terminated)
* `1`: Parent process already exited
* `-1`: Error occurred (use `Errno()` for details)

**Example:**

```javascript
let result = KillParent();
if (result === 0) {
    Info("Parent process terminated");
} else if (result === 1) {
    Info("Parent process already exited");
} else {
    Error("Failed to terminate parent: " + Errno());
}
```

### `KillProcess(pid)`

Terminates a specific process by PID.

**Parameters:**

* `pid` (number, required): The process ID to terminate

**Returns:**

* `0`: Success (process terminated)
* `1`: Process already exited
* `-1`: Error occurred (use `Errno()` for details)

**Safety:** This function has built-in protections against killing system processes (PID < 500), Jibril itself, or Jibril's parent process.

**Example:**

```javascript
let targetPid = 1234;
let result = KillProcess(targetPid);
if (result === 0) {
    Info("Process " + targetPid + " terminated");
} else if (result === 1) {
    Info("Process " + targetPid + " already exited");
} else {
    Error("Failed to terminate process " + targetPid + ": " + Errno());
}
```

## <mark style="color:yellow;">File System Functions</mark>

### `ReadFile(path)`

Reads the contents of a file.

**Parameters:**

* `path` (string, required): Path to the file to read

**Returns:**

* `string`: File contents on success
* `""` (empty string): On error (use `Errno()` for details)

**Example:**

```javascript
let content = ReadFile("/etc/passwd");
if (content !== "") {
    Info("File read successfully: " + content.length + " bytes");
} else {
    Error("Failed to read file: " + Errno());
}
```

### `WriteFile(path, data)`

Writes data to a file (creates or overwrites).

**Parameters:**

* `path` (string, required): Path to the file to write
* `data` (string, required): Data to write to the file

**Returns:**

* `0`: Success
* `-1`: Error occurred (use `Errno()` for details)

**Security:** Files are created with 0600 permissions (readable/writable by owner only).

**Example:**

```javascript
let result = WriteFile("/tmp/incident_log.txt", "Security incident detected");
if (result === 0) {
    Info("Incident log written successfully");
} else {
    Error("Failed to write log: " + Errno());
}
```

### `Stat(path)`

Gets file information and statistics.

**Parameters:**

* `path` (string, required): Path to the file or directory

**Returns:**

* `object`: File information object with properties: `size`, `mode`, `modTime`, `isDir`
* `null`: On error (use `Errno()` for details)

**Example:**

```javascript
let fileInfo = Stat("/etc/passwd");
if (fileInfo) {
    Info("File size: " + fileInfo.size + " bytes");
    Info("Modified: " + fileInfo.modTime);
    Info("Is directory: " + fileInfo.isDir);
    Info("Permissions: " + fileInfo.mode);
} else {
    Error("Failed to stat file: " + Errno());
}
```

## <mark style="color:yellow;">Temporary Directory Functions</mark>

### `CreateTempDir(pattern)`

Creates a temporary directory.

**Parameters:**

* `pattern` (string, required): Directory name pattern (must end with `*` for random suffix)

**Returns:**

* `string`: Path to created directory on success
* `""` (empty string): On error (use `Errno()` for details)

**Security:** Only allows creation within `/tmp` directory for security.

**Example:**

```javascript
let tmpDir = CreateTempDir("incident-*");
if (tmpDir !== "") {
    Info("Created temporary directory: " + tmpDir);

    // Use the directory for forensic evidence
    let evidenceFile = tmpDir + "/evidence.json";
    WriteFile(evidenceFile, JSON.stringify(data, null, 2));
} else {
    Error("Failed to create temp directory: " + Errno());
}
```

### `RemoveDir(path)`

Removes a directory and its contents.

**Parameters:**

* `path` (string, required): Path to the directory to remove

**Returns:**

* `0`: Success
* Error code: On failure (use `Errno()` for details)

**Security:** Only allows removal of safe subdirectories within `/tmp` for security.

**Example:**

```javascript
let result = RemoveDir("/tmp/old-incident-data");
if (result === 0) {
    Info("Directory removed successfully");
} else {
    Error("Failed to remove directory: " + Errno());
}
```

## <mark style="color:yellow;">Data Store Functions</mark>

The data store provides persistent key-value storage that survives across reaction executions. Each reaction has its own namespace based on the reaction name.

### `DataSet(key, value)`

Stores a key-value pair in the persistent data store.

**Parameters:**

* `key` (string, required): The key to store
* `value` (string, required): The value to store

**Returns:**

* `0`: Success
* Error code: On failure

**Example:**

```javascript
let result = DataSet("incident_count", "5");
if (result === 0) {
    Info("Data stored successfully");
}
```

### `DataGet(key)`

Retrieves a value from the persistent data store.

**Parameters:**

* `key` (string, required): The key to retrieve

**Returns:**

* `string`: The stored value, or `""` if key not found

**Example:**

```javascript
let count = DataGet("incident_count");
if (count !== "") {
    Info("Current incident count: " + count);
} else {
    Info("No incident count found");
}
```

### `DataDelete(key)`

Removes a key-value pair from the data store.

**Parameters:**

* `key` (string, required): The key to delete

**Returns:**

* `0`: Success

**Example:**

```javascript
DataDelete("temporary_data");
Info("Temporary data cleared");
```

### `DataPush(key, value)`

Adds a value to a list stored under the given key.

**Parameters:**

* `key` (string, required): The key for the list
* `value` (string, required): The value to add to the list

**Returns:**

* `0`: Success
* Error code: On failure

**Example:**

```javascript
DataPush("blocked_ips", "192.168.1.100");
DataPush("blocked_ips", "10.0.0.50");
Info("Added IPs to blocked list");
```

### `DataPop(key)`

Removes and returns the last value from a list.

**Parameters:**

* `key` (string, required): The key for the list

**Returns:**

* `string`: The popped value, or `""` if list is empty

**Example:**

```javascript
let lastIp = DataPop("blocked_ips");
if (lastIp !== "") {
    Info("Removed IP from list: " + lastIp);
}
```

### `DataKeys()`

Returns all keys in the data store for this reaction.

**Parameters:** None

**Returns:**

* `string`: JSON array of all keys as a string

**Example:**

```javascript
let keysJson = DataKeys();
if (keysJson !== "") {
    let keys = JSON.parse(keysJson);
    Info("Available keys: " + keys.join(", "));
}
```

### `DataValues()`

Returns all values in the data store for this reaction.

**Parameters:** None

**Returns:**

* `string`: JSON array of all values as a string

**Example:**

```javascript
let valuesJson = DataValues();
if (valuesJson !== "") {
    let values = JSON.parse(valuesJson);
    Info("Stored values: " + values.join(", "));
}
```

### `DataClear()`

Removes all key-value pairs for this reaction from the data store.

**Parameters:** None

**Returns:**

* `0`: Success

**Example:**

```javascript
DataClear();
Info("All reaction data cleared");
```

### `DataSize()`

Returns the number of key-value pairs in the data store for this reaction.

**Parameters:** None

**Returns:**

* `number`: The number of stored key-value pairs

**Example:**

```javascript
let size = DataSize();
Info("Data store contains " + size + " items");
```

### `DataIsEmpty()`

Checks if the data store is empty for this reaction.

**Parameters:** None

**Returns:**

* `true`: If the data store is empty
* `false`: If the data store contains data

**Example:**

```javascript
if (DataIsEmpty()) {
    Info("Data store is empty");
} else {
    Info("Data store contains data");
}
```

### `DataHasKey(key)`

Checks if a specific key exists in the data store.

**Parameters:**

* `key` (string, required): The key to check

**Returns:**

* `true`: If the key exists
* `false`: If the key does not exist

**Example:**

```javascript
if (DataHasKey("incident_count")) {
    Info("Incident count is tracked");
} else {
    DataSet("incident_count", "0");
}
```

### `DataHasValue(value)`

Checks if a specific value exists in the data store.

**Parameters:**

* `value` (string, required): The value to check

**Returns:**

* `true`: If the value exists
* `false`: If the value does not exist

**Example:**

```javascript
if (DataHasValue("high_priority")) {
    Info("High priority incident detected");
}
```

## <mark style="color:yellow;">Emergency System Functions</mark>

{% hint style="danger" %}
**These functions perform system-level operations and should be used with extreme caution. They are intended for emergency security situations only.**
{% endhint %}

### `PowerOff()`

Initiates an immediate system shutdown.

**Parameters:** None

**Returns:**

* `0`: Success (shutdown initiated)
* Error code: On failure

**Example:**

```javascript
// Only use in extreme situations
if (data.process.cmd.includes("rm -rf /")) {
    Warn("DESTRUCTIVE COMMAND DETECTED - EMERGENCY SHUTDOWN");
    PowerOff();
}
```

### `Panic()`

Triggers a kernel panic to immediately halt the system.

**Parameters:** None

**Returns:**

* `0`: Success (panic triggered)
* Error code: On failure

**Example:**

```javascript
// Extreme emergency measure only
if (rootkitDetected) {
    Error("ROOTKIT DETECTED - TRIGGERING KERNEL PANIC");
    Panic();
}
```

## <mark style="color:yellow;">Error Handling</mark>

### `Errno()`

Returns detailed error information for the last failed operation.

**Parameters:** None

**Returns:**

* `string`: Error message describing the last error, or `""` if no error

**Example:**

```javascript
let result = NetBlockIp("invalid-ip");
if (result === -1) {
    let errorMsg = Errno();
    Error("Network blocking failed: " + errorMsg);
}
```

## <mark style="color:yellow;">Common Usage Patterns</mark>

### Error Checking Pattern

```javascript
function process(data) {
    let result = SomeFunction();
    if (result === 0) {
        Info("Operation successful");
    } else if (result === 1) {
        Info("Operation had no effect (already done)");
    } else {
        Error("Operation failed: " + Errno());
        return; // Exit reaction on error
    }
}
```

### Data Store Tracking Pattern

```javascript
function process(data) {
    // Increment counter
    let count = parseInt(DataGet("incident_count") || "0") + 1;
    DataSet("incident_count", String(count));
    DataSet("last_incident", new Date().toISOString());

    Info("Incident #" + count + " processed");
}
```

### Network Flow Processing Pattern

```javascript
function process(data) {
    // Extract IPs from network flows
    let ips = [];
    if (data?.background?.flows?.protocols) {
        for (let protocol of data.background.flows.protocols) {
            if (protocol?.pairs) {
                for (let pair of protocol.pairs) {
                    if (pair?.nodes?.remote?.address) {
                        ips.push(pair.nodes.remote.address);
                    }
                }
            }
        }
    }

    // Process each IP
    for (let ip of ips) {
        Info("Processing IP: " + ip);
        NetBlockIp(ip);
    }
}
```

### Forensic Evidence Collection Pattern

```javascript
function process(data) {
    let forensicDir = CreateTempDir("evidence-*");
    if (forensicDir !== "") {
        let evidence = {
            timestamp: new Date().toISOString(),
            event_uuid: uuid,
            process: data.process,
            file: data.file,
            ancestry: data.base?.background?.ancestry
        };

        let evidenceFile = forensicDir + "/evidence.json";
        if (WriteFile(evidenceFile, JSON.stringify(evidence, null, 2)) === 0) {
            Info("Evidence collected: " + evidenceFile);
        }
    }
}
```
