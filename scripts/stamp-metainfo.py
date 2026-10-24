#!/usr/bin/env python3
"""Stamp a release entry into the AppStream metainfo before flatpak builds.

Usage: stamp-metainfo.py <metainfo-path> <version> <date>
"""
import sys

path, version, date = sys.argv[1:4]
text = open(path, encoding="utf-8").read()
entry = f'    <release version="{version}" date="{date}"/>'
if f'version="{version}"' in text:
    print(f"release {version} already stamped")
    raise SystemExit(0)
if "<releases>" in text:
    text = text.replace("</releases>", f"{entry}\n  </releases>", 1)
else:
    anchor = "</screenshots>"
    if anchor not in text:
        raise SystemExit(f"{anchor} not found in {path}")
    text = text.replace(anchor, f"{anchor}\n  <releases>\n{entry}\n  </releases>", 1)
open(path, "w", encoding="utf-8").write(text)
print(f"stamped {version} into {path}")
