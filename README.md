MTG Pack Generator

A program for generating 15-card MTG boosters of a given set.


To use:

After cloning, download the bulk data from Scryfall [here](https://scryfall.com/docs/api/bulk-data).
Default Cards is preferable; the smaller Oracle Cards will work just fine for the newest set and
decreasingly well for older sets.

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

The "generators" are distinct defined types, not to be confused with the Python generator type.
Each set gets its own generator. Kaldheim's generator is the only one written so far, and it
could use some work probably (collation may be insufficiently handled). Go to it.
