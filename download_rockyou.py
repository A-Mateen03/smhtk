#!/usr/bin/env python3
"""
Simple RockyOU Wordlist Downloader
Downloads rockyou.txt without requiring additional dependencies
"""

import os
import sys
import urllib.request

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
END = '\033[0m'

# Configuration
ROCKYOU_URL = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
WORDLIST_DIR = "wordlist"
ROCKYOU_PATH = os.path.join(WORDLIST_DIR, "rockyou.txt")

def download_with_progress(url, output_path):
    """Download file with progress indicator"""

    def reporthook(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(downloaded * 100.0 / total_size, 100)
            mb_downloaded = downloaded / (1024 * 1024)
            mb_total = total_size / (1024 * 1024)

            # Progress bar
            bar_length = 50
            filled = int(bar_length * percent / 100)
            bar = '=' * filled + '-' * (bar_length - filled)

            sys.stdout.write(f'\r[{bar}] {percent:.1f}% ({mb_downloaded:.1f}/{mb_total:.1f} MB)')
            sys.stdout.flush()

    try:
        print(f"{CYAN}[*] Downloading rockyou.txt...{END}")
        print(f"{YELLOW}[!] This may take a few minutes (file size: ~133 MB){END}\n")

        urllib.request.urlretrieve(url, output_path, reporthook=reporthook)
        print(f"\n\n{GREEN}[+] Download complete!{END}\n")
        return True
    except Exception as e:
        print(f"\n\n{RED}[!] Error downloading: {str(e)}{END}")
        return False

def main():
    print("\n" + "="*60)
    print("      RockyOU Wordlist Downloader")
    print("="*60 + "\n")

    # Check if already exists
    if os.path.exists(ROCKYOU_PATH):
        print(f"{YELLOW}[!] rockyou.txt already exists in {WORDLIST_DIR}/{END}")
        response = input(f"{CYAN}[?] Do you want to re-download it? (y/n): {END}").lower()
        if response != 'y':
            print(f"{GREEN}[+] Using existing rockyou.txt{END}\n")
            return
        os.remove(ROCKYOU_PATH)

    # Create wordlist directory
    os.makedirs(WORDLIST_DIR, exist_ok=True)

    # Download
    if download_with_progress(ROCKYOU_URL, ROCKYOU_PATH):
        # Display file info
        file_size = os.path.getsize(ROCKYOU_PATH) / (1024 * 1024)
        print(f"{GREEN}[+] File saved to: {ROCKYOU_PATH}{END}")
        print(f"{GREEN}[+] File size: {file_size:.2f} MB{END}")

        # Count lines
        print(f"{CYAN}[*] Counting passwords...{END}")
        try:
            with open(ROCKYOU_PATH, 'r', encoding='latin-1', errors='ignore') as f:
                line_count = sum(1 for _ in f)
            print(f"{GREEN}[+] Total passwords: {line_count:,}{END}\n")
        except:
            print(f"{YELLOW}[!] Could not count passwords{END}\n")

        print(f"{GREEN}[+] rockyou.txt is ready to use!{END}")
        print(f"{CYAN}[*] When prompted for wordlist, enter: rockyou.txt{END}\n")
    else:
        print(f"{RED}[!] Download failed!{END}")
        print(f"{YELLOW}[!] You can manually download from:{END}")
        print(f"{YELLOW}    {ROCKYOU_URL}{END}")
        print(f"{YELLOW}[!] Then place it in the '{WORDLIST_DIR}/' directory{END}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
