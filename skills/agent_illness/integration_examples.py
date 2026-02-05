"""
Agent Skills - Complete Integration Example
Shows how to use all skills together in a real application
"""

from dynamic_agent import DynamicAgent
from config import AgentConfig, PRESET_AGENTS


def example_preset_agents():
    """Example 1: Using preset agent configurations"""
    print("=" * 70)
    print("EXAMPLE 1: Preset Agent Configurations")
    print("=" * 70)
    
    config = AgentConfig()
    
    print("\nAvailable Preset Agents:")
    for name in config.list_preset_agents():
        preset = config.get_preset_agent(name)
        print(f"  - {name}: {preset['description']}")
    
    # Use a preset agent
    print("\n\nUsing 'academic' preset agent:")
    academic_preset = config.get_preset_agent('academic')
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_custom(
        academic_preset['profile'],
        academic_preset['style']
    )
    
    persona = agent.get_current_persona()
    print(f"\nAgent: {persona['agent_name']}")
    print(f"Role: {persona['role']}")
    print(f"Style: {persona['tone']}")


def example_conversation_modes():
    """Example 2: Different conversation modes"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Conversation Modes")
    print("=" * 70)
    
    config = AgentConfig()
    
    # Single Agent Mode
    print("\n1. SINGLE AGENT MODE (Same persona throughout)")
    print("-" * 70)
    agent = DynamicAgent()
    agent.initialize_persona()
    persona = agent.get_current_persona()
    print(f"Agent: {persona['agent_name']} ({persona['role']})")
    
    # Simulate conversation
    messages = ["Hello!", "How are you?", "Tell me more"]
    for msg in messages:
        agent.add_to_history('user', msg)
        agent.add_to_history('assistant', f"Response to: {msg}")
    
    print(f"\nConversation length: {len(agent.get_conversation_history())} messages")
    print(f"Agent still: {agent.get_current_persona()['agent_name']}")
    
    # Adaptive Mode
    print("\n\n2. ADAPTIVE MODE (Persona changes based on context)")
    print("-" * 70)
    agent = DynamicAgent()
    
    # Context 1: Technical
    print("\nContext 1: Technical help needed")
    agent.initialize_persona_with_profile('analyst')
    print(f"Switched to: {agent.get_current_persona()['agent_name']}")
    
    # Context 2: Mentoring
    print("\nContext 2: Need motivation and guidance")
    agent.change_persona()
    print(f"Switched to: {agent.get_current_persona()['agent_name']}")


def example_dynamic_response_styles():
    """Example 3: Getting different responses in different styles"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Same Topic, Different Styles")
    print("=" * 70)
    
    topic = "What is machine learning?"
    
    # Get expert perspective
    print("\n1. EXPERT/RESEARCH PERSPECTIVE:")
    print("-" * 70)
    agent = DynamicAgent()
    agent.initialize_persona_custom('researcher', 'professional')
    persona = agent.get_current_persona()
    print(f"Agent: {persona['agent_name']} ({persona['role']})")
    print(f"Style: {persona['tone']} ({persona['formality']})")
    print(f"System Prompt snippet:\n{agent.get_system_prompt()[:200]}...")
    
    # Get educator perspective
    print("\n\n2. EDUCATOR PERSPECTIVE:")
    print("-" * 70)
    agent = DynamicAgent()
    agent.initialize_persona_custom('educator', 'friendly')
    persona = agent.get_current_persona()
    print(f"Agent: {persona['agent_name']} ({persona['role']})")
    print(f"Style: {persona['tone']} ({persona['formality']})")
    print(f"System Prompt snippet:\n{agent.get_system_prompt()[:200]}...")
    
    # Get analyst perspective
    print("\n\n3. ANALYST PERSPECTIVE:")
    print("-" * 70)
    agent = DynamicAgent()
    agent.initialize_persona_custom('analyst', 'analytical')
    persona = agent.get_current_persona()
    print(f"Agent: {persona['agent_name']} ({persona['role']})")
    print(f"Style: {persona['tone']} ({persona['formality']})")
    print(f"System Prompt snippet:\n{agent.get_system_prompt()[:200]}...")


