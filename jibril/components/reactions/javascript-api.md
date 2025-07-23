---
icon: code
---

# JavaScript API Reference

This document provides a complete reference for all JavaScript helper functions available within reaction code. These functions provide controlled access to system resources and security operations.

## <mark style="color:yellow;">Global Variables</mark>

Every reaction has access to these global variables:

- **`kind`** (string): The type of detection event (e.g., "file_access", "execution", "network_peer")
- **`name`** (string): The name of the detection recipe that triggered this reaction
- **`uuid`** (string): Unique identifier for the specific event instance
- **`data`** (object): Complete JSON object containing all event details and context

## <mark style="color:yellow;">Logging Functions</mark>

### `Info(message)`

Logs an informational message to the Jibril log system.

**Parameters:**

- `message` (string): The message to log

**Returns:** `undefined`

**Example:**

```javascript
Info("Reaction executed successfully");
Info("Processing event: " + data.metadata.name);
```

### `Warn(message)`

Logs a warning message to the Jibril log system.

**Parameters:**

- `message` (string): The warning message to log

**Returns:** `undefined`

**Example:**

```javascript
Warn("Suspicious activity detected in: " + data.file.file);
```

### `Error(message)`

Logs an error message to the Jibril log system.

**Parameters:**

- `message` (string): The error message to log

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

- `ipAddress` (string, optional): Specific IP address to block. If omitted, blocks all remote IPs from the current event context.

**Returns:**

- `0`: Success
- `1`: All IPs were already blocked
- `-1`: Error occurred

**Example:**

```javascript
// Block a specific IP
let result = NetBlockIp("192.168.1.100");
if (result === 0) {
    Info("IP blocked successfully");
}

// Block all remote IPs from the event
let result = NetBlockIp();
if (result === 0) {
    Info("All remote IPs blocked");
}
```

### `NetBlockDomain([domain])`

Blocks network traffic to/from specified domains.

**Parameters:**

- `domain` (string, optional): Specific domain to block. If omitted, blocks all remote domains from the current event context.

**Returns:**

- `0`: Success
- `1`: All domains were already blocked
- `-1`: Error occurred

**Example:**

```javascript
// Block a specific domain
let result = NetBlockDomain("malicious-site.com");

// Block all domains from the event
let result = NetBlockDomain();
```

### `NetUnblockIp(ipAddress)`

Removes an IP address from the block list.

**Parameters:**

- `ipAddress` (string): IP address to unblock

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
let result = NetUnblockIp("192.168.1.100");
if (result === 0) {
    Info("IP unblocked successfully");
}
```

## <mark style="color:yellow;">Process Management Functions</mark>

### `KillCurrent()`

Terminates the current process associated with the security event.

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
let result = KillCurrent();
if (result === 0) {
    Info("Malicious process terminated");
} else {
    Error("Failed to kill process: " + Errno());
}
```

### `KillParent()`

Terminates the parent process of the current process.

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
let result = KillParent();
if (result === 0) {
    Info("Parent process terminated");
}
```

### `KillProcess()`

Kills processes based on the event context and ancestry information.

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
let result = KillProcess();
if (result === 0) {
    Info("Process killed successfully");
}
```

## <mark style="color:yellow;">File System Operations</mark>

### `ReadFile(path)`

Reads the contents of a file.

**Parameters:**

- `path` (string): Absolute path to the file to read

**Returns:**

- File contents as a string on success
- Empty string on error (check `Errno()` for details)

**Example:**

```javascript
let config = ReadFile("/etc/app/config.json");
if (config !== "") {
    Info("Config loaded: " + config.length + " bytes");
} else {
    Error("Failed to read config: " + Errno());
}
```

### `WriteFile(path, data)`

Writes data to a file with secure permissions (0600).

**Parameters:**

- `path` (string): Absolute path where to write the file
- `data` (string): Data to write to the file

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
let evidence = JSON.stringify({
    event: data.uuid,
    timestamp: new Date().toISOString(),
    process: data.process.cmd
});

