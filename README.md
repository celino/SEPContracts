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
| 0 | **Deploy a SEP field station in *biome*** — Central Station + one instrument landed in a biome of the home world, basic data returned or transmitted. One per biome. | `SEP_CentralStation`, `SEP_plug` and at least one instrument unlocked |
| 1 | **Exhaustive seismic survey of *biome*** — Passive Seismic Experiment run to Exhaustive in a biome of the home world. One per biome. | Tier 0 completed once, `SEP_PSE`, a scientist on the roster |

More tiers (first station off-world, N-instrument stations, exhaustive surveys of the
other instruments, atmospheric bodies) are planned.

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

## License

MIT.
