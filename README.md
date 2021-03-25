MTG Pack Generator

A simple Python script for randomly generating 15-card MTG boosters of a given set.


To use:

After cloning, download the bulk data from Scryfall [here](https://scryfall.com/docs/api/bulk-data).
Default Cards is preferable, but the smaller Oracle Cards will work just fine for the newest set.

Run the script:

  python3 \<generator/filepath\> \<bulk/JSON/filepath\> \<set-abbreviation(lowercase)\> \<packs-quantity\>

The packs-quantity argument is optional and will default to 1 if left out.
For example, generating a Kaldheim pack might look something like this:

  python3 generate_pack.py ../scryfall-data/default-cards.json khm

...and generating six Core Set 2015 packs like this:

  python3 generate_pack.py bulk-data/default-cards.json m15 6

Note:

The distribution of card rarities is that of current boosters:

  1 Rare/Mythic<br />
  3 Uncommons<br />
  10 Commons<br />
  1 Basic Land

The Basic Land was left in partly for whimsy, but mostly as a stand-in for
Snow-Covered Lands in relevant sets. If generating packs for drafting or
playing sealed with one of these sets, understand that these Lands represent
your Snow-Covered Lands.

