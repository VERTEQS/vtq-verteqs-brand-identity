#!/usr/bin/env python3
"""
S3からアセットをダウンロードするスクリプト
使用方法: python sync_assets.py
"""
import subprocess
import sys

BUCKET = "vtq-data-develop"
PROJECT = "verteqs-brand-identity"

def main():
    cmd = [
        "rclone", "sync",
        f"vtq-s3:{BUCKET}/main/{PROJECT}",
        ".",
        "--exclude", ".git/**",
        "--exclude", "*.py",
        "--progress"
    ]
    print(f"Syncing from S3: {BUCKET}/main/{PROJECT}")
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
