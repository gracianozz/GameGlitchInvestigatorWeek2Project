# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?


- What did the game look like the first time you ran it?
When first running the game, I started guessing based on the range that was displayed. I noticed that it would give false hints and mislead me to actually guessing the right number. Also, the game was a bit slow at times, not letting me start a new game, or not letting me guess a number. I also noticed that the number of attempts allowed was inconsistent from when clicking a difficulty to the actual attempts on screen. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

What I saw that was when I started is first, how the game gives false hints when inputting a guess. For example: If a number is 86 and the user inputs 74 as a guess, it will output to "go lower". 
A second broken aspect of the game would be the wrong logic in ranges in levels of difficulty. For the hard difficulty, it will display a range of 1-50, when the normal difficulty is 1-100. Having a smaller range would be more easy to guess.
A third broken aspect is that the secret number does not stay in range according to the difficulty it is in. The number always shuffles 1-100, disregarding the range it should be in respect to. For example: The secret number is shuffled to 68, when the range is 1-50.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI tool that I used for this project is Github Copilot. Github Copilot helped with properly fixing and adjusting bugs that I found were wrong in the code. Overall, 3 codes were fixed, and the code now runs better than before. 


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of when an AI suggestion was correct was how it fixed the hints given when a user guessed the number. Copilot identified and suggested the correct logic change to make the hints more reasonable. When running the program again, I saw that the logic error was fixed. 


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One example of an AI suggestion that was incorrect was when Copilot was trying to "fix" more than what I asked in my prompt. Copilot tried changing the overall format of the code layout after I had asked to move a logic function to the logic_utils.py. It moved more than the single intended function and added extra lines of code to fix more problems it "thought" it had detected. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
To decide whether a bug was fixed or not, I prompted Copilot to create pytests for the bugs that we fixed previously. Copilot generated 5 tests for the first and second bugs found and fixed, and when testing the tests on the terminal, all came back as passed. I also re-ran the program to see if everything was logical. Overall, with the new fixes, the program runs more smoothly and the user is better able to guess and choose a difficulty appropriately. 


- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
A test I ran manually was testing to see whether the correct hints were given when guessing the "secret" number. When starting a game, I would purposelly choose a number lower and a number higher than the "secret" number to verify whether the correct hint was outputted. Next, I tried playing a game without looking at the "secret" number to see whether I can guess the number using only the hints.


- Did AI help you design or understand any tests? How?
Yes, AI helped me design and understand the tests that were generated. AI gave comments about each test case to make me more understand what each test was testing for, as well as comments to know what should be returned. Using the assert keyword, this is what really determined whether each test passed or failed. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because of how everytime a button was clicked, streamlit reruns the whole program again, and basically "resetting" the app so it refreshes and changes its numbers. Variables are recreated and regenerated each time the button was clicked. This made it much harder to actually guess the correct number. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
An easy way I would explain how Streamlit "reruns" to a friend who has never used Streamlit would be that they can think of it as a writing on a paper. Every time a user interacts with a button or interacts with the app, the writing on the paper gets erased and the user has to start writing from the top again.

- What change did you make that finally gave the game a stable secret number?
The change that I made that gave the game a secret stable number was storing the number using st.session_state and assigning it to the generated number. This allows a number to be preserved , and does not allow the number to change with every rerun. Keeping the same number will help with actually having the chance at guessing the right number, and overall being able to play the game. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I have never been much familiar with using Git commands, and using them to implement this project helped me become more familiar with their use and how they work. I'd love to reuse these habits into future projects so they can help describe and show the work and projects I have collaborated and helped work on. 

- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently next time I work with AI on a coding task is to be as specific as possible when using AI for debugging. When focusing on a problem, I noticed that the best way to help solve a bug is to be as specific as possible, so the AI does not add any extra attributes or "fixes" it may think might help. This way it only focuses on what you ask the AI to do.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed the way I think about AI generated code by showing me how flawed AI can sometimes be when making apps. From simple logic erros, to actual crashes that may happen in the app, AI can make many mistakes, and being solely dependent on AI can cause many problems for upcoming projects and programs. 


