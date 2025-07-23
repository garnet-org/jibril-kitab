---
icon: plug
---

# Plugins

## <mark style="color:yellow;">Jibril Extension Plugins</mark> <a href="#jibril" id="jibril"></a>

<table data-header-hidden><thead><tr><th width="157.56640625">Plugin</th><th>Description</th></tr></thead><tbody><tr><td>hold</td><td><ul><li>Holds the execution until <code>ctrl+c</code> or <code>SIGTERM</code> is received.</li><li>Used for detection recipes needing continuous monitoring.</li></ul></td></tr><tr><td>procfs</td><td><ul><li>Reads <code>/proc</code> files during startup for existing processes.</li><li>Populates eBPF maps with existing data.</li></ul></td></tr><tr><td>printers</td><td><ul><li>Implements different end points (printers).</li><li>Simplest printer is <strong>stdout</strong>, which prints to the standard output.</li><li>The <strong>varlog</strong> printer logs output to <code>/var/log/{loader,jibril}.log</code>.</li></ul></td></tr><tr><td>netpolicy</td><td><ul><li>Enforces network policies based on CIDRs and domain names.</li></ul><ul><li>Able to drop DNS resolutions synchronously.</li></ul></td></tr><tr><td>detect</td><td><ul><li>Tracks every task and file and the actions performed on them.</li><li>Correlates tasks and files with other <a href="about:blank/overview/theory/#comprehensive-resource-tracking">resources</a>.</li><li>Provides the common ground for detection recipes.</li></ul></td></tr><tr><td>jbconfig &#x26;<br>pause</td><td><ul><li><p>Provides extra process information on detection events, such as:</p><ul><li>Distribution Flavor (including containers).</li><li>Package (of triggerer) name and version.</li><li>File's (binary, libraries) package names and versions.</li><li>and more.</li></ul></li></ul></td></tr><tr><td><a href="attenuator.md">attenuator</a></td><td><ul><li>Either blocks or amend detections for false-positives using AI.</li></ul></td></tr></tbody></table>

