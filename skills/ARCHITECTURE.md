# Agent Skills - Architecture & Design Guide

## System Architecture

### High-Level Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    DynamicAgent (Main Interface)             │
│  - Unified API for all agent operations                      │
│  - Manages persona lifecycle                                 │
│  - Tracks conversation history                               │
└────────┬──────────────┬──────────────┬───────────────────────┘
         │              │              │
    ┌────▼──────┐  ┌────▼────────────┐ │
    │ System    │  │ Agent Profile   │ │
    │ Prompt    │  │ Manager         │ │
    │ Skill     │  │ - Profiles      │ │
    │ - Template│  │ - Names/Roles   │ │
    │ - Format  │  │ - Expertise     │ │
    └──────┬────┘  └────┬────────────┘ │
           │            │              │
           │      ┌─────▼──────────────┘
           │      │
      ┌────▼──────▼────────┐
      │  Characteristic    │
      │  Manager           │
      │  - Styles          │
      │  - Tone            │
      │  - Personality     │
      │  - Communication   │
      └───────┬────────────┘
              │
         ┌────▼─────────────┐
         │  Config          │
         │  - Settings      │
         │  - Presets       │
         │  - Modes         │
         └──────────────────┘
```

### Data Flow Diagram

```
User Request
    │
    ▼
┌─────────────────────────────────────┐
│ DynamicAgent.initialize_persona()   │
└────────┬────────────────────────────┘
         │
         ▼
    ┌─────────────────────────────────┐
    │ SystemPromptSkill               │
    │ - Select Profile                │
    │ - Select Style                  │
    └────────┬────────────────────────┘
             │
    ┌────────┴────────┐
    ▼                 ▼
┌───────────┐     ┌──────────────┐
│ Profiles  │     │ Styles       │
│ - 6 built │     │ - 6 built    │
│ - Custom  │     │ - Custom     │
└───────────┘     └──────────────┘
    │                 │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────┐
    │ Format Prompt       │
    │ - Identity          │
    │ - Communication     │
    │ - Guidelines        │
    │ - Instructions      │
    └────────┬────────────┘
             │
             ▼
    ┌─────────────────────┐
    │ System Prompt       │
    │ (Ready for LLM)     │
    └─────────────────────┘
```

### Class Hierarchy

```
┌────────────────────────────────────────┐
│ AgentProfileManager                    │
│ - profiles: Dict[str, AgentProfile]    │
│ - current_profile: Optional[Profile]   │
├────────────────────────────────────────┤
│ + get_random_profile()                 │
│ + get_profile_by_role(role)            │
│ + get_all_profiles()                   │
│ + add_profile(key, profile)            │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ CharacteristicManager                  │
│ - talking_styles: Dict[str, Style]     │
│ - current_style: Optional[Style]       │
├────────────────────────────────────────┤
│ + get_random_style()                   │
│ + get_style_by_name(name)              │
│ + get_all_styles()                     │
│ + add_style(key, style)                │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ SystemPromptSkill                      │
│ - profile_manager: ProfileManager      │
│ - characteristic_manager: CharMgr      │
│ - prompt_template: str                 │
├────────────────────────────────────────┤
│ + generate_system_prompt()             │
│ + generate_system_prompt_for_profile() │
│ + generate_system_prompt_for_style()   │
│ + generate_system_prompt_custom()      │
│ + get_current_persona()                │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ DynamicAgent                           │
│ - system_prompt_skill: Skill           │
│ - current_system_prompt: str           │
│ - conversation_history: list           │
│ - persona_info: Dict                   │
├────────────────────────────────────────┤
│ + initialize_persona()                 │
│ + initialize_persona_with_profile()    │
│ + initialize_persona_with_style()      │
│ + initialize_persona_custom()          │
│ + change_persona()                     │
│ + add_to_history(role, message)        │
│ + get_conversation_history()           │
│ + get_agent_info()                     │
└────────────────────────────────────────┘
```

### Persona Selection Logic

```
Random Persona Selection:
├─ get_random_profile()
│  └─ Random from 6 profiles [researcher, educator, mentor, innovator, analyst, strategist]
│
├─ get_random_style()
│  └─ Random from 6 styles [enthusiastic, professional, friendly, analytical, concise, nurturing]
│
└─ Format both together = Complete dynamic persona

