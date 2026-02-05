"""
System Prompt Skill
Generates dynamic system prompts based on randomly selected agent profiles and characteristics
"""

from typing import Dict, Optional
from .agent_profiles import AgentProfileManager, AgentProfile
from .characteristics import CharacteristicManager, TalkingStyle


class SystemPromptSkill:
    """
    Generates dynamic system prompts for agents with randomly assigned roles and characteristics
    Allows agents to change their persona, name, and talking style dynamically
    """
    
    def __init__(self):
        """Initialize the system prompt skill with managers"""
        self.profile_manager = AgentProfileManager()
        self.characteristic_manager = CharacteristicManager()
        self.prompt_template = self._create_prompt_template()
    
    def _create_prompt_template(self) -> str:
        """Create the base template for system prompts"""
        return """You are {agent_name}, a {role}.

## Identity
- Role: {role}
- Name: {agent_name}
- Expertise Areas: {expertise_areas}
- Description: {description}

## Communication Style
- Tone: {tone}
- Formality Level: {formality}
- Pace: {pace}
- Verbosity: {verbosity}
- Personality Traits: {personality_traits}

## Communication Patterns
{communication_patterns}

## Behavioral Guidelines
1. Maintain your assigned role and expertise consistently
2. Communicate in the specified tone and formality level
3. Adapt your response pace to the conversation needs
4. Provide responses matching your verbosity preference
5. Demonstrate the personality traits listed above
6. Follow the communication patterns for greetings, explanations, and closings

## Core Instructions
- Always stay in character as {agent_name}
- Use your expertise areas to provide valuable insights
- Follow your communication style guidelines in every interaction
- Be helpful, honest, and harmless while maintaining your persona
- Adapt your responses to the user's needs while staying true to your characteristics
"""
    
    def generate_system_prompt(self) -> str:
        """
        Generate a random system prompt with a new persona and characteristics
        Returns a complete system prompt string
        """
        # Select random profile and characteristics
        profile = self.profile_manager.get_random_profile()
        style = self.characteristic_manager.get_random_style()
        
        return self._format_prompt(profile, style)
    
    def generate_system_prompt_for_profile(self, profile_key: str) -> str:
        """
        Generate a system prompt with a specific profile but random characteristics
        """
        profile = self.profile_manager.get_profile_by_role(profile_key)
        if not profile:
            raise ValueError(f"Profile '{profile_key}' not found")
        
        style = self.characteristic_manager.get_random_style()
        return self._format_prompt(profile, style)
    
    def generate_system_prompt_for_style(self, style_key: str) -> str:
        """
        Generate a system prompt with a random profile but specific characteristics
        """
        style = self.characteristic_manager.get_style_by_name(style_key)
        if not style:
            raise ValueError(f"Style '{style_key}' not found")
        
        profile = self.profile_manager.get_random_profile()
        return self._format_prompt(profile, style)
    
    def generate_system_prompt_custom(self, profile_key: str, style_key: str) -> str:
        """
        Generate a system prompt with specific profile and style
        """
        profile = self.profile_manager.get_profile_by_role(profile_key)
        style = self.characteristic_manager.get_style_by_name(style_key)
        
        if not profile:
            raise ValueError(f"Profile '{profile_key}' not found")
        if not style:
            raise ValueError(f"Style '{style_key}' not found")
        
        return self._format_prompt(profile, style)
    
    def _format_prompt(self, profile: AgentProfile, style: TalkingStyle) -> str:
        """
        Format the prompt template with profile and style information
        """
        communication_patterns_str = '\n'.join([
            f"  - {key.capitalize()}: {value}"
            for key, value in style.communication_patterns.items()
        ])
        
        prompt = self.prompt_template.format(
            agent_name=profile.name,
            role=profile.role,
            expertise_areas=', '.join(profile.expertise_areas),
            description=profile.description,
            tone=style.tone,
            formality=style.formality,
            pace=style.pace,
            verbosity=style.verbosity,
            personality_traits=', '.join(style.personality_traits),
            communication_patterns=communication_patterns_str
        )
        
        return prompt
    
    def get_current_persona(self) -> Dict[str, str]:
        """
        Get information about the current persona
        Returns a dictionary with profile and style information
        """
        profile = self.profile_manager.get_current_profile()
        style = self.characteristic_manager.get_current_style()
        
        if not profile or not style:
            return {}
        
        return {
            'agent_name': profile.name,
            'role': profile.role,
            'tone': style.tone,
            'formality': style.formality,
            'personality_traits': ', '.join(style.personality_traits)
        }
    
    def list_available_profiles(self) -> Dict[str, str]:
        """List all available agent profiles"""
        profiles = self.profile_manager.get_all_profiles()
        return {profile.role: profile.name for profile in profiles}
    
    def list_available_styles(self) -> Dict[str, str]:
        """List all available talking styles"""
        styles = self.characteristic_manager.get_all_styles()
        return {style.name.lower(): style.tone for style in styles}
