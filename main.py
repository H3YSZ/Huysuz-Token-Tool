from colorama import Fore, Style, init
import os
import webbrowser
import requests
import json
import random
import time
import hashlib
from PIL import Image, ExifTags

init(autoreset=True)

webbrowser.open("https://github.com/H3YSZ")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_from_data_folder(filename):
    filepath = os.path.join('data', filename)
    if not os.path.exists(filepath):
        print(Fore.RED + f"Uyarı: '{filename}' dosyası 'data' klasöründe bulunamadı. Lütfen oluşturun." + Style.RESET_ALL)
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                print(Fore.YELLOW + f"Uyarı: '{filename}' dosyası boş." + Style.RESET_ALL)
                return None
            return content
    except Exception as e:
        print(Fore.RED + f"Hata: '{filename}' okunurken bir sorun oluştu: {e}" + Style.RESET_ALL)
        return None

def load_list_from_data_folder(filename):
    filepath = os.path.join('data', filename)
    if not os.path.exists(filepath):
        print(Fore.RED + f"Uyarı: '{filename}' dosyası 'data' klasöründe bulunamadı. Lütfen oluşturun." + Style.RESET_ALL)
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = [line.strip() for line in f if line.strip()]
            if not content:
                print(Fore.YELLOW + f"Uyarı: '{filename}' dosyası boş." + Style.RESET_ALL)
            return content
    except Exception as e:
        print(Fore.RED + f"Hata: '{filename}' okunurken bir sorun oluştu: {e}" + Style.RESET_ALL)
        return []

def gradient(text):
    colors = [Fore.MAGENTA, Fore.BLUE]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

def banner():
    clear()
    print(gradient(r"""

                __  __                                ______            __    
               / / / /_  ____  _________  ______     /_  __/___  ____  / /____
              / /_/ / / / / / / / ___/ / / /_  /      / / / __ \/ __ \/ / ___/
             / __  / /_/ / /_/ (__  ) /_/ / / /_     / / / /_/ / /_/ / (__  ) 
            /_/ /_/\__,_/\__, /____/\__,_/ /___/    /_/  \____/\____/_/____/  
                        /____/                                                

                                 [GITHUB.COM/H3YSZ]

        """))
    print(Fore.CYAN + "                   Discord/API Tools " + Style.RESET_ALL)
    print(Fore.CYAN + "==================================================" + Style.RESET_ALL)
    print(Fore.GREEN + "[1] Discord Token Analyzer (Info, DMs, Guilds)" + Style.RESET_ALL)
    print(Fore.GREEN + "[2] Discord Invite Checker" + Style.RESET_ALL)
    print(Fore.GREEN + "[3] Discord Send Single Message" + Style.RESET_ALL)
    print(Fore.GREEN + "[4] Discord Token Info" + Style.RESET_ALL)
    print(Fore.GREEN + "[5] Discord Server Membership Check" + Style.RESET_ALL)
    print(Fore.GREEN + "[6] Discord DM Channel Info" + Style.RESET_ALL)
    print(Fore.GREEN + "[7] Discord Language Changer" + Style.RESET_ALL)
    print(Fore.GREEN + "[8] Discord Status Changer" + Style.RESET_ALL)
    print(Fore.GREEN + "[9] Discord Theme Changer" + Style.RESET_ALL)
    print(Fore.GREEN + "[10] Discord Token Login Page Open" + Style.RESET_ALL)
    print(Fore.GREEN + "[11] Discord Server Info" + Style.RESET_ALL)
    print(Fore.GREEN + "[12] Discord Webhook Sender" + Style.RESET_ALL)
    print(Fore.GREEN + "[13] Discord Webhook Info (No Delete)" + Style.RESET_ALL)
    print(Fore.YELLOW + "[14] Contact Info Lookup" + Style.RESET_ALL)
    print(Fore.YELLOW + "[15] Email Breach/Tracker" + Style.RESET_ALL)
    print(Fore.YELLOW + "[16] Username Info Lookup" + Style.RESET_ALL)
    print(Fore.YELLOW + "[17] Phone Number Validation" + Style.RESET_ALL)
    print(Fore.YELLOW + "[18] IP Address Information" + Style.RESET_ALL)
    print(Fore.YELLOW + "[19] Domain Whois Lookup" + Style.RESET_ALL)
    print(Fore.YELLOW + "[20] Social Media Username Checker" + Style.RESET_ALL)
    print(Fore.YELLOW + "[21] File Hash Analysis" + Style.RESET_ALL)
    print(Fore.YELLOW + "[22] Image/File EXIF Data Extractor" + Style.RESET_ALL)
    print(Fore.BLUE + "[23] Proxy Scraper" + Style.RESET_ALL)
    print(Fore.RED + "[0] Çıkış" + Style.RESET_ALL)
    print(Fore.CYAN + "==================================================" + Style.RESET_ALL)

