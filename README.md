# Plants vs. Zombies — a fan remake

This is my from-scratch remake of Plants vs. Zombies, built as one big HTML file you can just open in a browser. It started as a "can I actually rebuild the lawn defense I grew up with" experiment and slowly turned into something I kept adding to — night levels, fog, a pile of zombie types, and eventually a whole 2-player mode where a friend gets to play as the zombies.

**Play it here:** https://annorang.github.io/pvz/

It runs on desktop or phone, no install, no accounts.

## What's in it

The single-player side is the game you'd expect. You plant Sunflowers to build up sun, drop Peashooters and Wall-nuts to hold the line, and try to survive the wave. There are 15 levels split across three settings that each change how you play. Daytime is the straightforward version where sun drifts down from the sky. At night the sky gives you nothing, so you lean on Sun-shrooms for economy and deal with graves scattered across the lawn that split open during the big wave. The fog levels keep the night rules but hide the right half of the board, so you either plant blind or use Planterns to burn the fog away.

Along the way you unlock most of the plants I actually cared about recreating — Snow Pea, Repeater, Cherry Bomb, Potato Mine, Chomper, Squash, Torchwood (which sets peas on fire as they pass through), Jalapeño, Tall-nut, and the mushrooms. The zombies range from the basic shambler up through Coneheads, Bucketheads, Pole Vaulters that jump your first plant, Footballs, Newspaper zombies that rage when you shred their paper, Jack-in-the-Boxes, Screen Doors, and Dancers that summon backup. Lawnmowers still bail you out once per row, and there's a little synth soundtrack with a few tracks you can flip between.

## The 2-player mode

This is the part I'm most attached to. Instead of the computer sending waves at you, a second person plays the zombies — and I didn't want them to just click "spawn" endlessly, so I gave the zombie side an economy borrowed from Battle Cats. Brains slowly refill on their own, and you can pour brains back into raising your income rate, so there's a real push-and-pull between saving up for a Buckethead now versus investing so you can afford two later. Each zombie has its own cost and cooldown, and you send them down whichever row you like.

To keep it fair, both sides are on a clock. If any zombie makes it into the house, the zombie player wins on the spot. If the plant player holds out until the timer runs out, the plants win. It reuses the normal levels, so the plants you get and the zombies your opponent can buy are tied to the same level — harder levels arm both sides more.

You can play it two ways: across two devices using a short game code, or local hotseat on one screen for testing. The tricky part was doing online multiplayer with no server, since the whole thing is meant to live on GitHub Pages for free. I ended up using WebRTC (through PeerJS) with one device running the actual game and streaming the state to the other — the code you share is really just the peer address. There's a longer write-up of how that works, plus all the balance numbers, in [MULTIPLAYER_README.md](MULTIPLAYER_README.md).

## Playing

Click a seed packet then a tile to plant, click sun to bank it, grab the shovel to dig something up. In versus, the zombie player clicks a zombie card then a row to send it, and buys Income upgrades to grow their brains faster over the match. `P` pauses (single-player), `M` mutes, `Esc` deselects.

## A couple of honest notes

It's a fan project, not affiliated with PopCap or EA — I made it because I love the original. The art falls back to simple drawn shapes if a sprite is missing, so it always runs. And the versus balance is my best first guess; if one side feels unfair, the numbers are all sitting in one spot at the top of the code, easy to tweak. If you play it and something feels off, I'd genuinely like to know.
