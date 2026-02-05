# Agent Skills Package - Complete Overview

## What is Agent Skills?

Agent Skills is a comprehensive Python framework for creating AI agents with **dynamically assigned personalities, roles, and communication styles**. It enables you to:

- Generate agents with **random or manually selected personas**
- Change agent characteristics **at any time** during conversation
- Maintain **consistent conversation history** across persona changes
- Create **system prompts** that adapt to different communication contexts
- Manage **multiple agents** with different expertise and styles

## Quick Start (2 Minutes)

```python
from skills.agent_illness import DynamicAgent

# Create and initialize agent
agent = DynamicAgent()
system_prompt = agent.initialize_persona()

# Get agent info
print(f"Agent: {agent.get_current_persona()['agent_name']}")

# Use with your LLM
# response = llm.complete(system_prompt=system_prompt, user_message="Hi!")
```

## Key Features

### 1. **Dynamic Personas**
- 6 built-in roles: Researcher, Educator, Mentor, Innovator, Analyst, Strategist
- Each role has unique expertise areas and descriptions
- Add unlimited custom roles

### 2. **Flexible Communication Styles**
- 6 built-in styles: Enthusiastic, Professional, Friendly, Analytical, Concise, Nurturing
- Each style defines tone, formality, pace, and personality traits
- Add unlimited custom styles

### 3. **Random or Deterministic Assignment**
- Fully random for unpredictability
- Specific profile + random style
- Random profile + specific style
- Both specific for consistency

### 4. **Real-Time Persona Switching**
- Change agent personality mid-conversation
- Clear history or maintain transcript
- Perfect for multi-perspective analysis

### 5. **Conversation Management**
- Automatic conversation history tracking
- View complete transcript
- Clear history when needed
- Full context preservation

## Core Components

### SystemPromptSkill
Generates complete system prompts with structured sections:
- Identity (role, name, expertise)
- Communication style definitions
- Behavioral guidelines
- Core instructions

### AgentProfileManager
Manages agent roles and expertise areas with:
- Random profile selection
- Named profile retrieval
- Custom profile addition
- Profile listing

### CharacteristicManager
Manages talking styles with:
- Random style selection
- Named style retrieval
- Custom style addition
- Style descriptions

### DynamicAgent
Unified interface combining all skills with:
- Persona initialization
- Persona switching
- Conversation tracking
- Complete state management

## Use Cases

### 1. Chatbots with Rotating Personas
Create chatbots that change personality to feel fresh and engaging.

```python
agent = DynamicAgent()
agent.initialize_persona()

# Every new conversation, new persona
for user_input in user_messages:
    # Process with current persona
    if should_change_persona():
        agent.change_persona()
        agent.clear_history()
```

### 2. Multi-Perspective Analysis
Get different expert opinions on the same topic.

```python
topic = "AI Safety"

agents = [
    ('researcher', 'professional'),
    ('educator', 'friendly'),
    ('analyst', 'analytical')
]

for profile, style in agents:
    agent = DynamicAgent()
    agent.initialize_persona_custom(profile, style)
    # Get perspective from each agent
```

### 3. Adaptive Conversation Assistant
Adjust communication style based on user needs.

```python
agent = DynamicAgent()

if user_prefers_detailed:
    agent.initialize_persona_with_style('enthusiastic')
elif user_prefers_concise:
    agent.initialize_persona_with_style('concise')
```

### 4. Educational Assistant
Different teaching styles for different learning needs.

```python
# For visual learners
agent.initialize_persona_custom('educator', 'enthusiastic')

# For technical learners
agent.initialize_persona_custom('analyst', 'analytical')
```

### 5. Brainstorming Sessions
Get diverse perspectives from different agent personalities.

```python
agent = DynamicAgent()

perspectives = []
for _ in range(5):
    agent.change_persona()
    # Get perspective for problem
```

## Directory Structure

