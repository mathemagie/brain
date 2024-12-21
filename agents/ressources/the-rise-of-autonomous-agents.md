Title: The rise of autonomous agents

URL Source: https://www.aitidbits.ai/p/the-rise-of-autonomous-agents

Published Time: 2023-11-19T16:30:28+00:00

Markdown Content:
_Welcome to Deep Dives **\-** an AI Tidbits section providing editorial takes and insights to make sense of the latest in AI. Let’s go!_

Last February, Stanford published a paper that sparked everyone’s imagination. In [this paper](https://arxiv.org/abs/2304.03442), the researchers leveraged ChatGPT to power human-like agents. A mini-simulation of humanity.

A few weeks later, two viral open-source autonomous agents frameworks were introduced to the world - AutoGPT and BabyAGI. Their goal? Build fully autonomous AI agents. Those libraries generated a lot of excitement, but have yet to spawn useful agent-powered applications.

An autonomous agent, described simply, is an AI program capable of planning and executing tasks based on a given objective. Imagine asking an AI to “book a flight”, or “create a website for people interested in renting their apartments when they’re away” - and the agent goes to work. It does so by repeatedly asking itself “What should be the next steps to achieve the task at hand”, utilizing an LLM to answer this question.

[![Image 11](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1233bc47-fc94-4429-a749-614e720a8651_600x266.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1233bc47-fc94-4429-a749-614e720a8651_600x266.gif)

AutoGPT breaks down goals into tasks it then executes. [Source](https://medium.com/geekculture/autogpt-unleashed-the-autonomous-ai-agent-revolution-chat-gpt-ai-artificial-intelligence-productivity-19ad5b71c436)

Such objectives are great demo material, but demos are often cherry-picked, and the recent consensus is that AI agents are a great concept, but that’s about it. To me, it felt like agents were becoming the new Crypto - a lot of hype, with no one able to point to a concrete widespread use case.

That might have changed with [OpenAI’s recent release of GPTs](https://www.aitidbits.ai/p/openai-devday). GPTs are small ChatGPT wrappers that have the prompt, context, and tools baked into them, ready to roll.

Though powerful, they have yet to earn the “autonomous agents” badge–they still require a high degree of human feedback to achieve their goal. They are, however, capable of connecting to other services and APIs such as your calendar and email.

Combined with a few other headwinds, GPTs might represent the milestone the space has been waiting for, leading to a Cambrian explosion of capable autonomous agents.

[![Image 12](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d6038e-9f20-4dd5-81f8-9987cea292fd_1199x670.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d6038e-9f20-4dd5-81f8-9987cea292fd_1199x670.jpeg)

OpenAI announcing GPTs at DevDay 

_**Bonus at the end of the post**: a list of open-source repositories every agents builder should know and the startups leading the way._

AutoGPT, the largest autonomous agents framework to date, has over 150k stars on GitHub and 50k builders in its Discord server. With such a large community of developers, one might wonder why useful agents have yet to emerge. The answer lies in the inherent limitations of agents, which are slowly being addressed.
