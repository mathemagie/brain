Title: The Complete Beginners Guide To Autonomous Agents

URL Source: https://www.mattprd.com/p/the-complete-beginners-guide-to-autonomous-agents

Markdown Content:
Ok, let’s start with what you already know.

Artificial intelligence can be used to complete very specific tasks, such as recommending content, writing copy, answering questions, and even generating photographs indistinguishable from real life.

You tell the AI to complete the one task, it completes the one task. Simple.

But what if you don’t want to have to come up with all of the tasks for the AI to do? What if you want a teammate rather than just a tool? What if you want the AI to think for itself?

Like _really_ think for itself.

Imagine you made an AI that you could give an objective to, even something as vague as “Create the best ice cream in the world”, and the AI would come up with a todo list, do the todos, add new todos based on it’s progress, and then continue this process until the objective was met.

This is exactly what “Autonomous Agents” do, and they are the fastest growing trend amongst AI developers, yet most people don’t know about them.

(_At the time of writing this article, no major publications have written about autonomous agents, and since publishing, only a few have covered it, so if you’re reading this… you’re very early.)_

**What are autonomous agents?** Why are they such a big opportunity? How do they work? What does this look like in the future? How can I build or use one? How can I meet other people interested in autonomous agents?

These are the questions I’m going to answer for you right now.

**Ready?** Let’s do this.

“\[Intelligent\] autonomous agents are the natural endpoint of automation in general. In principle, an agent could be used to automate any other process. Once these agents become highly sophisticated and reliable, it is easy to imagine an exponential growth in automation across fields and industries.”

_p.s. I am CEO and co-founder of Octane AI, where for seven years we have been building conversational AI products, and are more recently building generative AI and autonomous agent solutions for brands. In 2016 I predicted that around now chatbot interfaces would take off and start to replace standard website UI, and now over 100 million people use ChatGPT and websites like it. I am now similarly predicting that autonomous agents will be widely adopted in the future, but this prediction won’t take seven years to come true, it will happen blazingly fast._

_p.p.s. After writing this article I showed the draft to 125 of the smartest and most interesting people I know, including_ _Emad Mostaque (Founder of Stability AI), Tony Hu (Former Acting Head of Emerging Technology for the FBI, and founder of Bondoo AI),_ _Troy Carter (Lady Gaga’s ex Manager), Sahil_ _Lavingia (Founder of Gumroad), Elizabeth Yin (Co-Founder of Hustlefund VC), Hugh Howey (Author of Wool), Chris Yeh (Author of Blitzscaling), experts from NVIDIA, Meta, investors like Ryan Hoover (creator of Product Hunt) and Erica Brescia (Manager Director of Redpoint Ventures, prior Github COO), and many many more. Their thoughts and opinions are sprinkled throughout, they will give you unique insights shared with the world for the first time._

### Want to watch a video instead of read an article?

![Image 33](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/29d7b2fd-822d-4197-968b-ecf86fb6ec7f/1_J-7Jfb3H2T-0BbjXtwhxIQ.png)

### **What Are Autonomous Agents?**

**Autonomous agents are programs, powered by AI, that when given an objective are able to create tasks for themselves, complete tasks, create new tasks, reprioritize their task list, complete the new top task, and loop until their objective is reached.**

Read that description above one more time, because while it is simple, it is _wild_.

“The future of autonomous agents looks like everybody becoming a manager.”

Yohei Nakajima, creator of BabyAGI

Autonomous agents can be designed to do any number of things, from managing a social media account, investing in the market, to coming up with the best children’s book.

“_And these are, like, real? These exist right now?”_

Yes, I know it sounds like science fiction, but these are functioning and real. If you can code you can make one in just a few minutes. And it is only the beginning.

“Humans waste inordinate amounts of time doing work that is tedious and manual when it could be done by computers and free them up for more creative pursuits, or to do things that only humans can currently do. Autonomous agents will enable people to get so much more done in so much less time, and - hopefully - spend much less time in front of screens over time!”

**The programming techniques and the AI needed to power autonomous agents are real and** _**extremely**_ **new.** There are many open source projects, like AutoGPT, BabyAGI, and Microsoft’s Jarvis, that are trending on Github and within AI communities and departments.

