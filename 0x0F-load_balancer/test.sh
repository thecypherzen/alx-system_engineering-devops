#!/usr/bin/env bash

#fs="$(command -v haproxy)"
#if [[ -z "$fs" ]]; then
#    echo "len 0"
#fi


sed -Ei "/newline$/a $(echo -e '\ta line with tab')" myfile
