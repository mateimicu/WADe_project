## WADe_project


### Release 0.2

* [  ] Update REST api mapping cu noile fields
* [  ] Update OpenAPI cu mesaje descriptive, coduri de eroare
* [  ] Expand Ontology
  * [  ] Link licentele cu cele de pe WikiData
  * [  ] Adauga legatura DSApplication --written with--> Limbaj de programare de pe wiki data
  * [  ] Adauga legatura DSApplication --works on --> OS(Linux, Windows, etc ...)/Platform(Kubernetes, DockerSwarm, etc ...)/CloudProvider(OpenStack, Amazon, etc ...)
* [  ] Adauga Posibilitatea sa vezi ce sparql se ruleaza pentru un query


### Release 0.1 - Done

* [x] Ontologia
* [x] Populat ontologia
* [x] Jena Fuseki (Sparql Endpoint)
* [x] REST API
* [x] OPEN API
* [x] Sparql Queries hardcoded
  * [x] Query in functie de proiect si popularitate
* [x] UI 
  * [x] Query PAGE
  * [x] Sparql editor
  * [x] GraphQL
* [x] Cloud Host
  * [x] Put everything in Docker containers 
  * [x] Deploy a Kubernetes Cluster
  * [x] Setup every microservice
* [x] Valideaza HTML/CSS (Done)
* [x] Update raport
* [ ] Video

### Future Work

- [  ] Ia limbajele de programare de pe GitHub
- [  ] Creaza un CI
- [  ] Parseaza Versiunile (mai ales daca sunt SemVer)
- [  ] Vezi daca e usor de deploy pe kubernetes daca are un chart public
- [  ] Parseaza de pe GitHub daca trece CI-ul proiectului si adauga asta in ontologie
- [  ] Adauga semantica la proiectele care sunt baze de date:
  - ce tip de baza de date sunt (relationala, ne relationala, storage)
  - ce semantica ofera si grad de consistenta
- [  ] Fa mai multe clase din DSApplication (in functie de categorie, subCategorie etc ...) ca sa poti adauga semantica specifica (pentru db-uri, pentru schedulers etc)

### Idei de query

* Este un proiect activ (lastTwittedDate, nrContriutors, vezi cati sunt activi, number of stars, number of closed PR/Issues)
* Este open source (cu grad de confidenta)
  * licenta open source
  * este scris in limbaj open source (sau aprobat de o fundatie open source)
  * functioneaza pe un cloud, platforma, OS open source
* Poti adauga daca au HQ aproape (corelare geografica)
* Design a system bazat pe kubernetes in care alegi
  * Daca vrei Kubernetes Hosted sau il instalezi tu 
  * daca ai nevoie de un api gateway (si filtrari pentru asta)
  * daca o sa folosesti FAAS
    * hosted vs installed
    * open source
    * ce vrei sa suporte
  * daca ai nevoie de service mesh
  * daca ai nevoie de service discovery
  * daca ai nevoie de CI/CD
  * daca ai nevoie de monitorizare
  * daca ai nevoie de logging
  * daca ai nevoie de tracing
