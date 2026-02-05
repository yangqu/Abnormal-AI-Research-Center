"""
Quick Start Guide for Agent Skills
"""

# Quick Start Guide

## 1. Installation
Simply import from the skills package:

```python
from skills.agent_illness import DynamicAgent, SystemPromptSkill
```

## 2. Quickest Way to Get Started

```python
from skills.agent_illness import DynamicAgent

# Create agent and initialize with random persona
agent = DynamicAgent()
system_prompt = agent.initialize_persona()

# Get agent info
persona = agent.get_current_persona()
print(f"Agent: {persona['agent_name']}")
print(f"Role: {persona['role']}")

# Use the system_prompt with your LLM
# response = llm.complete(system_prompt=system_prompt, user_message="Hi!")
```

## 3. Most Common Operations

### Generate Random Persona
```python
agent = DynamicAgent()
system_prompt = agent.initialize_persona()
```

### Use Specific Profile
```python
# Random style + educator profile
agent.initialize_persona_with_profile('educator')
```

### Use Specific Style
```python
# Random profile + professional style
agent.initialize_persona_with_style('professional')
```

### Both Profile AND Style
```python
# Mentor profile + nurturing style
agent.initialize_persona_custom('mentor', 'nurturing')
```

### Switch Persona Mid-Conversation
```python
agent.change_persona()
```

## 4. Available Profiles
- `researcher` - Research Expert
- `educator` - Educator
- `mentor` - Career Mentor
- `innovator` - Innovation Specialist
- `analyst` - Data Analyst
- `strategist` - Strategic Advisor

## 5. Available Styles
- `enthusiastic` - Excited and energetic
- `professional` - Formal and authoritative
- `friendly` - Warm and approachable
- `analytical` - Logical and objective
- `concise` - Direct and efficient
- `nurturing` - Supportive and patient

## 6. Track Conversation
```python
agent.add_to_history('user', 'Hello!')
agent.add_to_history('assistant', 'Hi there!')

history = agent.get_conversation_history()
agent.clear_history()  # Start fresh
```

## 7. Get System Prompt
```python
system_prompt = agent.get_system_prompt()
print(system_prompt)
```

## 8. Integration with LLM

### With OpenAI
```python
from skills.agent_illness import DynamicAgent
import openai

agent = DynamicAgent()
system_prompt = agent.initialize_persona()

response = openai.ChatCompletion.create(
    model="gpt-4",
    system_prompt=system_prompt,
    messages=[{"role": "user", "content": "Hello!"}]
)

agent.add_to_history('user', 'Hello!')
agent.add_to_history('assistant', response.choices[0].message.content)
```

### With Anthropic Claude
```python
from skills.agent_illness import DynamicAgent
import anthropic

agent = DynamicAgent()
system_prompt = agent.initialize_persona()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": "Hello!"}]
)

agent.add_to_history('user', 'Hello!')
agent.add_to_history('assistant', response.content[0].text)
```

## 9. List All Options
```python
from skills.agent_illness import SystemPromptSkill

skill = SystemPromptSkill()
print(skill.list_available_profiles())
print(skill.list_available_styles())
```

## 10. Custom Profiles and Styles
See the full README.md for detailed instructions on adding custom profiles and styles.

## Real-World Example: Multi-Turn Conversation

```python
from skills.agent_illness import DynamicAgent

# Initialize agent
agent = DynamicAgent()
agent.initialize_persona()

persona = agent.get_current_persona()
print(f"Talking to: {persona['agent_name']} ({persona['role']})")
print(f"Style: {persona['tone']}")

# Simulate conversation
messages = [
    "What's your expertise?",
    "Can you explain machine learning?",
    "How do I get started?"
]

for user_message in messages:
    agent.add_to_history('user', user_message)
    
    # In real scenario, you'd call your LLM here
    response = f"Response to: {user_message}"
    agent.add_to_history('assistant', response)
    
    print(f"User: {user_message}")
    print(f"Assistant: {response}\n")

# View conversation
print("\nFull Conversation:")
for msg in agent.get_conversation_history():
    print(f"{msg['role'].upper()}: {msg['content']}")
```

## Real-World Example: Persona Switching

```python
from skills.agent_illness import DynamicAgent

agent = DynamicAgent()

# Start with educator
agent.initialize_persona_with_profile('educator')
print(f"First agent: {agent.get_current_persona()['agent_name']}")

# Get response in educator style
# response1 = llm.complete(system_prompt=agent.get_system_prompt(), ...)

# Switch to analyst
agent.change_persona()
print(f"Second agent: {agent.get_current_persona()['agent_name']}")

# Get second opinion from analyst style
# response2 = llm.complete(system_prompt=agent.get_system_prompt(), ...)
```

## Tips & Best Practices

1. **Always call `initialize_persona()` first** before using an agent
2. **Use `change_persona()` to switch** mid-conversation while keeping history
3. **Call `clear_history()`** if starting completely fresh with new persona
4. **Get persona info** with `get_current_persona()` to understand current state
5. **Check available options** with `list_available_profiles()` and `list_available_styles()`
6. **For testing**, use `initialize_persona_custom()` to get consistent results
7. **Track important conversations** using `add_to_history()` for context

## Troubleshooting

**Q: How do I use the system prompt with my LLM?**
A: Pass `agent.get_system_prompt()` to your LLM's system parameter. It varies by provider.

**Q: Can I add my own profiles?**
A: Yes! See the full README.md for instructions on custom profiles and styles.

**Q: How do I reset the agent?**
A: Call `agent.initialize_persona()` with new parameters.

**Q: What if I want the same persona every time?**  
A: Use `initialize_persona_custom()` with specific profile and style keys.

**Q: Can I modify the system prompt template?**
A: Yes, access `agent.system_prompt_skill.prompt_template`.

---

For more detailed information, see [README.md](README.md)
