---
icon: docker
---

# Docker Container

> Check out Jibril's public recipes repository at [https://github.com/garnet-org/jibril-balag](https://github.com/garnet-org/jibril-balag).

## <mark style="color:yellow;">Create a Configuration File</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

```sh
$ mkdir /etc/jibril

$ vi /etc/jibril/config.yaml
```

> Use the [default configuration file ](../configuration-file/)as reference.

## <mark style="color:yellow;">Obtain the Image</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

```sh
$ docker pull garnetlabs/jibril:v2.4
```

## <mark style="color:yellow;">Run Jibril using Docker</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

```sh
$ docker run --rm --name=jibril --privileged \
    --pid=host --cgroupns=host --network=host \
    -e TERM=xterm -v /sys:/sys:ro \
    -v /sys/fs/bpf:/sys/fs/bpf:rw \
    -v /etc/jibril/:/etc/jibril:rw \
    -v /var/log/jibril:/var/log/jibril:rw \
    garnetlabs/jibril:v2.4 --config /etc/jibril/config.yaml
```

> This command is an example of how one can run Jibril using its docker image.

{% hint style="info" %}
For Kubernetes, use the [Kubernetes instructions](../kubernetes/).
{% endhint %}

## <mark style="color:yellow;">AI Filtering</mark> <a href="#run-jibril-using-command-line-arguments" id="run-jibril-using-command-line-arguments"></a>

#### <mark style="color:yellow;">The Attenuator</mark>

#### Want to try the [attenuator.md](../../customization/attenuator.md "mention") feature ?

```shell
$ docker run --rm --name=jibril --privileged \
    --pid=host --cgroupns=host --network=host \
    -e AI_TOKEN=$AI_TOKEN \
    -e AI_MODEL=o3 \
    -e AI_TEMPERATURE=1 \
    -e TERM=xterm -v /sys:/sys:ro \
    -v /sys/fs/bpf:/sys/fs/bpf:rw \
    -v /etc/jibril/:/etc/jibril:rw \
    -v /var/log/jibril:/var/log/jibril:rw \
    garnetlabs/jibril:v2.4 \
    --config /etc/jibril/config.yaml
```

#### Make sure your [configuration-file](../configuration-file/ "mention") `/etc/jibril/config,yaml` is set as:

```yaml
log-level: info
stdout: stdout
stderr: stderr
chop-lines: false
no-health: false
profiler: false
cardinal: true
daemon: false
notify: false
extension:
  - config
  - data
  - jibril
plugin:
  - jibril:hold
  - jibril:procfs
  - jibril:printers
  - jibril:attenuator:enabled=true:mode=reason
  - jibril:detect
printer:
  - jibril:printers:stdout
event:
  - jibril:detect:hidden_elf_exec
  - jibril:detect:plaintext_communication
```

#### <mark style="color:yellow;">Execute a test</mark>

Execute a simple test trying to get something from a paste-bin like URL

```shell
$ curl https://gist.githubusercontent.com/tempadmin2023/sysconfig-update/raw/critical_patch.sh
```

#### <mark style="color:yellow;">Observe the AI verdict</mark>

Observe the event + the verdict given by the AI model.

