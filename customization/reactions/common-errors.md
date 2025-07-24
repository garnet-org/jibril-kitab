---
description: Learn how to debug and troubleshoot common errors and mistakes.
icon: bomb
---

# Troubleshooting

## <mark style="color:yellow;">**Use Gradual Deployment**</mark>

1. **Test Environment**: Deploy with `enabled: false` first
2. **Limited Scope**: Start with specific file patterns or processes
3. **Monitoring**: Watch logs carefully for unexpected behavior
4. **Gradual Expansion**: Slowly expand scope and enable more reactions
5. **Production**: Only deploy fully tested reactions to production

This configuration guide provides the foundation for creating powerful, secure, and maintainable reactions within the Jibril security system.

## <mark style="color:yellow;">Debugging and Troubleshooting</mark>

### **Logging for Debugging**

Use comprehensive logging to debug reaction issues:

```javascript
reactions:
  - format: js
    code: |
      function process(data) {
        Info("=== REACTION DEBUG START ===");
        Info("Kind: " + kind);
        Info("Name: " + name);
        Info("UUID: " + uuid);

        // Log data structure
        Info("Data keys: " + Object.keys(data).join(", "));

        if (data.process) {
          Info("Process PID: " + data.process.pid);
          Info("Process CMD: " + data.process.cmd);
        }

        // Test helper functions
        let testResult = DataSet("debug_test", "success");
        Info("DataSet test result: " + testResult);

        let retrieved = DataGet("debug_test");
        Info("DataGet test result: " + retrieved);

        Info("=== REACTION DEBUG END ===");
      }
```

### **Error Handling**

Implement proper error handling:

```yaml
reactions:
  - format: js
    code: |
```

```javascript
      function process(data) {
        try {
          // Main reaction logic
          let result = NetBlockIp();
          if (result !== 0) {
            Error("Failed to block IP: " + Errno());
          }

          // File operations with error checking
          let writeResult = WriteFile("/tmp/reaction.log", "test");
          if (writeResult !== 0) {
            Error("Failed to write file: " + Errno());
          }

        } catch (error) {
          Error("Reaction error: " + error.toString());
        }
      }
```

## <mark style="color:yellow;">Testing Reactions</mark>

### **Test Configuration**

Create test reactions with disabled state:

```yaml
- kind: test_reaction
  name: my_test_reaction
  enabled: false  # Start disabled for testing
  version: 1.0
  description: Test reaction for development
  breed: file_access
  mechanism: file_access
  importance: low

  bases:
    - dir: /tmp/test
      base: trigger.txt
  file_actions:
    - unlink

  reactions:
    - format: js
      code: |
        # JavaScript function here
```

```javascript
        function process(data) {
          Info("=== TEST REACTION ===");
          Info("All systems operational");

          // Test all helper functions safely
          DataSet("test", "success");
          let value = DataGet("test");
          Info("Data store test: " + (value === "success" ? "PASS" : "FAIL"));

          DataDelete("test");
          Info("=== TEST COMPLETE ===");
        }
```

## <mark style="color:yellow;">Configuration Validation</mark>

Jibril validates reaction configurations at startup. Common validation errors include:

### **Missing Required Fields**

```javascript
reactions:
  - format: js
    # ERROR: Missing 'code' field
```

**Fix:**

```javascript
reactions:
  - format: js
    code: |
      function process(data) {
        Info("Valid reaction");
      }
```

### **Invalid Format**

```python
reactions:
  - format: python  # ERROR: Invalid format
    code: |
      print("Not supported")
```

**Fix:**

```javascript
reactions:
  - format: js  # Valid: js or shell only
    code: |
      function process(data) {
        Info("Valid format");
      }
```

### **Missing Process Function (JavaScript)**

```javascript
reactions:
  - format: js
    code: |
      # ERROR: Missing process() function
      Info("This won't work");
```

**Fix:**

```javascript
reactions:
  - format: js
    code: |
      function process(data) {
        Info("This will work");
      }
```

### **Network Helper Without netpolicy Plugin**

```javascript
reactions:
  - format: js
    code: |
      function process(data) {
        NetBlockIp(); # ERROR: Requires netpolicy plugin enabled
      }
```