```
skills/
├── agent_illness/
│   ├── __init__.py                 # Package exports
│   ├── system_prompt.py            # Core skill for prompt generation
│   ├── agent_profiles.py           # Profile management (role, name)
│   ├── characteristics.py          # Style management (tone, personality)
│   ├── dynamic_agent.py            # Unified agent implementation
│   ├── config.py                   # Configuration and presets
│   ├── examples.py                 # 8 basic usage examples
│   ├── integration_examples.py     # 6 advanced integration examples
│   ├── test_agent_skills.py        # Complete test suite
│   └── README.md                   # Detailed documentation
├── README.md                        # Package overview
├── QUICKSTART.md                    # Quick reference guide
└── __init__.py
```

## Installation & Setup

1. **Everything is included** - Just import and use:
   ```python
   from skills.agent_illness import DynamicAgent, SystemPromptSkill
   ```

2. **No external dependencies** - Pure Python implementation

3. **Easy to integrate** - Works with any LLM API

## Running Examples

### Basic Examples (8 examples)
```bash
python skills/agent_illness/examples.py
```

Shows:
- Random persona generation
- Specific profile selection
- Specific style selection
- Custom combinations
- Persona switching
- Listing options
- Conversation tracking
- Complete agent info

### Integration Examples (6 advanced examples)
```bash
python skills/agent_illness/integration_examples.py
```

Shows:
- Preset agent configurations
- Conversation modes
- Style dynamics
- Agent information system
- Configuration management
- Multi-context conversation

### Running Tests
```bash
pytest skills/agent_illness/test_agent_skills.py -v
```

Comprehensive test suite with:
- 30+ test cases
- Unit tests for each component
- Integration tests
- Workflow tests

## Common Patterns

### Pattern 1: Consistent Single Agent
```python
agent = DynamicAgent()
agent.initialize_persona_custom('mentor', 'nurturing')
# Uses same persona throughout
```

### Pattern 2: Rotating Personas
```python
agent = DynamicAgent()
for message in messages:
    agent.change_persona()
    agent.clear_history()
    # Process with new persona
```

### Pattern 3: Context-Aware Switching
```python
agent = DynamicAgent()
agent.initialize_persona_with_profile('analyst')

if needs_teaching:
    agent.change_persona()
    agent.initialize_persona_with_profile('educator')
```

### Pattern 4: Multiple Agents
```python
agents = {}
for profile in ['researcher', 'educator', 'mentor']:
    agent = DynamicAgent()
    agent.initialize_persona_with_profile(profile)
    agents[profile] = agent
```

### Pattern 5: Preset Configuration
```python
from skills.agent_illness.config import PRESET_AGENTS

preset = PRESET_AGENTS['academic']  # Researcher + Professional
agent = DynamicAgent()
agent.initialize_persona_custom(preset['profile'], preset['style'])
```

## Available Profiles

| Name | Role | Expertise | Traits |
|------|------|-----------|--------|
| Dr. Alexandria | Research Expert | Research, analysis, data interpretation | Scholarly, analytical |
| Professor Marcus | Educator | Teaching, explanation, learning guidance | Patient, clear |
| Coach Jordan | Career Mentor | Career guidance, motivation, development | Supportive, encouraging |
| Dr. Nova | Innovation Specialist | Ideation, creativity, problem-solving | Creative, visionary |
| Alex Sterling | Data Analyst | Data analysis, statistics, insights | Precise, methodical |
| Morgan Chase | Strategic Advisor | Strategy, planning, decision-making | Visionary, strategic |

## Available Talking Styles

| Name | Tone | Formality | Pace | Verbosity | Best For |
|------|------|-----------|------|-----------|----------|
| Enthusiastic | Excited, energetic | Casual | Fast | Detailed | Engagement |
| Professional | Formal, authoritative | Formal | Moderate | Balanced | Authority |
| Friendly | Warm, approachable | Casual | Moderate | Balanced | Relatability |
| Analytical | Logical, objective | Professional | Moderate | Balanced | Analysis |
| Concise | Direct, efficient | Professional | Fast | Concise | Efficiency |
| Nurturing | Supportive, patient | Casual | Slow | Detailed | Support |

## Advanced Features

