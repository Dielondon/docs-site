#!/usr/bin/env bash
# gates/no-external-links.sh — the docs ship offline: no http(s) links unless listed in
# docs/allowed-links.txt (one URL per line).
allowed="docs/allowed-links.txt"
bad=""
while IFS= read -r url; do
  if [ ! -f "$allowed" ] || ! grep -qxF "$url" "$allowed"; then bad="$bad$url"$'\n'; fi
done < <(grep -rhoE 'https?://[^) >"]+' docs/ --include='*.md' | sort -u)
if [ -n "$bad" ]; then
  echo "External links are not allowed in these docs (they ship offline):"
  printf '%s' "$bad" | sed 's/^/  /'
  echo "If one is really needed, a human adds it to $allowed."
  exit 1
fi
echo "No external links."
