# ansible_filter_plugins

## Plugin to convert octal modes to symbolic
Convert POSIX octal-style to symbolic permissions with an ansible filter. I was quite surprised not to find something like this readily available out there, but here we are... Let me know if you have another way of doing this!

Accepts `mode` as a 3-digit octal mode, with or without a `0` or `0o` prefix, as well as a single octal digit. Output is in standard `rwx` output, with `-` separators for 3-digit modes.

A single-digit octal value will return with no separator (e.g. `6` returns `rw`) by default, but can be changed by passing `format_long = true`.

For example:

```
{{ "0o644" | oct_to_sym }}                     -> rw-r--r--
{{ "0640" | oct_to_sym }}                      -> rw-r-----
{{ "755" | oct_to_sym }}                       -> rwxr-xr-x
{{ "6" | oct_to_sym }}                         -> rw
{{ "6" | oct_to_sym(format_long = true) }}     -> rw-
{{ "5" | oct_to_sym(format_long = true) }}     -> r-x
```

## Installation
Clone this repo to `filter_plugins` as described [here](https://docs.ansible.com/ansible/latest/plugins/filter.html).
