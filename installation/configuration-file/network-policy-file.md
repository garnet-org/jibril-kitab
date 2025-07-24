---
icon: sliders-up
---

# Network Policy File

## <mark style="color:yellow;">Defaults: /etc/jibril/netpolicy.yaml</mark>

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
    # - domain: "org"
    #   policy: "allow"
    # - domain: "google.com"
    #   policy: "allow"
    # Blacklisted Domains.
    - domain: "aol.com"
      policy: "deny"
    - domain: "uol.com.br"
      policy: "deny"
```

## <mark style="color:yellow;">Run Jibril</mark>

```shell-session
sudo -E ./build/loader --config /etc/jibril/config.yaml
```

making sure that the `config.yaml`file has:

```
- jibril:netpolicy:file=/etc/jibril/netpolicy.yaml
```

configured correctly.
