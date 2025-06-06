---
icon: map
---

# map\_xxx\_elem (v3.19)

## Summary

* `map_lookup_elem`\
  Retrieves the value associated with a given key from a map.
* **`map_update_elem`**\
  Updates the value associated with a given key in a map. \
  If the key does not exist, it can add the key-value pair.
* **`map_delete_elem`**\
  Removes the key-value pair associated with a given key from a map.

## Kernel Code

```c
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 10);
    __type(key, __u32);
    __type(value, __u32);
} my_map SEC(".maps");

SEC("socket")
int bpf_prog(struct __sk_buff *skb) {
    __u32 key = 1;
    __u32 *value;

    // Lookup element
    value = bpf_map_lookup_elem(&my_map, &key);
    if (value) {
        bpf_printk("Found value: %u\n", *value);
    } else {
        bpf_printk("Key not found\n");
    }

    // Update element
    __u32 new_value = 42;
    bpf_map_update_elem(&my_map, &key, &new_value, BPF_ANY);
    bpf_printk("Updated value to: %u\n", new_value);

    // Delete element
    bpf_map_delete_elem(&my_map, &key);
    bpf_printk("Deleted key: %u\n", key);

    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

**Summary:**

* A hash map `my_map` is defined with keys and values of type `__u32`.
* The eBPF program looks up a value with key `1`, updates it to `42`, and then deletes it.
* `bpf_printk` is used to print messages to the kernel log, which can be viewed using `dmesg`.

## Userland Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <bpf/bpf.h>
#include <bpf/libbpf.h>

#define PATH_TO_BPF_OBJ "my_bpf.o"

int load_bpf_program(const char *filename) {
    int fd = bpf_obj_get(filename);
    if (fd < 0) {
        perror("bpf_obj_get");
        return -1;
    }
    return fd;
}

int create_map() {
    struct bpf_create_map_attr attr = {
        .map_type = BPF_MAP_TYPE_HASH,
        .key_size = sizeof(__u32),
        .value_size = sizeof(__u32),
        .max_entries = 10,
    };
    int fd = bpf_create_map_xattr(&attr);
    if (fd < 0) {
        perror("bpf_create_map_xattr");
        return -1;
    }
    return fd;
}

int attach_program(int prog_fd, int sock_fd) {
    int ret = setsockopt(sock_fd, SOL_SOCKET, SO_ATTACH_BPF, &prog_fd, sizeof(prog_fd));
    if (ret < 0) {
        perror("setsockopt");
        return -1;
    }
    return 0;
}

int main(int argc, char **argv) {
    int bpf_fd, prog_fd, map_fd, sock_fd;
    struct bpf_object *obj;
    struct bpf_program *prog;

    // Load BPF object file
    obj = bpf_object__open(PATH_TO_BPF_OBJ);
    if (!obj) {
        perror("bpf_object__open");
        return 1;
    }

    // Load BPF programs and maps
    if (bpf_object__load(obj) < 0) {
        fprintf(stderr, "Failed to load BPF object\n");
        goto cleanup;
    }

    // Get file descriptor for the BPF program
    prog = bpf_object__find_program_by_name(obj, "bpf_prog");
    if (!prog) {
        fprintf(stderr, "Failed to find BPF program\n");
        goto cleanup;
    }
    prog_fd = bpf_program__fd(prog);
    if (prog_fd < 0) {
        fprintf(stderr, "Failed to get BPF program FD\n");
        goto cleanup;
    }

    // Create map
    map_fd = create_map();
    if (map_fd < 0) {
        fprintf(stderr, "Failed to create map\n");
        goto cleanup;
    }

    // Create socket
    sock_fd = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (sock_fd < 0) {
        perror("socket");
        goto cleanup;
    }

    // Attach BPF program to socket
    if (attach_program(prog_fd, sock_fd) < 0) {
        fprintf(stderr, "Failed to attach BPF program\n");
        goto cleanup;
    }

    printf("Attached BPF program. Press Ctrl+C to exit.\n");
    getchar();

cleanup:
    close(sock_fd);
    close(map_fd);
    bpf_object__close(obj);
    return 0;
}
```

**Summary:**

* The userland program loads the BPF object file using `bpf_object__open` and `bpf_object__load`.
* It retrieves the file descriptor for the BPF program using `bpf_program__fd`.
* A hash map is created using `bpf_create_map_xattr`.
* A raw socket is created and the BPF program is attached to it using `setsockopt`.
* The program waits for user input to keep the BPF program running, allowing it to execute.
* Resources are cleaned up when the program exits.

## Conclusions

* The example demonstrates the use of `map_lookup_elem`, `map_update_elem`, and `map_delete_elem` in a simple eBPF program.
* The userland code uses full libbpf functions to load, create maps, attach programs, and manage resources without using the skeleton generated by `bpftool`.
* The output from `bpf_printk` can be viewed using `bpftool` by running `bpftool prog trace`.
