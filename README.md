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

Example I Used HackTheBox Machine:
┌──(kali㉿kali)-[~/Downloads/local.ctf/ProjctScan]
└─$ python3 scan_things.py -t 10.129.244.202
/ ___||  _ \ / \ | \ | | ____|_   _|  _ \ 
 \___ \| | | |/ _ \ |  \| |  _|   | | | |_) |
  ___) | |_| / ___ \| |\  | |___  | | |  __/ 
 |____/|____/_/   \_\_| \_|_____| |_| |_|    
                                                 
                  Scan-Things v1.0
             Automated Reconnaissance Tool
          Smart Recon for Domains & IPs
============================================================
    
[*] Starting Scan-Things on 10.129.244.202 (http)
[*] Output directory created: scan_results_10.129.244.202_2026-03-26_13-13-03
[*] Running Nmap Scan...
Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-26 13:13 -0400
Nmap scan report for variatype.htb (10.129.244.202)
Host is up (0.75s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey: 
|   256 e0:b2:eb:88:e3:6a:dd:4c:db:c1:38:65:46:b5:3a:1e (ECDSA)
|_  256 ee:d2:bb:81:4d:a2:8f:df:1c:50:bc:e1:0e:0a:d1:22 (ED25519)
80/tcp open  http    nginx 1.22.1
|_http-title: VariaType Labs \xE2\x80\x94 Variable Font Generator
|_http-server-header: nginx/1.22.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.15 seconds

[*] Running Directory Brute-force on web server (Might Take Some Time)...
[*] Processing results...
[+] Found 22881 live directories!
[*] Scan-Things completed successfully!
[*] All results saved in folder: scan_results_10.129.244.202_2026-03-26_13-13-03

┌──(kali㉿kali)-[~/Downloads/local.ctf/ProjctScan]
└─$ ls   
scan_results_10.129.244.202_2026-03-26_13-13-03  scan_things.py
                                                                                                                                                                                  
┌──(kali㉿kali)-[~/Downloads/local.ctf/ProjctScan]
└─$ cd scan_results_10.129.244.202_2026-03-26_13-13-03 
                                                                                                                                                                                  
┌──(kali㉿kali)-[~/Downloads/local.ctf/ProjctScan/scan_results_10.129.244.202_2026-03-26_13-13-03]
└─$ ls 
directories.json  found_directories.txt  nmap_scan.txt


## Installation

```bash
git clone https://github.com/yourusername/scan-things.git
cd scan-things

# Install required tools (one time)
sudo apt update
sudo apt install nmap ffuf -y

# Optional but recommended for better wordlists
sudo apt install seclists -y
