import requests as r, sys as s

def M():
    print("TikTok Video Control\n\nusage:\n  python tiktok.py list\n  python tiktok.py delete <id>\n\nsetup:\n  when prompted, paste your TikTok sessionid and user_id\n\nhow to get them:\n  1. open TikTok in Chrome\n  2. press F12 → Application tab → Cookies\n  3. copy sessionid and user_id from the TikTok domain\n")

if len(s.argv)<2: M();exit()
S = input("sessionid: ").strip()
U = input("user_id: ").strip()
H = {"User-Agent":"com.ss.android.ugc.trill/270603 (Linux; U; Android 11)","Cookie":f"sessionid={S}"}

def L():
    u = f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/post/?user_id={U}&count=20"
    x = r.get(u,headers=H)
    if not x.ok: return print("failed to fetch")
    for i,v in enumerate(x.json().get("aweme_list",[]),1):
        print(f"{i}. {v['desc'][:40]}... — {v['aweme_id']}")

def D(a): 
    u = f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/delete/?aweme_id={a}"
    x = r.post(u,headers=H)
    print("deleted" if x.ok else "fail")

if s.argv[1]=="list": L()
elif s.argv[1]=="delete" and len(s.argv)==3: D(s.argv[2])
else: M()
