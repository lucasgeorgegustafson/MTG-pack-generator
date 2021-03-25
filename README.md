MTG Pack Generator

A simple Python script for randomly generating 15-card MTG boosters of a given set.


To use:

After cloning, download the bulk data (Oracle Cards) from scryfall [here](https://scryfall.com/docs/api/bulk-data).

Run the script:

  python \<generator/filepath\> \<bulk/JSON/filepath\> \<set-abbreviation(lowercase)\>

For example, generating a Kaldheim pack might look something like this:

  python generate_pack.py ../scryfall-data/oracle-cards.json khm


Note:

The distribution of card rarities is that of current boosters:

  1 Rare/Mythic
  3 Uncommons
  10 Commons
  1 Basic Land

The Basic Land was left in partly for whimsy, but mostly as a stand-in for
Snow-Covered Lands in relevant sets. If generating packs for drafting or
playing sealed with one of these sets, understand that these Lands represent
your Snow-Covered Lands.

If requested to generate a pack from a set without rares (or with few rares),
the script will generate a pack with four uncommons. Because the Oracle Cards
bulk JSON only lists the set of a cards most recent printing, the card pool
currently shrinks as the requested set grows older. So requesting an
anachronistic 15 pack booster from Beta, for example, currently prints:

Camouflage
Camouflage
Camouflage
Camouflage
False Orders
False Orders
False Orders
False Orders
False Orders
False Orders
False Orders
False Orders
False Orders
False Orders
Plains

A request for an Alpha pack fails entirely.

This bug will be fixed soon, at which point the correct Scryfall bulk JSON
file will be Default Cards.