let result = WriteFile("/var/log/security/incident.json", evidence);
if (result === 0) {
    Info("Evidence logged successfully");
}
```

### `Stat(path)`

Gets file metadata and statistics.

**Parameters:**

- `path` (string): Absolute path to the file

**Returns:**

- Object with file information on success
- `null` on error

**Object Properties:**

- `size` (number): File size in bytes
- `mode` (string): File permissions and type
- `modTime` (string): Last modification time (RFC3339 format)
- `isDir` (boolean): Whether the path is a directory

**Example:**

```javascript
let fileInfo = Stat("/suspicious/file");
if (fileInfo) {
    Info("File size: " + fileInfo.size + " bytes");
    Info("Last modified: " + fileInfo.modTime);
    Info("Is directory: " + fileInfo.isDir);
}
```

## <mark style="color:yellow;">Temporary Directory Management</mark>

### `CreateTempDir([pattern])`

Creates a secure temporary directory in `/tmp` with 0700 permissions.

**Parameters:**

- `pattern` (string, optional): Pattern for the directory name (default: "tmpdir-*")

**Returns:**

- Path to the created directory on success
- Empty string on error

**Example:**

```javascript
let tmpDir = CreateTempDir("security-*");
if (tmpDir !== "") {
    Info("Created temp directory: " + tmpDir);
    
    // Use the directory for forensic data
    WriteFile(tmpDir + "/evidence.json", JSON.stringify(data));
}
```

### `RemoveDir(path)`

Removes a directory and its contents.

**Parameters:**

- `path` (string): Path to the directory to remove

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
let result = RemoveDir("/tmp/cleanup-target");
if (result === 0) {
    Info("Directory removed successfully");
}
```

## <mark style="color:yellow;">Data Store Functions</mark>

The data store provides persistent key-value storage that survives across reaction executions. Each reaction has its own namespace based on the reaction name.

### `DataSet(key, value)`

Stores a key-value pair in the persistent data store.

**Parameters:**

- `key` (string): The key to store
- `value` (string): The value to associate with the key

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
DataSet("incident_count", "5");
DataSet("last_attack_ip", "192.168.1.100");
```

### `DataGet(key)`

Retrieves a value from the data store.

**Parameters:**

- `key` (string): The key to retrieve

**Returns:**

- The stored value as a string on success
- Empty string if key not found (check `Errno()` to distinguish)

**Example:**

```javascript
let count = DataGet("incident_count");
if (count !== "") {
    Info("Current incident count: " + count);
} else if (Errno() === "key not found in data store") {
    Info("No previous incidents recorded");
}
```

### `DataPush(value)`

Pushes a value onto a stack-like structure (LIFO).

**Parameters:**

- `value` (string): Value to push onto the stack

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
DataPush("192.168.1.100");
DataPush("192.168.1.101");
// Stack now contains: ["192.168.1.101", "192.168.1.100"]
```

### `DataPop()`

Pops the most recently pushed value from the stack.

**Returns:**

- The most recent value as a string
- Empty string if stack is empty

**Example:**

```javascript
let ip = DataPop(); // Returns "192.168.1.101"
let nextIp = DataPop(); // Returns "192.168.1.100"
```

### `DataDelete(key)`

Removes a key-value pair from the data store.

**Parameters:**

- `key` (string): The key to delete

**Returns:**

