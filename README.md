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

The contracts are about building and linking the station, not about returning the
science: a SEP instrument takes 75–100 days to run, so the data is your reward once the
run finishes, not a contract parameter.

More tiers (first station off-world, atmospheric bodies, long-run surveys such as an
Exhaustive PSE) are planned.

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

## License

MIT.
