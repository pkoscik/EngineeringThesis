#!/usr/bin/env bash
sudo watchexec --exts tex,cls --on-busy-update restart "./build.sh -b -u"
