---
icon: square-terminal
---

# Command Line

<figure><img src="../../.gitbook/assets/utilities-terminal.png" alt="" width="99"><figcaption></figcaption></figure>

> Check out Jibril's public recipes repository at [https://github.com/garnet-org/jibril-balag](https://github.com/garnet-org/jibril-balag).

## <mark style="color:yellow;">Obtain Jibril binaries</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

```sh
$ sudo curl -L -o /usr/bin/jibril https://rb.gy/b0x3wv

$ sudo chmod +x /usr/bin/jibril

$ /usr/bin/jibril --version
```

## <mark style="color:yellow;">Run Jibril using command line</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

All [configuration flags ](configuration-file/)can be given to Jibril through command line. Example:

```sh
$ sudo -E jibril \
        --log-level info \
        --extension example \
        --plugin example:helloworld \
        --extension config \
        --extension data \
        --extension jibril \
        --plugin jibril:hold \
        --printer jibril:printers:stdout \
        --printer jibril:printers:varlog
```

> This command does not show practical results, it is meant to show how Jibril can be executed. It runs the loader (binary named jibril), enables the _example_, _config_, _data_ and _jibril_ extensions, the _helloworld_ plugin from the _example_ extension, the _hold_ plugin from the _jibril_ extension, and the _datakeeper_ and _varlog_ printers from the _jibril_ extension.

{% hint style="info" %}
Find more information about [components](../components/).
{% endhint %}

## <mark style="color:yellow;">Select specific components</mark> <a href="#pick-a-plugin-and-an-event" id="pick-a-plugin-and-an-event"></a>

Jibril footprint can be minimized based on the amount of enabled components. Example:

```sh
$ sudo -E jibril \
        --log-level info \
        --extension config \
        --extension data \
        --extension jibril \
        --plugin jibril:detect \
        --event jibril:detect:net_sniff_tool_exec \
        --printer jibril:printers:stdout
```

Jibril will detect the execution of network sniffers and print the events to the stdout.

> This command runs the _loader_ (binary named _jibril_), enables the _config_, _data_ and _jibril_ extensions, the _detect_ plugin from the _jibril_ extension, the _net\_sniff\_tool\_exec_ event from the _detect_ plugin, and the _stdout_ printer from the _jibril_ extension.
