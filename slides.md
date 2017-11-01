class: center,middle
# Honesty, Kindness and Inspiration: Pick Three

### Jacob Stoebel (@jstoebel)

---
class: center, middle

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Code review can be:<br><br>• honest<br>• nice<br><br>Pick one...</p>&mdash; I Am Devloper (@iamdevloper) May 16, 2017</blockquote>

???
This seems to be the attitude among many developers: I can either 

- Give you feedback that is touchy feely and makes you feel good but is useless or 

- We can get some **real** work done but I will make you feel like garbage. 

- The Tweet received several objections from people wondering aloud why feedback can't be both honest **and** kind.

- Many employers seeking high code quality have created cultures that encourage code reviews leaving developers feeling unappreciated, overly criticized and, ultimately, burned out.

- Women, people of color and developers from other marginalized groups have documented overly harsh, unproductive code reviews that seem more combative than productive. 

- Some developers from those same groups have identified a double standard, where if _they_ were to give overly critical code reviews, they would be dismissed as angry, pushy or difficult to work with.

---

# Toxic Code Reviews: Some Examples
## Paraphrased heavily from Erik Dietrich (@daedtech)

 - Nit picking session: How to name variables, how to organize files, clever one liners...
 - Marathon: Let's go over every line and discuss _ad nauseum_ and compare it with what was changed.
 - Firing Squad: Reviewers' job is to find everything wrong with the code possible.
 - The Exit Exam: The code review is something to be "passed" in order for the PR to be merged.

???
 - There's a great blog article by Erik Dietrich called "How to Use a Code Review to Execute Someone’s Soul" that lists some of flavors of toxic code reviews
 - Nit picking session: Where we spend a lot of time pointing out little things about the code. 
 - I don't think code reviews are the best place for this sort of thing (linters are better)
 - So much of the stuff like this can come up as opinion disguised as fact. "I think local variables should be lowercase_underscored" becomes "variables in ruby should be underscored".
 - Marathon: where we go over everything _ad nauseum_. This may sound harmless enough but 1) do we really have time for that and 2) I've known people in my professional life that are able to get their way simply by talking the longest. When an argument ensues they just dig in their heels for as long as it takes until the opposing party can't go on (tired, hungry, need to pick up their kids, etc.) and they win by default.
 - Firing squad and Exit Exam: where the relationship becomes adversarial. I am going to try to poke as many holes in your code as I can to find deficiencies. Your code either "passes" and gets merged in or "fails" and it doesn't. I think this can have some serious side effects.

---
class: center, middle

# Don't take it personally

???
- I find this framework particularly concerning because it opens the door to toxic criticism couched in the disclaimer that "I'm just focused on the code. Don't take it personally."

- While I agree that as developers we might not want to be _too_ attached to our code, I think the phrase "Don't take it personally" is flawed. We are thought workers after all, and our code is a reflection of the way we view the world. The assumption that we can completely compartmentalize doesn't seem possible to me.

- In a toxic environment where teams don't trust each other we could imagine all kinds of abusive behavior justified with the "don't take it personally" defense.

- "I'm not a nice person, and I don't care about you. I care about the technology and the kernel—that's what's important to me." ~ Linus Torvalds

- I've given this talk before and I've been asked the question "But Linus Torvalds has created so much. For that matter so did Steve Jobs. Aren't brilliant jerks just something worth living with". 

