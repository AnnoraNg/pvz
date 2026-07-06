# 🌻 Plants vs. Zombies — Fan Remake 🧟

A single-file HTML5 canvas remake of Plants vs. Zombies, with a full solo campaign **and** a 2-player online versus mode.

### ▶ Play it live
**https://annorang.github.io/pvz/**

No install, no sign-up — it runs in the browser. Works on desktop and mobile.

---

## Game modes

Pick a mode on the title screen:

### ☀ 1 Player
The classic campaign — **15 levels** across three worlds:
- **Day** — sun falls from the sky; build your economy with Sunflowers.
- **Night** — no sky sun; grow Sun-shrooms, and watch for graves that crack open.
- **Fog** — night rules plus fog hiding the right side of the lawn; light it with Planterns.

Features 17 plants (Peashooter, Wall-nut, Snow Pea, Cherry Bomb, Chomper, Torchwood, Jalapeño, mushrooms and more) and a dozen zombie types (Coneheads, Buckets, Pole Vaulters, Football, Jack-in-the-Box, Screen Doors, Dancers…), lawnmower saves, huge waves, and 4 selectable music tracks.

### ⚔ 2 Players (Versus)
One player **defends with plants**, the other **commands the zombies**:
- The zombie player runs a **Battle-Cats-style economy** — "brains" regenerate over time and can be reinvested to raise the income rate, then spent to send zombies (each with its own cost and cooldown) down any row.
- **Win condition (survival timer):** any zombie that reaches the house = **zombies win**; if the plants survive until the timer runs out = **plants win**.
- Play **across two devices** with a 4-character game code, or **local hotseat** on one screen.

See **[MULTIPLAYER_README.md](MULTIPLAYER_README.md)** for how the networking and balancing work.

---

## How to play

**Plant side**
- Click a seed packet, then click a lawn tile to plant (costs sun).
- Click falling **sun** to collect it. Use the **shovel** to remove a plant.

**Zombie side (versus)**
- Click a zombie card, then click a **row** to send it in from the right.
- Buy **Income** upgrades to grow your brain income over the match.

**Keys:** `P` pause (solo) · `M` mute · `Esc` deselect.

---

## Tech notes
- Pure static site: one HTML file + `assets/` sprites. Falls back to built-in vector art if a sprite is missing.
- Multiplayer uses **WebRTC via PeerJS** (host-authoritative), so there's no backend — it deploys straight to GitHub Pages.
- The only external dependency is the PeerJS library, loaded from a CDN.

*A fan remake — not affiliated with PopCap or EA.*
