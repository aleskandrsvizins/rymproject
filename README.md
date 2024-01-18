# RYM Scraper

ir Python API, lai iegūtu datus no [rateyourmusic.com](https://rateyourmusic.com).

## Projekta Pārskats

Šis Python skripts automatizē albumu, EP un citu izdevumu klasificēšanas procesu no RateYourMusic.com charts sadaļas. Lietotāji var ievadīt savas preferences, lai filtrētu un sakārtotu izlaidumu sarakstu, pamatojoties uz žanriem. Un pēc tam izvadiet rezultātu vajadzīgajā formātā.

## Izmantotās Bibliotēkas

Projektā tiek izmantotas šādas Python bibliotēkas:

- 

## Projekta Soļi

1. **Importēju nepieciešamās bibliotēkas**: bibliotēkas, kas nepieciešamas tīmekļa kopēšanai – `BeautifulSoup` un `requests`, datu manipulēšanai – `pandas` un failu izvadei – `fpdf` PDF izvadei.
    
2. **Izgūstu datus no vietnes**: izmantoju `requests` bibliotēku, lai ielādētu RateYourMusic.com *charts* lapas HTML saturu.
    
3. **Parsēju HTML saturu**: izmantoju `BeautifulSoup`, lai parsētu ienesto HTML saturu.
    
4. **Izņemu nepieciešamo informāciju**: pārvietojos parsētajā HTML saturā, lai atrastu un izvilktu nepieciešamo informāciju par albumiem, EP un citiem izdevumiem. Šī informācija var būt ietverta īpašos HTML tagos vai atribūtos.
    
5. **Sakārto datus**: izmantoju `pandas`, lai sakārtotu iegūto informāciju DataFrame ērtai manipulēšanai un izvadīšanai.
    
6. **Lietotāja ievade izvades formātam**: prasa lietotājam vēlamo izvades formātu.
    
7. **Datu izvade**: atkarībā no lietotāja izvēles izvadīt izvada izvēlētajā formātā. Tas var ietvert DataFrame konvertēšanu par virkni un ierakstīšanu txt failā vai tādas bibliotēkas izmantošanu kā `fpdf`, lai ģenerētu PDF.