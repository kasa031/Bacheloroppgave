# ACIT4280 gruppeoppgave 1A - ICO lawful basis

Arbeidsnotat til innleveringen (ikke studieapp, ikke GitHub Pages).

**De fem tjenestene:** skatteetaten.no, netflix.no, fotball.no, document.no, babyshop.no.

**Kilder gjenfunnet fra OneDrive 1A_Webbkoll:**
- `Lawful basis assessment report.docx` (offisiell ICO-rapport, Skatteetaten skatt/folkeregister)
- `Netflix_Lawful basis assessment report.docx` (offisiell ICO-rapport, Netflix abonnement)
- `ICO_5sites_worksheet.html`
- `ACIT4280_1A_report.html` (gruppens rapport, Tabell 5)

ICO-verktøy: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/lawful-basis-interactive-guidance-tool/

---

## 1. Skatteetaten (skatteetaten.no) - FERDIG, trenger ikke ny ICO-kjøring for kjerneformålet

**Personvernerklæring:** Limt inn i chatten 26.08.2026 (hovedsiden). Samme tekst som https://www.skatteetaten.no/om-skatteetaten/sikkerhet/personvern/. Cookie- og analyseavsnittene nederst i utdraget er bare overskrifter; full cookie-tekst (samtykke, GA4, Matomo) ligger under «Bruk av informasjonskapsler» / «Analyseverktøy for webstatistikk» og ble hentet fra live-siden.

Kjerne: behandling «først og fremst hjemlet i lov». Ikke mulig å reservere seg som hovedregel. Oppgaver: folkeregister, riktig skatt/avgift, andre krav (bøter, barnebidrag), veiledning og kontroll. Samfunnsoppdrag: finansielt grunnlag for offentlig virksomhet. Navngitte lover bl.a. skatteforvaltningsloven, skattebetalingsloven, folkeregisterloven, A-opplysningsloven, MVA-loven. Behandlingsansvarlig: Skattedirektøren. PVO: personvernombud@skatteetaten.no.

Nettstedet: informasjonskapsler etter samtykke. Underside https://www.skatteetaten.no (Informasjonskapsler på skatteetaten.no), limt inn 26.08.2026:

- Nødvendige cookies er alltid på (innlogging, skjema, sikkerhet). Kan ikke velges bort.
- Valgfrie: analyse/statistikk/brukerinnsikt (Skyra, Matomo, Google Analytics, Siteimprove). Godkjenn alle, eller bare nødvendige.
- Data brukes bare til å forbedre Skatteetatens tjenester og deles ikke utenfor etaten (ifølge denne siden).
- Første besøk: velg. Hvis alle godkjennes, slettes valgfrie etter 90 dager og de spør på nytt. Samtykke kan endres når som helst.

Eget formål, ikke kjerne-ICO. Matcher Ja/Nei-banneret og den egne cookie-ICO-kjøringen (consent).

### Formål 1: skatt og folkeregister (den offisielle ICO-rapporten)

**Behandling:** identitet, adresse, inntekt og skattedata for skattefastsetting og folkeregisteret.

**Grunnlag i kunngjøringen:** rettslig plikt / påkrevd i lov (skatte- og folkeregisterregler). Kjerneoppgavene er ikke valgfrie.

**Offisiell ICO-rapport (Lawful basis assessment report.docx):**

| Grunnlag | ICO-utfall |
|----------|------------|
| Legal obligation | APPROPRIATE |
| Public task | APPROPRIATE |
| Consent | INCONCLUSIVE (ikke gyldig samtykke for kjernebehandling) |
| Contract | NOT APPROPRIATE |
| Vital interests | NOT APPROPRIATE |
| Recognised legitimate interest | NOT APPROPRIATE |
| Legitimate interests | NOT APPROPRIATE |

**Match:** Ja. Kunngjøringens lovgrunnlag stemmer med ICO.

ICO ba om å dokumentere hvorfor behandlingen er nødvendig for å overholde en navngitt plikt, og (for public task) hvilken offentlig oppgave/myndighet som har hjemmel i lov. Spesielle kategorier krever eget Art. 9-vilkår i tillegg.

### Formål 2: valgfrie statistikk-informasjonskapsler (egen ICO-kjøring)

**Behandling:** valgfrie webstatistikk-cookies etter Ja/Nei-banner.

**Grunnlag i kunngjøringen:** samtykke.

**ICO-resultat (worksheet):** Consent.

**Match:** Ja. Banneret er valgfritt. Cookie-siden skiller nødvendige (alltid på) og valgfrie (Skyra, Matomo, Google Analytics, Siteimprove). Hoved-ICO-rapporten ble consent INCONCLUSIVE fordi kjernebehandling ble blandet inn. For cookies alene: Q6 To some extent (behandler/formål ikke fullt ut i banneret). Q2 om maktposisjon: valgt No; offentlig myndighet kan argumentere Yes.