def example_agent_information_system():
    """Example 4: Complete agent information and metadata"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Complete Agent Information System")
    print("=" * 70)
    
    agent = DynamicAgent()
    agent.initialize_persona_custom('mentor', 'nurturing')
    
    # Add some conversation
    agent.add_to_history('user', 'How do I start learning programming?')
    agent.add_to_history('assistant', 'Great question! Start with fundamentals...')
    agent.add_to_history('user', 'Any specific resources?')
    agent.add_to_history('assistant', 'Yes, I recommend...')
    
    # Get complete information
    info = agent.get_agent_info()
    
    print("\nCOMPLETE AGENT STATE:")
    print(f"Current Persona: {info['persona']['agent_name']} ({info['persona']['role']})")
    print(f"Speaking Style: {info['persona']['tone']}")
    print(f"Conversation History: {info['history_length']} messages")
    print(f"\nAvailable Profiles: {len(info['available_profiles'])}")
    print(f"Available Styles: {len(info['available_styles'])}")
    
    print("\nCONVERSATION TRANSCRIPT:")
    for i, msg in enumerate(agent.get_conversation_history(), 1):
        print(f"  {i}. {msg['role'].upper()}: {msg['content']}")


def example_configuration_management():
    """Example 5: Configuration management"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Configuration Management")
    print("=" * 70)
    
    config = AgentConfig()
    
    print("\nDefault Configuration:")
    print(f"  Enable Random Switching: {config.get('enable_random_switching')}")
    print(f"  Max History Length: {config.get('max_history_length')}")
    print(f"  Auto Clear History: {config.get('auto_clear_history')}")
    print(f"  Logging Enabled: {config.get('logging_enabled')}")
    
    # Customize configuration
    print("\nCustomizing Configuration...")
    config.set('enable_random_switching', True)
    config.set('max_history_length', 500)
    
    print("\nUpdated Configuration:")
    print(f"  Enable Random Switching: {config.get('enable_random_switching')}")
    print(f"  Max History Length: {config.get('max_history_length')}")
    
    # Use preset
    print("\nAvailable Conversation Modes:")
    for mode in config.list_conversation_modes():
        mode_config = config.get_conversation_mode(mode)
        print(f"  - {mode}: {mode_config['description']}")


def example_multi_context_conversation():
    """Example 6: Managing multiple agents in different contexts"""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Multi-Context Conversation Management")
    print("=" * 70)
    
    contexts = {
        'technical': {
            'context': 'Technical problem solving',
            'profile': 'analyst',
            'style': 'analytical'
        },
        'mentoring': {
            'context': 'Career mentoring',
            'profile': 'mentor',
            'style': 'nurturing'
        },
        'teaching': {
            'context': 'Educational content',
            'profile': 'educator',
            'style': 'friendly'
        },
    }
    
    agents = {}
    
    print("\nInitializing agents for different contexts:")
    for context_name, context_config in contexts.items():
        agent = DynamicAgent()
        agent.initialize_persona_custom(
            context_config['profile'],
            context_config['style']
        )
        agents[context_name] = agent
        
        persona = agent.get_current_persona()
        print(f"\n{context_name.upper()}:")
        print(f"  Context: {context_config['context']}")
        print(f"  Agent: {persona['agent_name']}")
        print(f"  Role: {persona['role']}")
        print(f"  Style: {persona['tone']}")
    
    # Show how to switch between contexts
    print("\n\nSwitching between contexts:")
    print("-" * 70)
    
    user_query = "I need help with both technical issues and career guidance"
    
    print(f"\nUser: {user_query}")
    
    # Technical response
    print(f"\n[TECHNICAL CONTEXT]")
    print(f"Agent: {agents['technical'].get_current_persona()['agent_name']}")
    print(f"Would provide: Technical analysis and solutions")
    
    # Mentoring response
    print(f"\n[MENTORING CONTEXT]")
    print(f"Agent: {agents['mentoring'].get_current_persona()['agent_name']}")
    print(f"Would provide: Career guidance and encouragement")


if __name__ == '__main__':
    example_preset_agents()
    example_conversation_modes()
    example_dynamic_response_styles()
    example_agent_information_system()
    example_configuration_management()
    example_multi_context_conversation()
    
    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("=" * 70)
