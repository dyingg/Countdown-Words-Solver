# Countdown Words Solver

If 17 letters are taken the number of permutations of just those 17 words are **355687428096000**, this itself is not calculateable and that's not it for 17 words
we also have to consider 16 letter words and ways of selecting 16 letters is 17C16. Thus 17C16 * 16P16 possible words and so on for 15,14,13 .... 
letters. It is virtually impossible to create a list of all possible permutations and check if the created permutation is a valid word.

*Thus instead we go through all valid words* and check if they can be made with the letters we have. 

The time taken to do this reduces significantly with lesser
number of letters and increases slowly with increase in letters.

**Solver 1 uses this approach, and should take under 10 seconds for any reasonable number of letter input**




*No dependencies required*

```bash
python countdown-solver.py

Sucessfully Read Dictionary! Ready for Game!

Enter the game letters:

e e h n a i k y w n o a c t f p b
=========== Words with 17 letters ==========

=========== Words with 16 letters ==========

=========== Words with 15 letters ==========

=========== Words with 14 letters ==========

=========== Words with 13 letters ==========

=========== Words with 12 letters ==========

=========== Words with 11 letters ==========
acetophenin
benefaction
=========== Words with 10 letters ==========
cyaphenine
nonaphetic
nonhepatic
obtainance
pantheonic
phenacaine
phenacetin
phocaenine
phoenicean
pyoctanine
tachypnoea
=========== Words with 9 letters ==========
acanthine
acanthion
acetanion
aitchbone
anapnoeic
anaptychi
anywhence
anonychia
anthobian
anthocyan
anthokyan
antiphona
antiphony
antoecian
apothecia
batyphone
benthonic
betacaine
bipennate
cenotaphy
cinephone
citoyenne
cytopenia
coetanean
copataine
copintank
faineance
faineancy
fantocine
habitance
habitancy
hannayite
heptanoic
heptanone
hypnobate
hypnoetic
.......................truncated over 25000 words found
```


Uses the english words list provided [here](https://github.com/dwyl/english-words), works with any new line seperated list of words and
hence can work with any language.



### Solver 2

Provided to compare with solver 1, crashes for when input letters are larger than 15. Trivally create all possible (n to 2)letter word permutations with the given letters
and checks if they are a valid english word.
