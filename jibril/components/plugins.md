---
icon: plug
---

# Plugins

## <mark style="color:yellow;">Jibril Extension Plugins</mark> <a href="#jibril" id="jibril"></a>

<table data-header-hidden><thead><tr><th width="157.56640625">Plugin</th><th>Description</th></tr></thead><tbody><tr><td><strong>Hold</strong></td><td>- Holds the execution until <code>ctrl+c</code> or <code>SIGTERM</code> is received.<br>- Used for detection recipes needing continuous monitoring.</td></tr><tr><td><strong>Procfs</strong></td><td>- Reads <code>/proc</code> files during startup for existing processes.<br>- Populates eBPF maps with existing data.</td></tr><tr><td><strong>Printers</strong></td><td>- Implements different end points (printers).<br>- Simplest printer is <strong>stdout</strong>, which prints to the standard output.<br>- The <strong>varlog</strong> printer logs output to <code>/var/log/{loader,jibril}.log</code>.</td></tr><tr><td>NetPolicy</td><td>- Enforces network policies based on CIDRs and domain names.<br>- Able to drop DNS resolutions synchronously.</td></tr><tr><td><strong>Detect</strong></td><td>- Tracks every task and file and the actions performed on them.<br>- Correlates tasks and files with other <a href="about:blank/overview/theory/#comprehensive-resource-tracking">resources</a>.<br>- Provides the common ground for detection recipes.</td></tr></tbody></table>
