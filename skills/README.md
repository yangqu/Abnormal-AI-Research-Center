# Agent Skills Package

A comprehensive skill system for creating dynamic AI agents with randomly assigned roles, names, and characteristics. Perfect for building versatile agents that can adapt their personality and communication style based on context.

## Overview

The Agent Skills package provides a flexible framework for:
- **Dynamic Agent Personas**: Randomly generate or manually select agent roles and names
- **Adaptive Communication Styles**: Multiple talking styles that change the agent's tone, formality, and personality
- **System Prompt Generation**: Automatically create comprehensive system prompts for language models
- **Conversation Management**: Track and manage agent-user conversations

## Folder Structure

```
skills/
├── agent_illness/
│   ├── __init__.py                 # Package initialization
│   ├── system_prompt.py            # Core system prompt generation
│   ├── agent_profiles.py           # Agent role and name management
│   ├── characteristics.py          # Talking styles and behavioral traits
│   ├── dynamic_agent.py            # Complete agent implementation
│   ├── examples.py                 # Usage examples
│   └── README.md                   # This file
└── __init__.py
```

## Components

### 1. **SystemPromptSkill**
Generates dynamic system prompts with randomly selected or manually chosen personas.

**Methods:**
- `generate_system_prompt()` - Random profile + random style
- `generate_system_prompt_for_profile(profile_key)` - Specific profile + random style
- `generate_system_prompt_for_style(style_key)` - Random profile + specific style
- `generate_system_prompt_custom(profile_key, style_key)` - Both specific
- `get_current_persona()` - Get current persona information
- `list_available_profiles()` - List all agent profiles
- `list_available_styles()` - List all talking styles

### 2. **AgentProfileManager**
Manages a collection of agent roles, names, and expertise areas.

**Available Profiles:**
- **Research Expert** (Dr. Alexandria)
- **Educator** (Professor Marcus)
- **Career Mentor** (Coach Jordan)
- **Innovation Specialist** (Dr. Nova)
- **Data Analyst** (Alex Sterling)
- **Strategic Advisor** (Morgan Chase)

**Methods:**
- `get_random_profile()` - Select random profile
- `get_profile_by_role(role)` - Get specific profile
- `add_profile(key, profile)` - Add new profile
- `get_all_profiles()` - List all profiles

### 3. **CharacteristicManager**
Manages agent talking styles and behavioral characteristics.

**Available Styles:**
- **Enthusiastic** - Excited, energetic, detailed
- **Professional** - Formal, authoritative, balanced
- **Friendly** - Warm, approachable, relatable
- **Analytical** - Logical, objective, data-driven
- **Concise** - Direct, efficient, precise
- **Nurturing** - Supportive, patient, encouraging

**Style Attributes:**
- Tone
- Formality level
- Pace
- Verbosity
- Personality traits
- Communication patterns

**Methods:**
- `get_random_style()` - Select random style
- `get_style_by_name(name)` - Get specific style
- `add_style(key, style)` - Add new style
- `get_all_styles()` - List all styles

### 4. **DynamicAgent**
A complete agent implementation that uses all skills to provide a unified interface.

**Methods:**
- `initialize_persona()` - Start with random persona
- `initialize_persona_with_profile(profile_key)` - Start with specific profile
- `initialize_persona_with_style(style_key)` - Start with specific style
- `initialize_persona_custom(profile_key, style_key)` - Start with both specific
- `change_persona()` - Switch to new random persona mid-conversation
- `get_current_persona()` - Get current persona info
- `add_to_history(role, message)` - Track conversation
- `get_conversation_history()` - Retrieve full history
- `get_agent_info()` - Get complete agent state

## Usage Examples

### Basic Random Persona
```python
from skills.agent_illness import DynamicAgent

agent = DynamicAgent()
system_prompt = agent.initialize_persona()

# Use with your language model
# llm_response = llm.complete(
#     system_prompt=system_prompt,
#     user_message="Hello!"
# )

persona = agent.get_current_persona()
print(f"Agent: {persona['agent_name']} ({persona['role']})")
```

### Specific Profile + Random Style
```python
agent = DynamicAgent()
system_prompt = agent.initialize_persona_with_profile('educator')
print(agent.get_system_prompt())
```

### Random Profile + Specific Style
```python
agent = DynamicAgent()
system_prompt = agent.initialize_persona_with_style('professional')
```

### Both Profile and Style
```python
agent = DynamicAgent()
system_prompt = agent.initialize_persona_custom('mentor', 'nurturing')
```

