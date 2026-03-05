# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?


- What did the game look like the first time you ran it?
When first running the game, I started guessing based on the range that was displayed. I noticed that it would give false hints and mislead me actually guessing the right number. Also, the game was a bit slow at times, not letting me start a new game, or not letting me guess a number. I also noticed that the number of attempts allowed was different from when clicking a difficulty to the actual attempts on screen. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

What I saw that was when I started is, first, how the game gives false hints when inputting a guess. For example: If a number is 86 and the user inputs 74 as a guess, it will output to "go lower". 
A second broken aspect of the game would be the wrong ranges in levels of difficulty, for the hard difficulty, it will display a range of 1-50, when the normal difficulty is 1-100. Having a smaller range would be more easy to guess.
A third broken aspect is that the secret number does not stay in range according to the difficulty it is in. The number still shuffles through any number, disregarding the range it should be in respect to. For example: The secret number is shuffled to 68, when the range is 1-50.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
