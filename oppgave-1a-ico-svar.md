# ACIT4280 gruppeoppgave 1A - ICO lawful basis

Arbeidsnotat til innleveringen (ikke studieapp, ikke GitHub Pages, ikke oppgave 1B).

**Canvas:** Group assignment 1A, ACIT4280-1 26H. Frist 3 Sep 2026 08:00. 40 poeng. Rapport 1000-1500 ord + diagrammer. 20 min presentasjon (alle i gruppen).

**To deler i 1A:**
1. Webbkoll på listen (shopping, government, news/media, sport): tabell over 3. parts-deling, grenseoverskridende eksport og sporing + grafikk per sektor. Dette ligger i `ACIT4280_1A_report.html`.
2. **Gruppe 1-A (oss):** ICO lawful basis-verktøyet på **5 valgte tjenester** fra analysen. Finn personvernerklæring, kjør ICO, oppsummer i rapporten (Tabell 5). Ett konkret behandlingsformål per kjøring.

**Ikke 1B:** 1-B undersøker innsynsforespørsler. Det gjør vi ikke her.

**De fem tjenestene (1-A):** skatteetaten.no, netflix.no, fotball.no, document.no, babyshop.no.

**Kilder gjenfunnet fra OneDrive 1A_Webbkoll:**
- `Lawful basis assessment report.docx` (offisiell ICO-rapport, Skatteetaten skatt/folkeregister)
- `Netflix_Lawful basis assessment report.docx` (offisiell ICO-rapport, Netflix abonnement)
- `Fotball_Lawful basis assessment report.docx` (offisiell ICO-rapport, fotball.no kamphistorikk)
- `ICO_5sites_worksheet.html`
- `ACIT4280_1A_report.html` (gruppens rapport, Tabell 5)
- Full personvernerklæring for document.no limt inn 26.08.2026 (ingen Art. 6-merking)
- Kjøps- og abonnementsvilkår for Document Pluss limt inn 26.08.2026 (punkt 7 personvern)

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

## 3. fotball.no - FERDIG

**Formål:** publisere navn og klubb for aktive spillere 13+ for å vise kamphistorikk. Kontaktinfo til trenere/klubber og Cookiebot-cookies er egne formål.

