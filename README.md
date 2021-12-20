# Výpočetní inteligence 1 - Semestrální projekt - Dušek Jan

## Generování MIDI souboru z obrázku notového zápisu
Projekt je zaměřen na čtení obrázku ve formátu .png z kterého detekuje notový zápis.
Po zdárném detekování notového zápisu následuje procedura, která vede k zjištění použitých not a následnému vygenerování 
MIDI souboru, který lze použít například v libovolném hudebním softwaru.
###Mozart
Již zmíněnou proceduru pro čtení not zajišťuje volně dostupný projekt Mozart:<br>
[An optical music recognition Mozart](https://github.com/aashrafh/Mozart) <br>
Na odkazu výše je podrobný popis jak celá procedura probíhá, ve zkratce řečeno: <br>
<ol>
<li>Základní filtrování šumu a segmentace - jelikož noty jsou pravděpodobně zapsány černě na bílém, tak tvoří ideální prostředí pro strojové čtení</li>
<li>Detekce a odstranění notových linek</li>
<li>Vytvoření vlastních notových linek - nevytvoří pouze základních 5 linek ale přidají se i tam, kde standartně nejsou, čímž se zajistí, že každá nota leží na/nad/pod linkou. Díky tomu je zjištění polohy noty přesnější.</li>
<li>Samotná detekce symbolů - výstupem programu je seznam detekovaných symbolů. Symbolem může být myšleno kupříkladu:</li>
<ul>
<li>Nota</li>
<li>Tempo</li>
<li>Takt</li>
<li>Předznamenání</li>
<li>a jiné </li>
</ul>
</ol>

### MIDI file
Výstup Mozarta je předán další částu programu, která se stará o vytvoření MIDI souboru. Převezme list v kterém
jsou ulozeny jednotlivé informace o notovém zápisu a s pomocí knihovnou *midiutil* je vytvořen .mid soubor.
Ještě před samotným generováním je uživatel vyzván k zadání tempa a o kolik mají být noty transponovány.
### Spuštění
Spuštění je stejné jako u projektu Mozart, který je popsán v jeho dokumentaci. Nejjednoduší způsob:<br>
<ul>
<li>install Conda</li>
<li>conda env create -f requirements.yml</li>
<li>conda activate mozart</li>
<li>`python3 main.py &#60;input directory path&#62; &#60;output directory path&#62;`</li>
<li>jsou připraveny i 3 testové případy, jež je možné spustit jednotlivě tímto způsobem `python main.py ../inputCase1 ../outputFolder`</li>
</ul>

### Používané knihovny
- [NumPy](https://numpy.org/doc/stable/index.html)
- [OpenCV](https://opencv.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [scikit-image](https://scikit-image.org/)
- [MIDIUtil](https://github.com/MarkCWirt/MIDIUtil)
- [Mozart](https://github.com/aashrafh/Mozart)
