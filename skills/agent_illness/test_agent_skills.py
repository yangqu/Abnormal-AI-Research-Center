"""
Unit tests for Agent Skills
Validates all functionality works correctly
"""

import pytest
from agent_illness.system_prompt import SystemPromptSkill
from agent_illness.agent_profiles import AgentProfileManager, AgentProfile
from agent_illness.characteristics import CharacteristicManager, TalkingStyle
from agent_illness.dynamic_agent import DynamicAgent


class TestAgentProfileManager:
    """Test AgentProfileManager functionality"""
    
    def test_get_random_profile(self):
        """Test getting a random profile"""
        manager = AgentProfileManager()
        profile = manager.get_random_profile()
        assert profile is not None
        assert hasattr(profile, 'role')
        assert hasattr(profile, 'name')
        assert hasattr(profile, 'expertise_areas')
    
    def test_get_profile_by_role(self):
        """Test getting a specific profile by role"""
        manager = AgentProfileManager()
        profile = manager.get_profile_by_role('educator')
        assert profile is not None
        assert profile.role == 'Educator'
    
    def test_get_all_profiles(self):
        """Test getting all profiles"""
        manager = AgentProfileManager()
        profiles = manager.get_all_profiles()
        assert len(profiles) > 0
        assert len(profiles) == 6  # Should have 6 default profiles
    
    def test_add_profile(self):
        """Test adding a new profile"""
        manager = AgentProfileManager()
        new_profile = AgentProfile(
            role='Test Role',
            name='Test Name',
            description='Test Description',
            expertise_areas=['test']
        )
        manager.add_profile('test', new_profile)
        retrieved = manager.get_profile_by_role('test')
        assert retrieved is not None
        assert retrieved.name == 'Test Name'
    
    def test_get_current_profile(self):
        """Test getting current profile after selection"""
        manager = AgentProfileManager()
        manager.get_random_profile()
        current = manager.get_current_profile()
        assert current is not None


class TestCharacteristicManager:
    """Test CharacteristicManager functionality"""
    
    def test_get_random_style(self):
        """Test getting a random style"""
        manager = CharacteristicManager()
        style = manager.get_random_style()
        assert style is not None
        assert hasattr(style, 'tone')
        assert hasattr(style, 'formality')
    
    def test_get_style_by_name(self):
        """Test getting a specific style by name"""
        manager = CharacteristicManager()
        style = manager.get_style_by_name('professional')
        assert style is not None
        assert style.formality == 'formal'
    
    def test_get_all_styles(self):
        """Test getting all styles"""
        manager = CharacteristicManager()
        styles = manager.get_all_styles()
        assert len(styles) > 0
        assert len(styles) == 6  # Should have 6 default styles
    
    def test_add_style(self):
        """Test adding a new style"""
        manager = CharacteristicManager()
        new_style = TalkingStyle(
            name='Test Style',
            tone='test tone',
            formality='casual',
            pace='moderate',
            verbosity='balanced'
        )
        manager.add_style('test', new_style)
        retrieved = manager.get_style_by_name('test')
        assert retrieved is not None
        assert retrieved.tone == 'test tone'
    
    def test_get_style_description(self):
        """Test getting style description"""
        manager = CharacteristicManager()
        manager.get_random_style()
        description = manager.get_style_description()
        assert description is not None
        assert 'Style:' in description


class TestSystemPromptSkill:
    """Test SystemPromptSkill functionality"""
    
    def test_generate_system_prompt(self):
        """Test generating a random system prompt"""
        skill = SystemPromptSkill()
        prompt = skill.generate_system_prompt()
        assert prompt is not None
        assert len(prompt) > 0
        assert 'You are' in prompt
    
    def test_generate_system_prompt_for_profile(self):
        """Test generating prompt for specific profile"""
        skill = SystemPromptSkill()
        prompt = skill.generate_system_prompt_for_profile('mentor')
        assert prompt is not None
        assert 'You are' in prompt
    
    def test_generate_system_prompt_for_style(self):
        """Test generating prompt for specific style"""
        skill = SystemPromptSkill()
        prompt = skill.generate_system_prompt_for_style('professional')
        assert prompt is not None
        assert 'You are' in prompt
    
    def test_generate_system_prompt_custom(self):
        """Test generating prompt for specific profile and style"""
        skill = SystemPromptSkill()
        prompt = skill.generate_system_prompt_custom('educator', 'friendly')
        assert prompt is not None
        assert 'Educator' in prompt or 'Professor' in prompt
    
    def test_get_current_persona(self):
        """Test getting current persona"""
        skill = SystemPromptSkill()
        skill.generate_system_prompt()
        persona = skill.get_current_persona()
        assert persona is not None
        assert 'agent_name' in persona
        assert 'role' in persona
    
    def test_list_available_profiles(self):
        """Test listing available profiles"""
        skill = SystemPromptSkill()
        profiles = skill.list_available_profiles()
        assert len(profiles) > 0
    
    def test_list_available_styles(self):
        """Test listing available styles"""
        skill = SystemPromptSkill()
        styles = skill.list_available_styles()
        assert len(styles) > 0


