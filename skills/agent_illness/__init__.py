"""
Agent Illness Skills
Skills for managing agent personalities, roles, and characteristics
"""

from .system_prompt import SystemPromptSkill
from .agent_profiles import AgentProfileManager
from .characteristics import CharacteristicManager
from .dynamic_agent import DynamicAgent

__all__ = [
    'SystemPromptSkill',
    'AgentProfileManager',
    'CharacteristicManager',
    'DynamicAgent'
]
