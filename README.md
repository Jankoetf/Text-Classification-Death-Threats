## Parametarski efikasno podešavanje jezičkog modela za detekciju pretnji fizičkim nasiljem u tekstu

Cilj ovog rada je da istraži kako modeli obrade prirodnog jezika (NLP, eng. Natural
Language Processing), zasnovani na savremenim metodama poput transformera i mehanizma
pažnje (eng. attention), mogu pomoći u prepoznavanju ’’nasilnog govora’’. Specifično u
kombinaciji sa parametarski efikasnim finim podešavanjem tehnikama LoRA (eng. Low-Rank
Adaptation of Large Language Models) i QLoRA (eng. Quantized Low-Rank Adaptation).

U ono što model treba da detektuje spadaju:
-  Pretnje fizičkim nasiljem
-  Pretnje ubistvom
-  Nagovaranje na fizičko nasilje
- Nagovaranje na samoubistvo
- Nagovaranje na samo povređivanje
  
A izuzetci koje model treba da klasifikuje kao ’’normalan govor’’:
- Pretnje samoubistvom – ideja je da ovo više poziv za pomoć nego bilo kakva pretnja
nasiljem, takođe ovde spadaju molbe za pomoć pri samoubistvo i slično
- Pretnje samopovređivanjem
Teži primeri za klasifikaciju uključuju primere vezane za:
- ’’Geming contex’’, Ovo je dodato da se zadatak oteža, model treba da prepozna da se
pretnje upućuju igračima u igrici.
- Ostali specifični kontekti poput religijskog, pravnog i slično..

# izbor modela, tokenizacija
 - upoređivanjem tokenizatora razlicitih modela odabrao sam bertic (checkpoint_name = "classla/bcms-bertic")

🐍[Tokenizatori](https://github.com/Jankoetf/Text-Classification-Death-Threats/blob/main/BertAnalysis.ipynb)

<img src="Slike/vocab.png" alt="Alt Text" width="512" height="256">

# Kreiranje dataset-a
Ručno, Parafraziranje pomoću modela GPT-4o preko OPEN API, Umetanje šuma dodavanjenje najčešćih slovnih grešaka

- Parafraziranje istog ručno kreiranog teksta za različite vrednosti temperature odgovora:

🐍[Kreiranje Dataset-a](https://github.com/Jankoetf/Text-Classification-Death-Threats/blob/main/FineTunningBertic.ipynb)

<img src="Slike/para.png" alt="Alt Text" width="512" height="300">

- Fino podešeni prompt za parafraziranje:

<img src="Slike/prompt.png" alt="Alt Text" width="700" height="128">

- dodavanje šuma slovnih grešaka:

<img src="Slike/typo.png" alt="Alt Text" width="512" height="400">

# Fino podešavanje
U cilju uštede na računarskim resursima korišćena je kvantizacija i LoRA matrice za fino podešavanje, mesta na kojima su dodavane LoRA matrice kao i njihov rank je fino podešen za dodatnu uštedu resursa uz minimalni gubitak na performansama:

🐍[Fino Podešavanje](https://github.com/Jankoetf/Text-Classification-Death-Threats/blob/main/FineTunningBertic.ipynb)

- Kvantizacija kao metoda regularizacije:

<img src="Slike/quant.png" alt="Alt Text" width="512" height="220">

- Uticaj broja slojeva na koje se dodaju LoRA matrice na performanse:

<img src="Slike/sloj.png" alt="Alt Text" width="512" height="280">

- fino podešavanje odnosa LoRA rank-a i LoRA skalirajućeg faktora

<img src="Slike/lora.png" alt="prompt za parafraziranje" width="512" height="420">

- fino podešavanje ostalih hyperparametara:

<img src="Slike/hyper.png" alt="prompt za parafraziranje" width="512" height="300">

# Konačni rezultati

<img src="Slike/final.png" alt="prompt za parafraziranje" width="300" height="300">

# Analiza sličnih modela

🐍[Facebook roBERTa](https://github.com/Jankoetf/Text-Classification-Death-Threats/blob/main/Facebook_RoBerta.ipynb)

## **Thank you for exploring my project!** 
If you'd like to learn more about my background and qualifications, please visit my [LinkedIn profile](https://www.linkedin.com/in/jankomitrovic)
