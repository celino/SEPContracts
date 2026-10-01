# Contract Pack: Surface Experiment Package

[ContractConfigurator](https://github.com/KSP-RO/ContractConfigurator) contracts for the
[Surface Experiment Pack](https://github.com/CobaltWolf/Surface-Experiment-Pack) (SEP) on KSP 1.8–1.12.

The pack only offers what you can actually do: instruments come from
`AvailableExperiments(body)`, so an experiment is only asked for once its part is
unlocked in the tech tree and only on bodies where SEP allows it (Weather Scan needs an
atmosphere; Solar Wind and CCIG can't have one). Result levels (Basic / Detailed /
Exhaustive) follow SEP's calibration rules, which depend on the kerbal's profession and
level.

## Contracts

| Tier | Contract | Needs |
|---|---|---|
| 0 | **Deploy a SEP field station in *biome*** — Central Station + one instrument set up on the ground and linked, in a biome of the home world. One per biome. | `SEP_CentralStation`, `SEP_plug` and at least one instrument unlocked |
| 1 | **Expand the SEP station in *biome* to two instruments** — Central Station + two instruments linked, in a biome of the home world (expanding a tier-0 station counts). One per biome. | Tier 0 completed once, two instruments unlocked |
| 2 | **Plant a SEP station on the Mun or Minmus** — Central Station + one instrument linked, in a land biome of one of the home world's moons. One per biome. | Tier 0 completed, a landing on that moon, one instrument usable there |
| 3 | **Forecast the weather on Duna, Eve or Laythe** — Central Station + Weather Station + one more instrument. One per biome. | Tier 2 completed, a landing there, Weather Station usable |
| 3 | **Listen to the silence on Ike or Gilly** — Central Station + a vacuum instrument (Cold-Cathode Ion Gauge or Solar Wind Spectrometer) + one more instrument. One per biome. | Tier 2 completed, a landing there, a vacuum instrument usable |
| 4 | **The full package, anywhere airless** — Central Station + three instruments, at least one of them a vacuum instrument, on any airless world with a surface (planet packs included). Rewards scale with the destination, like stock contracts. One per biome. | A tier-3 contract completed, a landing there, three instruments usable |

**Upgrades** send you back to a station you already built and ask for one more instrument:

| Offered after | Contract | Station |
|---|---|---|
| Tier 1 | **Turn *station* into a research campus** — a third instrument | home world, two instruments |
| Tier 2 | **Go back to *station*** — a second instrument | the Mun or Minmus, one instrument |
| Tier 3 | **A return trip to *station*** — a third instrument | beyond the home system, two instruments |

The contracts are about building and linking the station, not about returning the
science: a SEP instrument takes 75–100 days to run, so the data is your reward once the
run finishes, not a contract parameter.

The instrument rules come from SEP itself: the Weather Station only works with an
atmosphere, the Cold-Cathode Ion Gauge and the Solar Wind Spectrometer only without one. Biomes that are mostly water are
never picked. A long-run survey tier (for example an Exhaustive PSE) is planned for a later
version.

## Requirements

- ContractConfigurator ≥ 2.13.4 **with the updated SEP experiment definitions**
  (`science/SurfaceExperimentPackage.cfg`, merged in
  [KSP-RO/ContractConfigurator#78](https://github.com/KSP-RO/ContractConfigurator/pull/78));
  older CC releases list experiment ids from 2016 that no longer exist, so no SEP
  experiment is ever "available". Until the next CC release, copy that file over
  `GameData/ContractConfigurator/science/SurfaceExperimentPackage.cfg`.
- Surface Experiment Pack 2.7.x, KIS, KAS ≥ 1.0 and the
  [SEP-KAS1-Patch](https://github.com/celino/SEP-KAS1-Patch) so the plugs can link
  (a linked instrument becomes part of the station's vessel, which the station
  parameters rely on).

## Install

Copy `GameData/ContractPacks/SEPContracts` into your `GameData`.

## Localization
All player-facing texts are in `Localization/` (`en-us`, `pt-br`). The contract cfgs call
`Format("#sepc.key", [ ... ])`, so the biome and body names are passed as `<<1>>`/`<<2>>`.
To add a language, copy `en-us.cfg`, rename the language node and translate the values.

## How this was made

This pack was written with the help of an AI assistant (Claude). I chose what to build,
reviewed every change and text, and tested each contract in game before release; any
mistakes are mine. Bug reports are welcome on the forum thread or on GitHub.

## License

MIT.