**Webbkoll/Nei-test:** Webbkoll klikker ikke banner. Egen test 24.08.2026: Nei på skatteetaten.no/person/. Figur: `figures/fig7_skatteetaten_cookie_banner.png`.

---

## 2. Netflix (netflix.no) - FERDIG

**Formål:** konto- og betalingsdata for betalt strømmeabonnement. Annonser, anbefalinger og markedsføring er egne formål.

**Personvernerklæring:** Full Privacy Statement fra første gjennomgang (Section A-F, Games-tillegg, EEA/UK Legal bases, Last Updated 10 April 2026). Ikke limt inn: egen cookie-typeliste («click here») og undersiden om internasjonale overføringer. EEA/UK oppgir contractual necessity, legitimate interests, legal obligation og consent. For *to provide our service* til medlemmer bruker Netflix contractual necessity.

**Offisiell ICO-rapport:** `Netflix_Lawful basis assessment report.docx`

| Grunnlag | ICO-utfall |
|----------|------------|
| Contract | APPROPRIATE |
| Legal obligation | NOT APPROPRIATE |
| Vital interests | NOT APPROPRIATE |
| Public task | NOT APPROPRIATE |
| Recognised legitimate interest | NOT APPROPRIATE |
| Consent | NOT APPROPRIATE / likely invalid (ingen ekte, løpende valg) |
| Legitimate interests | NOT APPROPRIATE |

Ingen grunnlag merket INCONCLUSIVE.

**Svar vi ga i ICO-verktøyet (dette formålet):**

| Spørsmål | Svar |
|----------|------|
| Vital interests Q1: save or protect someone's life? | No |
| Public task Q1: official tasks or public interest? | No |
| Recognised legitimate interest Q1: de fem allmenne formålene? | No |
| Consent Q1: ongoing power to decide? | No |
| Legitimate interests: full responsibility for justifying? | No |

Contract ble merket APPROPRIATE i sluttrapporten (abonnement under Terms of Use; konto og betaling er nødvendig for å levere tjenesten).

**Match:** Ja. ICO peker på contract, og EEA/UK-tillegget bruker contractual necessity for å levere tjenesten til medlemmer. Worksheet/Tabell 5 sa tidligere at Art. 6 ikke var merket; det stemmer ikke lenger og bør rettes. LI, legal obligation og consent i kunngjøringen gjelder *andre* formål og skal ikke blandes inn i denne ICO-kjøringen.

ICO minner om å dokumentere hvorfor behandlingen er nødvendig for kontrakten, og at barn under 18 må være part i kontrakten med tilstrekkelig kompetanse (Netflix krever 18 år, eller foresatt).

---

## 3. fotball.no - I GANG

**Formål vi tester (worksheet):** publisere navn og klubb for aktive spillere 13+ for å vise kamphistorikk. Kontaktinfo til trenere/klubber og Cookiebot-cookies er egne formål.

