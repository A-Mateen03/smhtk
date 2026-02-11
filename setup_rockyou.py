#!/usr/bin/env python3
"""
RockyOU Wordlist Setup Script
Downloads and extracts the rockyou.txt wordlist for use with the toolkit
"""

import os
import sys
import gzip
import shutil
import urllib.request
from rich.console import Console
from rich.progress import Progress, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

console = Console()

# RockyOU wordlist URL (from GitHub mirror)
ROCKYOU_URL = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
WORDLIST_DIR = "wordlist"
ROCKYOU_PATH = os.path.join(WORDLIST_DIR, "rockyou.txt")

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   YELLOW = '\033[93m'
   END = '\033[0m'
   CYAN = '\033[96m'

def download_rockyou():
    """Download the rockyou wordlist"""

    if os.path.exists(ROCKYOU_PATH):
        console.print(f"\n{color.YELLOW}[!] rockyou.txt already exists in {WORDLIST_DIR}/{color.END}")
        response = input(f"{color.CYAN}[?] Do you want to re-download it? (y/n): {color.END}").lower()
        if response != 'y':
            console.print(f"{color.GREEN}[+] Using existing rockyou.txt{color.END}")
            return True
        os.remove(ROCKYOU_PATH)

    console.print(f"\n{color.CYAN}[*] Downloading rockyou.txt wordlist...{color.END}")
    console.print(f"{color.YELLOW}[!] This may take a few minutes (file size: ~133 MB){color.END}\n")

    try:
        # Create wordlist directory if it doesn't exist
        os.makedirs(WORDLIST_DIR, exist_ok=True)

        # Download with progress bar
        with Progress(
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        ) as progress:

            def reporthook(block_num, block_size, total_size):
                if not hasattr(reporthook, 'task_id'):
                    reporthook.task_id = progress.add_task("Downloading", total=total_size)
                progress.update(reporthook.task_id, completed=block_num * block_size)

            urllib.request.urlretrieve(ROCKYOU_URL, ROCKYOU_PATH, reporthook=reporthook)

        console.print(f"\n{color.GREEN}[+] Successfully downloaded rockyou.txt to {WORDLIST_DIR}/{color.END}")

        # Display file info
        file_size = os.path.getsize(ROCKYOU_PATH) / (1024 * 1024)  # Convert to MB
        console.print(f"{color.GREEN}[+] File size: {file_size:.2f} MB{color.END}")

        # Count lines
        console.print(f"{color.CYAN}[*] Counting passwords...{color.END}")
        with open(ROCKYOU_PATH, 'r', encoding='latin-1', errors='ignore') as f:
            line_count = sum(1 for _ in f)
        console.print(f"{color.GREEN}[+] Total passwords: {line_count:,}{color.END}\n")

        return True

    except Exception as e:
        console.print(f"\n{color.RED}[!] Error downloading rockyou.txt: {str(e)}{color.END}")
        console.print(f"{color.YELLOW}[!] You can manually download it from: {ROCKYOU_URL}{color.END}")
        console.print(f"{color.YELLOW}[!] Then place it in the '{WORDLIST_DIR}/' directory{color.END}\n")
        return False

def verify_installation():
    """Verify rockyou.txt is properly installed"""
    if os.path.exists(ROCKYOU_PATH):
        console.print(f"{color.GREEN}[+] rockyou.txt is ready to use!{color.END}")
        console.print(f"{color.CYAN}[*] When prompted for wordlist, enter: rockyou.txt{color.END}\n")
        return True
    else:
        console.print(f"{color.RED}[!] rockyou.txt not found{color.END}\n")
        return False

def main():
    console.print("\n" + "="*60, style="bold cyan")
    console.print("      RockyOU Wordlist Setup", style="bold cyan", justify="center")
    console.print("="*60 + "\n", style="bold cyan")

    if download_rockyou():
        verify_installation()
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()