Specific Profile + Random Style:
├─ get_profile_by_role(profile_key)
│  └─ Get specific profile
│
├─ get_random_style()
│  └─ Random style
│
└─ Format both together

Random Profile + Specific Style:
├─ get_random_profile()
│  └─ Random profile
│
├─ get_style_by_name(style_key)
│  └─ Get specific style
│
└─ Format both together

Specific Profile + Specific Style:
├─ get_profile_by_role(profile_key)
│  └─ Get specific profile
│
├─ get_style_by_name(style_key)
│  └─ Get specific style
│
└─ Format both together
```

## Design Patterns Used

### 1. **Strategy Pattern**
Each communication style is a strategy for how the agent communicates.

```python
# Different strategies to accomplish "answer the user"
class FriendlyStrategy:
    tone = "warm and approachable"
    formality = "casual"

class ProfessionalStrategy:
    tone = "formal and authoritative"
    formality = "formal"
```

### 2. **Factory Pattern**
SystemPromptSkill acts as a factory for generating system prompts.

```python
skill = SystemPromptSkill()

# Different factories for different combinations
prompt1 = skill.generate_system_prompt()
prompt2 = skill.generate_system_prompt_for_profile('mentor')
prompt3 = skill.generate_system_prompt_custom('educator', 'friendly')
```

### 3. **Manager Pattern**
AgentProfileManager and CharacteristicManager manage collections of items.

```python
profile_mgr = AgentProfileManager()
profile_mgr.add_profile(key, profile)
profile = profile_mgr.get_profile_by_role(role)
```

### 4. **State Pattern**
DynamicAgent maintains and transitions between different states (personas).

```python
agent = DynamicAgent()

# State 1: Educator persona
agent.initialize_persona_with_profile('educator')
# Process interactions in educator state

# State 2: Analyst persona
agent.change_persona()
# Process interactions in analyst state
```

## System Prompt Structure

Generated prompts follow this template:

```
[Identity Section]
You are {agent_name}, a {role}.
- Role: {role}
- Name: {agent_name}
- Expertise Areas: {areas}
- Description: {description}

[Communication Style Section]
- Tone: {tone}
- Formality Level: {formality}
- Pace: {pace}
- Verbosity: {verbosity}
- Personality Traits: {traits}

[Communication Patterns]
- Greeting: {greeting_pattern}
- Explanation: {explanation_pattern}
- Closing: {closing_pattern}

[Behavioral Guidelines]
1. Maintain role consistency
2. Follow communication style
3. Adapt response pace
4. Match verbosity preference
5. Demonstrate personality traits
6. Follow communication patterns

[Core Instructions]
- Stay in character
- Use expertise areas
- Quality standards
```

## Data Models

### AgentProfile
```python
@dataclass
class AgentProfile:
    role: str                    # Official role title
    name: str                    # Agent's name
    description: str             # Role description
    expertise_areas: List[str]   # Areas of expertise
```

### TalkingStyle
```python
@dataclass
class TalkingStyle:
    name: str                              # Style name
    tone: str                              # Communication tone
    formality: str                         # 'formal', 'casual', 'professional'
    pace: str                              # 'fast', 'moderate', 'slow'
    verbosity: str                         # 'concise', 'balanced', 'detailed'
    personality_traits: List[str]          # Key traits
    communication_patterns: Dict[str, str] # Patterns for different scenarios
```

## Control Flow Examples

### Example 1: Simple Initialization
```
User: agent.initialize_persona()
  └─→ ProfileManager.get_random_profile()
      └─→ CharacteristicManager.get_random_style()
          └─→ SystemPromptSkill._format_prompt()
              └─→ Return formatted system prompt