### Persona Switching
```python
agent = DynamicAgent()
agent.initialize_persona()

# First conversation
print(f"Agent: {agent.get_current_persona()['agent_name']}")

# Switch persona
agent.change_persona()
agent.clear_history()  # Optional: start fresh

# Continue with new persona
print(f"New Agent: {agent.get_current_persona()['agent_name']}")
```

### Conversation Tracking
```python
agent = DynamicAgent()
agent.initialize_persona()

agent.add_to_history('user', 'What is your expertise?')
agent.add_to_history('assistant', 'My expertise includes...')

history = agent.get_conversation_history()
```

### List Available Options
```python
from skills.agent_illness import SystemPromptSkill

skill = SystemPromptSkill()
profiles = skill.list_available_profiles()
styles = skill.list_available_styles()

print("Available Profiles:", profiles)
print("Available Styles:", styles)
```

## Adding Custom Profiles and Styles

### Add Custom Profile
```python
from skills.agent_illness import AgentProfileManager, AgentProfile

manager = AgentProfileManager()
new_profile = AgentProfile(
    role='Domain Expert',
    name='Dr. Smith',
    description='Specialized expert in specific domain',
    expertise_areas=['domain1', 'domain2', 'domain3']
)
manager.add_profile('domain_expert', new_profile)
```

### Add Custom Talking Style
```python
from skills.agent_illness import CharacteristicManager, TalkingStyle

manager = CharacteristicManager()
new_style = TalkingStyle(
    name='Custom Style',
    tone='specific tone',
    formality='formal',
    pace='moderate',
    verbosity='balanced',
    personality_traits=['trait1', 'trait2'],
    communication_patterns={
        'greeting': 'how to greet',
        'explanation': 'how to explain',
        'closing': 'how to close'
    }
)
manager.add_style('custom', new_style)
```

## System Prompt Structure

Generated system prompts include:

1. **Identity Section**
   - Role and name
   - Expertise areas
   - Description

2. **Communication Style Section**
   - Tone, formality, pace, verbosity
   - Personality traits
   - Communication patterns

3. **Behavioral Guidelines**
   - Role consistency
   - Communication style adherence
   - Trait demonstration

4. **Core Instructions**
   - Character maintenance
   - Expertise utilization
   - Quality standards

## Use Cases

1. **Multi-Role Chatbots**: Agents that rotate through different personas
2. **Adaptive AI**: Adjust communication style based on user preferences
3. **Diverse Conversational AI**: Different perspectives on the same topic
4. **Role-Playing Simulations**: Educational or entertainment applications
5. **Consistent Personality**: Same persona for long-running conversations
6. **A/B Testing**: Test different personas' effectiveness

## Running Examples

Execute the examples file to see all features in action:

```bash
python skills/agent_illness/examples.py
```

This will demonstrate:
- Random persona generation
- Specific profile selection
- Specific style selection
- Custom combinations
- Persona switching
- Listing available options
- Conversation tracking
- Complete agent information

## Extending the Package

### Create New Profile Manager
Subclass `AgentProfileManager` to implement custom profile sources:

```python
class CustomProfileManager(AgentProfileManager):
    def load_profiles_from_database(self):
        # Load profiles from custom source
        pass
```

### Create New Characteristic Manager
Subclass `CharacteristicManager` for custom style sources:

```python
class CustomCharacteristicManager(CharacteristicManager):
    def load_styles_from_api(self):
        # Fetch styles from external API
        pass
```

### Create Custom Agent Class
Extend `DynamicAgent` for specialized behavior:

```python
class SpecializedAgent(DynamicAgent):
    def custom_method(self):
        # Add custom functionality
        pass
```

## API Reference

### SystemPromptSkill
```python
class SystemPromptSkill:
    def generate_system_prompt() -> str
    def generate_system_prompt_for_profile(profile_key: str) -> str
    def generate_system_prompt_for_style(style_key: str) -> str
    def generate_system_prompt_custom(profile_key: str, style_key: str) -> str
    def get_current_persona() -> Dict[str, str]
    def list_available_profiles() -> Dict[str, str]
    def list_available_styles() -> Dict[str, str]
```

### DynamicAgent
```python
class DynamicAgent:
    def initialize_persona() -> str
    def initialize_persona_with_profile(profile_key: str) -> str
    def initialize_persona_with_style(style_key: str) -> str
    def initialize_persona_custom(profile_key: str, style_key: str) -> str
    def change_persona() -> str
    def get_current_persona() -> Dict[str, str]
    def get_system_prompt() -> Optional[str]
    def add_to_history(role: str, message: str) -> None
    def get_conversation_history() -> list
    def clear_history() -> None
    def get_agent_info() -> Dict
```

## License

Licensed under the same license as the Abnormal-AI-Research-Center project.