```json
{
  "data": {
    "body": {
      "flow": {
        "ip_version": 4,
        "proto": "TCP",
        "service_port": 443,
        "icmp": {
          "type": "",
          "code": ""
        },
        "local": {
          "address": "192.168.1.125",
          "name": "192.168.1.125",
          "names": ["192.168.1.125"],
          "port": 39992
        },
        "remote": {
          "address": "185.199.110.133",
          "name": "gist.githubusercontent.com",
          "names": ["185.199.110.133", "gist.githubusercontent.com"],
          "port": 443
        },
        "properties": {
          "ingress": true,
          "egress": true,
          "incoming": false,
          "outgoing": true,
          "started": true,
          "ongoing": true,
          "ended": true,
          "terminator": true,
          "terminated": false
        },
        "settings": {
          "direction": "both",
          "initiated_by": "local",
          "status": "ended",
          "ended_by": "local"
        }
      },
      "fullinfo": {
        "files": {
          "etc": {
            "ca-certificates": {
              "extracted": {
                "tls-ca-bundle.pem": "open|read|close"
              }
            },
            "gai.conf": "open|read|close",
            "host.conf": "open|read|close",
            "ld.so.cache": "mmap|open|close",
            "ld.so.preload": "open|close",
            "nsswitch.conf": "open|read|close",
            "passwd": "open|read|close",
            "ssl": {
              "openssl.cnf": "open|read|close"
            }
          },
          "usr": {
            "bin": {
              "curl": "mmap|open|close|execve"
            },
            "lib": {
              "ld-linux-x86-64.so.2": "mmap|open|close",
              "libbrotlicommon.so.1.1.0": "mmap|open|read|close",
              "libbrotlidec.so.1.1.0": "mmap|open|read|close",
              "libc.so.6": "mmap|open|read|close",
              "libcap.so.2.75": "mmap|open|read|close",
              "libcom_err.so.2.1": "mmap|open|read|close",
              "libcrypto.so.3": "mmap|open|read|close",
              "libcurl.so.4.8.0": "mmap|open|read|close",
              "libgcc_s.so.1": "mmap|open|read|close",
              "libgssapi_krb5.so.2.2": "mmap|open|read|close",
              "libidn2.so.0.4.0": "mmap|open|read|close",
              "libk5crypto.so.3.1": "mmap|open|read|close",
              "libkeyutils.so.1.10": "mmap|open|read|close",
              "libkrb5.so.3.3": "mmap|open|read|close",
              "libkrb5support.so.0.1": "mmap|open|read|close",
              "libm.so.6": "mmap|open|read|close",
              "libnghttp2.so.14.28.4": "mmap|open|read|close",
              "libnghttp3.so.9.2.6": "mmap|open|read|close",
              "libnss_mymachines.so.2": "mmap|open|read|close",
              "libnss_resolve.so.2": "mmap|open|read|close",
              "libpsl.so.5.3.5": "mmap|open|read|close",
              "libresolv.so.2": "mmap|open|read|close",
              "libssh2.so.1.0.1": "mmap|open|read|close",
              "libssl.so.3": "mmap|open|read|close",
              "libunistring.so.5.2.0": "mmap|open|read|close",
              "libz.so.1.3.1": "mmap|open|read|close",
              "libzstd.so.1.5.7": "mmap|open|read|close",
              "locale": {
                "locale-archive": "mmap|open|close"
              },
              "systemd": {
                "resolv.conf": "open|read|close"
              }
            },
            "share": {
              "zoneinfo": {
                "America": {
                  "Sao_Paulo": "open|read|close"
                }
              }
            }
          }
        },
        "flows": [
          {
            "ip_version": 4,
            "proto": "TCP",
            "service_port": 443,
            "local": {
              "address": "192.168.1.125",
              "name": "",
              "names": ["192.168.1.125"],
              "port": 39992
            },
            "remote": {
              "address": "185.199.110.133",
              "name": "",
              "names": ["185.199.110.133", "gist.githubusercontent.com"],
              "port": 443
            },
            "settings": {
              "direction": "both",
              "initiated_by": "local",
              "status": "ended",
              "ended_by": "local"
            }
          }
        ],
        "ancestry": [
          {
            "start": "2025-03-12T03:34:41Z",
            "exit": "running",
            "retcode": 0,
            "uid": 0,
            "pid": 1,
            "ppid": 0,
            "comm": "systemd",
            "cmd": "systemd",
            "exe": "/usr/lib/systemd/systemd",
            "args": "/usr/lib/systemd/systemd --system --deserialize=74"
          },
          {
            "start": "2025-03-12T03:34:46Z",
            "exit": "running",
            "retcode": 0,
            "uid": 0,
            "pid": 684,
            "ppid": 1,
            "comm": "sshd",
            "cmd": "sshd",
            "exe": "/usr/bin/sshd",
            "args": "sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups"
          },
          {
            "start": "2025-04-19T23:54:51Z",
            "exit": "running",
            "retcode": 0,
            "uid": 0,
            "pid": 3043552,
            "ppid": 684,
            "comm": "sshd-session",
            "cmd": "sshd-session",
            "exe": "/usr/lib/ssh/sshd-session",
            "args": "sshd-session: rafaeldtinoco [priv]"
          },
          {
            "start": "2025-04-19T23:54:51Z",
            "exit": "running",
            "retcode": 0,
            "uid": 1000,
            "pid": 3043555,
            "ppid": 3043552,
            "comm": "sshd-session",
            "cmd": "sshd-session",
            "exe": "/usr/lib/ssh/sshd-session",
            "args": "sshd-session: rafaeldtinoco@pts/5"
          },
          {
            "start": "2025-04-19T23:54:51Z",
            "exit": "running",
            "retcode": 0,
            "uid": 1000,
            "pid": 3043556,
            "ppid": 3043555,
            "comm": "bash",
            "cmd": "bash",
            "exe": "/usr/bin/bash",
            "args": "-bash"
          },
          {
            "start": "2025-04-20T00:08:43Z",
            "exit": "2025-04-20T00:08:43Z",
            "retcode": 0,
            "uid": 1000,
            "pid": 3044971,
            "ppid": 3043556,
            "comm": "curl",
            "cmd": "curl",
            "exe": "/usr/bin/curl",
            "args": "curl https://gist.githubusercontent.com/tempadmin2023/sysconfig-update/raw/critical_patch.sh"
          }
        ]
      },
      "note": "plaintext_communication_1",
      "parent": {
        "start": "2025-04-19T23:54:51Z",
        "exit": "running",
        "retcode": 0,
        "uid": 1000,
        "pid": 3043556,
        "ppid": 3043555,
        "comm": "bash",
        "cmd": "bash",
        "exe": "/usr/bin/bash",
        "args": "-bash"
      },
      "process": {
        "start": "2025-04-20T00:08:43Z",
        "exit": "2025-04-20T00:08:43Z",
        "retcode": 0,
        "uid": 1000,
        "pid": 3044971,
        "ppid": 3043556,
        "comm": "curl",
        "cmd": "curl",
        "exe": "/usr/bin/curl",
        "args": "curl https://gist.githubusercontent.com/tempadmin2023/sysconfig-update/raw/critical_patch.sh"
      }
    },
    "head": {
      "name": "plaintext_communication",
      "version": "1.0",
      "format": "network_peers",
      "description": "Access to pastebin services",
      "documentation": "https://garnet.gitbook.io/jibril/detections/network-peers/plaintext_communication",
      "category": "command_and_control",
      "mechanism": "network_peers",
      "method": "application_layer_protocol_dns",
      "importance": "critical"
    },
    "timestamp": "2025-04-20T00:08:47Z",
    "unique_id": "2b9d8f99f2b71dafb361fd56ad8c7d3f502e85e0c6f041d1d5d26af06e861969"
  },
  "type": "plaintext_communication",
  "verdict": {
    "false_positive": false,
    "severity": "medium",
    "description": "An interactive SSH session executed curl to fetch a raw shell script named \"critical_patch.sh\" from a public GitHub Gist (gist.githubusercontent.com). Gists are frequently used to host arbitrary code, and the filename suggests system changes. The HTTPS connection, file open/read sequence, and user‑initiated download all occurred as recorded; there is no evidence the alert mis‑fired or that the traffic was misidentified. Without script content or verification of its provenance, treating this as benign would be risky, so the event is unlikely to be a false positive."
  }
}
```
