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

## 2. Netflix (netflix.no) - FERDIG

**Formål:** konto- og betalingsdata for betalt strømmeabonnement. Annonser, anbefalinger og markedsføring er egne formål.

**Personvernerklæring:** Privacy Statement, sist oppdatert 10. april 2026. EEA/UK-tillegget oppgir contractual necessity, legitimate interests, legal obligation og consent. For *to provide our service* til medlemmer bruker Netflix contractual necessity.

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
| netflix.no | betalt abonnement | contractual necessity (EEA/UK) | Contract APPROPRIATE; øvrige NOT APPROPRIATE | Ja |
| fotball.no | publisering kampstatistikk | public interest / opt-out | venter (forventet LI) | venter |
| document.no | Google Signals | ikke oppgitt; Google-innstillinger | venter (forventet consent) | venter |
| babyshop.no | kjøp og levering | contract (underforstått) | venter (forventet contract) | venter |
