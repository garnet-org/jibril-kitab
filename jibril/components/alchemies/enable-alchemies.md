---
description: Learn How to Enable Alchemies Plugin
icon: square-check
---

# Enable Alchemies

## <mark style="color:yellow;">Enabling the Alchemies Plugin</mark>

To use the alchemies feature, add it to your [config.yaml](../../installation/configuration-file/) file:

```yaml
plugin:
  # Or enable only built-in recipes (default behavior) only
  - jibril:alchemies

  # Enable the alchemies plugin with external recipe directory and builtin recipes
  - jibril:alchemies:builtin=true:path=/path/to/your/recipes/

  # Disable built-in recipes while using external ones
  - jibril:alchemies:builtin=false:path=/path/to/your/recipes/
```

## <mark style="color:yellow;">Plugin Options</mark>

* **`path`**: Directory path containing custom YAML recipe files.
* **`builtin`**: Enable/disable built-in recipes (default: true).

{% hint style="warning" %}
The directory path must be a valid path to a directory and is not recursive.
{% endhint %}

### Example Configuration

Example of a [config.yaml](../../installation/configuration-file/) file with the alchemies plugin configured:

```yaml
#### Jibril Configuration File

log-level: info
stdout: stdout
stderr: stderr

extension:
  - jibril

plugin:
  # Enable alchemies with custom recipe directory
  - jibril:alchemies:path=/etc/jibril/alchemies/
  - jibril:detect

printer:
  - jibril:printers:stdout

event:
  # Events will be automatically enabled based on recipes
  - jibril:detect:file_example
  - jibril:detect:exec_example
  - jibril:detect:peer_example
```
