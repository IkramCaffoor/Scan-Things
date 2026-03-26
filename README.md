# Scan-Things

  ____  ____ _   _ _____ _____ ____  
 / ___||  _ \ / \ | \ | | ____|_   _|  _ \ 
 \___ \| | | |/ _ \ |  \| |  _|   | | | |_) |
  ___) | |_| / ___ \| |\  | |___  | | |  __/ 
 |____/|____/_/   \_\_| \_|_____| |_| |_|    

                  Scan-Things v1.0
             Automated Reconnaissance Tool
          Smart Recon for Domains & IPs
============================================================

# Scan-Things

**A simple yet powerful automated reconnaissance scanner built for penetration testing practice.**

Scan-Things automatically performs:
- Full Nmap service and script scanning
- Directory brute-forcing on web servers (for IPs and domains)
- Subdomain enumeration (when a domain is provided)

Perfect for Hack The Box, TryHackMe, and real-world target reconnaissance.

---

## Features

- Smart detection: works with both IP addresses and domain names
- Runs Nmap scan with service version detection (-sC -sV)
- Directory brute-force with common extensions (.php, .html, .txt, .git)
- Automatic Subdomain Enumeration when target is a domain
- Creates clean result files (`found_directories.txt` and `found_subdomains.txt`)
- Saves everything in a timestamped folder for easy organization
- Clean msfconsole-style output

---

## Installation

```bash
git clone https://github.com/yourusername/scan-things.git
cd scan-things

# Install required tools (one time)
sudo apt update
sudo apt install nmap ffuf -y

# Optional but recommended for better wordlists
sudo apt install seclists -y
