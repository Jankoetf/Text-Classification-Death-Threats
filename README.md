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

<img src="Slike/vocab.png" alt="Alt Text" width="512" height="256">

# Fino podešavanje
U cilju uštede na računarskim resursima korišćena je kvantizacija i LoRA matrice za fino podešavanje, mesta na kojima su dodavane LoRA matrice kao i njihov rank je fino podešen za dodatnu uštedu resursa uz minimalni gubitak na performansama:

- Kvantizacija kao metoda regularizacije:

<img src="Slike/quant.png" alt="Alt Text" width="512" height="384">

- Uticaj broja slojeva na koje se dodaju LoRA matrice na performanse:

<img src="Slike/sloj.png" alt="Alt Text" width="512" height="640">

- fino podešavanje odnosa LoRA rank-a i LoRA skalirajućeg faktora

<img src="Slike/lora.png" alt="Alt Text" width="512" height="896">




## Filtering Sections
- Next I experimented with different digital image preprocessing filters in order to get that edge detection, in most cases order of operation is
1. Bluring
2. Edge detection
3. Thresholding

Here are examples of filtered images:
- Manual sharpen and edge detection masks
<img src="Pictures/c1.PNG" alt="Alt Text" width="512" height="256">

- Canny filter + thresholding
<img src="Pictures/c2.PNG" alt="Alt Text" width="512" height="256">

- Sobel filter + thresholding
<img src="Pictures/c3.PNG" alt="Alt Text" width="512" height="256">

- Using adaptive tresholding on Gaussian and Median Blur
<img src="Pictures/c4.PNG" alt="Alt Text" width="512" height="256">


## Fitting Sections
When I just preproces whole train and test set with one of these filters and fit model, I dont get much of improvement.
My strategy is:
1. Loading whole train set
2. Preprocessing it with one of best filter
3. Creating a model
4. Train the model for 10 epochs
5. Preprocessing whole train set again using different filter
6. Training an already trained model for 3 or 5 more epochs
7. Repeat 5. 6. several times

What I found is that filters that do adaptive thresholding on blured image, works the best in combination.
With this aproach I imroved generalization of model, in the end of process I get accuracy around 80%.


<img src="Pictures/last.PNG" alt="Alt Text" width="342" height="378">

## **Thank you for exploring my project!** 
If you'd like to learn more about my background and qualifications, please visit my [LinkedIn profile](https://www.linkedin.com/in/jankomitrovic)
