---
icon: bomb
---

# Common Errors

## <mark style="color:yellow;">Configuration Validation</mark>

Jibril validates reaction configurations at startup. Common validation errors include:

### **Missing Required Fields**

```yaml
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
