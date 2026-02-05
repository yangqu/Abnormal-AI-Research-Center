# Abnormal AI Research Center

Explore the boundaries and possibilities of AI.

---

## Projects

### 1. Agent Skills Package 🤖

A comprehensive Python package for creating dynamic AI agents with **randomly assigned or manually selected personas, roles, and communication styles**.

**Features:**
- ✅ **6 Built-in Agent Profiles** (Researcher, Educator, Mentor, Innovator, Analyst, Strategist)
- ✅ **6 Communication Styles** (Enthusiastic, Professional, Friendly, Analytical, Concise, Nurturing)
- ✅ **Dynamic System Prompts** - Ready for any LLM (OpenAI, Claude, Hugging Face, etc.)
- ✅ **Persona Switching** - Change agent character mid-conversation
- ✅ **Conversation Tracking** - Automatic message history management
- ✅ **Zero Dependencies** - Pure Python implementation
- ✅ **Fully Tested** - 30+ comprehensive test cases
- ✅ **Production Ready** - Complete documentation and examples

**Quick Start:**

```python
from skills.agent_illness import DynamicAgent

# Create agent with random persona
agent = DynamicAgent()
system_prompt = agent.initialize_persona()

# Get agent information
persona = agent.get_current_persona()
print(f"Agent: {persona['agent_name']}")
print(f"Role: {persona['role']}")

# Use system_prompt with your LLM
# response = llm.complete(system_prompt=system_prompt, user_message="Your question")
```

**Documentation:**
- [Quick Start Guide](skills/QUICKSTART.md) - 10-minute introduction
- [Complete Overview](skills/OVERVIEW.md) - High-level system overview
- [API Reference](skills/README.md) - Comprehensive documentation
- [Architecture Guide](skills/ARCHITECTURE.md) - System design and patterns
- [File Listing](skills/FILE_LISTING.md) - Complete file reference

**Run Tests:**

```bash
# Complete functionality test
python test_agent_skills_demo.py

# Unit and integration tests
pytest skills/agent_illness/test_agent_skills.py -v
```

**Examples:**

```bash
# 8 basic examples
python skills/agent_illness/examples.py

# 6 advanced integration examples
python skills/agent_illness/integration_examples.py
```

See: [skills/README.md](skills/README.md)

---

### 2. Multi-Model Agent Framework

A universal Agent framework supporting multiple LLM providers, similar to OpenClaw.

**Supported Models:**
- OpenAI (GPT-4, GPT-4o)
- Anthropic (Claude-3)
- Google (Gemini)
- DeepSeek
- Minimax
- Qwen (Tongyi)
- Zhipu (ChatGLM)
- Moonshot (Kimi)
- Ollama (Local Models)

**Quick Start:**

```bash
cd src/multi-model-agent
pip install -r requirements.txt
python main.py --interactive
```

See: `src/multi-model-agent/README.md`

---

## Project Statistics

- **16 Files** - Complete Agent Skills package
- **2000+ Lines** - Implementation code
- **2000+ Lines** - Documentation
- **30+ Tests** - Comprehensive test coverage
- **14 Examples** - Working code samples
- **6 Profiles** - Built-in agent roles
- **6 Styles** - Communication styles
- **0 Dependencies** - Pure Python

---

## License

MIT
