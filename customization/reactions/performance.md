---
icon: chart-waterfall
---

# Performance

## <mark style="color:yellow;">Performance Considerations</mark>

* **Parallel Execution**: Multiple reactions run concurrently for optimal performance
* **V8 Compilation**: JavaScript reactions are pre-compiled for fast execution
* **Context Isolation**: Each reaction runs in its own isolated environment
* **Memory Management**: Automatic cleanup of reaction contexts
* **Resource Limits**: Built-in safeguards prevent resource exhaustion

## <mark style="color:yellow;">**Best Practices for Performance**</mark>

1. **Keep reactions lightweight** - Avoid complex computations
2. **Use the data store efficiently** - Don't store large objects
3. **Minimize file I/O** - Only write essential data
4. **Handle errors gracefully** - Don't let failed reactions impact others
5. **Test thoroughly** - Validate reactions before production deployment

## <mark style="color:yellow;">**Example: Optimized Reaction**</mark>

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

> In a detection system, distinguishing between what belongs in the reaction phase and what should be part of the detection logic is crucial. Think of reactions as an extension of Jibril: they encompass scripts that collect, analyze, interpret, and act on data—similar to the Jibril detection mechanism.

> **Key Points**
>
> * **Jibril Detection Mechanism**\
>   Optimized for enhanced results, efficient caching, and additional functionalities.
> * **Reaction Logic**\
>   Should focus on responding to events, without being responsible for filtering or decision-making, which is handled by `arbitraries` or specific detection features.

{% hint style="warning" %}
Remember: Jibril detection mechanisms are faster and optimized. This makes the use of reactions logic, such as showed above, targeted to fine-grained business logic (and not to replace it).
{% endhint %}
