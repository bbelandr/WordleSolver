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
wordFound = False
for i in range(6):
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
    for recommendedItem in sortedScores:
        recommendedWord = recommendedItem[0]
        recommendedScore = recommendedItem[1][0]
        recommendedPercent = recommendedItem[1][1]
        while True:     # Nested for loop to let us keep printing sortedScores without iterating to the next item
            print(f"I recommend this word: {recommendedWord}, score of {recommendedPercent}")
            colors = input("Tell me the colors of the letters in order (like 'bbgyb'): ")
            if colors == 'p':
                print(sortedScores)
            else: 
                break
        if colors == 'n':   # User wants to see the next recommended word
            continue
        if len(colors) == 5 and set(colors).issubset({'g', 'b', 'y'}):  # User entered colors
            break;
        else:   # User entered something that wasn't recognized
            break

    if colors == 'ggggg' or colors == 'q':   # We solved the puzzle or the user just wants to stop the whole program
        break
        

    # Count green and yellow occurrences for each letter in the guess
    from collections import Counter

    guess = recommendedWord
    green_yellow_counts = Counter()
    for i, c in enumerate(colors):
        if c in ('g', 'y'):
            green_yellow_counts[guess[i]] += 1

    toRemove = set()
    for word in scoreDict:
        remove = False
        word_counter = Counter(word)
        # First, check green and yellow rules
        for i, c in enumerate(colors):
            l = guess[i]
            if c == 'g':
                if word[i] != l:
                    remove = True
                    break
            elif c == 'y':
                if word[i] == l or l not in word:
                    remove = True
                    break
        # Now, check black rules
        for i, c in enumerate(colors):
            l = guess[i]
            if c == 'b':
                allowed = green_yellow_counts[l]
                if word_counter[l] > allowed:
                    remove = True
                    break
        if remove:
            toRemove.add(word)

    for word in toRemove:
        del scoreDict[word]

    # Reset scoreDict scores (but keep the remaining words)
    for word in scoreDict:
        scoreDict[word][0] = 0