### Adding Custom Profiles
```python
from skills.agent_illness import AgentProfileManager, AgentProfile

manager = AgentProfileManager()
new_profile = AgentProfile(
    role='Security Expert',
    name='Dr. Guardian',
    description='Cybersecurity specialist',
    expertise_areas=['security', 'encryption', 'protocols']
)
manager.add_profile('security', new_profile)
```

### Adding Custom Styles
```python
from skills.agent_illness import CharacteristicManager, TalkingStyle

manager = CharacteristicManager()
new_style = TalkingStyle(
    name='Mysterious',
    tone='enigmatic',
    formality='formal',
    pace='slow',
    verbosity='concise',
    personality_traits=['intriguing', 'thoughtful'],
    communication_patterns={
        'greeting': 'Intriguing greeting',
        'explanation': 'Thought-provoking',
        'closing': 'Open-ended conclusion'
    }
)
manager.add_style('mysterious', new_style)
```

### Extending DynamicAgent
```python
from skills.agent_illness import DynamicAgent

class SpecializedAgent(DynamicAgent):
    def domain_specific_method(self):
        # Add custom functionality
        pass
```

## Configuration

### Default Settings
```python
from skills.agent_illness.config import AgentConfig

config = AgentConfig()
config.get('max_history_length')      # 1000
config.get('logging_enabled')         # True
config.get('auto_clear_history')      # False
```

### Preset Agents
Quick configurations for common scenarios:
- `academic` - Researcher + Professional
- `mentor` - Mentor + Nurturing
- `teacher` - Educator + Friendly
- `analyst` - Analyst + Analytical
- `innovator` - Innovator + Enthusiastic
- `advisor` - Strategist + Professional

### Conversation Modes
- `single_agent` - Same persona throughout
- `adaptive` - Persona changes based on context
- `multi_agent` - Multiple agents in parallel

## API Quick Reference

### DynamicAgent Methods
```python
agent.initialize_persona()                          # Random all
agent.initialize_persona_with_profile(key)        # Specific profile
agent.initialize_persona_with_style(key)          # Specific style
agent.initialize_persona_custom(profile, style)   # Both specific
agent.change_persona()                            # New random persona
agent.get_current_persona()                       # Persona info dict
agent.get_system_prompt()                         # Current prompt
agent.add_to_history(role, content)              # Add message
agent.get_conversation_history()                  # Full transcript
agent.clear_history()                             # Reset transcript
agent.get_agent_info()                            # Complete state
```

### SystemPromptSkill Methods
```python
skill.generate_system_prompt()                    # Random
skill.generate_system_prompt_for_profile(key)    # Specific profile
skill.generate_system_prompt_for_style(key)      # Specific style
skill.generate_system_prompt_custom(p, s)        # Both specific
skill.get_current_persona()                      # Current info
skill.list_available_profiles()                  # Profile dict
skill.list_available_styles()                    # Styles dict
```

## Integration Examples

### With OpenAI
```python
import openai
from skills.agent_illness import DynamicAgent

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

### With Claude
```python
import anthropic
from skills.agent_illness import DynamicAgent

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

## Best Practices

1. **Always call `initialize_persona()` first** before using an agent
2. **Use `initialize_persona_custom()`** for consistent testing
3. **Call `clear_history()`** when starting completely fresh
4. **Check persona info** with `get_current_persona()` before important decisions
5. **Log system prompts** if implementing persistence
6. **Test with different profiles** before production
7. **Use presets** for common scenarios

## Troubleshooting

**Q: System prompt is None**
A: Call `initialize_persona()` or one of its variants first

**Q: Persona keeps changing**
A: Use `initialize_persona_custom()` for consistency

**Q: History not tracking**
A: Remember to call `add_to_history()` after each message

**Q: Want deterministic results for testing**
A: Use `initialize_persona_custom(profile, style)` with fixed values

## License

Licensed under the same license as the Abnormal-AI-Research-Center project.

---

For more information:
- See [README.md](README.md) for detailed documentation
- See [QUICKSTART.md](QUICKSTART.md) for quick reference
- See [examples.py](agent_illness/examples.py) for basic examples
- See [integration_examples.py](agent_illness/integration_examples.py) for advanced examples
