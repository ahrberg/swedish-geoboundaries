# Swedish geographical boundaries

## Why?

In many projects I have been involved in developing Web and Mobile apps where access to open geographical data with boundaries have been an issue. Open data exist in Sweden shared by [SBC](https://www.scb.se) (Statistiska Centralbyrån) and by [Lantmäteriet](https://www.lantmateriet.se) but this data does not well represent common areas that people are used to. Regions (län), municipality's (kommun) and districts (distrikt) are defined and shared by SCB and Lantmäteriet. Regions and municipality's are well known by people and could be used, this boundaries are large. When municipality's are divided the defined districts are not always the representation of areas people use today. This project aims to define boundaries more commonly used and well known to people.

## Goal

The goal is to have geodata for a division (no overlapping boundaries) of the Swedish municipality's that are well known by the people living in the area and corresponds to the modern division of the municipality's and the city's. The goal is not to get a totally acuate representation rather something that is good enough for general purpose use. Each boundary should reference a region and a municipality.

## Strategy

1. `DONE` Use the [district division](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/oppna-data/#faq=b82a) that is shared by Lantmäteriet under the [CC0 Licence](https://creativecommons.org/publicdomain/zero/1.0/legalcode) as the starting point.
2. `DONE` Add the regions and municipality's as attributed to the districts. This may not be 100% actuate. [Source](https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Sveriges_distrikt)
3. Merge/modify districts to represent well known municipality's/city boundaries. The source from this may differ and sometimes be guessed by best effort.
4. Continue this according to [people population](https://www.scb.se/hitta-statistik/statistik-efter-amne/befolkning/befolkningens-sammansattning/befolkningsstatistik/pong/tabell-och-diagram/topplistor-kommuner/folkmangd-topp-50/)

## TODO

| Municipality  | Done date  |
| ------------- | ---------- |
| ~~Stockholm~~ | 2020-04-03 |
| ~~Göteborg~~  | 2020-04-03 |
| ~~Malmö~~     | 2020-04-03 |
| ~~Uppsala~~   | 2020-04-04 |
| Linköping     |            |
| Örebro        |            |
| Västerås      |            |
| Helsingborg   |            |
| Norrgköping   |            |
| Jönköping     |            |
| Umeå          |            |
| ...           |            |

## Contribute

Please contribute if you like!

## License

Distributed under CC0 License. Please reference this project if you use it.

Material from Lantmäteriet are used in this project under the CC0 Licence.
