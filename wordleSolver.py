#!/usr/bin/env python3

# While unsolved:
    # Determine what word to choose
        # Running total
            # For each word in scoreDict:
                # clear presentLetters
                # For each letter in word:
                    # presentLetters.Pushback each non-duplicate letter (use a set)
                # For each letter in presentLetters:
                    # Increment wordLetters by letter
        # Scoring the words
            # For each word in scoreDict:
                # # For each letter in word:
                    # presentLetters.Pushback each non-duplicate letter (use a set)
                # For each letter in presentLetters:
                    # letterScore = wordLetters[letter]
                    # scoreDict[word][0] += letterScore
        # Sort 
        # Pick the greatest one from scoreDict
        # Reset the scoreDict if the word managed to go through
    # Read what the colors of the word were
    # Update the list of possible words

import re

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I N I T I A L I Z A T I O N
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

introString = """\n\n\n\n\n\n\n\n\n\n\n

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
                                                   
███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗   
██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗  
███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝  
╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗  
███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║  
╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝  
"""
print(introString)

# Layout is like this:
# "Word": [score, percent chance of being in wordle]
scoreDict = {}

goodWords = open("wordleWords").read().splitlines()
for line in goodWords:
    lineElements = line.split()
    scoreDict[lineElements[0]] = [0, float(lineElements[1].strip('%'))]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# D E T E R M I N E   W H A T   W O R D   T O   C H O O S E
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Running total
    # For each word in scoreDict:
        # For each letter in word:
            # presentLetters.Pushback each non-duplicate letter (use a set)
        # For each letter in presentLetters:
            # Increment wordLetters by letter
wordLetters = {chr(c): 0 for c in range(ord('A'), ord('Z') + 1)}   # Dictionary of characters A-Z
presentLetters = set()
for word in scoreDict:
    presentLetters.clear()
    for letter in word:
        presentLetters.add(letter)
    for letter in presentLetters:
        wordLetters[letter] += 1
# print (wordLetters)

# Scoring the words
    # For each word in scoreDict:
        # # For each letter in word:
            # presentLetters.Pushback each non-duplicate letter (use a set)
        # For each letter in presentLetters:
            # letterScore = wordLetters[letter]
            # scoreDict[word][0] += letterScore
for word in scoreDict:
    presentLetters.clear()
    for letter in word:
        presentLetters.add(letter)
    for letter in presentLetters:
        letterScore = wordLetters[letter]
        scoreDict[word][0] += letterScore

# Sorting the results
sortedScores = sorted(scoreDict.items(), key=lambda item: item[1][0], reverse=True)

# Choosing a word to present to the user
recommendedItem = sortedScores[0]
recommendedWord = sortedScores[0][0]
recommendedScore = recommendedItem[1][0]
recommendedPercent = recommendedItem[1][1]
print(f"I recommend this word: {recommendedWord}, score of {recommendedPercent}")

colors = input("Tell me the colors of the letters in order (like 'bbgyb'): ")
for i in range(5):
    color = colors[i]
    letter = recommendedWord[i]
    toRemove = set()    # Marks words to be removed because we can't remove them during iteration in the for loop
    if color == 'g':
        # Removing all words that don't have this letter in spot 'i'
        for word in scoreDict:
            if word[i] != letter:
                toRemove.add(word)
    if color == 'b':
        # Removing all words that have this letter
        for word in scoreDict:
            indices = [idx for idx, char in enumerate(word) if char == letter]
            # indicies = list of every occurance of current letter
            # for each index in indicies:
                # looking for greens first
                # if colors[index] = 'g':
                    # remove all words without the letter in index
            
            # if len(indices) != 0: # if this letter is in word
            #     if 
            #     toRemove.add(word)

    # Removing words marked for removal
    for word in toRemove:
        del scoreDict[word]
print(scoreDict)
