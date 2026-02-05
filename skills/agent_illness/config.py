"""
Agent Skills Configuration
Configure default settings and profiles for agent skills
"""

from typing import Dict, List, Optional

# Default configuration
DEFAULT_CONFIG = {
    'enable_random_switching': False,
    'max_history_length': 1000,
    'auto_clear_history': False,
    'default_profile': None,  # None = random
    'default_style': None,    # None = random
    'logging_enabled': True,
}

# Preset agent configurations for quick setup
PRESET_AGENTS = {
    'academic': {
        'profile': 'researcher',
        'style': 'professional',
        'description': 'Academic researcher with professional tone'
    },
    'mentor': {
        'profile': 'mentor',
        'style': 'nurturing',
        'description': 'Supportive mentor with encouraging tone'
    },
    'teacher': {
        'profile': 'educator',
        'style': 'friendly',
        'description': 'Friendly teacher with engaging approach'
    },
    'analyst': {
        'profile': 'analyst',
        'style': 'analytical',
        'description': 'Data-focused analyst with logical reasoning'
    },
    'innovator': {
        'profile': 'innovator',
        'style': 'enthusiastic',
        'description': 'Creative innovator with exciting energy'
    },
    'advisor': {
        'profile': 'strategist',
        'style': 'professional',
        'description': 'Strategic advisor with clear guidance'
    },
}

# Conversation modes
CONVERSATION_MODES = {
    'single_agent': {
        'description': 'Single agent maintains same persona throughout',
        'allow_persona_switch': False,
    },
    'adaptive': {
        'description': 'Agent adapts persona based on context',
        'allow_persona_switch': True,
    },
    'multi_agent': {
        'description': 'Multiple agents with different personas',
        'allow_persona_switch': True,
    },
}


class AgentConfig:
    """Configuration manager for agent skills"""
    
    def __init__(self, config: Optional[Dict] = None):
        """Initialize with optional custom configuration"""
        self.config = DEFAULT_CONFIG.copy()
        if config:
            self.config.update(config)
    
    def get(self, key: str, default=None):
        """Get a configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value) -> None:
        """Set a configuration value"""
        self.config[key] = value
    
    def get_preset_agent(self, name: str) -> Optional[Dict]:
        """Get a preset agent configuration"""
        return PRESET_AGENTS.get(name)
    
    def list_preset_agents(self) -> List[str]:
        """List all available preset agents"""
        return list(PRESET_AGENTS.keys())
    
    def get_conversation_mode(self, mode: str) -> Optional[Dict]:
        """Get conversation mode configuration"""
        return CONVERSATION_MODES.get(mode)
    
    def list_conversation_modes(self) -> List[str]:
        """List all available conversation modes"""
        return list(CONVERSATION_MODES.keys())
    
    def reset_to_defaults(self) -> None:
        """Reset configuration to defaults"""
        self.config = DEFAULT_CONFIG.copy()
    
    def __repr__(self) -> str:
        """String representation of configuration"""
        return f"AgentConfig({self.config})"


# Global configuration instance
_global_config = AgentConfig()


def get_global_config() -> AgentConfig:
    """Get the global configuration instance"""
    return _global_config


def configure_global(config: Dict) -> None:
    """Update global configuration"""
    _global_config.config.update(config)
