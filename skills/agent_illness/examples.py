"""
Examples demonstrating how to use Agent Skills
Shows various ways to generate dynamic agent personas
"""

from dynamic_agent import DynamicAgent
from system_prompt import SystemPromptSkill


def example_1_random_persona():
    """Example 1: Generate a completely random persona"""
    print("=" * 60)
    print("Example 1: Random Persona Generation")
    print("=" * 60)
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona()
    
    print("\nGenerated System Prompt:")
    print(system_prompt)
    print("\nCurrent Persona:")
    print(agent.get_current_persona())


def example_2_specific_profile():
    """Example 2: Use a specific profile with random style"""
    print("\n" + "=" * 60)
    print("Example 2: Specific Profile with Random Style")
    print("=" * 60)
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_with_profile('educator')
    
    print("\nGenerated System Prompt:")
    print(system_prompt)
    print("\nCurrent Persona:")
    print(agent.get_current_persona())


def example_3_specific_style():
    """Example 3: Use a specific talking style with random profile"""
    print("\n" + "=" * 60)
    print("Example 3: Specific Style with Random Profile")
    print("=" * 60)
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_with_style('professional')
    
    print("\nGenerated System Prompt:")
    print(system_prompt)
    print("\nCurrent Persona:")
    print(agent.get_current_persona())


def example_4_custom_combination():
    """Example 4: Use specific profile AND style combination"""
    print("\n" + "=" * 60)
    print("Example 4: Custom Profile and Style Combination")
    print("=" * 60)
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_custom('mentor', 'nurturing')
    
    print("\nGenerated System Prompt:")
    print(system_prompt)
    print("\nCurrent Persona:")
    print(agent.get_current_persona())


def example_5_persona_switching():
    """Example 5: Switch personas during conversation"""
    print("\n" + "=" * 60)
    print("Example 5: Persona Switching")
    print("=" * 60)
    
    agent = DynamicAgent()
    
    # First persona
    print("\nFirst Persona:")
    agent.initialize_persona()
    persona1 = agent.get_current_persona()
    print(f"Agent: {persona1['agent_name']} ({persona1['role']})")
    print(f"Tone: {persona1['tone']}")
    
    # Switch persona
    print("\n--- Switching Persona ---")
    agent.change_persona()
    persona2 = agent.get_current_persona()
    print(f"\nNew Agent: {persona2['agent_name']} ({persona2['role']})")
    print(f"Tone: {persona2['tone']}")


def example_6_list_options():
    """Example 6: List all available profiles and styles"""
    print("\n" + "=" * 60)
    print("Example 6: Available Options")
    print("=" * 60)
    
    skill = SystemPromptSkill()
    
    print("\nAvailable Profiles:")
    profiles = skill.list_available_profiles()
    for role, name in profiles.items():
        print(f"  - {role}: {name}")
    
    print("\nAvailable Talking Styles:")
    styles = skill.list_available_styles()
    for style_key, tone in styles.items():
        print(f"  - {style_key}: {tone}")


def example_7_conversation_tracking():
    """Example 7: Track conversation history with agent"""
    print("\n" + "=" * 60)
    print("Example 7: Conversation History Tracking")
    print("=" * 60)
    
    agent = DynamicAgent()
    agent.initialize_persona()
    
    print(f"\nAgent: {agent.get_current_persona()['agent_name']}")
    
    # Simulate conversation
    agent.add_to_history('user', 'Hello, what can you help me with?')
    agent.add_to_history('assistant', 'I can help you with various tasks!')
    agent.add_to_history('user', 'Great, tell me more.')
    agent.add_to_history('assistant', 'Here is detailed information...')
    
    print("\nConversation History:")
    for msg in agent.get_conversation_history():
        print(f"{msg['role'].upper()}: {msg['content']}")


def example_8_agent_info():
    """Example 8: Get complete agent information"""
    print("\n" + "=" * 60)
    print("Example 8: Complete Agent Information")
    print("=" * 60)
    
    agent = DynamicAgent()
    agent.initialize_persona_custom('innovator', 'enthusiastic')
    
    info = agent.get_agent_info()
    print("\nAgent Information:")
    print(f"Persona: {info['persona']}")
    print(f"History Length: {info['history_length']}")
    print(f"\nAvailable Profiles: {len(info['available_profiles'])}")
    print(f"Available Styles: {len(info['available_styles'])}")


if __name__ == '__main__':
    example_1_random_persona()
    example_2_specific_profile()
    example_3_specific_style()
    example_4_custom_combination()
    example_5_persona_switching()
    example_6_list_options()
    example_7_conversation_tracking()
    example_8_agent_info()
