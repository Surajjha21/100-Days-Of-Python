🃏 Day 11 - Blackjack Capstone Project
What is this?

A text-based Blackjack game built in Python as part of Dr. Angela Yu's 100 Days of Code bootcamp. You play against a computer dealer — hit, stand, bust, or hit Blackjack.

Features
Random card dealing
Hit / Stand decisions
Dealer auto-draws until 17+
Ace adjusts from 11 → 1 when needed
Bust, Blackjack, Win, Lose, Draw detection
Restart option after each game
How to Run
bash
python blackjack.py

Requires Python 3.x. That's it.

My Experience

Honestly this one took me around 9+ hours and was the hardest thing I've built so far.

I didn't watch any of Angela's hint videos — just read the rules, drew a flowchart on paper, and figured it out from there. A lot of that time was just me staring at the dealer logic trying to understand why it wasn't working.

The parts that gave me the most trouble:

Dealer draw logic
Ace handling (when to flip 11 → 1)
Managing all the win/lose/draw conditions without making the code a mess
Recursive game flow (which I later learned could've been a while loop)

The code isn't perfect and I know that. But I wanted to finish it my way before watching the solution.

What I Learned

Functions, lists, loops, conditionals, recursion, random module — all the usual stuff. But honestly the bigger thing I learned is that struggling for hours on something and finally getting it to work feels different from following along with a tutorial.

What I'll Fix Later
Replace recursion with a while loop
Show A, J, Q, K instead of numbers
Break it into smaller cleaner functions
Remove repeated print logic
Course

Dr. Angela Yu – 100 Days of Code | Day 11