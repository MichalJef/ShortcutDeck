[*EN-US*](https://github.com/MichalJef/ShortcutDeck/blob/main/README.md) / [**CS-CZ**](https://github.com/MichalJef/ShortcutDeck/blob/main/README_CZ.md)

---

# ShortcutDeck

![Project Image Placeholder](https://github.com/MichalJef/ShortcutDeck/blob/main/docs/ShortcutDeckLogo.png)

Jednoduchá, ale výkonná domácí makro klávesnice s mikrokontrolerem, obsahující 12 hot-swap kláves (F13–F24) a multifunkční rotační enkodér. Navrženo jako flexibilní, minimalistické a open-source.

## Funkce

### Rotační enkodér:
- **Otočení doprava:** Zvýšení hlasitosti / Další skladba *(v režimu přehrávání pouze 1 příkaz za 500 ms)*
- **Otočení doleva:** Snížení hlasitosti / Předchozí skladba *(stejné omezení)*
- **Krátké stisknutí:** Ztlumit / Přehrát–Pauza
- **Dvojité stisknutí:** Přepnutí mezi režimem Hlasitosti a Přehrávání

### Klávesy:
- 12 fyzických spínačů mapovaných na F13–F24
- Hot-swap sockety pro snadnou výměnu spínačů
- Možnost vlastních nebo tištěných keycapů

---

## Potřebné komponenty

### Elektronika:
- Raspberry Pi Pico (nebo kompatibilní mikrokontroler — vyžaduje úpravu kódu a zapojení)
- 1x rotační enkodér (ideálně Keyes KY-040)
- 12x mechanických spínačů (Kailh, Cherry MX atd.)
- 12x Hot-swap socketů
- ~36x female Dupont konektorů
- 13x 90° male Dupont konektorů (plus dle potřeby podle tvého mikrokontroleru, pokud je bez pinů)
- Dupont konektory:
  - 1x 7-pin  
  - 1x 6-pin  
  - 1x 5-pin  
  - 3x 4-pin  
  - 2x 2-pin  
  - 2x 1-pin
- 18x vodičů, každý 95 mm, 26AWG (~2m celkem, klasický arduino propojovací vodič)
- Pájecí vybavení (mikropájka, cín, pryskyřice/tavidlo)

### 3D tištěné díly:
- K dispozici na [Printables](https://www.printables.com/model/1300028-shortcutdeck-printable-parts)
- 1x Horní kryt `Top`
- 1x Spodní kryt `Shell`
- 1x Otočný knoflík (hladký nebo s texturou) `Knob`
- 12x Keycapů *(volitelné, pokud nemáš vlastní)*  
- 4x Gumové nožky *(volitelné, nebo lze použít nábytkové samolepicí podložky)* `Feet`

### DPS a kompletace:
- 1x jednostranná cuprextitová deska 80x85mm (tloušťka 1.6mm, měď 0.35µm)
- Leptací roztok – chlorid železitý
- Fotomiska/podmiska či jiná nízká plastová nádoba (např. PP)
- Permanentní alkoholový fix (tloušťka 0.1–0.3 mm)
- Vrták 0.8 mm + další podle velikosti otvorů (podle [PDF](https://github.com/MichalJef/ShortcutDeck/blob/main/ShortcutDeck%20PCB%20v1.pdf))
- Brusný papír a alkohol (technický líh, ...) na čištění
- 4x šrouby (1–2 mm x 8–10 mm)

---

## Postup sestavení

### 1. Výroba DPS
1. Odřízni měděnou desku 80x85 mm.
2. Vytiskni rozložení DPS [PDF](https://github.com/MichalJef/ShortcutDeck/blob/main/ShortcutDeck%20PCB%20v1.pdf) a přilep ho na desku tyčinkovým lepidlem.
   - Zkontroluj měřítko pomocí označeného čtverečku 14x14 mm.
3. Vyznač všechny otvory důlčíkem a papír odlep.
4. Předvrtej otvory vrtákem 0.8 mm a dokonči správnými velikostmi.
5. Obrus povrch a vyčisti alkoholem.
6. Ručně nakresli spoje a plošky fixem.
7. Zahřej leptací roztok na cca 50°C  a nalij do nádoby.
8. Ponoř DPS na 10–20 minut (pravidelně kontroluj).
9. Odstraň fix alkoholem, zkontroluj spoje a změř odpor (cílem < 10kΩ).
10. Napájej konektory.

![Obrázek DPS](https://github.com/MichalJef/ShortcutDeck/blob/main/docs/PCB%20preview.jpg)

### 2. Zapojení a příprava mikrokontroleru

- Pokud máš Pico s headery (piny): opatrně sundej plastovou lištu a piny ohni do 90°.
- Pokud ne: napájej 90° konektory rovnou.
- Nakrimpuj a zapoj všechny Dupont konektory přesně podle schématu zapojení (pozor na správný pinout! Viz [dokumentace Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pinout-and-design-files-4)).
- Společný pin všech spínačů na DPS je GND, a zároveň začátek pinoutu 0–12.

![Schéma zapojení](https://github.com/MichalJef/ShortcutDeck/blob/main/docs/ShortcutDeck1.png)

```bash
00 - GND 
01 - GP28
02 - GP27
03 - GP26
04 - GP22
05 - GP21
06 - GP20
07 - GP19
08 - GP18
09 - GP17
10 - GP16
11 - GP15
12 - GP14
```

### 3. Sestavení

1. Vytiskni všechny 3D díly v libovolném materiálu a barvě. (Nožky doporučuji z flexibilního materiálu)
2. Vlož spínače do mřížky a připoj k DPS.
3. Umísti matku enkodéru do šestihranného otvoru a přišroubuj enkodér, piny by měly mířit doprava při pohledu shora.
4. DPS se spínači by měla přesně pasovat do horního krytu. (zespoda)
5. Umísti mikrokontroler do spodní části krytu. Micro USB port by to měl usnadnit.
6. Nakonec do sebe zasaď horní a spodní část do sebe a zajisti 4 šroubky. (Pokud mikrokontroler nedrží, improvizuj šroubem nebo páskou)
7. Nasaď otočný knoflík (knob) a přilep gumové nožky.

![Assembly Image Placeholder](https://github.com/MichalJef/ShortcutDeck/blob/main/docs/preview.png)

---

## Naprogramování

### CircuitPython:

1. Nahraj CircuitPython firmware na své pico (oficiální návod [zde](https://circuitpython.org/board/raspberry_pi_pico/)).
2. Zkopíruj svůj python kód `main.py` do kořenového adresáře mikrokontroleru.
3. Nainstaluj [potřebné knihovny](https://github.com/MichalJef/ShortcutDeck/tree/main/lib) do složky `/lib`.

### Debug & Úpravy:
- Použij **Thonny IDE** na nahrání, testování nebo ladění přes USB.
- Očekáváme že si uživatelé budou vytvářet vlastní úpravy - nebojte se je sdílet!
