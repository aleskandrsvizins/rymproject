# README

## Projekta Pārskats

Šis Python skripts plaši izmanto Selenium bibliotēku, lai iegūtu datus no [rateyourmusic.com](https://rateyourmusic.com) chartiem. Skripts ļauj lietotājiem pielāgot datu vākšanas procesu, pamatojoties uz dažādiem parametriem, piemēram, vērtējuma veidu, relīzu veidiem, laika diapazonu un apkopojamo izlaidumu skaitu. 

Programma tika izstrādā izmantojot Visual Studio Code.

## Projekta mērķi

Šī projekta galvenie mērķi ir:

1. **Datu vākšana:** izgūstiet informāciju par mūzikas izlaidumiem no RateYourMusic chartiem, pamatojoties uz lietotāja definētiem kritērijiem.
2. **Lietotāja pielāgošana:** ļauj lietotājiem pielāgot datu vākšanas procesu, atlasot vērtējuma veidus, relīzu veidus, laika diapazonu un apkopojamo relīzu skaitu.
3. **Datu eksportēšana:** saglabājiet apkopotos datus tīrā un sakārtotā CSV failā turpmākai analīzei.

## Prasības

- Python 3.6+
- Selenium WebDriver
- pandas

## Kā Izmantot

1. **Instalējiet Atkarības:**
    
    - Pārliecinieties, vai jūsu datorā ir instalēts Python.
    - Instalējiet vajadzīgās Python pakotnes, izmantojot šo komandu:
        
```bash
pip install selenium pandas
# jā nepieciešams → pip install python-math time datetime random re
```

- **Selenium:** Izmanto tiešsaistes tīmekļa lietojumprogrammu (web application) testēšanai un automatizācijai. Ārkārtīgi noderīga, ja ir nepieciešams veikt darbības tiešsaistes vietnēs vai iegūt datus no tīmekļa lapām.

- **Pandas:** Lieliska bibliotēka datu analīzei un manipulācijām. To izmanto, lai ērti strādātu ar datu tabulām, filtrētu datus, veiktu aprēķinus un citus datu apstrādes uzdevumus.

- **Math:** Python iebūvētā matemātikas bibliotēka, kas nodrošina dažādas matemātiskas funkcijas un konstantes.

- **Time un Datetime:** Šīs bibliotēkas tiek izmantotas laika operācijām. `Time` izmanto, lai mērītu izpildes laiku, bet `Datetime` piedāvā plašas iespējas darbam ar datumu un laiku.

- **Random:** Ārkārtīgi noderīga, ja nepieciešams iegūt gadījuma skaitļus vai veikt citas gadījuma operācijas.

- **Re:** Regular Expressions bibliotēka, kas ļauj veikt teksta meklēšanu un manipulāciju, pamatojoties uz noteiktiem rakstzīmju modeļiem.

> Katru no šīm bibliotēkām izmanto, lai efektīvi risinātu konkrētus uzdevumus un uzlabotu izstrādes procesu atkarībā no projekta prasībām.
        
3. **Palaidiet Skriptu:**
    
    - Izpildiet skriptu Python vidē.
      
```bash
python project.py
```

### Lietotāja ievade
    
- Izpildiet norādījumus, lai atlasītu izlaiduma veidu un vērtējuma opciju.

```bash
Rate by:
[1] Top (As determined by users' ratings)
[2] Popular (Most number of ratings)
[3] Esoteric (Relatively unknown but with high average ratings)
[4] Diverse (Artists are limited to one entry per chart)
[5] Bottom (As determined by users' ratings)
Choose an option: 2                                                                               # Chosen rating option: Popular rating
```

```bash
Selected types: ['album', 'djmix'] 

[x] [1]: Album
[ ] [2]: EP
[ ] [3]: Mixtape
[x] [4]: DJ Mix
[ ] [5]: Single
[ ] [6]: Compilation
[ ] [7]: All

Select a release type by entering the corresponding number. Press Enter when done.
```

```bash

[1] All-time (charts from all time)
[2] Specific year or decade (for example '1984', '2010s')
[3] Year-range (for example '1984-2016')

Select a time option by entering the corresponding number: 1                                        # Selected time option: All-time

```

- Ievadiet izlaidumu skaitu, ko vēlaties scrapot.

```bash
Enter the number of releases to be collected: 12
```

- Pagaidiet, līdz skripts tiks pabeigts. Tas pāriet uz RateYourMusic charts lapu, izgūs nepieciešamo informāciju un saglabās to CSV failā.

```python
df.to_csv(f"list ranked by {rating_url} rating {date_url}.csv", index=False)                         # save the data
```

- Kad skripts ir pabeigts, tas izdrukās `🫲 here is your clean file. enjoy.` un atmest.

### Apkopoti Dati 

Skripts apkopo šādus datus par katru relīzu:

- Rank
- Title
- Ratings
- Artist
- Date
- Primary Genres
- Secondary Genres
- Descriptors

### Izvade
    
 Dati tiek saglabāti CSV failā ar nosaukumu `list ranked by [rating option] rating [date].csv`. Fails tiek saglabāts tajā pašā direktorijā, kurā atrodas skripts.
 
### **Izbaudiet savus datus**
    
Atveriet ģenerēto CSV failu, lai izpētītu un analizētu apkopoto informāciju. 💫

## Piezīme

- Nodrošiniet stabilu interneta savienojumu izpildes laikā, jo skripts balstās uz tīmekļa nokopšanu.
- Skripts gaida 10 līdz 15 sekundes pirms katra pieprasījuma veikšanas, lai nepārslogotu RateYourMusic serverus un netiktu banēts jūsu IP. *ko rym toatally izdarīja ar mani*
- Ievērojiet RateYourMusic pakalpojumu sniegšanas noteikumus un izmantojiet šo skriptu atbildīgi.
