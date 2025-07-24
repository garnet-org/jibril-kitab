---
description: A Powerful Dynamic Recipe Generation System for Jibril
icon: eye
---

# Overview

The **Alchemies** feature introduces a powerful dynamic recipe generation system for Jibril that allows users to define detection rules in YAML format instead of only relying in the built-in hardcoded recipes.

> Check out Jibril's public recipes repository at [https://github.com/garnet-org/jibril-wahy](https://github.com/garnet-org/jibril-wahy).

## <mark style="color:yellow;">Key Features</mark>

* **YAML-based recipe definitions**: Define detection rules in human-readable YAML format
* **Dynamic loading**: Recipes can be loaded from YAML files at runtime.
* **Hot reload**: Monitor external recipe directories for changes (add/modify/remove).
* **Built-in recipes**: Pre-configured detection recipes shipped with Jibril.
* **Validation**: Comprehensive validation of recipe configurations.
* **Multiple recipe types**: Support for file access, execution, and network peer detections.

## <mark style="color:yellow;">Architecture</mark>

The alchemies system consists of several key components:

1. **Alchemy**: The YAML representation of a detection recipe
2. **Recipe**: The runtime detection rule generated from an alchemy
3. **Monitor**: Watches external directories for YAML file changes
4. **Recipes**: Handles built-in recipe loading from embedded files
5. **Validation**: Ensures recipe configurations are correct

## <mark style="color:yellow;">Monitoring and Hot Reload</mark>

When using external recipe directories with the `path` option, the alchemies system automatically:

1. Monitors the directory for changes
2. Loads new YAML files when added
3. Reloads modified files
4. Removes recipes when files are deleted
5. Validates all changes before applying

## <mark style="color:yellow;">Best Practices</mark>

1. **Use descriptive names**: Recipe `kind` and `name` should clearly indicate what they detect
2. **Set appropriate limits**: Use `times` entries to reduce false positives
3. **Test thoroughly**: Start with `enabled: false` and test before enabling
4. **Document well**: Include links to documentation explaining the detection logic
5. **Version control**: Track recipe files in git for change management
6. **Organize by type**: Group similar recipes in subdirectories

## <mark style="color:yellow;">Common Issues</mark>

1. **Recipe not loading**:
   * Check YAML syntax
   * Verify all required fields are present
   * Look for validation errors in logs
2. **Too many alerts**:
   * Adjust `times` limits
   * Add `arbitrary` filters
   * Use more specific patterns
3. **Missing detections**:
   * Verify `enabled: true`
   * Check file/network patterns match
   * Ensure correct `file_actions` are specified

## <mark style="color:yellow;">Debug Tips</mark>

* Set `log-level: debug` in `config.yaml`
* Check logs for `activating` and `deactivating` messages
* Validation errors will appear as `ignoring errored recipe`