```

### Example 2: Specific Profile, Random Style
```
User: agent.initialize_persona_with_profile('educator')
  └─→ ProfileManager.get_profile_by_role('educator')
      └─→ CharacteristicManager.get_random_style()
          └─→ SystemPromptSkill._format_prompt()
              └─→ Return formatted system prompt
```

### Example 3: Conversation Lifecycle
```
User: agent.initialize_persona()
  └─→ Generate system prompt
      └─→ Ready for LLM interaction

User: agent.add_to_history('user', 'Hello')
  └─→ Store in conversation_history

LLM: Generate response
  └─→ System prompt + history → Response

User: agent.add_to_history('assistant', response)
  └─→ Update conversation_history

User: agent.change_persona()
  └─→ Generate new system prompt
      └─→ Keep history intact
          └─→ Continue conversation with new persona
```

## Performance Characteristics

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| initialize_persona() | O(1) | O(n) | n = prompt length |
| change_persona() | O(1) | O(n) | New prompt + existing history |
| get_random_profile() | O(n) | O(1) | n = number of profiles |
| get_random_style() | O(m) | O(1) | m = number of styles |
| add_to_history() | O(1) | O(1) | Append to list |
| get_conversation_history() | O(1) | O(k) | k = history size |

## Extension Points

### 1. Add Custom Profiles
```python
manager.add_profile('custom_role', AgentProfile(...))
```

### 2. Add Custom Styles
```python
manager.add_style('custom_style', TalkingStyle(...))
```

### 3. Override Prompt Template
```python
skill.prompt_template = """Your custom template here"""
```

### 4. Subclass DynamicAgent
```python
class CustomAgent(DynamicAgent):
    def custom_method(self):
        pass
```

### 5. Create Custom Manager
```python
class CustomProfileManager(AgentProfileManager):
    def load_from_database(self):
        pass
```

## Configuration Architecture

```
┌──────────────────────────┐
│ AgentConfig              │
│ - config: Dict           │
├──────────────────────────┤
│ + get(key, default)      │
│ + set(key, value)        │
│ + get_preset_agent(name) │
│ + list_preset_agents()   │
│ + reset_to_defaults()    │
└──────────────────────────┘
         │
         ▼
    ┌────────────────┐
    │ PRESET_AGENTS  │ (6 presets)
    │ - academic     │
    │ - mentor       │
    │ - teacher      │
    │ - analyst      │
    │ - innovator    │
    │ - advisor      │
    └────────────────┘

    ┌────────────────┐
    │ CONVERSATION   │ (3 modes)
    │ MODES          │
    │ - single_agent │
    │ - adaptive     │
    │ - multi_agent  │
    └────────────────┘
```

## Integration Points

### With LLM APIs
```python
System Prompt (from DynamicAgent)
    ↓
LLM API (OpenAI, Anthropic, Hugging Face, etc.)
    ↓
Response with context of persona
```

### With Application Logic
```python
User Input
    ↓
DynamicAgent (manage persona)
    ↓
LLM with System Prompt
    ↓
Response + Conversation History
    ↓
Application Logic
```

## Testing Strategy

### Unit Tests
- Test each component independently
- Verify profile selection
- Verify style selection
- Verify prompt generation

### Integration Tests
- Test multiple components together
- Test complete workflows
- Test persona switching
- Test conversation management

### Regression Tests
- Ensure changes don't break existing functionality
- Test with fixed persona combinations
- Test with various input patterns

---

## Summary

**Architecture**: Modular, composable components with clear separation of concerns
**Design Patterns**: Strategy, Factory, Manager, State patterns
**Extensibility**: Easy to add custom profiles, styles, and behaviors
**Performance**: O(1) operations for common tasks
**Integration**: Works with any LLM API
**Testing**: Comprehensive test coverage with unit and integration tests
