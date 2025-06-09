---
icon: list-tree
---

# Systemd Service

<figure><img src="../../../.gitbook/assets/com.github.artemanufrij.graphui.png" alt="" width="99"><figcaption></figcaption></figure>

> Check out Jibril's public recipes repository at [https://github.com/garnet-org/jibril-balag](https://github.com/garnet-org/jibril-balag).

## <mark style="color:yellow;">Obtain Jibril binaries</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

```sh
$ sudo curl -L -o /usr/bin/jibril https://bit.ly/3FLyV1x

$ sudo chmod +x /usr/bin/jibril

$ /usr/bin/jibril --version
```

## <mark style="color:yellow;">Run Jibril as a Systemd Service</mark> <a href="#run-jibril-as-a-systemd-service" id="run-jibril-as-a-systemd-service"></a>

Jibril can be run as a systemd service.

This is the recommended way to run Jibril in staging/production environments. The following steps will guide you through the installation and configuration of Jibril as a systemd service.

### <mark style="color:yellow;">Install the Service</mark> <a href="#install-the-service" id="install-the-service"></a>

To install the service, run:

```sh
$ sudo -E /usr/bin/jibril --systemd install
```

This command will create:

1. [`/etc/systemd/system/jibril.service`](systemd-config.md)
2. [`/etc/jibril/config.yaml`](../configuration-file/)
3. [`/etc/jibril/netpolicy.yaml`](../../components/network-policy.md)
4. `/etc/jibril/recipes/*.yaml`

The systemd service will be installed, but not enabled yet.

> All the recipes automatically installed in `etc` directory are already [builtin in Jibril ](../../components/alchemies/builtin-recipes.md)- with a few other [private recipes](../../components/alchemies/builtin-recipes.md#private-recipes). If you chose to execute [Jibril with the alchemies plugin](../../components/alchemies/) (allowing you to define your own detection recipes), make sure to have the [alchemies directory](../../components/alchemies/create-recipes.md) configured to `/etc/jibril/recipes/`directory AND to have those **recipes disabled** in the [configuration file](../configuration-file/).

### <mark style="color:yellow;">Edit the Configuration File</mark> <a href="#edit-the-configuration-file" id="edit-the-configuration-file"></a>

Edit the configuration file at `/etc/jibril/config.yaml`. The default configuration enables Jibril with most of its plugins and the detection events.

{% hint style="info" %}
<mark style="color:red;">The default configuration should be changed for production environments. It is recommended to fine-tune the configuration files to enable only the necessary plugins, printers and events.</mark>
{% endhint %}

### <mark style="color:yellow;">Enable the Service</mark> <a href="#enable-the-service" id="enable-the-service"></a>

After editing the configuration file, enable the service by running:

```sh
$ sudo -E jibril --systemd enable-now
```

This will enable the service to start at boot time AND start the service immediately.

### <mark style="color:yellow;">Check the Service Status</mark> <a href="#check-the-service-status" id="check-the-service-status"></a>

To check the status of the service, run:

```sh
$ sudo systemctl status jibril
```

### <mark style="color:yellow;">Check the Logs</mark> <a href="#check-the-logs" id="check-the-logs"></a>

The `varlog` printer is enabled by default in the configuration file. This means that the JSON events are printed to `/var/log/jibril.out`, while Jibril stdout and stderr are redirected to systemd journal.

To check the logs, run:

```sh
$ sudo journalctl -u jibril
```

and to check the events, run:

```sh
$ sudo cat /var/log/jibril.out | jq
```

## <mark style="color:yellow;">Disable the Service</mark> <a href="#disable-the-service" id="disable-the-service"></a>

God forbid, but if you need to disable the service, run:

```sh
$ sudo -E jibril --systemd disable-now
```

This will disable the service from starting at boot time AND stop the service immediately.