**Personvernerklæring (full tekst lest 26.08.2026, https://www.fotball.no/personvern):**

- FIKS: Art. 6(1)(b) avtale for medlemskap, kamper og roller. Historiske data etter utmelding vises til Personvernnemnda PVN-2005-14 og personvernloven § 8, ikke til en plikt om å publisere navn på nett.
- fotball.no-undersiden: kamphistorikk av allmenn interesse, opt-out via klubb. Ingen Art. 6(c).
- Stamdata: «samtykke om publisering». FIFA-connect: teksten sier bokstav b men siterer berettiget interesse (f).
- Wifi-Ullevaal: Art. 6(1)(f) LI, pluss samtykke til CRM.
- CRM B2C (billetter/supporterklubb): «Vi er pålagt å lagre kjøpshistorikk» (regnskap/avgift). Det er **et annet formål** enn ICO-kjøringen.
- Cookiebot (limt inn 26.08.2026): ekomlov for nødvendige cookies; samtykke for Preferences/Statistics/Marketing. Tilstand: Deny. Tredjeparter bl.a. YouTube, Google, Vimeo, Spotify, Cookiebot. Eget formål.

Vi tester **ett** formål: visning av navn og klubb på fotball.no.

**ICO-gjennomgang (publisering av kamphistorikk):**

| Grunnlag | Status | Svar |
|----------|--------|------|
| Contract Q1: Do you have (or intend to have) a contract with the individual? | fylt | **No** |
| Consent Q1: Do you want to give individuals the ongoing power to decide whether or not you process their data? | fylt | **No** |
| Legal obligation Q1: Are you processing this personal data to comply with the law? | fylt | **No** |
| Vital interests Q1: Are you processing the personal data to save or protect someone's life? | fylt | **No** |
| Public task Q1: Are you processing the data to carry out your official tasks or functions, or other specific tasks in the public interest? | fylt | **No** |
| Recognised legitimate interest Q1: Do you need to process the data for any of the following purposes? | fylt | **No** |
| Legitimate interests | ikke fylt | Worksheet: Yes, med balancing og opt-out |
| ICO-konklusjon | ikke fylt | forventet: legitimate interests |

**Hvorfor No på contract Q1:** Vi tester visning av navn og klubb på nett, ikke medlemsadministrasjon i FIKS. FIKS kan bruke kontrakt for medlemskap, men kamphistorikk på fotball.no er ikke det samme som å oppfylle en avtale med spilleren. ICO: svar No når du behandler noen andres opplysninger enn den du har kontrakt med, eller når formålet ikke er å utføre kontrakten. Worksheet startet med No her.

**Hvorfor No på legal obligation Q1:** Ingen norsk lov pålegger NFF å legge ut spillernavn og klubb på fotball.no. FIKS-grunnlaget er avtale (b), ikke rettslig plikt (c). Setningen om pålagt lagring av kjøpshistorikk gjelder CRM/billetter, ikke denne ICO-kjøringen. Ikke velg To some extent.

**Hvorfor No på vital interests Q1:** Kamphistorikk (navn og klubb) redder ikke liv. ICO vital interests er liv og død. Skadetelefon i bunnen av nff.no er ikke dette formålet.

**Hvorfor No på public task Q1:** NFF er en medlemsorganisasjon, ikke forvaltningsorgan. Art. 6(1)(e) krever offisiell myndighet eller en konkret samfunnsoppgave med hjemmel i lov. «Kamphistorikk av allmenn interesse» er argument for LI-balancing, ikke public task. Ikke velg To some extent.

**Hvorfor No på recognised legitimate interest Q1:** Listen er vern av sårbare, nødsituasjon, kriminalitet, nasjonal sikkerhet, eller utlevering til noen som ber om data til sin offentlige oppgave. Publisering av navn og klubb for kamphistorikk er ingen av disse.

**Hvorfor No på consent Q1:** Navn og klubb publiseres som standard. Spilleren kan stoppe det via klubben, men det er ikke løpende, fritt samtykke (slik Cookiebot er). Stamdata «samtykke om publisering» er ikke det samme som Art. 6(1)(a) for denne visningen. Ikke velg To some extent.

**ICO-steg nå:** velg No på consent Q1, Continue. Neste forventet: legitimate interests Yes.

### Formål 2: Cookiebot (ikke denne ICO-kjøringen)

Nødvendige cookies uten samtykke (ekomlov). Øvrige krever tillatelse; samtykke kan trekkes. Nåværende tilstand Deny (26.08.2026 11:58 GMT+2). Dette er **ikke** grunnlaget for å vise spillernavn.

---

## 4. document.no - venter på ICO-kjøring

**Formål:** Google Signals / reklameanalyse fra nettstedsaktivitet.

**Kunngjøring:** ikke navngitt Art. 6; kjører bare hvis innlogget Google med annonsepersonalisering; opt-out-lenker.

**Forventet ICO:** consent. Worksheet: Contract Q1 No, deretter consent-spørsmål etter at lesing av artikler ikke krever Signals.

---

## 5. babyshop.no - venter på ICO-kjøring

**Formål:** navn, adresse, kontakt, ordre og betaling for kjøp og levering.

**Kunngjøring:** ikke merket Art. 6(1)(b); policy sier at kundedata behandles ved kjøp for å oppfylle ordre. Markedsføring/profilering: consent. Annet: legitimate interests.

**Forventet ICO:** contract. Worksheet: Q1 Yes, Q2 Yes, Q3 No.

---

## Sammenligning (Tabell 5 i rapporten)

| Tjeneste | Formål | Notice | ICO | Match |
|----------|---------|--------|-----|-------|
| skatteetaten.no | skatt/folkeregister | legal obligation | legal obligation + public task APPROPRIATE | Ja |
| skatteetaten.no | valgfrie cookies | consent | consent | Ja (egen kjøring) |
| netflix.no | betalt abonnement | contractual necessity (EEA/UK) | Contract APPROPRIATE; øvrige NOT APPROPRIATE | Ja |
| fotball.no | publisering kampstatistikk | public interest / opt-out; FIKS contract for medlemskap | pågår (contract No, legal obligation No, vital interests No, public task No, recognised LI No, consent Q1 No) | venter |
| document.no | Google Signals | ikke oppgitt; Google-innstillinger | venter (forventet consent) | venter |
| babyshop.no | kjøp og levering | contract (underforstått) | venter (forventet contract) | venter |
