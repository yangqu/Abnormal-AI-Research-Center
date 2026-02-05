"""
Agent Skills Package
Manages various skills for AI agents with dynamic characteristics
"""

from .agent_illness.system_prompt import SystemPromptSkill
from .agent_illness.agent_profiles import AgentProfileManager
from .agent_illness.characteristics import CharacteristicManager

__all__ = [
    'SystemPromptSkill',
    'AgentProfileManager',  
    'CharacteristicManager'
]
