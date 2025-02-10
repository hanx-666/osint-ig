# Wkwk mau recode? ya ya ambil aja
# Tapi jan lupa kasih credit gw © HanX

import sys
import subprocess

# Auto-install module jika belum tersedia
try:
    import instaloader
except ModuleNotFoundError:
    print("\n\033[93m[!] Module 'instaloader' belum terinstal, menginstal sekarang...\033[0m\n")
    subprocess.run([sys.executable, "-m", "pip", "install", "instaloader"], check=True)
    import instaloader  # Import ulang setelah instalasi berhasil

def get_instagram_info(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"\n\033[32m[+] Informasi Akun Instagram: @{profile.username}\033[0m\n")
        print(f"ID                  : {profile.userid}")
        print(f"Nama Lengkap        : {profile.full_name}")
        print(f"Biografi            : {profile.biography}")
        print(f"URL Eksternal       : {profile.external_url}")
        print(f"Pengikut            : {profile.followers}")
        print(f"Mengikuti           : {profile.followees}")
        print(f"Jumlah Postingan    : {profile.mediacount}")
        print(f"Akun Bisnis         : {profile.is_business_account}")
        print(f"Akun Private        : {profile.is_private}")
        print(f"Akun Verified       : {profile.is_verified}")
        print(f"Punya Sorotan       : {profile.has_highlight_reels}")
        print(f"IGTV Post           : {profile.igtvcount}")
        print(f"Link Profil         : https://instagram.com/{profile.username}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"\033[91m[!] Username '{username}' tidak ditemukan.\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Terjadi kesalahan: {e}\033[0m")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\n\033[93m[!] Penggunaan: python hanx.py username_instagram\033[0m\n")
        sys.exit(1)

    username = sys.argv[1]
    get_instagram_info(username)
