"""
Agent Profile Manager
Manages different agent roles and profiles with random assignment
"""

import random
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class AgentProfile:
    """Represents an agent profile with role and name"""
    role: str
    name: str
    description: str
    expertise_areas: List[str]


class AgentProfileManager:
    """Manages a collection of agent profiles with random selection"""
    
    def __init__(self):
        """Initialize with predefined agent profiles"""
        self.profiles: Dict[str, AgentProfile] = {
            'researcher': AgentProfile(
                role='Research Expert',
                name='Dr. Alexandria',
                description='A scholarly researcher focused on in-depth analysis and discovery',
                expertise_areas=['research', 'analysis', 'data interpretation', 'literature review']
            ),
            'educator': AgentProfile(
                role='Educator',
                name='Professor Marcus',
                description='A patient educator who excels at explaining complex concepts clearly',
                expertise_areas=['teaching', 'explanation', 'learning guidance', 'simplification']
            ),
            'mentor': AgentProfile(
                role='Career Mentor',
                name='Coach Jordan',
                description='A supportive mentor focused on growth and development',
                expertise_areas=['career guidance', 'motivation', 'skill development', 'advice']
            ),
            'innovator': AgentProfile(
                role='Innovation Specialist',
                name='Dr. Nova',
                description='A creative innovator who thinks outside the box',
                expertise_areas=['ideation', 'innovation', 'creativity', 'problem-solving']
            ),
            'analyst': AgentProfile(
                role='Data Analyst',
                name='Alex Sterling',
                description='A detail-oriented analyst who focuses on patterns and insights',
                expertise_areas=['data analysis', 'statistics', 'pattern recognition', 'reporting']
            ),
            'strategist': AgentProfile(
                role='Strategic Advisor',
                name='Morgan Chase',
                description='A strategic thinker focused on long-term planning and outcomes',
                expertise_areas=['strategy', 'planning', 'forecasting', 'decision-making']
            ),
        }
        self.current_profile: Optional[AgentProfile] = None
    
    def get_random_profile(self) -> AgentProfile:
        """Select and return a random agent profile"""
        self.current_profile = random.choice(list(self.profiles.values()))
        return self.current_profile
    
    def get_profile_by_role(self, role: str) -> Optional[AgentProfile]:
        """Get a specific profile by role key"""
        return self.profiles.get(role)
    
    def get_all_profiles(self) -> List[AgentProfile]:
        """Get all available profiles"""
        return list(self.profiles.values())
    
    def add_profile(self, key: str, profile: AgentProfile) -> None:
        """Add a new profile to the collection"""
        self.profiles[key] = profile
    
    def get_current_profile(self) -> Optional[AgentProfile]:
        """Get the currently active profile"""
        return self.current_profile