- For one thing, I think this ignores the externalities involved when people in power are allowed to abuse that power under the excuse that their output is so great. Those externalities could include team burnout, people being afraid to speak out or make mistakes (we're a creative profession we need to have _some_ freedom to fail). This can be from the jerk, but also from others due to the negative culture that they contribute to. At its worst there's sexual assault, sexual harassment, discrimination, and workplace bullying just to name a few. If you add all of that up, are brilliant jerks still worth it?

- At its most fundamental level though, I'm not convinced we can ask team mates to just leave their emotions at the door. There is a large body of research out there that we are, at a neurological level, emotional creatures. Emotions are a fundamental part of who we are.

- Where does that leave us? There needs to be some way to help each other arrive at the best code possible.

---
class: center, middle

# Poop Sandwich

_I really liked how you did X, but that part where you did Y, was not so good. You should do Z instead. ...But on the whole I loved how it was ..._

???
- The poop sandwich approach is a _little_ bit better. It helps develop trust within teams because the stuff that's hard to hear is padded between two nice things.
- In a past life, I was a high school drama teacher. Balancing critical feedback with kindness was something always at the forefront of my mind.
- The problem was that the receiver of the feedback sometimes thought of it like a report card: "I got two good grades and one bad one. On the whole I've got a decent GPA."
- The creator thought of the good spots as as uniformly good, not needing change and the bad spots as unfixable, impossible to get any better at.

---
class: center, middle
# Liz Lermon Critical Response Process
_Objective: inspire the creator to go back to their work with fresh eyes, excited about making their creation even better._

???
- I propose that the concept of balancing kindness and honesty is a false dichotomy. Really its about inspiration: inspiration to to go back to the work and make it even better.
- This talk is about the Liz Lerman Critical Response process.
- The basic gist is to inspire the creator to go back to their work with fresh eyes, excited about making their creation even better.
- This story takes us to, believe it or not the dance world. The dance world which Liz Lerman comes from, was and is notoriously harsh in its culture of feedback. Lerman wanted a framework where creators were encouraged to think critically about their work and _wanted_ to revise it as opposed to earning a "good grade" in order to further their career.
- This makes sense: if you're number one objective is to earn a "good grade", what impact would you expect on creativity?
- The Critical Response Process has been used by artists, administrators, scientists, academics, and even in the corporate sector. It isn't constrained to works that we would traditionally call "Art". Really, its for anything creative. Software is a perfect use case for this!

---
class: middle

# The roles

 1. The creator(s): people directly responsible for the work.
 2. The responder(s): offering their honest, encouraging feedback to the work.
 3. Facilitator: keeps us on track by following the framework.

???
Roles can sometimes get blurred.

---
class: middle

# Step 1: Statements of Meaning

- Responders state what about the work had meaning, was interesting or stood out.
- Statements are not evaluative in this step (save those for later)

???
There are four steps to this feedback process:

Step 1: Responders state what about the work had meaning, was interesting or stood out. We can think of this as a way to generate material of what to talk about in more depth later in the process. The important part here is that statements are not evaluative in this step. We save those for later.

There's a great talk from RailsConf 2016 by Nadia Odunayo called _The Guest: A Guide To Code Hospitality_ In it, she proposes that we think about introducing a person to a code base in the same way that a host welcomes a guest into their home. If you are a guest in someone's home you probably wouldn't, upon walking into their home for the first time point out the dirty clothes on the floor. 
---
class: middle

.left-column.column[
## Good Example
"I noticed that the codebase has no dependencies outside the standard library."

]
.right-column.column[
## Bad Example
"This version of Rails is out of date. You should update to Rails 5"
]

???
- Good example: "I noticed that the codebase has no dependencies outside the standard library."
- Bad Example: "This version of Rails is out of date. You should update to Rails 5"
- To be clear: this process isn't trying to somehow silence important criticism. It only asks that those opinions be saved for later.
---
class: middle

# Step 2: Questions From the Creator(s)

Creator(s) ask the responders questions about their work. Responders may give their opinion about things explicitly asked about.

???
- This process aims to put the creator in the driver's seat. That's why the creator gets to go first by asking questions: they get to steer the conversation in the direction that is most useful for them
- Responders may give their opinion about things explicitly asked about.

---
class: middle
# Step 2: a good example

Q: In the docs was it clear to you what this method does and why? If not how could I make it more clear.

A: I think I understand how to call the method but not why I would want to use it. Maybe think about including an example use case.

???
a good example

Q: In the docs was it clear to you what this method does and why? If not how could I make it more clear.
A: I think I understand how to call the method but not why. Maybe think about including an example use case.

---
class: middle
# Step 2: a not so good example

_same question as above_

A: No, and in general the docs were not so well organized. The way you should organize it is...

???
a not so good example
A: No, and in general the docs were not so well organized. The way you should organize it is…
This is out of scope of the original question. Responders should answer the question and nothing else.

---
class: middle

# Step 3: Neutral Questions from Responder(s)

Responder ask questions to make sure they understand the full context. **Questions should not have an embedded opinion.**

???
Step 3: Neutral Questions from the Responders
Responder ask questions to make sure they understand the full context. Questions should not have an embedded opinion.

**LET'S HAVE AN EXAMPLE HERE** 

**If you’ve ever given a talk and had someone give a critique disguised as a question, you know what this is.**

---
class: middle

.left-column.column[
## Good Example
"What ideas guided you to select FactoryBot for this project?"

]
.right-column.column[
## Bad Example
"What were you thinking when you chose FactoryBot for this project?"
]

???
Good Example: "What ideas guided you to select FactoryBot for this project?"

Bad Example: "What were you thinking when you chose FactoryBot for this project?"

Starting a sentence with “what were you thinking” makes your opinion clear. Opinions come at the end. Which brings us to...

---
class: middle

# Step 4: Opinions

Here's where responders may give their opinions on the work **with the consent of the creator(s).**

???
Step 4: Opinions
Here's where responders may give their opinions on the work with the consent of the creator(s).

---
class: middle

.left-column.column[
Responder: I have an opinion about response times in production. Would you like to hear it?

Creator(s): Sure!

Responder: _opinion here_
]

.right-column.column[
Responder: I have an opinion about the use of FactoryBot in this project, would you like to hear it?

Creator(s): No thanks!

_moving on..._
]

---
class: middle

# Alternatives implementations could...
 - Involve agreeing on a standard work flow ahead of time.
 - Happen on the fly

???
 - You may be saying to yourself, this all sounds great, but it wouldn't work for me or my team because of _____. 
 - That's fine! The great thing about this process is that its adaptable. For example:
 - In many work places you can't simply say "no thanks" to your manager. But maybe you can come up with a shared understand of when and how feedback should be given. Here, opinions (so long as they are thoughtful and well timed) are allowed based on the working relationship.
 - On the fly: on the other hand teams can fluidly slip into this process, on the fly, without a formal deceleration that "we are going to do the critical response process now". 
 - As a responder, any time you ask a clarifying question or two before giving an opinion (step 3) that's a win, because you are empowering the creator. The creator doesn't even need to know about the Critical Response Process.
 - Likewise, as a creator you can (given a positive workplace culture) set the conversation on a productive path by asking questions that you are dying to know about your work.
---

# Resources

 - [https://lizlerman.com/critical-response-process/](https://lizlerman.com/critical-response-process/)
 - _Liz Lerman's critical response process: A method for getting useful feedback on anything you make, from dance to dessert_, Liz Lerman and John Borstel (2003)
 - [http://www.jstoebel.com/honesty-kindness-and-inspiration-pick-three/](http://www.jstoebel.com/honesty-kindness-and-inspiration-pick-three/)

---
class: center, middle

# Jacob Stoebel

# @jstoebel

# www.jstoebel.com

