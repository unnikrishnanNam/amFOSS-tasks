cmd = input()
spellWordCount, wordsCount = cmd.split()
spellWordCount = int(spellWordCount)
wordsCount = int(wordsCount)

wordDic = {}

for i in range(wordsCount):
    translationWords = input('')
    firstWord, secondWord = translationWords.split()
    if len(firstWord) < len(secondWord):
        firstWord, secondWord = secondWord, firstWord
        wordDic[firstWord] = secondWord
    if len(firstWord) == len(secondWord):
        wordDic[secondWord] = firstWord
    else:
        wordDic[firstWord] = secondWord

spell = input()
spellLst = []
spellLst = spell.split()

for count, word in enumerate(spellLst, start=0):
    if spellLst[count] in wordDic:
        spellLst[count] = wordDic[word]

finalSpell = ""
for j in spellLst:
    finalSpell = finalSpell + j + ' '
    
print(finalSpell)