**In the first two weeks of the creation of open sourced autonomous agent code bases, almost 100,000 developers are building autonomous agents, improving them, and pushing them to their limits, and thats only in the first few weeks of these concepts being invented.** The number of developers working with this technology is growing at an increasingly faster rate.

“AI agents will be everywhere. Billion-dollar companies will come from a small team that deploys ai agents.”

It has grown larger than long time popular codebases including laravel, bitcoin, django, and pytorch.

![Image 34](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/436026dd-2207-4670-ad61-df9bb1f8e6b2/star-history-2023417.png)

Auto-GPT Github popularity increasing exponentially, faster than any codebase in history

This is not science fiction. Many think these autonomous agents are the beginning of true Artificial General Intelligence, or commonly referred to as “AGI”, which is a term used to describe an AI that has gained sentience and become “alive”.

“Autonomous agents may end up commoditizing all applications of factual knowledge. If access to factual knowledge also becomes universal, then human qualities like creativity, emotion, and strategic vision will become even more distinctive. But it is also possible that knowledge becomes increasingly proprietary, as individuals and companies try to gain economic advantage in a world where applications of factual knowledge are commoditized, and the collective knowledge of humanity begins to stagnate.”

**Check out this autonomous agent that was just released from HyperWrite**, you can see it living in the browser and helping you order a pizza.

You just say “_order a large plain pizza from Dominos to One Vanderbilt_” and it just… does it.

