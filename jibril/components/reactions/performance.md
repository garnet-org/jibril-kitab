---
icon: chart-waterfall
---

# Performance

## <mark style="color:yellow;">Performance Considerations</mark>

### **Reaction Execution**

* **Parallel Execution**: Multiple reactions for the same recipe run concurrently
* **V8 Compilation**: JavaScript reactions are pre-compiled for fast execution
* **Context Isolation**: Each reaction runs in its own isolated environment
* **Resource Management**: Automatic cleanup prevents memory leaks

### **Best Practices for Performance**

1. **Keep reactions lightweight** - Avoid complex computations
2. **Use the data store efficiently** - Don't store large objects
3. **Minimize file I/O** - Only write essential data
4. **Handle errors gracefully** - Don't let failed reactions impact others
5. **Test thoroughly** - Validate reactions before production deployment

### **Example: Optimized Reaction**

```javascript
reactions:
  - format: js
    code: |
      function process(data) {
        // Fast path for common cases
        if (!data.process || !data.process.cmd) {
          return; // Exit early if no process data
        }
        
        // Efficient data access
        let cmd = data.process.cmd;
        let isHighRisk = cmd.includes("wget") || cmd.includes("curl");
        
        if (isHighRisk) {
          // Only log essential information
          Info("High-risk process: " + cmd);
          
          // Use efficient data store operations
          let count = parseInt(DataGet("risk_count") || "0") + 1;
          DataSet("risk_count", String(count));
          
          // Take action only when necessary
          if (count > 5) {
            NetBlockIp();
          }
        }
      }
```

> There is a thin line in between what should go in the reaction and what should be done in the detection recipe (or logic) itself. One can see the reaction as being an extension of Jibril since scripts can collect, analyze and interpret data the same way as Jibril does.

> Remember: Jibril detection mechanisms are faster and optimized. This makes the use of reactions logic, such as showed above, targeted to fine-grained business logic (and not to replace it).
