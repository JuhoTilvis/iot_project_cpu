# iot_project_cpu
cpu temp

Tämän sovelluksen käyttötarkoitus on julkaista raspberry pi:n CPU lämpötilat HTML sivulle käyttäen pythonia, HMTL ja CSS.
index.html sekä styles.css sivut ovat julkaistu myös Azuren Storage Account ominaisuuden avulla seuraavalle nettisivulle 
https://iotprojectcputemp.z1.web.core.windows.net/

1. Python script käynnistetään Linux pohjaisella raspberry pi:llä, tiedot julkaistaan Thingspeak sovellukseen.
2. HTML käyttää Thingspeak palvelimen tarjoamaa <iframe> koodia jakaakseen tiedon CPU lämpötilasta HTML sivulle.
3. CSS muokkaa HTML sivun tagien asettelua.

Tekijät
Oliwer Kronqvist
Juho Tilvis
Atte Kemppinen
