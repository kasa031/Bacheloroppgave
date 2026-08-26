# ACIT4280 gruppeoppgave 1A - ICO lawful basis

Arbeidsnotat til innleveringen (ikke studieapp, ikke GitHub Pages).

**De fem tjenestene:** skatteetaten.no, netflix.no, fotball.no, document.no, babyshop.no.

**Kilder gjenfunnet fra OneDrive 1A_Webbkoll:**
- `Lawful basis assessment report.docx` (offisiell ICO-rapport, Skatteetaten skatt/folkeregister)
- `ICO_5sites_worksheet.html`
- `ACIT4280_1A_report.html` (gruppens rapport, Tabell 5)

ICO-verktøy: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/lawful-basis-interactive-guidance-tool/

---

## 1. Skatteetaten (skatteetaten.no) - FERDIG, trenger ikke ny ICO-kjøring for kjerneformålet

**Personvernerklæring:** https://www.skatteetaten.no/om-skatteetaten/sikkerhet/personvern/

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

**Match:** Ja. Banneret er valgfritt. I hovedrapporten ble consent INCONCLUSIVE fordi kjernebehandling ble blandet inn. For cookies alene: Q6 To some extent (behandler/formål ikke fullt ut i banneret). Q2 om maktposisjon: valgt No; offentlig myndighet kan argumentere Yes.

**Webbkoll/Nei-test:** Webbkoll klikker ikke banner. Egen test 24.08.2026: Nei på skatteetaten.no/person/. Figur: `figures/fig7_skatteetaten_cookie_banner.png`.

---

## 2. Netflix (netflix.no) - I GANG

**Formål vi tester (worksheet):** konto- og betalingsdata for betalt strømmeabonnement. Annonser, anbefalinger og markedsføring er egne formål.

**Personvernerklæring 10. april 2026 (EEA/UK) oppgir faktisk Art. 6-grunnlag:** contractual necessity, legitimate interests, legal obligation, consent. Worksheet/rapport-utkastet sa tidligere at Art. 6 ikke var merket; det bør oppdateres i Tabell 5.

### ICO-gjennomgang (betalt abonnement)

| Grunnlag | Status | Svar |
|----------|--------|------|
| Vital interests Q1: Are you processing the personal data to save or protect someone's life? | fylt | **No** |
| Public task Q1: Are you processing the data to carry out your official tasks or functions, or other specific tasks in the public interest? | fylt | **No** |
| Recognised legitimate interest Q1: Do you need to process the data for any of the following purposes? | fylt | **No** |
| Consent Q1: Do you want to give individuals the ongoing power to decide whether or not you process their data? | fylt | **No** |
| Contract | ikke fylt | Worksheet: Q1 Yes, Q2 Yes, Q3 No (kan ikke levere uten konto/betaling). Forventet utfall: contract |
| Legal obligation | ikke fylt | |
| Legitimate interests | ikke fylt | |
| ICO-konklusjon | ikke fylt | forventet: contract |

**Hvorfor No på vital interests:** Strømmetjeneste, ikke liv og død. Netflix lister ikke vital interests.

**Hvorfor No på public task:** Netflix er et privat selskap, ikke offentlig myndighet. Art. 6(1)(e) gjelder offisielle oppgaver med hjemmel i lov. EEA/UK-tillegget lister ikke public task. Skatteetaten fikk Yes her; Netflix skal ha No.

**Hvorfor No på recognised legitimate interest:** ICO More information-listen er: vern av sårbare (inkl. barn), nødsituasjon, kriminalitet, nasjonal sikkerhet, eller utlevering til noen som ber om data til sin offentlige oppgave. Konto og betaling for strømmeabonnement er ingen av disse. Svindel/sikkerhet hos Netflix er et annet formål og skal ikke blandes inn i denne ICO-kjøringen. ICO-rapporten for Skatteetaten avviste også dette grunnlaget.

**Hvorfor No på consent Q1:** Spørsmålet er om abonnenten løpende kan si nei til behandling av konto- og betalingsdata og likevel ha tjenesten. Det kan de ikke. Samtykke hos Netflix gjelder atferdsreklame og enkelte markedsføringsmeldinger, ikke kjerneabonnementet. Å si opp kontoen er kontrakt, ikke samtykke. Ikke velg To some extent.

**ICO-steg nå:** velg No, Continue. Når contract kommer: Yes / Yes / No etter worksheet.

---

## 3. fotball.no - venter på ICO-kjøring

**Formål:** publisere navn og klubb for aktive spillere 13+ (kampstatistikk).

**Kunngjøring:** allmenn interesse / opt-out via klubb; FIKS viser kontrakt for medlemskap; stamdata har publiseringssamtykke. Ikke tydelig Art. 6 på fotball.no-siden for selve publiseringen.

**Forventet ICO:** legitimate interests med balancing test. Worksheet: Contract Q1 No, consent No, legal obligation No, vital interests No, public task No, LI Yes.

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
| netflix.no | betalt abonnement | contract (nå eksplisitt i EEA/UK-tillegg) | pågår (vital interests No, public task No, recognised LI No, consent Q1 No) | venter |
| fotball.no | publisering kampstatistikk | public interest / opt-out | venter (forventet LI) | venter |
| document.no | Google Signals | ikke oppgitt; Google-innstillinger | venter (forventet consent) | venter |
| babyshop.no | kjøp og levering | contract (underforstått) | venter (forventet contract) | venter |
