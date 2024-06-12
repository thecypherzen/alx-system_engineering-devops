#!/usr/bin/env bash
fs="$(command -v haproxy)"
if [[ -z "$fs" ]]; then
    echo "len 0"
fi
