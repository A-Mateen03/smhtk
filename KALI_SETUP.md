# Kali Linux Setup Guide

Complete guide to set up and run the Social Media Hacking Toolkit on Kali Linux with RockyOU wordlist integration.

## Prerequisites

- Kali Linux (or any Debian-based Linux distribution)
- Python 3.x installed
- Internet connection
- Root/sudo access

---

## Step 1: Transfer Project to Kali Linux

Choose one of the following methods:

### Option A: Using Git (Recommended)
```bash
git clone <your-repo-url>
cd SocialMediaHackingToolkit
```

### Option B: Using SCP from Mac/Windows
```bash
scp -r "/Users/mateen/Desktop/untitled folder/SocialMediaHackingToolkit" user@kali-ip:~/
```

### Option C: Download and Extract
```bash
# Download zip file and extract
unzip SocialMediaHackingToolkit.zip
cd SocialMediaHackingToolkit
```

---

## Step 2: Extract RockyOU Wordlist

RockyOU comes pre-installed on Kali Linux but is compressed.

```bash
# Navigate to your project directory
cd ~/SocialMediaHackingToolkit

# Check if rockyou exists
ls -lh /usr/share/wordlists/rockyou.txt.gz

# Extract rockyou (it comes compressed on Kali)
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Copy to your project's wordlist directory
cp /usr/share/wordlists/rockyou.txt ./wordlist/

# Verify it's there
ls -lh wordlist/
```

**Expected output:**
```
-rw-r--r-- 1 user user 134M rockyou.txt
-rw-r--r-- 1 user user 417  spongebob.txt
```

---

## Step 3: Install Python Dependencies

```bash
# Update system packages
sudo apt update

# Install Python3 and pip (if not already installed)
sudo apt install python3 python3-pip -y

# Install project requirements
pip3 install -r requirements.txt
```

**Or install dependencies individually:**
```bash
pip3 install requests bs4 instaloader rich distro
```

**Verify installation:**
```bash
python3 -c "import requests, bs4, instaloader, rich, distro; print('All dependencies installed!')"
```

---

## Step 4: Setup Windscribe VPN (Optional)

The toolkit supports VPN rotation using Windscribe for enhanced anonymity.

```bash
# Install Windscribe CLI from included package
sudo dpkg -i dependencies/windscribe-cli.deb

# Or download latest version:
wget https://windscribe.com/install/desktop/linux_deb_x64 -O windscribe.deb
sudo dpkg -i windscribe.deb

# Fix any dependency issues
sudo apt-get install -f

# Login to Windscribe (requires account)
windscribe login

# Start Windscribe service
sudo systemctl start windscribe
sudo systemctl enable windscribe

# Test connection
windscribe connect
```

**Note:** VPN is optional. You can select "VPN off" when running the toolkit.

---

## Step 5: Make Scripts Executable

```bash
# Make the Linux launcher executable
chmod +x linux.sh

# Make setup script executable (if you want to re-download rockyou)
chmod +x setup_rockyou.py
```

---

## Step 6: Run the Toolkit

### Method 1: Using Shell Script
```bash
./linux.sh
```

### Method 2: Direct Python Execution
```bash
cd cmd
python3 main.py
```

---

## Step 7: Using RockyOU Wordlist

When prompted for a wordlist during bruteforce attacks, enter:
```
rockyou.txt
```

The toolkit will automatically display available wordlists:
- `spongebob.txt` - Small custom wordlist (417 bytes)
- `rockyou.txt` - Famous wordlist (14,344,391 passwords, ~133 MB)

---

## Quick Setup Script (All-in-One)

Run this single command to set up everything automatically:

```bash
cd ~/SocialMediaHackingToolkit && \
sudo gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null ; \
cp /usr/share/wordlists/rockyou.txt ./wordlist/ && \
pip3 install -r requirements.txt && \
chmod +x linux.sh && \
echo "Setup complete! Run ./linux.sh to start"
```

---

## Usage Example

```bash
# Start the toolkit
./linux.sh

# Follow the interactive prompts:

# Step 1: Choose social media platform
# :: 1 instagram | 2 facebook | 3 gmail | 4 twitter ::
1

# Step 2: Enable/Disable VPN
# :: 0 vpn off | 1 vpn on ::
0

# Step 3: Choose attack type
# :: 1 bruteforce | 2 mass report | 3 phishing ::
1

# Step 4: Enter target username
# :: username ::
targetuser

# Step 5: Choose wordlist
# :: wordlist ::
# Available wordlists:
# 1. spongebob.txt
# 2. rockyou.txt
rockyou.txt
```

---

## Troubleshooting

### RockyOU not found
```bash
# Use the Python setup script to download
python3 setup_rockyou.py

# Or manually download
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt -O wordlist/rockyou.txt
```

### Permission Errors
```bash
# Fix directory permissions
sudo chmod -R 755 ~/SocialMediaHackingToolkit

# Fix file ownership
sudo chown -R $USER:$USER ~/SocialMediaHackingToolkit
```

### Missing Dependencies
```bash
# Install with --user flag
pip3 install --user requests bs4 instaloader rich distro

# Or use sudo
sudo pip3 install requests bs4 instaloader rich distro
```

### Python Module Not Found
```bash
# Ensure Python3 is default
python --version
python3 --version

# Add to PATH if needed
export PATH="$HOME/.local/bin:$PATH"
```

### Windscribe VPN Issues
```bash
# Check service status
sudo systemctl status windscribe

# Restart service
sudo systemctl restart windscribe

# View logs
journalctl -u windscribe -f
```

### Clear Screen Not Working
```bash
# Install ncurses if needed
sudo apt install ncurses-bin
```

---

## File Structure

```
SocialMediaHackingToolkit/
├── cmd/
│   ├── main.py              # Main entry point
│   ├── utils.py             # Utility functions
│   ├── asciiart.py          # ASCII art
│   ├── supported-attack.txt
│   └── supported-social.txt
├── wordlist/
│   ├── spongebob.txt        # Sample wordlist
│   ├── rockyou.txt          # RockyOU wordlist (after setup)
│   └── README.md            # Wordlist documentation
├── dependencies/
│   └── windscribe-cli.deb   # VPN package
├── docs/
│   └── README.md
├── linux.sh                 # Linux launcher
├── windows.bat              # Windows launcher
├── setup_rockyou.py         # RockyOU setup script
├── requirements.txt         # Python dependencies
├── KALI_SETUP.md           # This file
└── README.md
```

---

## RockyOU Wordlist Information

- **File Size:** ~133 MB
- **Total Passwords:** 14,344,391
- **Format:** Plain text, one password per line
- **Encoding:** Latin-1
- **Source:** Real-world passwords from data breaches
- **Use Case:** Password strength testing, security audits

---

## Security & Legal Notice

**IMPORTANT:** This toolkit is for authorized security testing only.

- Only use on systems you own or have explicit permission to test
- Unauthorized access to computer systems is illegal
- Use responsibly and ethically
- The authors are not responsible for misuse

---

## Additional Resources

- [RockyOU Wordlist Info](https://wiki.skullsecurity.org/index.php/Passwords)
- [Windscribe VPN](https://windscribe.com/)
- [Kali Linux Documentation](https://www.kali.org/docs/)

---

## Support

For issues or questions:
- Check the main README.md
- Review troubleshooting section above
- Ensure all dependencies are installed
- Verify you have proper permissions

---

**Last Updated:** February 2026
