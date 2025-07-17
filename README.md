# 🔥 SBv4.2.py — Scambak: Insult Generator & Player for Termux on Android

*“Developed by the BGGremlin Group — Creating Unique Tools for Unique Individuals”*


---

# 📜 Description

SBv4.2.py is not your grandma’s Python script.

This is a fierce, unapologetic, and brutally honest tool built for scambaiters, hacktivists, and justice-fueled digital rebels who don’t just want to waste a scammer’s time—they want to roast them into next week. 🔥

Using high-octane insult packs spoken via Google Text-to-Speech (gTTS) and blasted through Termux like a megaphone of shame, this CLI weapon delivers profanity-laced cultural payloads designed to humiliate, demoralize, and expose scammers across the globe.

If you’ve ever wanted to tell a scammer where to shove it—in a hundred regional dialects, poetic burns, and multi-generational curses—this is your tool.


---

# ⚙️ Features

✅ 100+ custom-crafted, regionally-roasted desi insults
✅ Spoken aloud using gTTS in Hindi/English
✅ Fully CLI-operated with intuitive menu (no command-line args!)
✅ Easily extendable insult packs (supports JSON and in-code)
✅ Logs all actions to ~/.scambait.log
✅ Persistent configuration system (.scambait_config.json)
✅ Interactive menu with Termux-native controls
✅ Designed for Termux + Android, with storage support


---

# 💣 Use Cases

📞 When scammers call you for the 8th time this week

🎙️ When you want to send an audio file full of verbal destruction

🎧 When you just want to vibe and hear someone get verbally dissected

💻 When you’re training the next generation of scambaiters in the art of verbal evisceration



---

# 🧪 Installation

Make sure you're on Android with Termux. Then:

pkg update
pkg install python git ffmpeg -y
pip install gTTS termcolor
termux-setup-storage

Clone or copy the script into a working folder:

mkdir ~/scambak
mv SBv4.2.py ~/scambak/
cd ~/scambak
chmod +x SBv4.2.py
./SBv4.2.py


---

# 🎤 Audio Output

By default, the script uses gTTS to convert insults to .mp3 and plays them directly using termux-media-player or play. Make sure ffmpeg or audio player support is enabled on your Termux install.

If needed:

pkg install sox -y


---

# 🧱 Folder Structure

The program creates and uses:

~/.scambait_config.json — Stores chosen insult packs

~/.scambait.log — Detailed logs for actions/plays/errors

Optional insult packs stored inside the script for now — full external JSON support coming in v5.x


---

# 🚫 Warnings & Legal Stuff

> ⚠️ This script contains heavy profanity, explicit insults, and regional slurs.
It’s designed specifically for scammer-targeted responses in controlled scambaiting operations. Use responsibly. Do not direct this toward innocent individuals.


---

# 🛠 Roadmap

[ ] External JSON insult pack loader

[ ] Language switching (multilingual packs)

[ ] Voice pack selector

[ ] Loop mode & automated insult barrage

[ ] GUI frontend for Termux (Termux GUI API integration)



---

# 👑 Attribution

**Developed by: BGGremlin Group**
“Creating Unique Tools for Unique Individuals*


---

# 🧠 Cultural Note

The insults crafted in this tool pull from South Asian languages and cultural idioms. While they are offensive by design (that’s the point), they are targeted solely at scammers, designed to hit their psyche where it hurts most—family, legacy, and self-worth—and leverage linguistic authenticity for max effect.

This isn't just cussing. This is a fucking art form.


---

# 📦 Want to Contribute?

Pull requests, regional insult packs, localization contributions, or extended sound support are welcome. Ping the devs or fork it.
