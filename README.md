### Find the Superbug

Welkom bij het bioinformatica deel van 'Find the Superbug'. Onze onderzoekers zijn aan de slag gegaan met de samples die jullie in het veld hebben verzameld, en natuurlijk de samples van de patienten. 

In deze folder vinden jullie samples.txt, in dit bestand zitten de beste DNA fragmenten die wij hebben kunnen sequencen 

Scroll er eens door. Ja, daar kan je niks mee. DNA data is voor mensen eigenlijk niet te lezen. Daarom hebben we hulp van de computer nodig. We hebben al wat code staan die jullie kan helpen.

Echter is dit programma nog niet compleet af...

Het stappenplan: 

**Missie 1:** Van de samples die we hebben zijn een deel microben, maar er kan ook nog menselijk DNA van de patienten tussen zitten. 
Een manier om dit te checken is door het GC-percentage te berkenen. Mensen hebben een GC percentage van ~41% 
**gebruik het script 'DNA_Checker.py' om uit te vinden welk DNA menselijk is, en welk DNA niet**

**Missie 2:** Nu we een selectie hebben gaan we op zoek naar genen. DNA wordt vertaald in hapjes van 3, oftewel codons. Voor elk codon 
staat een Aminozuur, deze vormen uiteindelijk het eiwit. In het script 'DNA_Translator.py' staat een functie 'translate', oftewel vertaal. 
Hierin zit een dictionary met alle mogelijke codons, en de aminozuren die daar bij horen. Deze functie is echter nog niet af. 
**Kunnen jullie deze functie repareren/afmaken?** (Let op: er zijn meerdere Reading Frames)

**Missie 3:** In het lichaam word DNA via RNA vertaald tot een eiwit door de Ribosomen. Het vertalen begint op een startcodon, en eindigt bij een stopcodon.
Een regio van DNA dat op deze manier vertaald kan worden noemen we een 'open reading frame' oftewel een ORF.
DNA dat geen deel is ven een gen heeft vaak meerdere korte ORFs, omdat het DNA daar meer willekeurig instaat. 
Een echt gen heeft een of meerdere grote ORFs.
Wij zijn uiteraard op zoek naar een eiwit dat we kunnen koppelen aan een microorganisme. 
**Gebruik het script 'Protein_Analyser.py' en kijk of je het eiwit kan vinden.**

Heb je het eiwit gevonden?
Dan is de laatste stap het ontmaskeren van de Superbug
Hiervoor gebruiken we een (online) database en een krachtig algoritme (BLAST) dat razendsnel stukken DNA en eiwit met elkaar kan vergelijken. 
Gebruik deze link: [NCBI's Protein BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome)
**Voer je (eiwit!!)sequentie in en vind de Superbug!!!**