def discord_token_analyzer():
    print(Fore.MAGENTA + "\n[Discord Token Analyzer] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + "Token analiz ediliyor..." + Style.RESET_ALL)
    headers = {"Authorization": token}
    try:
        user_info_response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if user_info_response.status_code == 200:
            user_info = user_info_response.json()
            print(Fore.GREEN + f"Token geçerli! Kullanıcı: {user_info.get('username')}#{user_info.get('discriminator')} (ID: {user_info.get('id')})" + Style.RESET_ALL)

            print(Fore.YELLOW + "\nDM Kanalları Listeleniyor..." + Style.RESET_ALL)
            channels_response = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
            if channels_response.status_code == 200:
                channels = channels_response.json()
                for channel in channels:
                    if channel["type"] == 1:
                        recipient_name = channel.get('recipients', [{}])[0].get('username', 'Bilinmeyen Kullanıcı')
                        print(Fore.CYAN + f"  - DM: {recipient_name} (ID: {channel['id']})" + Style.RESET_ALL)
            else:
                print(Fore.RED + "DM listesi alınamadı!" + Style.RESET_ALL)

            print(Fore.YELLOW + "\nKatılınan Sunucular Listeleniyor..." + Style.RESET_ALL)
            guilds_response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
            if guilds_response.status_code == 200:
                guilds = guilds_response.json()
                for guild in guilds:
                    print(Fore.CYAN + f"  - Sunucu: '{guild['name']}' (ID: {guild['id']})" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Sunucu listesi alınamadı!" + Style.RESET_ALL)

        else:
            print(Fore.RED + "Token geçersiz veya yetkisiz!" + Style.RESET_ALL)
            return
        print(Fore.GREEN + "Token analizi tamamlandı." + Style.RESET_ALL)
    except requests.exceptions.RequestException as req_e:
        print(Fore.RED + f"Ağ hatası oluştu: {req_e}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Beklenmeyen hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_invite_checker():
    print(Fore.MAGENTA + "\n[Discord Invite Checker] Modülü çalışıyor..." + Style.RESET_ALL)
    invite_code = load_from_data_folder("servers.txt")
    if not invite_code:
        invite_code = input("Sunucu Davet Kodu (örnek: wia): ").strip()
        if not invite_code:
            print(Fore.RED + "Davet kodu girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + f"Davet kodu '{invite_code}' kontrol ediliyor..." + Style.RESET_ALL)
    try:
        response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
        if response.status_code == 200:
            invite_info = response.json()
            print(Fore.GREEN + "Davet kodu geçerli!" + Style.RESET_ALL)
            print(Fore.CYAN + f"  Sunucu Adı: {invite_info['guild']['name']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"  Davet Kodu: {invite_info['code']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"  Üye Sayısı: {invite_info.get('approximate_member_count', 'Bilinmiyor')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Davet kodu geçersiz veya bulunamadı! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_send_single_message():
    print(Fore.MAGENTA + "\n[Discord Send Single Message] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    channel_id = input("Kanal ID: ").strip()
    message = input("Gönderilecek Mesaj: ").strip()

    if not channel_id or not message:
        print(Fore.RED + "Kanal ID veya mesaj girilmedi!" + Style.RESET_ALL)
        return

    headers = {"Authorization": token}
    payload = {"content": message}
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    print(Fore.YELLOW + "Mesaj gönderiliyor..." + Style.RESET_ALL)
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 204:
            print(Fore.GREEN + "Mesaj başarıyla gönderildi!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Mesaj gönderilemedi! Hata: {response.status_code}, {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_token_info():
    print(Fore.MAGENTA + "\n[Discord Token Info] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + "Token bilgileri alınıyor..." + Style.RESET_ALL)
    headers = {"Authorization": token}
    try:
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            print(Fore.GREEN + "\n--- Token Bilgileri ---" + Style.RESET_ALL)
            print(Fore.CYAN + f"ID: {user_info.get('id')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Kullanıcı Adı: {user_info.get('username')}#{user_info.get('discriminator')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Email: {user_info.get('email', 'Yok')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Telefon: {user_info.get('phone', 'Yok')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Avatar: https://cdn.discordapp.com/avatars/{user_info.get('id')}/{user_info.get('avatar')}.png?size=1024" + Style.RESET_ALL)
            print(Fore.CYAN + f"2FA Etkin: {user_info.get('mfa_enabled')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Doğrulanmış: {user_info.get('verified')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Token bilgileri alınamadı! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_server_membership_check():
    print(Fore.MAGENTA + "\n[Discord Server Membership Check] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    guild_id = load_from_data_folder("servers.txt")
    if not guild_id:
        guild_id = input("Kontrol edilecek Sunucu ID: ").strip()
        if not guild_id:
            print(Fore.RED + "Sunucu ID girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + f"Token'ın sunucu üyeliği kontrol ediliyor (Sunucu ID: {guild_id})..." + Style.RESET_ALL)
    headers = {"Authorization": token}
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
        if response.status_code == 200:
            guilds = response.json()
            is_member = False
            for guild in guilds:
                if guild['id'] == guild_id:
                    print(Fore.GREEN + f"Token, '{guild['name']}' ({guild_id}) sunucusunun üyesi." + Style.RESET_ALL)
                    is_member = True
                    break
            if not is_member:
                print(Fore.YELLOW + f"Token, {guild_id} ID'li sunucunun üyesi değil." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Sunucu listesi alınamadı! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_dm_info():
    print(Fore.MAGENTA + "\n[Discord DM Channel Info] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    channel_id = input("Bilgisini görmek istediğiniz DM Kanal ID: ").strip()
    if not channel_id:
        print(Fore.RED + "Kanal ID girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"DM Kanal bilgileri alınıyor (ID: {channel_id})..." + Style.RESET_ALL)
    headers = {"Authorization": token}
    try:
        response = requests.get(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
        if response.status_code == 200:
            dm_info = response.json()
            print(Fore.GREEN + "\n--- DM Kanal Bilgileri ---" + Style.RESET_ALL)
            print(Fore.CYAN + f"Kanal ID: {dm_info.get('id')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Kanal Tipi: {dm_info.get('type')} (1: DM, 3: Grup DM)" + Style.RESET_ALL)
            if dm_info.get('type') == 1 and dm_info.get('recipients'):
                recipient = dm_info['recipients'][0]
                print(Fore.CYAN + f"  Alıcı Kullanıcı Adı: {recipient.get('username')}#{recipient.get('discriminator')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Alıcı ID: {recipient.get('id')}" + Style.RESET_ALL)
            elif dm_info.get('type') == 3 and dm_info.get('recipients'):
                print(Fore.CYAN + "  Grup DM Katılımcıları:" + Style.RESET_ALL)
                for recipient in dm_info['recipients']:
                    print(Fore.CYAN + f"    - {recipient.get('username')}#{recipient.get('discriminator')} (ID: {recipient.get('id')})" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Grup Adı: {dm_info.get('name', 'Belirtilmemiş')}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "  Alıcı bilgisi bulunamadı veya grup DM değil." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"DM Kanal bilgileri alınamadı! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")


def discord_language_changer():
    print(Fore.MAGENTA + "\n[Discord Language Changer] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    language = input("Yeni Dil (örnek: tr, en-US): ").strip()
    if not language:
        print(Fore.RED + "Dil girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Dil '{language}' olarak değiştiriliyor..." + Style.RESET_ALL)
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"locale": language}
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"Dil başarıyla '{language}' olarak değiştirildi!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Dil değiştirilemedi! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_status_changer():
    print(Fore.MAGENTA + "\n[Discord Status Changer] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    status = input("Yeni Durum (online, idle, dnd, invisible): ").strip().lower()
    if status not in ["online", "idle", "dnd", "invisible"]:
        print(Fore.RED + "Geçersiz durum! Lütfen online, idle, dnd veya invisible girin." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Durum '{status}' olarak değiştiriliyor..." + Style.RESET_ALL)
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"status": status}
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"Durum başarıyla '{status}' olarak değiştirildi!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Durum değiştirilemedi! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_theme_changer():
    print(Fore.MAGENTA + "\n[Discord Theme Changer] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    theme = input("Yeni Tema (dark, light): ").strip().lower()
    if theme not in ["dark", "light"]:
        print(Fore.RED + "Geçersiz tema! Lütfen dark veya light girin." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Tema '{theme}' olarak değiştiriliyor..." + Style.RESET_ALL)
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"theme": theme}
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"Tema başarıyla '{theme}' olarak değiştirildi!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Tema değiştirilemedi! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_token_login_page_open():
    print(Fore.MAGENTA + "\n[Discord Token Login Page Open] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + "Token geçerliliği kontrol ediliyor ve Discord giriş sayfası açılıyor..." + Style.RESET_ALL)
    try:
        headers = {"Authorization": token}
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            print(Fore.GREEN + f"Token geçerli! Kullanıcı: {user_info.get('username')}#{user_info.get('discriminator')}" + Style.RESET_ALL)
            webbrowser.open("https://discord.com/login")
        else:
            print(Fore.RED + f"Token geçersiz veya bir hata oluştu! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_server_info():
    print(Fore.MAGENTA + "\n[Discord Server Info] Modülü çalışıyor..." + Style.RESET_ALL)
    token = load_from_data_folder("tokens.txt")
    if not token:
        token = input("Hedef Discord Token (data/tokens.txt'de yoksa): ").strip()
        if not token:
            print(Fore.RED + "Token girilmedi!" + Style.RESET_ALL)
            return

    guild_id = load_from_data_folder("servers.txt")
    if not guild_id:
        guild_id = input("Sunucu ID: ").strip()
        if not guild_id:
            print(Fore.RED + "Sunucu ID girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + "Sunucu bilgileri alınıyor..." + Style.RESET_ALL)
    headers = {"Authorization": token}
    try:
        response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers)
        if response.status_code == 200:
            server_info = response.json()
            print(Fore.GREEN + "\n--- Sunucu Bilgileri ---" + Style.RESET_ALL)
            print(Fore.CYAN + f"Adı: {server_info.get('name')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"ID: {server_info.get('id')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Sahip ID: {server_info.get('owner_id')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Üye Sayısı: {server_info.get('approximate_member_count', 'Bilinmiyor')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Açık Kanal Sayısı (Yaklaşık): {len(server_info.get('channels', []))}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Bölge: {server_info.get('region', 'Bilinmiyor')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Oluşturulma Tarihi: {server_info.get('joined_at', 'Bilinmiyor')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Doğrulama Seviyesi: {server_info.get('verification_level', 'Bilinmiyor')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Sunucu bilgileri alınamadı! Hata Kodu: {response.status_code}, Cevap: {response.json()}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_webhook_sender():
    print(Fore.MAGENTA + "\n[Discord Webhook Sender] Modülü çalışıyor..." + Style.RESET_ALL)
    webhook_url = load_from_data_folder("webhooks.txt")
    if not webhook_url:
        webhook_url = input("Webhook URL: ").strip()
        if not webhook_url:
            print(Fore.RED + "Webhook URL girilmedi!" + Style.RESET_ALL)
            return

    message = input("Gönderilecek Mesaj: ").strip()
    if not message:
        print(Fore.RED + "Mesaj girilmedi!" + Style.RESET_ALL)
        return

    payload = {"content": message}
    print(Fore.YELLOW + "Mesaj gönderiliyor..." + Style.RESET_ALL)
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print(Fore.GREEN + "Mesaj başarıyla gönderildi!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Mesaj gönderilemedi! Hata: {response.status_code}, {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def discord_webhook_info():
    print(Fore.MAGENTA + "\n[Discord Webhook Info] Modülü çalışıyor..." + Style.RESET_ALL)
    webhook_url = load_from_data_folder("webhooks.txt")
    if not webhook_url:
        webhook_url = input("Webhook URL: ").strip()
        if not webhook_url:
            print(Fore.RED + "Webhook URL girilmedi!" + Style.RESET_ALL)
            return

    print(Fore.YELLOW + "Webhook bilgileri alınıyor..." + Style.RESET_ALL)
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_info = response.json()
            print(Fore.GREEN + "\n--- Webhook Bilgileri ---" + Style.RESET_ALL)
            print(Fore.CYAN + f"ID: {webhook_info.get('id')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Adı: {webhook_info.get('name', 'Yok')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Avatar: {webhook_info.get('avatar', 'Yok')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Kanal ID: {webhook_info.get('channel_id')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Guild ID: {webhook_info.get('guild_id', 'Yok')}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Uygulama ID: {webhook_info.get('application_id', 'Yok')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Webhook bilgileri alınamadı! Hata Kodu: {response.status_code}, Cevap: {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def contact_info_lookup():
    print(Fore.MAGENTA + "\n[Contact Info Lookup (Email/Domain)] Modülü çalışıyor..." + Style.RESET_ALL)
    target = input("Hedef Email veya Domain (örnek: example@domain.com veya domain.com): ").strip()

    hunter_api_key = load_from_data_folder("hunter_io_api.txt")
    if not hunter_api_key:
        print(Fore.RED + "Uyarı: 'data/hunter_io_api.txt' bulunamadı. Email doğrulama ve domain araması kısıtlı olabilir." + Style.RESET_ALL)

    if not target:
        print(Fore.RED + "Hedef email veya domain girilmedi!" + Style.RESET_ALL)
        return

    is_email = "@" in target

    if is_email:
        print(Fore.YELLOW + f"Email '{target}' için bilgiler aranıyor..." + Style.RESET_ALL)
        if hunter_api_key:
            try:
                response = requests.get(f"https://api.hunter.io/v2/email-verifier?email={target}&api_key={hunter_api_key}")
                if response.status_code == 200:
                    data = response.json()["data"]
                    print(Fore.GREEN + f"  Email Durumu: {data['status'].upper()}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Güvenilirlik Puanı: {data['score']}/100" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Geçici Email: {'Evet' if data['disposable'] else 'Hayır'}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Rol Tabanlı: {'Evet' if data['role'] else 'Hayır'}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Kaynaklar: {', '.join(source['uri'] for source in data['sources']) if data['sources'] else 'Yok'}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"  API Hatası ({target}): {response.status_code}, {response.json().get('errors', [{}])[0].get('message', 'Bilinmeyen Hata')}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"  Email doğrulamada hata oluştu: {e}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "  Hunter.io API anahtarı olmadığı için email doğrulaması yapılamadı." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"Domain '{target}' için bilgiler aranıyor..." + Style.RESET_ALL)
        if hunter_api_key:
            try:
                response = requests.get(f"https://api.hunter.io/v2/domain-search?domain={target}&api_key={hunter_api_key}")
                if response.status_code == 200:
                    data = response.json()["data"]
                    print(Fore.GREEN + f"  Domain: {data['domain']}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Kurumsal Adı: {data.get('organization', 'Yok')}" + Style.RESET_ALL)
                    if data.get('emails'):
                        print(Fore.CYAN + "  Bulunan Email Adresleri:" + Style.RESET_ALL)
                        for email_entry in data['emails']:
                            print(Fore.LIGHTCYAN_EX + f"    - {email_entry['value']} (Tip: {email_entry['type']}, Güvenilirlik: {email_entry.get('score', 'Yok')})" + Style.RESET_ALL)
                            if email_entry.get('sources'):
                                print(Fore.MAGENTA + "      Kaynaklar:" + Style.RESET_ALL)
                                for source in email_entry['sources']:
                                    print(Fore.MAGENTA + f"        - {source.get('uri')}" + Style.RESET_ALL)
                    else:
                        print(Fore.YELLOW + "  Bu domain için email adresi bulunamadı." + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"  API Hatası ({target}): {response.status_code}, {response.json().get('errors', [{}])[0].get('message', 'Bilinmeyen Hata')}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"  Domain aramasında hata oluştu: {e}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "  Hunter.io API anahtarı olmadığı için domain araması yapılamadı." + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def email_breach_tracker():
    print(Fore.MAGENTA + "\n[Email Breach/Tracker (Email/Domain)] Modülü çalışıyor..." + Style.RESET_ALL)
    target = input("Hedef Email veya Domain: ").strip()

    hibp_api_key = load_from_data_folder("hibp_api.txt")
    if not hibp_api_key:
        print(Fore.RED + "Uyarı: 'data/hibp_api.txt' bulunamadı. Veri ihlali araması kısıtlı olabilir." + Style.RESET_ALL)

    if not target:
        print(Fore.RED + "Hedef email veya domain girilmedi!" + Style.RESET_ALL)
        return

    is_email = "@" in target
    headers = {'User-Agent': 'YourAppName', 'hibp-api-key': hibp_api_key}

    if is_email:
        print(Fore.YELLOW + f"Email '{target}' için veri ihlalleri aranıyor..." + Style.RESET_ALL)
        if hibp_api_key:
            try:
                response = requests.get(f"https://haveibeenpwned.com/api/v3/breaches?account={target}&truncateResponse=false", headers=headers)
                if response.status_code == 200:
                    breaches = response.json()
                    if breaches:
                        print(Fore.RED + f"\n--- '{target}' için Bulunan Veri İhlalleri ---" + Style.RESET_ALL)
                        for breach in breaches:
                            print(Fore.LIGHTRED_EX + f"  Adı: {breach.get('Title')}" + Style.RESET_ALL)
                            print(Fore.CYAN + f"  Tarih: {breach.get('BreachDate')}" + Style.RESET_ALL)
                            print(Fore.CYAN + f"  Açıklama: {breach.get('Description', 'Yok')}" + Style.RESET_ALL)
                            print(Fore.CYAN + f"  Veri Kategorileri: {', '.join(breach.get('DataClasses', []))}" + Style.RESET_ALL)
                            print(Fore.CYAN + f"  Web Sitesi: {breach.get('Domain', 'Yok')}\n" + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + f"'{target}' için bilinen bir veri ihlali bulunamadı." + Style.RESET_ALL)
                elif response.status_code == 404:
                    print(Fore.GREEN + f"'{target}' için bilinen bir veri ihlali bulunamadı." + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"API hatası (HIBP): {response.status_code}, {response.text}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Veri ihlali aramasında hata oluştu: {e}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Have I Been Pwned API anahtarı olmadığı için veri ihlali araması yapılamadı." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Domain için doğrudan ihlal araması desteklenmiyor. Lütfen bir email adresi girin." + Style.RESET_ALL)

    input("\nDevam için ENTER...")

def username_info_lookup():
    print(Fore.MAGENTA + "\n[Username Info Lookup] Modülü çalışıyor..." + Style.RESET_ALL)
    username = input("Hedef Kullanıcı Adı: ").strip()

    if not username:
        print(Fore.RED + "Kullanıcı adı girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"'{username}' için bilgi aranıyor..." + Style.RESET_ALL)

    social_sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "LinkedIn": f"https://www.linkedin.com/in/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}/"
    }

    results_found = False
    for site, url in social_sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"  {site}: Kullanıcı adı bulunuyor! URL: {url}" + Style.RESET_ALL)
                results_found = True
            elif response.status_code == 404:
                print(Fore.YELLOW + f"  {site}: Kullanıcı adı bulunamadı." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  {site}: Kontrol edilirken hata oluştu ({response.status_code})." + Style.RESET_ALL)
        except requests.exceptions.Timeout:
            print(Fore.RED + f"  {site}: Zaman aşımı hatası." + Style.RESET_ALL)
        except requests.exceptions.ConnectionError:
            print(Fore.RED + f"  {site}: Bağlantı hatası." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"  {site}: Beklenmeyen hata: {e}" + Style.RESET_ALL)

    if not results_found:
        print(Fore.YELLOW + f"'{username}' için popüler platformlarda bilgi bulunamadı. Daha fazla araştırma gerekebilir." + Style.RESET_ALL)

    input("\nDevam için ENTER...")

def phone_number_validation():
    print(Fore.MAGENTA + "\n[Phone Number Validation] Modülü çalışıyor..." + Style.RESET_ALL)
    phone_number = input("Hedef Telefon Numarası (örnek: +15551234567): ").strip()

    numlookup_api_key = load_from_data_folder("numlookupapi.txt")
    if not numlookup_api_key:
        print(Fore.RED + "Uyarı: 'data/numlookupapi.txt' bulunamadı. Telefon numarası doğrulama kısıtlı olabilir." + Style.RESET_ALL)

    if not phone_number:
        print(Fore.RED + "Telefon numarası girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Telefon numarası '{phone_number}' doğrulanıyor..." + Style.RESET_ALL)
    if numlookup_api_key:
        try:
            response = requests.get(f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey={numlookup_api_key}")
            if response.status_code == 200:
                data = response.json()
                if data.get('valid'):
                    print(Fore.GREEN + f"  Numara Geçerli: {phone_number}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Ülke: {data.get('country_name')} ({data.get('country_code')})" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Operatör: {data.get('carrier')}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"  Hat Tipi: {data.get('line_type')}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"  Numara Geçersiz veya Bilgi Bulunamadı: {phone_number}" + Style.RESET_ALL)
                    print(Fore.YELLOW + f"  Hata Mesajı: {data.get('error', {}).get('message', 'Bilinmeyen Hata')}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  API Hatası ({phone_number}): {response.status_code}, {response.json().get('error', {}).get('message', 'Bilinmeyen Hata')}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"  Telefon numarası doğrulamada hata oluştu: {e}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "  NumLookupAPI anahtarı olmadığı için telefon numarası doğrulaması yapılamadı." + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def ip_info_lookup():
    print(Fore.MAGENTA + "\n[IP Address Information] Modülü çalışıyor..." + Style.RESET_ALL)
    ip_address = input("Hedef IP Adresi (örnek: 8.8.8.8): ").strip()

    if not ip_address:
        print(Fore.RED + "IP adresi girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"IP adresi '{ip_address}' bilgileri aranıyor..." + Style.RESET_ALL)
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                print(Fore.GREEN + f"\n--- IP Bilgileri ({ip_address}) ---" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Ülke: {data.get('country')} ({data.get('countryCode')})" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Bölge: {data.get('regionName')} ({data.get('region')})" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Şehir: {data.get('city')}, {data.get('zip')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Koordinatlar: Lat {data.get('lat')}, Lon {data.get('lon')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Zaman Dilimi: {data.get('timezone')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  ISS: {data.get('isp')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Kuruluş: {data.get('org')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  AS Numarası/Adı: {data.get('as')}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  IP bilgileri alınamadı: {data.get('message', 'Bilinmeyen Hata')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"  API Hatası ({ip_address}): {response.status_code}, {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def domain_whois_lookup():
    print(Fore.MAGENTA + "\n[Domain Whois Lookup] Modülü çalışıyor..." + Style.RESET_ALL)
    domain = input("Hedef Domain Adı (örnek: example.com): ").strip()

    if not domain:
        print(Fore.RED + "Domain adı girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Domain '{domain}' için Whois bilgileri aranıyor..." + Style.RESET_ALL)
    try:
        print(Fore.YELLOW + "  Bu modül, ücretli veya ücretsiz API anahtarı gerektirebilir. Örnek bir sorgu yapılıyor..." + Style.RESET_ALL)
        whois_api_key = load_from_data_folder("whois_api.txt")
        if not whois_api_key:
            print(Fore.RED + "  Uyarı: 'data/whois_api.txt' bulunamadı. Whois sorgusu kısıtlı olabilir." + Style.RESET_ALL)
            print(Fore.YELLOW + "  Lütfen geçerli bir Whois API anahtarı sağlayın veya başka bir Whois servisi kullanın." + Style.RESET_ALL)
            return

        url = f"https://www.whoisxmlapi.com/whoisservers/WhoisService?apiKey={whois_api_key}&domainName={domain}&outputFormat=JSON"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get('WhoisRecord'):
                record = data['WhoisRecord']
                print(Fore.GREEN + f"\n--- Whois Bilgileri ({domain}) ---" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Domain Adı: {record.get('domainName')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Kayıt Oluşturulma Tarihi: {record.get('createdDate')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Son Güncelleme Tarihi: {record.get('updatedDate')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Bitiş Tarihi: {record.get('expiresDate')}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Kayıt Şirketi: {record.get('registrarName')}" + Style.RESET_ALL)

                registrant = record.get('registrant')
                if registrant:
                    print(Fore.CYAN + "\n  Registrant Bilgileri:" + Style.RESET_ALL)
                    print(Fore.CYAN + f"    Adı: {registrant.get('name', 'Yok')}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"    Organizasyon: {registrant.get('organization', 'Yok')}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"    Email: {registrant.get('email', 'Yok')}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"    Telefon: {registrant.get('telephone', 'Yok')}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"    Ülke: {registrant.get('country', 'Yok')}" + Style.RESET_ALL)

                name_servers = record.get('nameServers', {}).get('hostNames', [])
                if name_servers:
                    print(Fore.CYAN + "\n  İsim Sunucuları (Name Servers):" + Style.RESET_ALL)
                    for ns in name_servers:
                        print(Fore.CYAN + f"    - {ns}" + Style.RESET_ALL)

            else:
                print(Fore.RED + f"  Whois bilgileri bulunamadı veya hata: {data.get('ErrorMessage', 'Bilinmeyen Hata')}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"  API Hatası ({domain}): {response.status_code}, {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")


def social_username_checker():
    print(Fore.MAGENTA + "\n[Social Media Username Checker] Modülü çalışıyor..." + Style.RESET_ALL)
    username = input("Kontrol edilecek Kullanıcı Adı: ").strip()

    if not username:
        print(Fore.RED + "Kullanıcı adı girilmedi!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"'{username}' kullanıcı adı sosyal medya platformlarında kontrol ediliyor..." + Style.RESET_ALL)

    social_platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Snapchat": f"https://story.snapchat.com/@{username}",
        "LinkedIn (public profile)": f"https://www.linkedin.com/in/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}/",
        "GitHub": f"https://github.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Telegram": f"https://t.me/{username}"
    }

    found_profiles = []
    for platform, url in social_platforms.items():
        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            if response.status_code == 200:
                if "page not found" not in response.text.lower() and \
                   "account suspended" not in response.text.lower() and \
                   "user not found" not in response.text.lower() and \
                   "oops! that page doesn't exist" not in response.text.lower():
                    found_profiles.append(f"{platform}: {url}")
                else:
                    print(Fore.YELLOW + f"  {platform}: Kullanıcı adı muhtemelen yok (İçerik analizi)." + Style.RESET_ALL)
            elif response.status_code == 404:
                print(Fore.YELLOW + f"  {platform}: Kullanıcı adı bulunamadı (HTTP 404)." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  {platform}: Kontrol edilirken hata oluştu (HTTP {response.status_code})." + Style.RESET_ALL)
        except requests.exceptions.Timeout:
            print(Fore.RED + f"  {platform}: Zaman aşımı hatası." + Style.RESET_ALL)
        except requests.exceptions.ConnectionError:
            print(Fore.RED + f"  {platform}: Bağlantı hatası." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"  {platform}: Beklenmeyen hata: {e}" + Style.RESET_ALL)
        time.sleep(0.5)

    if found_profiles:
        print(Fore.GREEN + f"\n--- '{username}' için Bulunan Sosyal Medya Profilleri ---" + Style.RESET_ALL)
        for profile in found_profiles:
            print(Fore.GREEN + f"  {profile}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"'{username}' için bilinen sosyal medya platformlarında aktif bir profil bulunamadı." + Style.RESET_ALL)

    input("\nDevam için ENTER...")

def file_hash_analyzer():
    print(Fore.MAGENTA + "\n[File Hash Analysis] Modülü çalışıyor..." + Style.RESET_ALL)
    file_path = input("Analiz edilecek dosyanın yolu: ").strip()

    if not os.path.exists(file_path):
        print(Fore.RED + "Belirtilen dosya bulunamadı!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"'{file_path}' dosyasının hash değerleri hesaplanıyor..." + Style.RESET_ALL)

    try:
        md5_hash = hashlib.md5()
        sha1_hash = hashlib.sha1()
        sha256_hash = hashlib.sha256()

        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
                sha1_hash.update(chunk)
                sha256_hash.update(chunk)

        print(Fore.GREEN + "\n--- Dosya Hash Bilgileri ---" + Style.RESET_ALL)
        print(Fore.CYAN + f"  MD5:    {md5_hash.hexdigest()}" + Style.RESET_ALL)
        print(Fore.CYAN + f"  SHA1:   {sha1_hash.hexdigest()}" + Style.RESET_ALL)
        print(Fore.CYAN + f"  SHA256: {sha256_hash.hexdigest()}" + Style.RESET_ALL)

        print(Fore.YELLOW + "\nBu hash değerlerini VirusTotal gibi platformlarda arayarak kötü amaçlı yazılım olup olmadığını kontrol edebilirsiniz." + Style.RESET_ALL)

        virustotal_api_key = load_from_data_folder("virustotal_api.txt")
        if virustotal_api_key:
            print(Fore.YELLOW + "\nVirusTotal üzerinde otomatik arama yapılıyor (API anahtarı mevcut)..." + Style.RESET_ALL)
            vt_url = f"https://www.virustotal.com/api/v3/files/{sha256_hash.hexdigest()}"
            vt_headers = {
                "x-apikey": virustotal_api_key,
                "User-Agent": "YourPythonApp"
            }
            vt_response = requests.get(vt_url, headers=vt_headers)
            if vt_response.status_code == 200:
                vt_data = vt_response.json()
                attributes = vt_data['data']['attributes']
                last_analysis_stats = attributes.get('last_analysis_stats', {})
                malicious_count = last_analysis_stats.get('malicious', 0)
                undetected_count = last_analysis_stats.get('undetected', 0)
                total_engines = sum(last_analysis_stats.values())

                print(Fore.GREEN + "\n--- VirusTotal Analiz Sonucu ---" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Algılanan Kötü Amaçlı: {malicious_count} / {total_engines} motor" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Algılanmayan: {undetected_count} / {total_engines} motor" + Style.RESET_ALL)
                print(Fore.CYAN + f"  İlk Gönderim Tarihi: {time.ctime(attributes.get('first_submission_date', 0))}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  Son Analiz Tarihi: {time.ctime(attributes.get('last_analysis_date', 0))}" + Style.RESET_ALL)
                print(Fore.CYAN + f"  VirusTotal Rapor URL: https://www.virustotal.com/gui/file/{sha256_hash.hexdigest()}/detection" + Style.RESET_ALL)
            elif vt_response.status_code == 404:
                print(Fore.YELLOW + "  Dosya VirusTotal'de bulunamadı (yeni olabilir)." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  VirusTotal API hatası: {vt_response.status_code}, {vt_response.text}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "  VirusTotal API anahtarı 'data/virustotal_api.txt' içinde bulunamadı. Otomatik arama yapılamadı." + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + "Dosya bulunamadı. Lütfen doğru yolu girin." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")

def exif_data_extractor():
    print(Fore.MAGENTA + "\n[Image/File EXIF Data Extractor] Modülü çalışıyor..." + Style.RESET_ALL)
    file_path = input("EXIF verisi çekilecek resim dosyasının yolu: ").strip()

    if not os.path.exists(file_path):
        print(Fore.RED + "Belirtilen dosya bulunamadı!" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"'{file_path}' dosyasından EXIF verileri çekiliyor..." + Style.RESET_ALL)

    try:
        image = Image.open(file_path)
        exifdata = image.getexif()

        if not exifdata:
            print(Fore.YELLOW + "Bu resimde EXIF verisi bulunamadı." + Style.RESET_ALL)
            image.close()
            input("\nDevam için ENTER...")
            return

        print(Fore.GREEN + "\n--- EXIF Verileri ---" + Style.RESET_ALL)
        for tag_id, value in exifdata.items():
            tag_name = ExifTags.TAGS.get(tag_id, tag_id)
            if tag_name == "GPSInfo":
                print(Fore.CYAN + "  GPS Bilgisi:" + Style.RESET_ALL)
                for key, val in value.items():
                    gps_tag_name = ExifTags.GPSTAGS.get(key, key)
                    print(Fore.MAGENTA + f"    {gps_tag_name}: {val}" + Style.RESET_ALL)
            else:
                print(Fore.CYAN + f"  {tag_name}: {value}" + Style.RESET_ALL)
        
        image.close()

    except FileNotFoundError:
        print(Fore.RED + "Dosya bulunamadı. Lütfen doğru yolu girin." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"EXIF verisi çekilirken hata oluştu: {e}" + Style.RESET_ALL)
    input("\nDevam için ENTER...")


def proxy_scraper():
    print(Fore.MAGENTA + "\n[Proxy Scraper] Modülü çalışıyor..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Ücretsiz proxy listeleri toplanıyor. Bu proxy'lerin güvenilirliği ve çalışma garantisi yoktur." + Style.RESET_ALL)
    
    proxy_sites = [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/proxy4free/proxy-list/main/proxy.txt",
        "https://raw.githubusercontent.com/Uptobox/proxy-list/master/proxy.txt",
    ]
    
    all_proxies = set()
    
    for url in proxy_sites:
        try:
            print(Fore.CYAN + f"  Proxy kaynağı çekiliyor: {url}" + Style.RESET_ALL)
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies = response.text.splitlines()
                for proxy in proxies:
                    proxy = proxy.strip()
                    if proxy and ":" in proxy:
                        all_proxies.add(proxy)
                print(Fore.GREEN + f"  {len(proxies)} proxy çekildi. Toplam: {len(all_proxies)}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  Proxy çekilemedi ({url}): HTTP {response.status_code}" + Style.RESET_ALL)
        except requests.exceptions.Timeout:
            print(Fore.RED + f"  Zaman aşımı hatası ({url})." + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"  Bağlantı hatası ({url}): {e}" + Style.RESET_ALL)
        time.sleep(1)

    if all_proxies:
        output_file = os.path.join('data', 'proxies.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            for proxy in all_proxies:
                f.write(proxy + "\n")
        print(Fore.GREEN + f"\nToplam {len(all_proxies)} adet proxy 'data/proxies.txt' dosyasına kaydedildi." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Hiç proxy bulunamadı." + Style.RESET_ALL)

    input("\nDevam için ENTER...")

def main():
    while True:
        banner()
        choice = input(Fore.YELLOW + "Seçiminizi yapın: " + Style.RESET_ALL).strip()

        if choice == '1':
            discord_token_analyzer()
        elif choice == '2':
            discord_invite_checker()
        elif choice == '3':
            discord_send_single_message()
        elif choice == '4':
            discord_token_info()
        elif choice == '5':
            discord_server_membership_check()
        elif choice == '6':
            discord_dm_info()
        elif choice == '7':
            discord_language_changer()
        elif choice == '8':
            discord_status_changer()
        elif choice == '9':
            discord_theme_changer()
        elif choice == '10':
            discord_token_login_page_open()
        elif choice == '11':
            discord_server_info()
        elif choice == '12':
            discord_webhook_sender()
        elif choice == '13':
            discord_webhook_info()
        elif choice == '14':
            contact_info_lookup()
        elif choice == '15':
            email_breach_tracker()
        elif choice == '16':
            username_info_lookup()
        elif choice == '17':
            phone_number_validation()
        elif choice == '18':
            ip_info_lookup()
        elif choice == '19':
            domain_whois_lookup()
        elif choice == '20':
            social_username_checker()
        elif choice == '21':
            file_hash_analyzer()
        elif choice == '22':
            exif_data_extractor()
        elif choice == '23':
            proxy_scraper()
        elif choice == '0':
            print(Fore.RED + "Çıkış yapılıyor..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Geçersiz seçim, lütfen tekrar deneyin." + Style.RESET_ALL)
            time.sleep(1)

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
        print(Fore.YELLOW + "'data' klasörü oluşturuldu. API anahtarlarınızı ve diğer verileri buraya kaydedebilirsiniz." + Style.RESET_ALL)
    
    required_files = ["tokens.txt", "servers.txt", "webhooks.txt", "hunter_io_api.txt", "numlookupapi.txt", "hibp_api.txt", "whois_api.txt", "virustotal_api.txt", "proxies.txt"]
    for filename in required_files:
        filepath = os.path.join('data', filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                pass
            print(Fore.YELLOW + f"'{filepath}' dosyası oluşturuldu." + Style.RESET_ALL)

    main()