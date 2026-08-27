# Importer masteroppgave-litteratur til Zotero

Jeg har ikke direkte tilgang til Zotero-biblioteket ditt, men filen ligger i:

```
oslomet/masterthesis/master_thesis_zotero.bib
```

**Viktig:** Masteroppgaven skrives på **engelsk**, men **norsk litteratur er inkludert** der den er relevant (SSB, NSM, Helsedirektoratet, norske studier osv.). I thesis-teksten siterer du dem på engelsk (oversatte titler); i Zotero kan du beholde norske titler i `note`-feltet.

## APA 7 (Kildekompasset)

Referanselisten i thesis er formatert etter **APA 7** i tråd med [Kildekompasset](https://www.kildekompasset.no/regler/hvordan-skal-litteraturlista-se-ut-2/):

- Alfabetisk sortering etter forfatter
- Hengende innrykk i litteraturlista
- DOI som `https://doi.org/...` der tilgjengelig
- Nettsider: `Retrieved [dato] from [URL]`
- Norske kilder: titler oversatt til engelsk i thesis-tekst; institution navn beholdt

Importer `.bib` til Zotero og bruk **APA 7th edition** som stil. Verifiser at Zotero-output matcher Kildekompasset før endelig innlevering.

## Slik importerer du (2 minutter)

1. Åpne **Zotero**
2. Gå til **File → Import**
3. Velg filen `master_thesis_zotero.bib`
4. Velg **Place imported collection in new collection**
5. Gi samlingen navnet: `Master Thesis - Phishing and Loneliness`
6. Klikk **Import**

## Filtrer norsk litteratur i Zotero

Alle norske kilder er tagget `norwegian-literature`. I Zotero:

1. Klikk på samlingen
2. Søk i biblioteket: `tag:norwegian-literature`

## Slik siterer du norsk litteratur på engelsk (APA 7)

Eksempel i thesis-teksten:

> Statistics Norway (2025) found that 14.5% of adults report being quite or very troubled by loneliness...

I referanselisten (engelsk):

> Statistics Norway. (2025). *How many people feel lonely in Norway?* Livskvalitetsundersøkelsen 2025. https://www.ssb.no/...

Regler:
- **Institusjonsnavn på engelsk** (Statistics Norway, Norwegian Directorate of Health)
- **Tittel oversatt til engelsk**; original norsk tittel kan stå i parentes første gang
- **URL og årstall** som normalt

## Etter import (anbefalt)

1. **Høyreklikk** på samlingen → **Rename Collection** om du vil
2. For kilder med DOI: marker dem → **Right click → Find Available PDF**
3. Sjekk at sitestil er **APA 7th edition**
4. Vurder under-samling: `Norwegian context` (tag `norwegian-literature`)

## Hva som ligger i filen (ca. 48 kilder)

| Tema | Eksempler |
|------|-----------|
| **Norsk kontekst** | SSB 2025, Barstad 2021, FHI, Helsedirektoratet, SHoT, Khrono/NSO |
| **Norsk cybersikkerhet** | NSM 2026, Nettvett, Politiet, NSR Mørketall, Finans Norge, Nkom |
| **Norsk forskning phishing** | Tjostheim & Waterworth 2020/2022 (nasjonale utvalg i Norge) |
| **Studenter & ensomhet** | SiO, Samskipnaden, OsloMet Lunsjvenn |
| **Internasjonal kjerne** | Wen, Cacioppo, Hadnagy, Klütsch et al., Parker & Flowerday |
| **Metode** | Braun & Clarke 2006 |

## Merk

- `Klütsch et al. 2024` = korrekt forfatter for "Friend or phisher"
- Alle poster har taggen `master-thesis`
- Norske kilder har i tillegg `norwegian-literature`
- PDF-lenke: https://raw.githubusercontent.com/kasa031/Bacheloroppgave/cursor/master-phishing-forslag-d899/master_thesis_zotero.bib
- Alternativ (commit): https://raw.githubusercontent.com/kasa031/Bacheloroppgave/1ca76f2/master_thesis_zotero.bib
- GitHub visning: https://github.com/kasa031/Bacheloroppgave/blob/cursor/master-phishing-forslag-d899/master_thesis_zotero.bib