**Personvernerklæring (full tekst lest 26.08.2026, https://www.fotball.no/personvern):**

- FIKS: Art. 6(1)(b) avtale for medlemskap, kamper og roller. Historiske data etter utmelding vises til Personvernnemnda PVN-2005-14 og personvernloven § 8, ikke til en plikt om å publisere navn på nett.
- fotball.no-undersiden: kamphistorikk av allmenn interesse, opt-out via klubb. Ingen Art. 6(c).
- Stamdata: «samtykke om publisering». FIFA-connect: teksten sier bokstav b men siterer berettiget interesse (f).
- Wifi-Ullevaal: Art. 6(1)(f) LI, pluss samtykke til CRM.
- CRM B2C (billetter/supporterklubb): «Vi er pålagt å lagre kjøpshistorikk» (regnskap/avgift). Det er **et annet formål** enn ICO-kjøringen.
- Cookiebot (limt inn 26.08.2026): ekomlov for nødvendige cookies; samtykke for Preferences/Statistics/Marketing. Tilstand: Deny. Tredjeparter bl.a. YouTube, Google, Vimeo, Spotify, Cookiebot. Eget formål.

Vi tester **ett** formål: visning av navn og klubb på fotball.no.

**Offisiell ICO-rapport:** `Fotball_Lawful basis assessment report.docx`

| Grunnlag | ICO-utfall |
|----------|------------|
| Legitimate interests | APPROPRIATE |
| Contract | NOT APPROPRIATE |
| Legal obligation | NOT APPROPRIATE |
| Vital interests | NOT APPROPRIATE |
| Public task | NOT APPROPRIATE |
| Recognised legitimate interest | NOT APPROPRIATE |
| Consent | NOT APPROPRIATE / likely invalid (ingen ekte, løpende valg) |

Ingen grunnlag merket INCONCLUSIVE. ICO skriver at legitimate interests *is likely to be an appropriate lawful basis*.

**Svar vi ga i ICO-verktøyet (dette formålet):**

| Grunnlag | Status | Svar |
|----------|--------|------|
| Contract Q1: Do you have (or intend to have) a contract with the individual? | fylt | **No** |
| Consent Q1: Do you want to give individuals the ongoing power to decide whether or not you process their data? | fylt | **No** |
| Legal obligation Q1: Are you processing this personal data to comply with the law? | fylt | **No** |
| Vital interests Q1: Are you processing the personal data to save or protect someone's life? | fylt | **No** |
| Public task Q1: Are you processing the data to carry out your official tasks or functions, or other specific tasks in the public interest? | fylt | **No** |
| Recognised legitimate interest Q1: Do you need to process the data for any of the following purposes? | fylt | **No** |
| Legitimate interests: Are you happy to take full responsibility for justifying your processing? | fylt | **Yes** |
| Legitimate interests Q2: Are you processing the data to perform your tasks as a public authority? | fylt | **No** |
| Legitimate interests Q3: Have you identified a legitimate interest? | fylt | **Yes** |
| Legitimate interests Q4: Is there another reasonable way to achieve your purpose without processing the data? | fylt | **No** |
| Legitimate interests Q5: Is your legitimate interest compelling enough to justify the potential impact on individuals, or any element of the processing which would be unexpected? | fylt | **Yes** |
| ICO-konklusjon | fylt | **Legitimate interests APPROPRIATE**; øvrige NOT APPROPRIATE |

**Hvorfor No på contract Q1:** Vi tester visning av navn og klubb på nett, ikke medlemsadministrasjon i FIKS. FIKS kan bruke kontrakt for medlemskap, men kamphistorikk på fotball.no er ikke det samme som å oppfylle en avtale med spilleren. ICO: svar No når du behandler noen andres opplysninger enn den du har kontrakt med, eller når formålet ikke er å utføre kontrakten. Worksheet startet med No her.

**Hvorfor No på legal obligation Q1:** Ingen norsk lov pålegger NFF å legge ut spillernavn og klubb på fotball.no. FIKS-grunnlaget er avtale (b), ikke rettslig plikt (c). Setningen om pålagt lagring av kjøpshistorikk gjelder CRM/billetter, ikke denne ICO-kjøringen. Ikke velg To some extent.

**Hvorfor No på vital interests Q1:** Kamphistorikk (navn og klubb) redder ikke liv. ICO vital interests er liv og død. Skadetelefon i bunnen av nff.no er ikke dette formålet.

**Hvorfor No på public task Q1:** NFF er en medlemsorganisasjon, ikke forvaltningsorgan. Art. 6(1)(e) krever offisiell myndighet eller en konkret samfunnsoppgave med hjemmel i lov. «Kamphistorikk av allmenn interesse» er argument for LI-balancing, ikke public task. Ikke velg To some extent.

**Hvorfor No på recognised legitimate interest Q1:** Listen er vern av sårbare, nødsituasjon, kriminalitet, nasjonal sikkerhet, eller utlevering til noen som ber om data til sin offentlige oppgave. Publisering av navn og klubb for kamphistorikk er ingen av disse.

**Hvorfor No på consent Q1:** Navn og klubb publiseres som standard. Spilleren kan stoppe det via klubben, men det er ikke løpende, fritt samtykke (slik Cookiebot er). Stamdata «samtykke om publisering» er ikke det samme som Art. 6(1)(a) for denne visningen. Ikke velg To some extent.

**Hvorfor Yes på legitimate interests (full responsibility):** Dette er LI-spørsmålet. For visning av navn og klubb (allmenn interesse, opt-out via klubb) er det NFF som må dokumentere balancing. Worksheet forventet LI. Dette er motsatt av Netflix-abonnementet, der vi sa No fordi kontrakt passet bedre.

**Hvorfor No på LI Q2 (public authority):** NFF er idrettsforbund, ikke forvaltningsorgan. Offentlig myndighet kan som hovedregel ikke bruke LI til offisielle oppgaver. Yes her ville stenge LI. Skatteetaten ville svart Yes på dette spørsmålet.

**Hvorfor Yes på LI Q3:** Undersiden sier formålet er kamphistorikk av allmenn interesse. Det er en identifisert interesse (NFF, klubber, fans). Ikke To some extent.

**Hvorfor No på LI Q4:** Spørsmålet er om formålet kan nås *uten* å behandle personopplysningene. Yes her ville bety at behandlingen ikke er nødvendig. Formålet er å vise *hvem* som spilte (navn og klubb). Resultat uten navn (bare klubb mot klubb) er et annet formål. Anonymiserte oppstillinger gir ikke kamphistorikk av allmenn interesse slik NFF beskriver det. Ikke velg To some extent.

**Hvorfor Yes på LI Q5:** Balancing-testen. Behandlingen er begrenset (navn og klubb, ikke kontaktinfo). Aktive spillere 13+ i offisielle kamper kan rimelig forvente at navn vises i kamphistorikk. Allmenn interesse og opt-out via klubb veier opp for inngrepet. Publisering på nett er ikke uventet i organisert fotball. Ikke To some extent: det gjør ICO usikker, og worksheet forventer at LI holder.

**Match:** Ja for formålet vi testet. Undersiden (kamphistorikk av allmenn interesse + opt-out via klubb) er Art. 6(1)(f) i praksis, og ICO merker legitimate interests APPROPRIATE. Contract og public task er NOT APPROPRIATE: vi testet ikke FIKS-medlemskap, og NFF er ikke forvaltningsorgan. Consent er NOT APPROPRIATE / likely invalid: stamdata-formuleringen «samtykke om publisering» matcher ikke ICO for denne visningen (publiseres som standard). FIFA-connect-teksten som blander bokstav b og f skal ikke brukes som grunnlag for denne raden. Cookiebot er eget formål.

ICO minner om å dokumentere en legitimate interests assessment (LIA), holde den oppdatert, vurdere DPIA ved vesentlig risiko, og skrive i personvernerklæringen at de bruker berettiget interesse og *hvilken* interesse det er. For 13-17 år peker ICO også til veiledningen om barns opplysninger.

### Formål 2: Cookiebot (ikke denne ICO-kjøringen)

Nødvendige cookies uten samtykke (ekomlov). Øvrige krever tillatelse; samtykke kan trekkes. Nåværende tilstand Deny (26.08.2026 11:58 GMT+2). Dette er **ikke** grunnlaget for å vise spillernavn.

---

## 4. document.no - I GANG

**Formål vi tester:** Google Signals / reklameanalyse (demografi, interesser, aktivitet på tvers av enheter). Medlemskonto, kommentarer, kjøp og nødvendige cookies er egne formål.

**Personvernerklæring:** Full tekst limt inn i chatten 26.08.2026. Samme som https://www.document.no/personvernerklaering/. Document Media AS, kontakt@document.no. Org.nr. 893 068 392.

Art. 6 er **ikke navngitt** noe sted. Rettighetene nevner samtykke og avtale bare under dataportabilitet, uten å si hvilket grunnlag som gjelder for Signals. Utlevering til myndigheter «dersom vi er lovpålagt» er et annet formål.

Avsnittet «Google Analytics og annonsefunksjoner (Google Signals)»:
- Annonsefunksjoner i GA gir statistikk om demografi, interesser og kryssenhet-bruk.
- De kaller det «samlet og anonymisert», men bruker likevel Google, første- og tredjepartscookies og andre identifikatorer.
- Innsamling bare hvis du er logget inn på Google og har tillatt personlig tilpasning av annonser.
- Opt-out: Google Ads Settings, mobil, NAI, Google Analytics-tillegg.

Ikke bland inn: kommentarer (IP, Gravatar), innlogging/«Husk meg», kjøpshistorikk, kundeforhold i 36 måneder, eller innebygd innhold fra andre nettsteder.

**Kjøps- og abonnementsvilkår (Document Pluss, limt inn 26.08.2026):** Det finnes en avtale for *betalt abonnement* (Ordinært, Premium, VIP, Bedrift). Punkt 7: de lagrer det som kreves for å levere tjenesten du har kjøpt, og for å sende tilbud «i den utstrekning vi har lov til det». Henviser til personvernerklæringen. Å «godta» vilkårene ved bruk er ikke Art. 6-samtykke. Donasjoner gir ikke tilgang og er ikke underlagt vilkårene.

Det endrer **ikke** Contract Q1 for denne ICO-kjøringen. En egen kjøring på konto og betaling for Document Pluss ville vært som Netflix (forventet contract). Google Signals er ikke nødvendig for å levere Pluss.

**ICO-gjennomgang (Google Signals):**

| Grunnlag | Status | Svar |
|----------|--------|------|
| Contract Q1: Do you have (or intend to have) a contract with the individual? | fylt | **No** |
| Legal obligation Q1: Are you processing this personal data to comply with the law? | fylt | **No** |
| Vital interests Q1: Are you processing the personal data to save or protect someone's life? | fylt | **No** |
| Public task Q1: Are you processing the data to carry out your official tasks or functions, or other specific tasks in the public interest? | fylt | **No** |
| Recognised legitimate interest Q1: Do you need to process the data for any of the following purposes? | fylt | **No** |
| Consent Q1: Do you want to give individuals the ongoing power to decide whether or not you process their data? | fylt | **Yes** |
| Consent Q2: Are you in a position of power over the individual, which means they might feel they have to say yes? | fylt | **No** |
| Consent Q3: Have you made consent to processing a precondition of your service? | fylt | **No** |
| Consent Q4: Do you ask individuals to take a positive action to opt in? | fylt | **Yes** |
| Consent Q5: Is your consent request clear, prominent, and separate from general terms and conditions? | fylt | **To some extent** |
| ICO-konklusjon | ikke fylt | forventet: consent (kan bli INCONCLUSIVE pga. Q5) |

**Hvorfor No på contract Q1:** Vi tester reklameanalyse, ikke Document Pluss. Det er ingen avtale om Google Signals. Signals styres av Google-innlogging og annonsetilpasning, ikke av abonnementet. ICO: svar No når formålet ikke er å utføre kontrakten. Worksheet startet med No her.

**Hvorfor No på legal obligation Q1:** Ingen norsk lov pålegger Document å slå på Google Signals. Setningen om utlevering til myndigheter «dersom vi er lovpålagt» er et annet formål. Ikke velg To some extent.

**Hvorfor No på vital interests Q1:** Reklameanalyse redder ikke liv. ICO vital interests er liv og død. Ikke To some extent.

**Hvorfor No på public task Q1:** Document Media AS er et privat mediehus, ikke forvaltningsorgan. Art. 6(1)(e) krever offisiell myndighet eller en konkret samfunnsoppgave med hjemmel i lov. Google Signals er reklameanalyse, ikke journalistikk som offentlig oppgave. Ikke To some extent.

**Hvorfor No på recognised legitimate interest Q1:** Listen er vern av sårbare, nødsituasjon, kriminalitet, nasjonal sikkerhet, eller utlevering til noen som ber om data til sin offentlige oppgave. Google Signals er ingen av disse.

**Hvorfor Yes på consent Q1:** Motsetning til fotball.no og Netflix-abonnementet. Erklæringen sier at Signals bare samles hvis du er logget inn på Google og har tillatt personlig tilpasning av annonser, med opt-out via Ads Settings, mobil, NAI eller Analytics-tillegg. Lesing av artikler krever ikke Signals. Vi *vil* at personen skal kunne si ja eller nei løpende. Ikke To some extent: det gjør ICO usikker. At valget skjer hos Google, tas i senere consent-spørsmål.

**Hvorfor No på consent Q2:** Document Media AS er et privat mediehus, ikke arbeidsgiver eller forvaltningsorgan. Lesere må ikke si ja til Signals for å unngå ulempe hos staten (slik Skatteetaten kunne argumenteres). Ikke To some extent.

**Hvorfor No på consent Q3:** Lesing av artikler krever ikke Google Signals. Erklæringen sier at data bare samles hvis du er logget inn på Google med annonsetilpasning. Et Pluss-abonnement krever heller ikke Signals. Yes her ville gjort samtykket ugyldig (tvunget). Ikke To some extent.

**Hvorfor Yes på consent Q4:** Erklæringen krever at du har *tillatt* personlig tilpasning av annonser. Det er en handling (Google-innstilling), ikke stillhet eller «ved å bruke siden». Document har ikke beskrevet et eget ja-banner for Signals; det tar vi i spørsmål om klart, fremtredende samtykke. Ikke No: det ville kuttet consent-sporet. Ikke To some extent.

**Hvorfor To some extent på consent Q5:** Valget skjer hos Google (Ads Settings / annonsetilpasning), ikke i et klart, fremtredende Document-banner. Signals er beskrevet i personvernerklæringen, ikke som en atskilt ja-forespørsel. Pluss-vilkårene sier at du ved bruk godtar vilkår og personvernerklæring; det er ikke gyldig, atskilt samtykke. Yes ville overdrevet et banner vi ikke har dokumentert. No ville kuttet consent helt. Samme type hull som Skatteetatens cookie-Q6.

**ICO-steg nå:** velg To some extent, trykk Continue. ICO kan merke consent INCONCLUSIVE. Det er et funn til Tabell 5: Art. 6 er ikke merket, og forespørselen ligger hos Google.

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
| fotball.no | publisering kampstatistikk | allmenn interesse / opt-out (LI i praksis); FIKS contract for medlemskap | Legitimate interests APPROPRIATE; øvrige NOT APPROPRIATE | Ja (dette formålet) |
| document.no | Google Signals | ikke oppgitt; Google-innstillinger | venter (forventet consent) | venter |
| babyshop.no | kjøp og levering | contract (underforstått) | venter (forventet contract) | venter |
