# Wordlist Directory

This directory contains password wordlists used for security testing.

## Available Wordlists

- **spongebob.txt** - Small custom wordlist
- **rockyou.txt** - Famous password wordlist (14+ million passwords)

## Setting up RockyOU Wordlist

The RockyOU wordlist is one of the most popular password lists used in security testing and penetration testing. It contains over 14 million real-world passwords.

### Automatic Setup (Recommended)

Run the setup script from the project root directory:

```bash
python3 setup_rockyou.py
```

This will automatically download and install the rockyou.txt wordlist into this directory.

### Manual Setup

If you're on Kali Linux or have rockyou already:

1. **On Kali Linux:**
   ```bash
   # Extract rockyou if it's compressed
   sudo gunzip /usr/share/wordlists/rockyou.txt.gz

   # Copy to project wordlist directory
   cp /usr/share/wordlists/rockyou.txt ./wordlist/
   ```

2. **Manual Download:**
   - Download from: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
   - Place the file in this `wordlist/` directory

### Usage

When the toolkit prompts for a wordlist, simply enter:
```
rockyou.txt
```

## File Information

- **rockyou.txt**: ~133 MB, 14,344,391 passwords
- **Format**: Plain text, one password per line
- **Encoding**: Latin-1

## Adding Custom Wordlists

To add your own wordlists:
1. Place any `.txt` file in this directory
2. Ensure one password per line
3. Use the filename when prompted by the toolkit

## Notes

- Larger wordlists like rockyou.txt may take longer to process
- Ensure you have proper authorization before using these tools
- These wordlists are for authorized security testing only
