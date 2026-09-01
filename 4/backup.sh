#!/bin/bash
backup_dir="$Home/backups"
mkdir -p "$backup_dir"

timestamp=$(date +%Y%m%d_%H%M%S)
tar -czf "$backup_dir/backup_$timestamp.tar.gz" ~/myscript.sh
echo "Backup created: backup_$timestamp.tar.gz"

