---
description: Adjust Jibril Pattern Analysis Cadence as Needed
icon: stopwatch-20
---

# Cadence Configuration

## <mark style="color:yellow;">What is Cadence?</mark>

In Jibril, **cadence** refers to the evaluation intervals that determine how frequently the system analyzes behavioral patterns for potential security threats. These intervals control the timing of pattern detection checks, not the detection accuracy itself.

## <mark style="color:yellow;">Core Concept</mark>

Think of cadences as the "heartbeat" of your security monitoring:

* Each cadence type represents a different monitoring category
* The interval value determines how often that category is evaluated
* All behavioral data collected between intervals is analyzed during each evaluation

## <mark style="color:yellow;">How Cadences Work</mark>

#### Continuous Collection vs. Periodic Evaluation

1. **Data Collection**: Jibril **continuously** monitors and caches behavioral data
2. **Pattern Evaluation**: Analysis occurs at **cadence intervals**
3. **Detection Events**: Generated when patterns match during evaluation

```
Timeline Example (9-second cadence):
0s -------- 9s -------- 18s -------- 27s -------- 36s
|           |           |            |            |
Collection  Eval #1     Eval #2      Eval #3      Eval #4
(continuous)
```

## <mark style="color:yellow;">Cadence Types</mark>

### 1. File Access Cadence (`file_access`)

Controls evaluation of file system behavioral patterns:

* File creation, modification, deletion patterns
* Suspicious file access sequences
* Unauthorized access attempts
* File permission changes

### 2. Network Peers Cadence (`network_peers`)

Controls evaluation of network endpoint patterns:

* Connection to suspicious domains
* Communication with known threat actors
* Unusual peer communication patterns
* DNS resolution anomalies

### 3. Network Flows Cadence (`network_flows`)

Controls evaluation of network flow patterns:

* Abnormal traffic volumes
* Unusual protocol usage
* Data exfiltration patterns
* Command and control communications

## <mark style="color:yellow;">Configuration Syntax</mark>

```yaml
cadences:
  file_access: 9      # Interval in seconds
  network_peers: 9    # Interval in seconds
  network_flows: 9    # Interval in seconds
```

## <mark style="color:yellow;">Performance Impact</mark>

### CPU Usage Patterns

The relationship between cadence intervals and CPU usage:

```
Interval | CPU Impact | Evaluation Frequency
---------|------------|--------------------
1s       | Very High  | 60 evals/minute
5s       | High       | 12 evals/minute
9s       | Moderate   | ~7 evals/minute
30s      | Low        | 2 evals/minute
60s      | Very Low   | 1 eval/minute
```

### Memory Considerations

Shorter cadences may require larger caches because:

* Less time to process cached data before new data arrives
* Risk of cache overflow if processing takes too long
* Need to maintain more granular behavioral state

## <mark style="color:yellow;">Choosing Cadence Values</mark>

### Factors to Consider

1. **Environment Activity Level**
   * High-traffic systems: Consider longer intervals
   * Critical systems: Use shorter intervals for faster detection
2. **Threat Model**
   * Advanced persistent threats: Shorter intervals
   * General monitoring: Standard intervals sufficient
3. **System Resources**
   * Limited CPU: Increase intervals
   * Ample resources: Decrease for better responsiveness
4. **Detection Requirements**
   * Real-time needs: 1-5 second intervals
   * Near real-time: 5-15 second intervals
   * Delayed acceptable: 15-60 second intervals

### Common Configurations

#### **Default Configuration (Balanced)**

```yaml
cadences:
  file_access: 9
  network_peers: 9
  network_flows: 9
```

#### **High-Security Configuration**

```yaml
cadences:
  file_access: 3
  network_peers: 5
  network_flows: 5
```

#### **Resource-Conscious Configuration**

```yaml
cadences:
  file_access: 30
  network_peers: 30
  network_flows: 15
```

#### **Mixed Priority Configuration**

```yaml
cadences:
  file_access: 5      # High priority on file monitoring
  network_peers: 30   # Lower priority on peer analysis
  network_flows: 15   # Medium priority on flow analysis
```

## <mark style="color:yellow;">Important Notes</mark>

### Cadence vs. Detection Accuracy

Cadences DO NOT affect:

* What patterns are detected
* The accuracy of pattern matching
* The types of threats identified

**Cadences DO affect:**

* How quickly threats are identified after occurring
* CPU usage patterns
* System responsiveness

#### Behavioral State Persistence

* Behavioral data is **not lost** between evaluations
* All activity is cached and available for analysis
* Longer intervals mean more data to process per evaluation

## <mark style="color:yellow;">Best Practices</mark>

1. **Start Conservative**: Begin with default 9-second intervals
2. **Monitor System Impact**: Use system metrics to guide adjustments
3. **Test Incrementally**: Change one cadence at a time
4. **Consider Peak Hours**: Account for system load variations
5. **Document Changes**: Track configuration changes and their effects

## <mark style="color:yellow;">Troubleshooting</mark>

### High CPU Usage

* Increase cadence intervals
* Check for excessive behavioral activity
* Verify cache sizes are appropriate

### Delayed Detection

* Decrease cadence intervals
* Ensure caches aren't overflowing
* Check system resource availability

### Missed Events

* Usually NOT a cadence issue
* Check cache configuration
* Verify detection rules are enabled

## <mark style="color:yellow;">Advanced Tuning</mark>

### Dynamic Cadence Adjustment

While not built-in, you can implement time-based cadence changes:

```yaml
# Peak hours configuration (via external scheduler)
cadences:
  file_access: 5      # More frequent during business hours

# Off-hours configuration
cadences:
  file_access: 30     # Less frequent overnight
```

### Cadence Synchronization

Consider staggering cadences to distribute CPU load:

```yaml
cadences:
  file_access: 9      # Evaluates at 0, 9, 18, 27...
  network_peers: 10   # Evaluates at 0, 10, 20, 30...
  network_flows: 11   # Evaluates at 0, 11, 22, 33...
```

## <mark style="color:yellow;">Summary</mark>

Cadences are the timing mechanism that controls when Jibril evaluates collected behavioral data for security threats. Proper cadence configuration balances detection responsiveness with system resource usage. Remember: faster isn't always better—choose intervals that match your security requirements and system capabilities.