![Image 35](https://lh3.googleusercontent.com/Vbxoc1iegjM5hexwdepwXbXZ4nSIbJTVD_brQJayST0vbxRi3ba1ZZnIuYS4mcpkIm5lCCfTfIUfFPB-wUxmeKs2EZOIU_obZXqI_GeValwwv6kkFJcSgDn1IKVBxSxsoIHZK3WWew4orRFE-JSyYAg)

HyperWrite’s autonomous agent controlling the browser to order pizza

Or, maybe even more impressive, **check out this experiment done in collaboration between Stanford and Google where they created a virtual town of 25 autonomous agents, and told one of them to plan a Valentine’s day party.**

The simulated people went about their days, talking to each other, forming new memories, and eventually most of them heard about, and showed up to, the Valentine’s day party.

![Image 36](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e17f0051-f42b-41ca-9c59-988f6f7d119a/What-are-Generative-Agents.jpg)

From the research paper “Generative Agents: Interactive Simulacra of Human Behavior”

“_Ok, uh, crazy… So autonomous agents are real... And you just tell it what it’s goal is and then after that it manages itself forever?_”

Yep.

**You just give it the one objective, and the autonomous agent does the rest.**

Just like a really good employee or teammate.

Although, if you wanted to, you could also design the autonomous agent to check in with you at certain key decision making moments so that you could momentarily collaborate on their work.

“It is "primitive AGI". It is remarkable that simply wrapping an LLM inside a loop gets you an autonomous agent that can reason, plan, think, remember, learn - all on its own. It demonstrates the untapped power and flexibility of what LLMs can do if wrapped in the right structures and prompts. The entire concept is less than month old so I can't wait to see how increasingly sophisticated agents built off of increasingly more capable LLMs impact the world.”

“_But what can autonomous agents do, Matt? Like when you say they complete tasks, what the heck do you mean by that?_”

Great question!

**In addition to analyzing their objective, and coming up with tasks, autonomous agents can have a range of abilities that can enable them to complete any digital task a human could, such as:**

*   Access to browsing the internet and using apps
    
*   Long-term and short-term memory
    
*   Control of your computer
    
*   Access to a credit card or other form of payment
    
*   Access to large language models (LLMs) like GPT for analysis, summarization, opinion, and answers.
    

Also, these autonomous agents will come in all shapes and sizes. Some will operate behind the scenes where the user is unaware of what they are doing, while some will be visible, like in the example above, where the user can follow along with each “thought” the AI has.

“Autonomous agents will allow everyone to live like a head of state! Need something done? Just ask, and your agents will take care of the rest. Never again will you have to waste brainpower on the routine or mundane.”

“_Matt, I’m reading what you’re writing, I think I know what you are saying, but can you write out an example in plain english so I can be sure I understand._”

Yes, of course.

(_pssst… Are you liking this article so far? I’m thinking of making some YouTube videos too!_ _[Subscribe to my YouTube @MattPRD](https://www.youtube.com/@mattprd?sub_confirmation=1&utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents)_ _to get alerted when they are up._)

#### **Here is a super simple example of how an autonomous agent could work.**

Let’s say that there is an autonomous agent that helps with research, and we want a summary of the latest news about a certain topic, let’s say “News about Twitter”

*   We tell the agent “Your objective is to find out the recent news about Twitter and then send me a summary”.
    
*   So the agent looks at the objective, uses an AI like OpenAI’s GPT-4 which allows it to understand what it is reading, and it comes up with it’s first task. “Task: Search google for news related to Twitter”.
    
*   The agent then searches google for Twitter news, finds the top articles, and comes back with a list of links. The first task is complete.
    
*   Now the agent looks back at its main objective (to find out the recent news about Twitter and then send a summary) and at what it just completed (got a bunch of links of news about Twitter) and decides what its next tasks need to be.
    
*   It comes up with two new tasks. 1) Write a summary of the news. 2) Read the contents of the news links found via google.
    
*   Now the agent stops for a second before continuing, it needs to make sure that these tasks are in the right order. Should it really be writing the summary first? No, it determines that the top priority is to read the contents of the news links found via google.
    
*   The agent reads the content from the articles, and then once again comes back to the to do list. It thinks to add a new task to summarize the content but that task is already on the todo list so it doesn’t add it.
    
*   The agent checks the todo list, the only item left is to summarize the content it read, so it does that. It sends you the summary just like you asked.
    

**Here is a diagram showing how this works**.

![Image 37](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4a72cdad-debc-4ec4-b5a0-9efbb92bfedd/1_jlH0NK5y1lDFoYT0NNEYtw.png)

From Yojei Nkajima’s BabyAGI

Pretty cool right?

And keep in mind that this is the very beginning of this new paradigm. **It’s not perfect, it hasn’t taken over the world yet, but the concept is frighteningly powerful and with increased development and experimentation will quickly find it’s way into our daily lives.**

“This will soon transform many industries. It will be a lot easier for people to do many things at once with the use of Autonomous Agents. Just give it a task, and it will complete it. Such a powerful concept so far…”

So now you understand at a high level what an autonomous agent is, but why exactly are these such a big opportunity?

Let’s get into it.

“If we're able to get the information we need faster, will this allow us to free up time to dedicate to thinking and vs. doing? Will even better and more creative ideas surge as a consequence of investing less time on tasks that can be carried by this AI agent?**”**

![Image 38](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e5f56bd-f116-4277-90dc-97dd9f10f197/1_nsL0aXig57B0oDgnTI94Zw.png)

### **Why Autonomous Agents Are Such A Big Opportunity**

It’s pretty clear that soon you won’t only have the options of hiring humans as employees, you will have the ability to hire AIs in the form of autonomous agents.

“In the mid-term, I believe you’re going to see a huge rise in 1-2 people startups that use a combination of AutoGPTs and tools like ChatGPT. And they’ll be able to make the kind of progress you’d previously had expected from a 100 person startup. Long-term I believe that most work can and will be replaced by AutoGPTs.”

And they are not going to be nearly as expensive as people are, they won’t sleep, they won’t quit, and they will work extremely efficiently.

“Part of the thesis when I started Product Hunt in 2013 was a belief that the barrier to build software products would continue to lower, enabling smaller teams (or a single person) to build more and faster than ever before. This has never been more true today, accelerated by AI and autonomous agents. This introduces anxiety for some and opportunity for others that leverage this tech to scale their ideas with fewer people and capital required. In the end, consumers will greatly benefit through increased competition and experimentation of new solutions to their problems.”

#### **These autonomous agents will exist in every industry and for every task imaginable.**

These are just a handful of examples. Let your imagination run wild.

![Image 39](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/216320e2-5892-461e-be2a-3b641de4dd54/image.png)

The list can go on and on. Anything a person could do, an autonomous agent will (eventually, but soon, and in some cases already) be able to do better.

“The music industry has imposed too many unnecessary layers that sit between an artist and success. Those layers cost an artist close to 35% of their net income. Autonomous Agents will be able to build and execute marketing strategies, engage with fans, build communities, route tours, book venues, and negotiate contracts. Saving the artist money and time.”

So what do you do with this information?

**There are two very real opportunities.**

1.  **You create autonomous agents** and make them available for others to hire.
    
2.  **You hire autonomous agents** and can now afford to be more productive in your personal life, or in business.
    

“Autonomous Agents are the next wave — not just in tech, but in business at large. I predict that within 10 years, there will be multiple billion-dollar companies run entirely by autonomous agents. It is inevitable.”

Imagine a world where one person builds a company with only autonomous agents on their team. Within your lifetime you will likely see a one person team do this and reach a market cap of over a billion dollars, something it usually takes many many people working together to accomplish.

“Personalization at scale is going to be a very interesting use case. You will be able to put on auto-pilot multi-step processes that humans do today that involves generating personalized images, videos, websites, emails or even calls at scale. One use case that has sparked a lot of interest is sales prospecting”

Right now in the early days there will be a period of time where early movers, either on making autonomous agents, or using them, will have a huge advantage against competition that is not yet leveraging these systems.

“In the near future, I expect to see lunch meetings, phone calls, and interviews appear on my calendar without my involvement. My agents and their agents will have made it happen, taking care of all the details. I just need to be there.”

By reading this article you are already ahead of 99% of the world.

Let’s dive into more detail on how these autonomous agents work.

“Autonomous agents have the potential to supercharge the output of smaller content creators and community members, especially those with creative imaginations. This will be a boon for many Web3 projects.”

![Image 40](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f303f1df-e8cc-44d9-b65a-006863f6acc8/1__Ps7KZUjIRR2zJuXc3y0Lg.png)

### **How Autonomous Agents Work**

You’ve already read over a high level of how autonomous agents work, but I thought it would be helpful to give you one version of an overall framework, as well as break down a couple examples of autonomous agents step by step.

“I see AI as a whole right now and we are in the building blocks that will evolve to become artificial intelligence assistants like we have seen in the movies -- like Jarvis from Ironman or TARS from Interstellar.

Right now is a time to build out the frameworks because the AI itself is still improving. The answers might not be that good. It might have errors. But just looking at how much has improved with respect to AI in the last 6 months, I think we can barely imagine how things will be in the next 1-2 years. So this is about experimenting early, fast, and skating where the puck is heading.”

**First, here a generalized framework for an autonomous agent**:

1.  **Initialize Goal**: Define the objective for the AI.
    
2.  **Task Creation**: The AI checks its memory for the last X tasks completed (if any), and then uses it’s objective, and the context of it’s recently completed tasks, to generate a list of new tasks.
    
3.  **Task Execution**: The AI executes the tasks autonomously.
    
4.  **Memory Storage**: The task and executed results are stored in a vector database.
    
5.  **Feedback Collection**: The AI collects feedback on the completed task, either in the form external data or internal dialogue from the AI. This feedback will be used to inform the next iteration of the Adaptive Process Loop.
    
6.  **New Task Generation**: The AI generates new tasks based on the collected feedback and internal dialogue.
    
7.  **Task Prioritization**: The AI reprioritizes the task list by reviewing it’s objective and looking at the last task completed.
    
8.  **Task Selection**: The AI selects the top task from the prioritized list, and proceeds to execute them as described in step 3.
    
9.  **Iteration**: The AI repeats steps 4 through 8 in a continuous loop, allowing the system to adapt and evolve based on new information, feedback, and changing requirements.
    

_Pretty incredible._

But, now lets apply it to a few different use cases I decided to extrapolate on.

“Autonomous agents are truly captivating to me because they embody the ultimate productivity booster. As someone who highly values automation for tedious or repetitive tasks, I find that these agents have the potential to revolutionize the way we work, allowing us to direct our mental energy towards more meaningful pursuits.”

Gabriel Menezes, Director of Engineering at Octane AI

![Image 41](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f2c8e3de-907a-45eb-a20a-43bcaea19d64/1_h3CgCiahAzcNJV80BUtIkg.png)

#### **Example #1: Social Media Manager Autonomous Agent**

Let’s say that instead of hiring a social media manager to manage your social media accounts, instead you wanted an autonomous agent to do everything for you at a fraction of the cost and with round-the-clock intelligence.

“This is beyond just virtual assistants. This is a revolution in accelerating all work, research, and even play online. Anything you can do online that takes hours, days, months can now be completed in the background in minutes.”

Here’s what a framework for that autonomous agent might look like.

1.  **Initialize Goal**: Set up the initial parameters, such as target audience, social media platforms, content categories, and posting frequency.
    
2.  **Data Collection**: Collect data on past social media posts, user interactions, and platform-specific trends. This could include likes, shares, comments, and other engagement metrics.
    
3.  **Content Analysis**: Analyze the collected data to identify patterns, popular topics, hashtags, and influencers relevant to your target audience. This step could involve natural language processing and machine learning techniques to understand the content and its context.
    
4.  **Content Creation**: Based on the analysis, generate content ideas and create social media posts tailored to the platform and audience preferences. This could involve using AI-generated text, images, or videos, as well as incorporating user-generated content or curated content from other sources.
    
5.  **Scheduling**: Determine the optimal time to post each piece of content based on platform-specific trends, audience activity, and desired frequency. Schedule the posts accordingly.
    
6.  **Performance Monitoring**: Track the performance of each post in terms of engagement metrics, such as likes, shares, comments, and click-through rates. Gather user feedback, if possible, to further refine the understanding of audience preferences.
    
7.  **Iteration and Improvement**: Analyze the performance data and user feedback to identify areas for improvement. Update the content strategy, creation, and scheduling processes to incorporate these insights. Iterate through steps 2–7 to continuously refine the social media management system and improve its effectiveness over time.
    

“People will own personal agents which communicate with agents owned by other people and businesses. Most computing devices will primarily serve as communication devices for speaking with agents.”

By incorporating this loop-type system in social media management, you can create a dynamic and adaptive strategy that evolves with your audience’s preferences and the constantly changing social media landscape. This will help to increase engagement, reach, and overall effectiveness of your social media efforts.

“Another use case for an autonomous agent that excites me is its application in the realm of music composition. By leveraging the power of AI-driven algorithms, these agents can analyze my personal preferences, favorite genres, and even specific musical elements that resonate with me. They can then generate original melodies, harmonies, and rhythms, effectively co-creating music alongside me. This creative collaboration has the potential to broaden my musical horizons, enabling me to explore new styles and genres I may not have considered before. Moreover, the autonomous agent can provide valuable feedback on my compositions and offer suggestions for improvement, nurturing my growth as a musician. The fusion of AI and human creativity in the music composition process can lead to innovative and unique results, expanding the boundaries of artistic expression.”

![Image 42](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e75c3dbc-651b-4764-8ca3-d882f12b14f4/1_897Tp2yVdC4_HsA15Q_hmA.png)

#### **Example #2: Political Campaign Manager Autonomous Agent**

What if you are running for political office and you want to leverage an intelligent and never-sleeping assistant to help you win?

“I’m excited about agents that do work that’s not necessarily hard to do but just require some time and effort for example things like booking flights I would love to outsource to an agent”

This is what an autonomous agent that helps you win an election might look like.

1.  **Initialize Goal**: Win the election by securing the majority of votes.
    
2.  **Data Collection**: Gather data on voters, demographics, key issues, campaign messaging, and other relevant information.
    
3.  **Context Analysis**: Analyze the collected data to identify trends, opportunities, and challenges. Refine the initial goal into specific subgoals based on this analysis, such as targeting undecided voters, increasing voter turnout in key areas, or improving campaign messaging on particular issues.
    
4.  **Task Generation**: Generate tasks related to the refined subgoals, such as planning voter outreach events, creating targeted advertisements, or developing policy proposals.
    
5.  **Task Prioritization**: Rank tasks based on their potential impact on achieving the subgoals and the overall goal of winning the election.
    
6.  **Task Execution**: Execute the highest priority tasks, allocating resources and assigning team members as needed.
    
7.  **Performance Monitoring**: Assess the effectiveness of completed tasks by tracking key performance indicators like voter engagement, public opinion, and fundraising metrics. Evaluate the success of individual tasks and overall campaign progress toward the subgoals and initial goal.
    
8.  **Iteration and Improvement**: Analyze the performance data to identify areas for improvement. Update the campaign strategy to incorporate these insights. Iterate through steps 2–8 to continuously refine the political campaign management system and improve its effectiveness over time.
    

“I'm most excited by the recursive self-cloning capability. The AI agent can create a copy of itself, pass on task directives, and start talking with its own sibling to get the job done. It is quite a remarkable but alien emergent ability.”

At first one candidate might use an autonomous agent and have a huge advantage over everyone, but then imagine what this looks like once every candidate has one… or many.

“I don't think everyone will use autonomous agents. They will be everywhere but as AI becomes ubiquitous there will be a revival of 100% human work. Many people will rediscover pen and paper, want human only made art... We will see many products and creations that will advertise "only made by humans". It should become a very popular label very soon. The more technology grows the more I am enjoying myself long periods of completely offline time, soon also "off AI" time.”

![Image 43](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/478aeb81-9701-4968-946f-4142f8b27c64/1_j-ESi7uCbpxvutDwr_lmPg.png)

#### **Example #3: Math Tutor Autonomous Agent**

Here is an autonomous agent that is designed to teach a child math.

“This is a breakthrough paradigm that has a LOT of room for exploration. Although early experiments have limited agents to search queries, we're going to see a wide range of research and side projects arming autonomous agents with new batches of tools. Each set of tools will significantly expand the potential use cases.”

1.  **Initialize Goal**: Identify the child’s current math skill level and set a personalized learning path to help them improve.
    
2.  **Data Collection**: Gather information on the child’s learning style, progress, and performance through assessments, interactions, and feedback.
    
3.  **Context Analysis**: Analyze the collected data to identify strengths, weaknesses, and learning preferences, as well as any external factors influencing the child’s progress.
    
4.  **Task Generation**: Generate tutoring tasks based on the child’s needs and learning path, such as selecting appropriate exercises, providing explanations, or offering real-life examples and applications.
    
5.  **Task Prioritization**: Rank tutoring tasks based on their potential impact on the child’s learning and skill development, ensuring a balance between challenge and engagement.
    
6.  **Task Execution**: Execute the highest priority tasks, adapting the tutoring approach and content delivery as needed to maximize the child’s learning and engagement.
    
7.  **Performance Monitoring**: Assess the effectiveness of the tutoring by tracking key performance indicators (KPIs) such as progress toward learning goals, improvement in math skills, and the child’s engagement and satisfaction.
    
8.  **Feedback Loop**: Continuously monitor the child’s performance and update the context analysis, task generation, and task prioritization steps based on new data and insights. Adjust the initial goal and learning path as necessary to better support the child’s math skill development.
    
9.  **Iteration and Improvement**: Analyze the child’s performance and update the context analysis, task generation, and task prioritization steps based on new data and insights. Adjust the initial goal and learning path as necessary to better support the child’s math skill development. Iterate through steps 2–9 to continuously refine the political campaign management system and improve its effectiveness over time.
    

This autonomous agent loop type system outlines a process for an educational math tutor to adaptively support and guide a child’s learning experience, focusing on continuous improvement and personalization based on the child’s needs and progress.

“Just like there will be numerous models of all sizes in the future, you'll have multiple agents for different facets of your life: an agent for work, an agent for your family/home life, an agent for self-improvement, all working in tandem with other agents. Automating mundane tasks or giving you professional superpowers are the first obvious use cases, but your digital twin will be capable of so much - perhaps even going on dates without your involvement to assess fit, forever eliminating the bad first date.”

Vivian Cheng, Principal at CRV

![Image 44](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/aadcd332-5336-4837-be7f-37c9cda65b72/1_gHPkou7cb1US-HLzA4uNWA.png)

### **The Future Of Autonomous Agents**

Right now humanity is in the very beginning of developing autonomous agents. We’re poking around, breaking things, experimenting, making bad things, making good things.

“Autonomous agents will bring your ideas to life simply by requesting their assistance. These agents can serve as friends, colleagues, and collaborators, affording you an abundance of leisure time. I'm curious to know, how would you choose to spend this newfound freedom?”

Barely any commercialized products have even been released, everyone is still in development mode.

But soon, that is going to change. Autonomous agents are going to start showing up all over the place until one day it will be incredibly strange for someone to not have one, or multiple, autonomous agents helping them out at any given time.

“Rather than focus on replacing people's work, focus on augmenting what they can do. Making something "smart" used to mean making its data available via api. The next generation of making something smart will be to ask how that product can better assist you. As an example, a "smart" email address might be able to take action in interesting ways based on your preferences. If you're a big shopper, maybe it monitors emails for when an item you're interested in goes on sale, price compares, or even negotiates price on your behalf, knowing privately to what degree you value the item and how much you're willing to pay.”

People will move through life with autonomous agents of all kinds augmenting their movements, decisions, and actions. If at some point we have neural implants then this will all happen seamlessly just like thinking in your own head works today.

“Everyone will have access to a virtual researcher, assistant, writer, or worker at no or low cost. Access is democratized.”

Here are my predictions for the future of autonomous agents:

*   **2023** multiple commercialized autonomous agents for gaming, personal use, marketing, and sales.
    
*   **2024** commercialized autonomous agents for every category but not mainstream adoption.
    
*   **2025** mainstream adoption of autonomous agents in every category for everything imaginable.
    
*   **2026** most people in first-world countries are going about every day life with the support of an army of autonomous agents.
    

**In the next 2-5 years most people will work for an autonomous agent instead of a human.**
-------------------------------------------------------------------------------------------

“I see using an augmented reality Holodeck, almost wholly driven by AIs, where lots of things are happening both automatically and with your manual prompting. Yes, people will work for the AIs. Everyone will use them, yes, but only a few will know what they are or how to make them. The world is about to change deeply because of LLMs and the coming autonomous agents and systems. LLMs (Large Language Models) are the most democratizing force humans have ever invented. Why? LLMs can now run on cheap computers without being connected to a central server. That little engine basically includes all human knowledge. Incredible that you can run that on something that isn't connected to the Internet. Autonomous agents just make this Holodeck run almost automatically. Everything from weather to pizza delivery happening almost automatically with very little human input.”

“_This is a lot to take in Matt, the future is going to be wild. Where can I start with autonomous agents today though?_”

This is the best question to ask. I have all the resources you need.

Let me show you.

“In this future, everyone will likely use autonomous agents in some capacity, whether for personal productivity, business operations, or creative endeavors. For the most part, people will serve as "maestros" to these AI agents, setting their goals and nudging them along. We will also "work for AI agents" in the same way that we must work within the constraints of companies, processes and other systems. However I think AI Agents will in many cases do a much better job than companies and systems in society do today, and will create opportunities that will benefit everyone on the whole.”

![Image 45](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8373fad1-639e-49cc-b447-26491ce7d8c6/1__QpGWrAxQg1oliB8iaIWbA.png)

### **How To Build And Use Autonomous Agents**

You are now ready to jump headfirst into the world of autonomous agents. I’m going to give you the resources you need to get started building or using autonomous agents on your own.

“Find a specific B2B use case with a lot of repetitive tasks. Sales ops. Ad ops. Event ops. Accounting ops. There are so many to choose from right now.”

I’m excited to see what you can do with this, and if you make something cool, I would love to check it out.

“First, narrow down your use case, as much as you can. Then, design a product that involves a human-in-the-loop, and a way to estimate the process' success. And step-by-step increase automation. And only then expand to adjacent use cases.”

#### **Building Autonomous Agents**

You have a couple different options here.

1.  **Build It Yourself**: Look at the framework I provided earlier and embark on a journey to build everything from scratch! You can definitely do this, it’s not a scary as it might sound. Some recommended software solutions are [OpenAI’s GPT-4](http://openai.com/?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents), [Pinecone vector database](http://pinecone.io/?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents), and [LangChain’s framework](https://langchain.com/?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents).
    
2.  [Auto-GPT](https://github.com/Torantulino/Auto-GPT?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents): This is a popular open source option created by Toran Richards. It includes options to connect to the internet, use apps, long-term and short-term memory, and more.
    
3.  [BabyAGI](https://github.com/yoheinakajima/babyagi?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents): Another popular open source option, this one created by Yohei Nakajima. While this one doesn’t connect to the internet yet, it is extremely elegant with under 200 lines of code.
    
4.  [Microsoft’s Jarvis](https://github.com/microsoft/JARVIS?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents): Very similar to Auto-GPT and BabyAGI, but much more robust and brought to you by Microsoft and HuggingFace.
    

“I think we'll initially have vertical-specific autonomous agents that are fine-tuned on a certain set of data that allows them to take on a role in that field. The two (only?) areas of LLMs where we've seen big adoption so far is copywriting and programming. Extrapolating further, it makes sense to think that the AIs we have in those two spaces will start to become more autonomous. One way that could play out in the near future is that instead of the human giving a prompt to initialize the copy writing or the code completion, the AI autonomously gives you new suggestions each day for you to review, without you first having to start or prompt them.”

#### **Using Autonomous Agents**

Ready to have your own agent? Here are some options.

1.  Spin up any of the options in the build your own section above!
    
2.  [AgentGPT](https://agentgpt.reworkd.ai/?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents): Create and run an autonomous agent (AutoGPT) from a website, no login required.
    
3.  **HyperWrite Assistant**: Add a chrome extension that lets you give your browser commands and the browser follows through.
    

people from all walks of life can benefit from the expertise and efficiency previously reserved for the upper echelons of society. This democratization of personal assistance can lead to greater productivity and a more balanced work-life experience, empowering individuals to focus on their passions, creativity, and personal growth while their AI assistants take care of the more mundane aspects of their daily lives.”

### **Additional Resources:**

*   [Autonomous Agents & Agent Simulations](https://blog.langchain.dev/agents-round/?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents) (via Langchain)
    
*   [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/pdf/2304.03442.pdf?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents) (via arxiv)
    
*   [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/pdf/2303.17580.pdf?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents) (via arxiv)
    

No matter if you can code, or you don’t yet know how, I encourage you to take a few hours to experiment with these. It is not as complex or as difficult as it may seem and the quicker you get your hands dirty the faster you’re going to learn about autonomous agents.

“As an investor, using autonomous agents as to do the jobs of analysts and associates or at least super charge them really excites me. They could be programmed to source deals under certain conditions, analyze via certain factors and then tee up custom emails for me to send in order to start conversations.”

The autonomous agent landscape is wide open for interpretation and innovation. 99% of use cases have not been created or attempted, the possibilities are endless and the opportunity is yours for the taking.

“I'm very interested in the orchestration and modularization of smaller programming tasks towards a bigger end goal. We know LLMs are good at programming on a problem basis but we haven't seen proof points that they could, for example, port an entire codebase from Android to iOS, or even create an app from scratch. I suspect an agent with the right orchestration scheme and memory structure could make this happen.”

**This space is moving incredibly fast, faster than anything I have ever seen before.** Every hour it feels like there is new information, new experiments, and new releases.

**So how do you keep up with it all?**

I got you covered. Come with me.

![Image 46](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/974984ae-deee-4840-9f68-18a8feb82ee1/1_sjLWB-sXPuKe78AWIR_miA.png)

### **How To Meet People Interested In Autonomous Agents**

You are only at the beginning of your autonomous agents journey, and I know you are still burning with questions and ideas you want to share.

If you’re sitting there thinking any of the following then I have the perfect solutions for you:

*   “_I wish I could stay up to date on new developments in autonomous agents_”
    
*   “_I have an idea for an autonomous agent, I want to share it with someone and see what they think!_”
    
*   “_I built an autonomous agent, I would love to share it with people!_”
    
*   “_I want to invest in people building autonomous agents_”
    

If this sounds like you, and your autonomous agent curiosity has been sparked, here’s what you should do next.

1.  **[Subscribe to my newsletter](https://www.mattprd.com/subscribe)** and **[subscribe to my new YouTube channel](https://www.youtube.com/@mattprd?sub_confirmation=1&utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents)** to continue to get more insights, news, and product thoughts on AI and autonomous agents. I have been building products (used by thousands of businesses) in this space since 2016 and try to always be on the forefront of what is happening.
    
2.  **[Join the Autonomous Agents group on Facebook](https://www.facebook.com/groups/autonomousagents?utm_source=www.mattprd.com&utm_medium=referral&utm_campaign=the-complete-beginners-guide-to-autonomous-agents)**. Here you can share content, projects, and opinions on autonomous agents.
    

For example when I talked about autonomous agents to Emad Mostaque, the founder and CEO of Stability AI, his response was a coy “_Swarm intelligence will beat AGI.”_ What does he mean by that? Subscribe to my newsletter and we’ll explore it deeper.

The world is changing fast and I am so excited to dive headfirst with you into merging humanity with artificial intelligence.

Build something people want. Try not to destroy the world on accident. I’ll talk to you soon.

_p.s. Want to chat? I’d love to hear from you. Reach out on Twitter @MattPRD or send me an email at matt at mattprd dot com._