- `0`: Success (even if key didn't exist)

**Example:**

```javascript
DataDelete("old_incident_data");
```

### `DataKeys()`

Returns all keys in the data store for the current reaction.

**Returns:** JSON array string containing all keys

**Example:**

```javascript
let keysJson = DataKeys();
let keys = JSON.parse(keysJson);
for (let i = 0; i < keys.length; i++) {
    Info("Key: " + keys[i]);
}
```

### `DataValues()`

Returns all values in the data store for the current reaction.

**Returns:** JSON array string containing all values

**Example:**

```javascript
let valuesJson = DataValues();
let values = JSON.parse(valuesJson);
for (let i = 0; i < values.length; i++) {
    Info("Value: " + values[i]);
}
```

### `DataClear()`

Removes all data for the current reaction from the data store.

**Returns:**

- `0`: Success

**Example:**

```javascript
DataClear(); // Clean slate
```

### `DataSize()`

Returns the number of key-value pairs stored for the current reaction.

**Returns:** Number of items as integer

**Example:**

```javascript
let size = DataSize();
Info("Data store contains " + size + " items");
```

### `DataIsEmpty()`

Checks if the data store is empty for the current reaction.

**Returns:**

- `true`: Data store is empty
- `false`: Data store contains data

**Example:**

```javascript
if (DataIsEmpty()) {
    Info("No previous data found");
}
```

### `DataHasKey(key)`

Checks if a specific key exists in the data store.

**Parameters:**

- `key` (string): The key to check

**Returns:**

- `true`: Key exists
- `false`: Key does not exist

**Example:**

```javascript
if (DataHasKey("incident_count")) {
    let count = DataGet("incident_count");
    Info("Previous incidents: " + count);
}
```

### `DataHasValue(value)`

Checks if a specific value exists in the data store.

**Parameters:**

- `value` (string): The value to search for

**Returns:**

- `true`: Value exists
- `false`: Value does not exist

**Example:**

```javascript
if (DataHasValue("192.168.1.100")) {
    Info("This IP has been seen before");
}
```

## <mark style="color:yellow;">Emergency System Functions</mark>

{% hint style="danger" %}
**These functions perform system-wide operations and should be used with extreme caution. They are intended for critical security situations where immediate system shutdown is necessary.**
{% endhint %}

### `PowerOff()`

Initiates an immediate system shutdown.

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
// Only use in critical situations
if (data.metadata.importance === "critical") {
    Info("Critical threat detected - initiating shutdown");
    PowerOff();
}
```

### `Panic()`

Triggers a kernel panic for immediate system halt.

**Returns:**

- `0`: Success
- `-1`: Error occurred

**Example:**

```javascript
// Emergency response to severe compromise
if (systemCompromised) {
    Error("System compromise detected - triggering panic");
    Panic();
}
```

## <mark style="color:yellow;">Error Handling</mark>

### `Errno()`

Returns the error message from the last operation that failed.

**Returns:** Error message as a string, or empty string if no error

**Example:**

```javascript
let result = NetBlockIp("invalid-ip");
if (result !== 0) {
    Error("Failed to block IP: " + Errno());
}
```

## <mark style="color:yellow;">Common Error Codes</mark>

- `0`: Success
- `1`: Operation succeeded but had no effect (e.g., IP already blocked)
- `-1`: Generic error occurred
- `-2`: Item not found

## <mark style="color:yellow;">Best Practices</mark>

1. **Always check return values** from functions that can fail
2. **Use `Errno()`** to get detailed error information
3. **Log operations** for audit trails
4. **Validate input data** before using it in operations
5. **Use data store** for maintaining state across reactions
6. **Test reactions thoroughly** before deploying to production

## <mark style="color:yellow;">Example: Complete Reaction</mark>

```javascript
function process(data) {
    Info("Processing " + kind + " event: " + name);
    
    // Check if this is a repeat offender
    let lastSeen = DataGet("last_seen_" + data.process.pid);
    if (lastSeen !== "") {
        Warn("Repeat offender detected: " + data.process.cmd);
        
        // Escalate response
        let result = KillCurrent();
        if (result === 0) {
            Info("Terminated repeat offender");
            DataSet("terminated_count", String(parseInt(DataGet("terminated_count") || "0") + 1));
        }
    } else {
        // First offense - log and monitor
        Info("First offense logged for PID: " + data.process.pid);
        DataSet("last_seen_" + data.process.pid, new Date().toISOString());
        
        // Block associated network traffic
        let blockResult = NetBlockIp();
        if (blockResult === 0) {
            Info("Blocked network traffic from process");
        }
    }
    
    // Log to forensic file
    let evidence = {
        timestamp: new Date().toISOString(),
        event_id: uuid,
        process: data.process.cmd,
        action_taken: lastSeen !== "" ? "terminated" : "monitored"
    };
    
    WriteFile("/var/log/security/reactions.log", JSON.stringify(evidence) + "\n");
}
```
