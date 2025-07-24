---
description: >-
  Enhance Jibril's detection capabilities through AI-powered analysis of
  security events.
icon: filters
---

# The Attenuator

The Attenuator is an advanced and powerful feature of Jibril designed to significantly enhance its security detection capabilities. It leverages cutting-edge AI-powered analysis to meticulously examine and interpret security events, providing an additional layer of safeguard against potential threats.

<figure><img src="../.gitbook/assets/image (31).png" alt="" width="563"><figcaption><p>Detection Event Reasoning</p></figcaption></figure>

> Quickly check how to use this feature at [docker-container.md](../installation/methods/docker-container.md "mention") session.

## <mark style="color:yellow;">Overview</mark>

The Attenuator acts as an intelligent filter that can analyze security events detected by Jibril and provide additional context, severity classifications, and even determine if an event is likely a false positive. This feature leverages AI models (like GPT-4o) to bring expert-level security analysis to each detection.

## <mark style="color:yellow;">How It Works</mark>

When a security event is detected, the Attenuator:

1. Takes the event details and forwards them to an AI service
2. Prompts the AI to perform a security analysis of the event
3. Determines if the event is likely a false positive (with high confidence)
4. Independently assesses the severity of the event
5. Provides a detailed description justifying its analysis

The Attenuator operates in three possible modes:

* **Amend**\
  Adds the AI verdict to the event without blocking it (default). This mode is particularly useful during initial deployment and fine-tuning periods when you're optimizing model parameters, temperature settings, and other configurations.
* **Reason**\
  Adds the AI verdict along with detailed reasoning to the event
* **Block**\
  Filters out events determined to be false positives

{% hint style="warning" %}
You can choose to either amend events with AI analysis or filter them entirely.\
\
During initial deployment, the amend mode is recommended to evaluate the AI's performance before enabling blocking behavior.
{% endhint %}

## <mark style="color:yellow;">Configuration</mark>

You can configure the Attenuator through Jibril's configuration file or environment variables:

### <mark style="color:$primary;">Configuration Options</mark>

<table><thead><tr><th>Description</th><th>Config Option</th><th width="178.89703369140625">Env Variable</th><th>Default Value</th></tr></thead><tbody><tr><td>Feature<br>Flag</td><td><code>enabled</code></td><td>-</td><td><code>false</code></td></tr><tr><td>API token</td><td><code>token</code></td><td><code>AI_TOKEN</code></td><td>-</td></tr><tr><td>AI Model<br>Name</td><td><code>model</code></td><td><code>AI_MODEL</code></td><td><code>gpt-4o</code></td></tr><tr><td>Model Temperature</td><td><code>temperature</code></td><td><code>AI_TEMPERATURE</code></td><td><code>0.3</code></td></tr><tr><td>Operational<br>Mode</td><td><code>mode</code></td><td><code>AI_MODE</code></td><td><code>amend</code></td></tr><tr><td>AI Service<br>URL</td><td><code>url</code></td><td><code>AI_URL</code></td><td>OpenAI API URL</td></tr></tbody></table>

### <mark style="color:$primary;">Example Configuration</mark>

To enable and configure the Attenuator in your Jibril setup, add the following to your configuration:

```yaml
plugin:
  - jibril:hold
  - jibril:procfs
  - jibril:printers
  - jibril:attenuator:enabled=true:mode=reason
  - jibril:detect
  # - jibril:netpolicy:file=/home/rafaeldtinoco/netpolicy.yaml
```

Use the [options above](attenuator.md#configuration-options) with the **attenuator** plugin line at the [configuration file](attenuator.md#example-configuration).

Alternatively, you can set environment variables:

```bash
export AI_TOKEN=your-ai-token
export AI_MODEL=gpt-4o
export AI_TEMPERATURE=0.3
export AI_MODE=reason
```

### <mark style="color:$primary;">Local and Private Models</mark>

<figure><img src="../.gitbook/assets/image (22).png" alt="" width="375"><figcaption></figcaption></figure>

The Attenuator can be used with local inference engines like [Ollama](https://ollama.com/) to run private models on your own infrastructure. This approach offers several advantages:

* Data Privacy: Keeps security event data within your environment
* Cost Efficiency: Eliminates API usage costs
* Customization: Allows fine-tuning of models for security-specific tasks

To use Ollama with the Attenuator, set the URL to your Ollama instance:

```yaml
extensions:
  jibril:
    plugins:
      attenuator:
        enabled: "true"
        url: "http://localhost:11434/v1/chat/completions"
        model: "deepseek-coder:latest"
```

{% hint style="success" %}
For now, jibril recommends the use of [DeepSeek R1 : 14B](https://ollama.com/library/deepseek-r1) model. It shows the best results with shorter inference times.
{% endhint %}

## <mark style="color:yellow;">Response Format</mark>

The Attenuator provides rich context for each security event it analyzes:

```json
{
  "false_positive": false,
  "severity": "high",
  "description": "Detailed explanation of why this event is or isn't a false positive",
  "reasoning": "Additional context and analysis (only in 'reason' mode)"
}
```

## <mark style="color:yellow;">Use Cases</mark>

The Attenuator is particularly useful for:

1. Reducing Alert Fatigue\
   By filtering out false positives (in block mode)
2. Prioritizing Alerts\
   Through accurate severity classification
3. Contextualizing Detections\
   Adding expert analysis to help security teams understand the significance of events
4. CI/CD Environments\
   Automatically filtering security events in automated workflows

## <mark style="color:yellow;">Integration with GitHub Actions</mark>

The Attenuator is automatically enabled in GitHub Actions environments when an API token is provided, making it perfect for security testing in CI/CD pipelines.

## <mark style="color:yellow;">Best Practices</mark>

* Begin with "amend" or "reason" mode to evaluate the AI's judgments before using "block" mode
* Use a higher temperature setting for more diverse analyses
* For production environments, consider using the most advanced AI model available
* When using private models, allocate sufficient resources for inference, especially for real-time security monitoring