class TestDynamicAgent:
    """Test DynamicAgent functionality"""
    
    def test_initialize_persona(self):
        """Test initializing with random persona"""
        agent = DynamicAgent()
        prompt = agent.initialize_persona()
        assert prompt is not None
        assert len(prompt) > 0
    
    def test_initialize_persona_with_profile(self):
        """Test initializing with specific profile"""
        agent = DynamicAgent()
        prompt = agent.initialize_persona_with_profile('innovator')
        assert prompt is not None
    
    def test_initialize_persona_with_style(self):
        """Test initializing with specific style"""
        agent = DynamicAgent()
        prompt = agent.initialize_persona_with_style('analytical')
        assert prompt is not None
    
    def test_initialize_persona_custom(self):
        """Test initializing with specific profile and style"""
        agent = DynamicAgent()
        prompt = agent.initialize_persona_custom('strategist', 'concise')
        assert prompt is not None
    
    def test_change_persona(self):
        """Test changing to new persona"""
        agent = DynamicAgent()
        agent.initialize_persona()
        persona1 = agent.get_current_persona()
        
        agent.change_persona()
        persona2 = agent.get_current_persona()
        
        # May or may not be different due to randomness, but both should exist
        assert persona1 is not None
        assert persona2 is not None
    
    def test_get_current_persona(self):
        """Test getting current persona information"""
        agent = DynamicAgent()
        agent.initialize_persona()
        persona = agent.get_current_persona()
        assert 'agent_name' in persona
        assert 'role' in persona
        assert 'tone' in persona
    
    def test_get_system_prompt(self):
        """Test getting system prompt"""
        agent = DynamicAgent()
        assert agent.get_system_prompt() is None
        
        agent.initialize_persona()
        prompt = agent.get_system_prompt()
        assert prompt is not None
    
    def test_add_to_history(self):
        """Test adding messages to conversation history"""
        agent = DynamicAgent()
        agent.add_to_history('user', 'Hello')
        agent.add_to_history('assistant', 'Hi there!')
        
        history = agent.get_conversation_history()
        assert len(history) == 2
        assert history[0]['role'] == 'user'
        assert history[1]['role'] == 'assistant'
    
    def test_clear_history(self):
        """Test clearing conversation history"""
        agent = DynamicAgent()
        agent.add_to_history('user', 'Hello')
        assert len(agent.get_conversation_history()) == 1
        
        agent.clear_history()
        assert len(agent.get_conversation_history()) == 0
    
    def test_get_agent_info(self):
        """Test getting complete agent information"""
        agent = DynamicAgent()
        agent.initialize_persona()
        
        info = agent.get_agent_info()
        assert 'persona' in info
        assert 'system_prompt' in info
        assert 'history_length' in info
        assert 'available_profiles' in info
        assert 'available_styles' in info
    
    def test_conversation_workflow(self):
        """Test a complete conversation workflow"""
        agent = DynamicAgent()
        agent.initialize_persona_custom('mentor', 'nurturing')
        
        # Add messages
        agent.add_to_history('user', 'How can I improve?')
        agent.add_to_history('assistant', 'Start by setting clear goals.')
        
        # Verify
        history = agent.get_conversation_history()
        assert len(history) == 2
        assert history[0]['content'] == 'How can I improve?'
    
    def test_persona_consistency(self):
        """Test that persona remains consistent until changed"""
        agent = DynamicAgent()
        agent.initialize_persona_custom('researcher', 'professional')
        
        persona1 = agent.get_current_persona()
        prompt1 = agent.get_system_prompt()
        
        persona2 = agent.get_current_persona()
        prompt2 = agent.get_system_prompt()
        
        # Should be same until change
        assert persona1['agent_name'] == persona2['agent_name']
        assert prompt1 == prompt2


class TestIntegration:
    """Integration tests for complete workflows"""
    
    def test_multi_person_conversation(self):
        """Test simulating conversation with multiple personas"""
        topic = "What is artificial intelligence?"
        
        # Get different perspectives
        agents = []
        perspectives = []
        profiles = [('researcher', 'analytical'), ('educator', 'friendly')]
        
        for profile, style in profiles:
            agent = DynamicAgent()
            agent.initialize_persona_custom(profile, style)
            agents.append(agent)
            
            persona = agent.get_current_persona()
            perspectives.append({
                'name': persona['agent_name'],
                'role': persona['role'],
                'tone': persona['tone']
            })
        
        assert len(perspectives) == 2
        assert perspectives[0]['role'] != perspectives[1]['role']
    
    def test_adaptive_agent_switching(self):
        """Test agent adapting to different contexts"""
        agent = DynamicAgent()
        
        # Context 1: Technical support
        agent.initialize_persona_custom('analyst', 'professional')
        context1_persona = agent.get_current_persona()
        
        # Context 2: Mentoring
        agent.change_persona()
        context2_persona = agent.get_current_persona()
        
        # Both should be valid
        assert context1_persona['agent_name'] is not None
        assert context2_persona['agent_name'] is not None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
