---
icon: cabin
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Systemd Config

## <mark style="color:yellow;">Systemd Service File (for reference)</mark>

```systemd
[Unit]
Description=jibril
Conflicts=example.service
Conflicts=loader.service

[Service]
User=root
#
Type=notify
NotifyAccess=all
RemainAfterExit=no
Restart=no
#
TTYReset=yes
TTYPath=/dev/pts/0
#
Environment=TERM=xterm
Environment=LANG=en_US.UTF-8
Environment=LC_ALL=en_US.UTF-8
Environment=LANGUAGE=en_US.UTF-8
Environment=PATH=/usr/sbin:/usr/bin:/sbin:/bin
Environment=LISTENDEV_DEBUG_PRINTER=/var/log/jibril.events
#
EnvironmentFile=-/etc/default/jibril
EnvironmentFile=-/var/run/jibril/default
#
PrivateTmp=true
PrivateDevices=false
PrivateIPC=false
PrivateMounts=false
PrivateNetwork=false
PrivateUsers=false
#
ExecStartPre=rm -f /var/run/{jibril.pid,jibril.log,jibril.err,jibril.events}
ExecStart=jibril                    \
--notify                            \
--log-level info                    \
--stdout /var/log/jibril.log        \
--stderr /var/log/jibril.err        \
--config /etc/jibril/config.yaml
ExecStopPost=bash -c 'cat /var/log/jibril.err'
#
TimeoutStartSec=300
TimeoutStopSec=600
#
KillMode=control-group

[Install]
WantedBy=multi-user.target
```

> This systemd service file is [created automatically.](./#install-the-service)
