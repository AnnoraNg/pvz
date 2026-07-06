# Plants vs. Zombies — 1P & 2P (Versus) Guide

This is a single-file HTML5 canvas game (`pvz.html`). It now has **two modes**, chosen on a new title screen:

- **1 Player** — the original campaign (Day / Night / Fog worlds, 15 levels). Unchanged.
- **2 Players (Versus)** — one player grows plants and defends; the other commands the zombies with a Battle-Cats-style economy and tries to reach the house.

No build step, no server code. It runs by opening `pvz.html`, and deploys to GitHub Pages as a static site.

---

## How 2-Player mode works

### The flow
Title screen → **2 Players** → lobby. Three ways to play:

1. **Host a Game** — creates a room and shows a 4-character code. Pick the level and which side you want (Plants or Zombies). Your opponent gets the other side. When they join, press **Start Match**.
2. **Join a Game** — enter the host's code. You get whichever side the host didn't take.
3. **Local (same screen)** — both players share one device (plants use the top bar, zombies the bottom bar). Great for testing without a second device.

The plant player picks a seed loadout (same "choose your plants" screen as solo). The zombie player's palette is fixed by the level.

### Win rules (survival timer)
- **Zombies win** the instant any zombie gets past the lawnmowers into the house.
- **Plants win** if they survive until the match timer (default **4 minutes**) runs out.
- Lawnmowers still act as a one-time-per-row safety net for the plant side.

### The zombie economy (the "Battle Cats" part)
- **Brains** regenerate automatically over time.
- The zombie player can spend brains on an **Income upgrade** to raise the regen rate (like the worker cat) — up to 6 levels.
- Zombies are bought from a **card palette**, each with its own brain cost and cooldown. Select a card, then click a **row** to send that zombie in from the right.
- There's an **8-second grace period** at the start so the plant player can set up before the horde can be released.

### Balance
2P uses the **same levels as 1P**: the level decides the plant loadout *and* which zombies the attacker can buy (the zombies that level normally spawns). Harder levels give the attacker stronger units, but the defender gets more plants too, so both sides scale together.

All balance knobs live in one place near the top of the script, in the `VS` object and the `ZCOST` table:

```js
const VS = {
  matchTime:   240,  // seconds the plant player must survive
  startBrains: 75,   // zombie player's opening brains
  baseRate:    7,    // brains/sec at income level 1
  ratePerLvl:  3.5,  // extra brains/sec per income upgrade
  incomeBase:  100,  // cost of the first income upgrade
  incomeStep:  75,   // added to income cost each level
  maxIncome:   6,
  brainCap:    900,
  spawnGrace:  8,    // seconds before zombies can be released
  startSun:    150,  // plant player's opening sun
};
```

Tune these numbers and reload — no other changes needed.

---

## Multiplayer architecture (how two devices stay in sync)

The transport is **WebRTC via [PeerJS](https://peerjs.com/)**, chosen so the game can be a **pure static site** (no backend to deploy or pay for).

### Host-authoritative model
```
        HOST device (room creator)                 GUEST device (joiner)
   ┌───────────────────────────────┐          ┌───────────────────────────┐
   │  runs the FULL game simulation │          │  renders snapshots only    │
   │  (plants, zombies, physics,    │  state   │  (never simulates)         │
   │   economy, win checks)         │ ───────► │                            │
   │                                │ ~20/sec  │                            │
   │  validates + applies inputs    │ ◄─────── │  sends input intents:      │
   │                                │  inputs  │  "plant here" / "spawn     │
   └───────────────────────────────┘          │   zombie row N" / "collect  │
                                               │   sun id" / "upgrade"      │
                                               └───────────────────────────┘
```

- **One machine (the host) is the single source of truth.** It runs the exact same deterministic tick loop the solo game uses.
- The host **broadcasts a compact JSON snapshot ~20 times/second** over a WebRTC data channel (plants, zombies, projectiles, suns, economy, timer — typically ~1 KB).
- The guest **never simulates**. It just paints the latest snapshot and sends **input intents** ("I clicked row 3 with a Conehead selected"). The host validates each intent against the real state (enough brains? off cooldown? cell empty?) and applies it. This makes desync impossible — there's only ever one game.

Because PvZ is slow and tick-based, 20 Hz is plenty smooth and bandwidth is tiny.

### What the "session code" is
- The host creates a PeerJS peer with the id `pvz2p-<CODE>` (e.g. `pvz2p-K7QP`).
- The guest connects to that id by typing the code.
- **PeerJS's free public broker is used only for the initial handshake** (exchanging connection info). Once connected, game traffic flows **directly device-to-device** — it does not pass through any server we run.

### Trade-offs / limitations of this choice
- Relies on PeerJS's free public signaling broker being up. If you want production reliability, you can later self-host a tiny PeerServer or swap in a WebSocket relay — the game logic wouldn't change, only `netHost` / `netJoin`.
- WebRTC occasionally can't punch through strict corporate/symmetric NATs or firewalls without a TURN server (the public broker includes a limited free STUN/TURN). For two home/mobile networks it's usually fine.
- Both players must be online at the same time (it's real-time, not async).

---

## Deploying to GitHub Pages (step by step)

Because everything is static (one HTML file + the `assets/` folder + the PeerJS CDN script), GitHub Pages hosts it directly.

1. **Create a repo** on GitHub, e.g. `pvz`.
2. **Push these files** to it (keep the folder structure):
   ```
   pvz.html
   assets/            (all the .png sprites)
   MULTIPLAYER_README.md
   ```
   From the project folder:
   ```bash
   git init
   git add pvz.html assets
   git commit -m "PvZ fan remake with 1P + 2P versus"
   git branch -M main
   git remote add origin https://github.com/<you>/pvz.git
   git push -u origin main
   ```
3. *(Recommended)* Rename `pvz.html` to **`index.html`** so the game opens at the site root. Or leave it and visit `.../pvz.html`.
4. On GitHub: **Settings → Pages → Build and deployment → Source: “Deploy from a branch”**, pick **`main`** branch and **`/ (root)`**, then **Save**.
5. Wait ~1 minute. Your game is live at:
   ```
   https://<you>.github.io/pvz/            (if you renamed to index.html)
   https://<you>.github.io/pvz/pvz.html    (otherwise)
   ```
6. **Must be served over HTTPS** for WebRTC to work — GitHub Pages already is, so you're good. (Opening the file locally with `file://` works for solo and *local* 2P, but online 2P needs `https://` or `http://localhost`.)

### Testing multiplayer
- Open the Pages URL on two devices (or two browser windows). On one, **Host** and read the code. On the other, **Join** and type the code. 
- To test on a single machine first, use **Local (same screen)**, or open two browser tabs and Host in one / Join in the other.

---

## Files
- `pvz.html` — the entire game (solo + versus + networking).
- `assets/` — sprites (the game falls back to vector art if any are missing).
- The only external dependency is the PeerJS library, loaded from a CDN in the `<head>`:
  `https://unpkg.com/peerjs@1.5.4/dist/peerjs.min.js`

*Fan remake — not affiliated with PopCap/EA.*
