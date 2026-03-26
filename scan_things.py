#!/usr/bin/env python3
import subprocess
import argparse
import os
from datetime import datetime

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error: {e}"

def print_banner():
    print(r"""
  ____  ____ _   _ _____ _____ ____  
 / ___||  _ \ / \ | \ | | ____|_   _|  _ \ 
 \___ \| | | |/ _ \ |  \| |  _|   | | | |_) |
  ___) | |_| / ___ \| |\  | |___  | | |  __/ 
 |____/|____/_/   \_\_| \_|_____| |_| |_|    
                                                 
                  Scan-Things v1.0
             Automated Reconnaissance Tool
          Smart Recon for Domains & IPs
============================================================
    """)

def is_ip_address(target):
    parts = target.split('.')
    return len(parts) == 4 and all(p.isdigit() for p in parts)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Scan-Things - Automated Reconnaissance Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target DOMAIN or IP (e.g. variatype.htb or 10.129.244.202)")
    parser.add_argument("--https", action="store_true", help="Use HTTPS instead of HTTP")
    args = parser.parse_args()

    target = args.target
    protocol = "https" if args.https else "http"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = f"scan_results_{target}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    print(f"[*] Starting Scan-Things on {target} ({protocol})")
    print(f"[*] Output directory created: {output_dir}")

    # 1. Nmap Scan
    print("[*] Running Nmap Scan...")
    nmap_cmd = f"nmap -sC -sV -oN {output_dir}/nmap_scan.txt {target}"
    nmap_result = run_command(nmap_cmd)
    print(nmap_result[:1200] + "\n... [truncated]" if len(nmap_result) > 1200 else nmap_result)

    # Better wordlist
    wordlist = "/usr/share/wordlists/dirb/common.txt"
    if os.path.exists("/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt"):
        wordlist = "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt"

    # 2. Directory Brute-force (always runs)
    print("[*] Running Directory Brute-force on web server (Might Take Some Time)...")
    ffuf_dir_cmd = (
        f'ffuf -w {wordlist} -u {protocol}://{target}/FUZZ '
        f'-mc 200,301,302 -e .php,.html,.txt,.git -o {output_dir}/directories.json -of json -t 60'
    )
    run_command(ffuf_dir_cmd)

    # 3. Subdomain Enumeration (only if target is a domain)
    if not is_ip_address(target):
        print("[*] Target is domain → Running Subdomain Enumeration...")
        ffuf_sub_cmd = (
            f'ffuf -w {wordlist} -u {protocol}://FUZZ.{target} '
            f'-mc 200 -o {output_dir}/subdomains.json -of json -t 60'
        )
        run_command(ffuf_sub_cmd)

    # 4. Create clean result files
    print("[*] Processing results...")
    try:
        import json
        # Directory results
        if os.path.exists(f"{output_dir}/directories.json"):
            with open(f"{output_dir}/directories.json", 'r') as f:
                data = json.load(f)
            found_dirs = [entry['input']['FUZZ'] for entry in data.get('results', []) if entry.get('status') in [200, 301, 302]]
            if found_dirs:
                with open(f"{output_dir}/found_directories.txt", 'w') as f:
                    f.write("\n".join(found_dirs))
                print(f"[+] Found {len(found_dirs)} live directories!")

        # Subdomain results (if existed)
        if os.path.exists(f"{output_dir}/subdomains.json"):
            with open(f"{output_dir}/subdomains.json", 'r') as f:
                data = json.load(f)
            found_subs = [entry['input']['FUZZ'] for entry in data.get('results', []) if entry.get('status') == 200]
            if found_subs:
                with open(f"{output_dir}/found_subdomains.txt", 'w') as f:
                    f.write("\n".join(found_subs))
                print(f"[+] Found {len(found_subs)} live subdomains!")
    except:
        pass

    print(f"[*] Scan-Things completed successfully!")
    print(f"[*] All results saved in folder: {output_dir}")

if __name__ == "__main__":
    main()
