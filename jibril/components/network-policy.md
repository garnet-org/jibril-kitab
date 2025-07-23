---
icon: chart-network
---

# Network Policy

## <mark style="color:yellow;">Jibril Network Policy Plugin</mark>

The **Network Policy Plugin** allows users to define and enforce traffic policies based on CIDRs (IP ranges) and domain resolutions. It supports advanced configurations for alerting, enforcing, and bypassing traffic rules, ensuring flexible network control.

Jibril execution:

```sh
sudo -E jibril --log-level info --extension config --extension data --extension jibril --plugin jibril:hold --printer jibril:printers:stdout
```

Enable the `Network Policy Plugin`:

```sh
--plugin jibril:netpolicy:file=/path/to/policy.yaml
```

Enable the alert events:

```sh
... --event jibril:netpolicy:dropip --event jibril:netpolicy:dropdomain
```

in case `alert` or `both` modes are enabled.

## <mark style="color:yellow;">Configuration Example</mark> <a href="#configuration-example" id="configuration-example"></a>

```yaml
#
# Alert and deny all traffic by default, allowing only declared domains to be resolved.
#
network_policy:
  #
  # The CIDR mode and policy define the IP address policy. Users can choose to block,
  # alert, enforce, or bypass traffic based on CIDR rules.
  #
  # * "cidr_mode":
  #
  # - "bypass": Allow all traffic.
  # - "alert": Alert on denied traffic to CIDRs or domains.
  # - "enforce": Block denied traffic to CIDRs or domains.
  # - "both": Alert and block denied traffic to CIDRs or domains.
  #
  # * "cidr_policy":
  #
  # - "allow": Allow traffic to CIDRs or domains by default.
  # - "deny": Block traffic to CIDRs or domains by default.
  #
  # As an example, the user might have a default "cidr_policy" set to "deny" and allow all
  # IPs with "cidr" set to "0.0.0.0/0". Then, the user might block an IP with a higher
  # prefix length, such as "9.9.9.9/32".
  #
  cidr_mode: "both"
  cidr_policy: "allow"
  #
  # The RESOLVE mode and policy define the domain resolution policy. Users can block
  # specific domains from being resolved or allow them with alerts.
  #
  # For example, if "resolve_mode" is set to "bypass" but a domain is declared as denied,
  # the resolution will be allowed, but the resolved IPs will be blocked.
  #
  # When "resolve_mode" is enabled (alert, enforce, or both), "resolve_policy" determines
  # whether the resolution should be allowed or denied by default.
  #
  # 1. To be alerted on denied domain resolutions, set "resolve_mode" to "alert" and
  #    "resolve_policy" to "deny". You may still block IPs resolved from specific domains.
  #
  # 2. To block the resolution of denied domains, set "resolve_mode" to "enforce"
  #    and "resolve_policy" to "deny". Be aware that if "mode" is set to "bypass", the
  #    resolution will be disallwed, but direct IP connections to the domain will
  #    still be allowed.
  #
  # * "resolve_mode":
  #
  # - "bypass": Allow all domains to be resolved.
  # - "alert": Alert on denied domain resolutions.
  # - "enforce": Block the resolution of denied domains.
  # - "both": Alert and block the resolution of denied domains.
  #
  # * "resolve_policy":
  #
  # - "allow": Allow domain resolution by default.
  # - "deny": Block domain resolution by default.
  #
  # NOTE: domain rules exist independently of "resolve_mode". If a domain is declared
  #       as "deny", its resolved IPs won't be reachable, regardless of "resolve_mode",
  #       which only controls the resolution process.
  #
  resolve_mode: "bypass"
  resolve_policy: "allow"
  #
  rules:
    # Whitelist Everything (test only).
    # - cidr: "0.0.0.0/0"
    #   policy: "allow"
    # Whitelisted CIDRs (localhost).
    - cidr: "127.0.0.0/8"
      policy: "allow"
    - cidr: "::1/128"
      policy: "allow"
    # Whitelisted CIDRs (internal networks).
    - cidr: "192.168.0.0/16"
      policy: "allow"
    - cidr: "172.16.0.0/16"
      policy: "allow"
    - cidr: "10.0.0.0/8"
      policy: "allow"
    - cidr: "10.0.0.1/32"
      policy: "allow"
    # Whitelisted CIDRs (nameservers).
    - cidr: "8.8.8.8/32"
      policy: "allow"
    - cidr: "8.8.4.4/32"
      policy: "allow"
    - cidr: "1.1.1.1/32"
      policy: "allow"
    - cidr: "9.9.9.9/32"
      policy: "allow"
    # Whitelisted Domains.
    - domain: "org"
      policy: "allow"
    - domain: "google.com"
      policy: "allow"
    # Blacklisted Domains.
    - domain: "example.com"
      policy: "deny"
    - domain: "uol.com.br"
      policy: "deny"
```

## <mark style="color:yellow;">Configuration Overview</mark> <a href="#configuration-overview" id="configuration-overview"></a>

<table><thead><tr><th width="183.47265625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong><code>cidr_mode</code></strong></td><td>Defines the mode for handling traffic based on CIDRs.<br>Possible values: <code>bypass</code>, <code>alert</code>, <code>enforce</code>, <code>both</code>.</td></tr><tr><td><strong><code>cidr_policy</code></strong></td><td>Determines the default policy for CIDRs.<br>Possible values: <code>allow</code>, <code>deny</code>.</td></tr><tr><td><strong><code>resolve_mode</code></strong></td><td>Defines the mode for handling domain resolutions.<br>Possible values: <code>bypass</code>, <code>alert</code>, <code>enforce</code>, <code>both</code>.</td></tr><tr><td><strong><code>resolve_policy</code></strong></td><td>Determines the default policy for domain resolutions.<br>Possible values: <code>allow</code>, <code>deny</code>.</td></tr><tr><td><strong><code>rules</code></strong></td><td>List of custom rules for specific CIDRs or domains.</td></tr></tbody></table>

