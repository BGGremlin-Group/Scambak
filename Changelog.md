# 📓 CHANGELOG.md
> Scambak Insult Generator  
> Developed by BGGremlin Group  
> Creating Unique Tools for Unique Individuals

---

## [v4.2.0] - 2025-07-17
### 🔥 Major Release
- Finalized production-grade CLI for Termux and Desktop
- Modular config and log paths using `Pathlib`
- Colorful banner and option flow redesigned
- Full insult lifecycle: translate → speak → save → replay
- Termux-aware audio fallback: `termux-media-player` or `termux-tts-speak`
- Robust error handling and cross-platform playback detection
- Cleanly formatted logging and config file (`.scambait_config.json` & `.scambait.log`)
- Updated branding to full **Scambak** name

---

## [v4.0.0] - 2025-07-10
### 🧱 Infrastructure Upgrade
- Renamed to `SBv4.py` (Scambak)
- Introduced insult **packs** (Pack1, Pack2, Pack3) inside dictionary structures
- Transplanted 100+ culturally roasted, region-specific Hindi insults
- Refactored functions for translation, saving, playing, and generating
- Implemented JSON-based configuration pathing
- Setup groundwork for external insult pack loaders (v5+)

---

## [v3.5.x – v3.8.5] - June 2025
### 🎯 Mid-Life Expansion
- Added PRESET insult pool with randomized generation
- Improved user prompts, input validation, and playback reliability
- Introduced `random.choice()` flow
- Hardened against bad inputs and added structured main loop
- Upgraded menu navigation and banner styling
- Experimental Termux compatibility baked in

---

## [v2.x] - May 2025
### 📱 Android Compatibility Pass
- Migrated media player handling to Termux’s ecosystem
- Added fallback for `termux-tts-speak`
- Built cross-platform awareness for audio execution
- Replaced brittle OS-dependent audio logic

---

## [v1.0.0] - April 2025
### 💡 Project Genesis
- Raw CLI insult generator with gTTS playback
- Input to Hindi translation pipeline
- Single hardcoded insult paragraph
- No persistence, no file saving
- Just pure spite, audio, and script chaos

---

## 🚧 Planned for v5.x
- External insult pack loader via JSON
- gTTS voice selector or clone integration
- Multilingual insult cycling
- Auto-barrage mode (loop insult packs)
- GUI frontend for Termux GUI or desktop tkinter
- MP3 naming by timestamp or hash
- Full packaging for `.deb` and `.exe` deployment

---
# BGGG ***Creating Unique Tools for Unique Individuals***
