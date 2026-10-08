# Changelog

What changed in each version of Contract Pack: Surface Experiment Package. Albert Kermin
Industries reads this file before signing anything; so should you.

## Unreleased

- No more copying a file into Contract Configurator by hand: a ModuleManager patch brings in
  the updated SEP experiment definitions (CC #78 and #79) until a CC release has them.
- Flown in a career save so far: tiers 0 and 1. Tiers 2–4 and the upgrade contracts load and
  pass the checks, but I haven't played them through yet.

## 0.4.0 (2026-10-01)

- **Tier 2:** plant a station on the Mun or Minmus.
- **Tier 3:** Duna, Eve or Laythe with the Weather Station; Ike or Gilly with a vacuum
  instrument (Cold-Cathode Ion Gauge or Solar Wind Spectrometer).
- **Tier 4:** three instruments on any airless world, with rewards scaled by the destination.
- **Upgrade contracts:** go back to a tier 1, 2 or 3 station, by name, and add one more
  instrument.
- The Solar Wind Spectrometer counts as a vacuum instrument.
- English and Brazilian Portuguese texts for all of the above.

## 0.3.0 (2026-09-27)

- All texts moved to `Localization/`, in English and Brazilian Portuguese.
- Biome filter works in any game language.
- Contract Configurator's auto-generated lines under the part checks are hidden, so the
  contract reads the same in every language.

## 0.2.0 (2026-09-21)

- Contracts are about building the station, not waiting for the science: a SEP run takes
  75–100 days, so the reward comes when the station is up and linked.
- Tier 1 asks for a station with two instruments (expanding the tier-0 station counts).
- A station that reloads a few centimetres above the ground ("flying") still counts as landed.

## 0.1.0 (2026-09-18)

- Tier 0: a field station in a biome of Kerbin.
- Tier 1: an exhaustive run of the Passive Seismometer.