***

## <mark style="color:yellow;">Modes and Policies</mark> <a href="#modes-and-policies" id="modes-and-policies"></a>

### CIDR Modes <a href="#cidr-modes" id="cidr-modes"></a>

<table><thead><tr><th width="187.390625">Mode</th><th>Description</th></tr></thead><tbody><tr><td><code>bypass</code></td><td>Allow all traffic to and from the specified CIDRs.</td></tr><tr><td><code>alert</code></td><td>Alert when traffic violates CIDR rules but does not block it.</td></tr><tr><td><code>enforce</code></td><td>Block traffic that violates CIDR rules.</td></tr><tr><td><code>both</code></td><td>Both alert and block traffic that violates CIDR rules.</td></tr></tbody></table>

### CIDR Policy <a href="#cidr-policy" id="cidr-policy"></a>

<table><thead><tr><th width="189.0234375">Policy</th><th>Description</th></tr></thead><tbody><tr><td><code>allow</code></td><td>Allow traffic to CIDRs by default.</td></tr><tr><td><code>deny</code></td><td>Block traffic to CIDRs by default.</td></tr></tbody></table>

### Resolve Modes <a href="#resolve-modes" id="resolve-modes"></a>

<table><thead><tr><th width="190.18359375">Mode</th><th>Description</th></tr></thead><tbody><tr><td><code>bypass</code></td><td>Allow all domain resolutions.</td></tr><tr><td><code>alert</code></td><td>Alert when domain resolution violates rules but does not block it.</td></tr><tr><td><code>enforce</code></td><td>Block domain resolutions that violate rules.</td></tr><tr><td><code>both</code></td><td>Both alert and block domain resolutions that violate rules.</td></tr></tbody></table>

### Resolve Policy <a href="#resolve-policy" id="resolve-policy"></a>

<table><thead><tr><th width="192.05078125">Policy</th><th>Description</th></tr></thead><tbody><tr><td><code>allow</code></td><td>Allow domain resolutions by default.</td></tr><tr><td><code>deny</code></td><td>Block domain resolutions by default.</td></tr></tbody></table>

## <mark style="color:yellow;">Rule Details</mark> <a href="#rule-details" id="rule-details"></a>

### CIDR Rules <a href="#cidr-rules" id="cidr-rules"></a>

<table><thead><tr><th width="196.23828125">CIDR</th><th width="135.4140625">Policy</th><th>Description</th></tr></thead><tbody><tr><td><code>127.0.0.0/8</code></td><td><code>allow</code></td><td>Allow all traffic to localhost.</td></tr><tr><td><code>::1/128</code></td><td><code>allow</code></td><td>Allow IPv6 localhost traffic.</td></tr><tr><td><code>192.168.0.0/16</code></td><td><code>allow</code></td><td>Allow traffic within the internal network.</td></tr><tr><td><code>172.16.0.0/16</code></td><td><code>allow</code></td><td>Allow traffic within the internal network.</td></tr><tr><td><code>10.0.0.0/8</code></td><td><code>allow</code></td><td>Allow traffic within the internal network.</td></tr><tr><td><code>8.8.8.8/32</code></td><td><code>allow</code></td><td>Allow traffic to Google Public DNS.</td></tr><tr><td><code>8.8.4.4/32</code></td><td><code>allow</code></td><td>Allow traffic to Google Public DNS.</td></tr><tr><td><code>1.1.1.1/32</code></td><td><code>allow</code></td><td>Allow traffic to Cloudflare DNS.</td></tr><tr><td><code>9.9.9.9/32</code></td><td><code>allow</code></td><td>Allow traffic to Quad9 DNS.</td></tr></tbody></table>

### Domain Rules <a href="#domain-rules" id="domain-rules"></a>

<table><thead><tr><th width="200.6171875">Domain</th><th width="131.44921875">Policy</th><th>Description</th></tr></thead><tbody><tr><td><code>org</code></td><td><code>allow</code></td><td>Allow resolution of all <code>.org</code> domains.</td></tr><tr><td><code>google.com</code></td><td><code>allow</code></td><td>Allow resolution of <code>google.com</code>.</td></tr><tr><td><code>example.com</code></td><td><code>deny</code></td><td>Block resolution of <code>example.com</code>.</td></tr><tr><td><code>uol.com.br</code></td><td><code>deny</code></td><td>Block resolution of <code>uol.com.br</code>.</td></tr></tbody></table>

## <mark style="color:yellow;">Key Features</mark> <a href="#key-features" id="key-features"></a>

* **Alert and Enforce Modes**\
  Flexibly alert or block traffic and domain resolutions based on custom rules.
* **Granular Rule Definition**\
  Define specific CIDRs or domains to allow or deny traffic.
* **Default Policy Configuration**\
  Set default allow or deny policies for both CIDRs and domains.
* **Independent Rules**\
  Domain resolution rules operate independently of CIDR traffic rules for fine-grained control.
* **Testing Support**\
  Easily configure test rules, such as whitelisting all traffic, for development and debugging purposes.

{% hint style="warning" %}
Ensure that CIDR and domain rules are carefully planned to avoid unintended blockings.
{% endhint %}
