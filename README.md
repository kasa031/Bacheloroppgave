# Cybersikkerhet – informasjonsnettside

**GitHub:** [kasa031/Bacheloroppgave](https://github.com/kasa031/Bacheloroppgave)  
**Live nettside (GitHub Pages):** [kasa031.github.io/Bacheloroppgave](https://kasa031.github.io/Bacheloroppgave)

En enkel nettside med kort og oversiktlig informasjon om cybersikkerhet. Prosjektet er laget for å formidle grunnleggende kunnskap om trusler på nettet og hvordan man beskytter seg.

## Innhold

- **Hva er cybersikkerhet?** – definisjon og betydning  
- **Vanlige trusler** – malware, phishing, hacking, identitetstyveri  
- **Hvordan beskytte deg** – oppdateringer, passord, 2FA  
- **Gode passord** – tips og anbefalinger  
- **Phishing** – hvordan gjenkjenne og unngå det  

## Teknologi

- Ren HTML, CSS og JavaScript (ingen rammeverk)
- Responsiv layout
- Blå fargepalett med lyse accenter

## Kjøre lokalt

1. Klon repoet eller last ned filene.
2. Åpne `index.html` i nettleseren, eller start en lokal server:
   ```bash
   python -m http.server 8080
   ```
   Åpne deretter **http://localhost:8080** i nettleseren.

## Test prosjektet – sjekkliste

### 1. Test lokalt
- Åpne `index.html` i nettleseren, eller kjør: `python -m http.server 8080` og åpne **http://localhost:8080**.
- Sjekk at design, menyer, bildet (landskap.png) og alle seksjoner fungerer.

### 2. Push til GitHub
- Kjør **`push-til-github.ps1`** (PowerShell) fra prosjektmappen.  
  Hvis `git` ikke finnes: kjør først **`legg-git-i-path.ps1`** eller installer [Git](https://git-scm.com/download/win).
- Etter push: sjekk at alle filer ligger på [github.com/kasa031/Bacheloroppgave](https://github.com/kasa031/Bacheloroppgave).

### 3. GitHub Pages (med GitHub Actions)
- På GitHub: **Settings** → **Pages**.
- Under **Build and deployment** → **Source** velg **GitHub Actions**.
- Ved neste push til `main` kjører workflowen og deployer siden.

### 4. Åpne live-nettsiden
- **Adresse:** **https://kasa031.github.io/Bacheloroppgave**
- Det kan ta 1–2 minutter etter push før siden oppdateres. Sjekk **Actions**-fanen på GitHub for deploy-status.

## Fargepalett (anbefalt)

- **Mørk blå** `#0d2137` – bakgrunn
- **Blå** `#1a3a5c` – seksjoner
- **Accent** `#4fc3f7` – overskrifter og lenker
- **Lys blå** `#b3e5fc` / `#e1f5fe` – tekst og lysere elementer

## Lisens

Fritt å bruke til læringsformål.
