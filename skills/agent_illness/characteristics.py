"""
Characteristic Manager
Manages agent talking styles and behavioral characteristics
"""

import random
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class TalkingStyle:
    """Represents a specific talking style with attributes"""
    name: str
    tone: str
    formality: str  # 'formal', 'casual', 'professional'
    pace: str  # 'fast', 'moderate', 'slow'
    verbosity: str  # 'concise', 'balanced', 'detailed'
    personality_traits: List[str] = field(default_factory=list)
    communication_patterns: Dict[str, str] = field(default_factory=dict)


class CharacteristicManager:
    """Manages agent characteristics and talking styles"""
    
    def __init__(self):
        """Initialize with predefined talking styles"""
        self.talking_styles: Dict[str, TalkingStyle] = {
            'enthusiastic': TalkingStyle(
                name='Enthusiastic',
                tone='excited and energetic',
                formality='casual',
                pace='fast',
                verbosity='detailed',
                personality_traits=['optimistic', 'engaging', 'motivating'],
                communication_patterns={
                    'greeting': 'excited and warm',
                    'explanation': 'detailed with examples',
                    'closing': 'uplifting and encouraging'
                }
            ),
            'professional': TalkingStyle(
                name='Professional',
                tone='formal and authoritative',
                formality='formal',
                pace='moderate',
                verbosity='balanced',
                personality_traits=['competent', 'trustworthy', 'precise'],
                communication_patterns={
                    'greeting': 'formal and respectful',
                    'explanation': 'structured and clear',
                    'closing': 'professional and conclusive'
                }
            ),
            'friendly': TalkingStyle(
                name='Friendly',
                tone='warm and approachable',
                formality='casual',
                pace='moderate',
                verbosity='balanced',
                personality_traits=['empathetic', 'supportive', 'relatable'],
                communication_patterns={
                    'greeting': 'warm and personal',
                    'explanation': 'conversational',
                    'closing': 'friendly and open-ended'
                }
            ),
            'analytical': TalkingStyle(
                name='Analytical',
                tone='logical and objective',
                formality='professional',
                pace='moderate',
                verbosity='balanced',
                personality_traits=['logical', 'methodical', 'data-driven'],
                communication_patterns={
                    'greeting': 'straightforward',
                    'explanation': 'fact-based and structured',
                    'closing': 'evidence-based conclusion'
                }
            ),
            'concise': TalkingStyle(
                name='Concise',
                tone='direct and efficient',
                formality='professional',
                pace='fast',
                verbosity='concise',
                personality_traits=['efficient', 'focused', 'precise'],
                communication_patterns={
                    'greeting': 'brief and direct',
                    'explanation': 'minimal but comprehensive',
                    'closing': 'short and clear'
                }
            ),
            'nurturing': TalkingStyle(
                name='Nurturing',
                tone='supportive and encouraging',
                formality='casual',
                pace='slow',
                verbosity='detailed',
                personality_traits=['caring', 'patient', 'encouraging'],
                communication_patterns={
                    'greeting': 'warm and welcoming',
                    'explanation': 'step-by-step guidance',
                    'closing': 'supportive and affirming'
                }
            ),
        }
        self.current_style: Optional[TalkingStyle] = None
    
    def get_random_style(self) -> TalkingStyle:
        """Select and return a random talking style"""
        self.current_style = random.choice(list(self.talking_styles.values()))
        return self.current_style
    
    def get_style_by_name(self, name: str) -> Optional[TalkingStyle]:
        """Get a specific style by name"""
        return self.talking_styles.get(name)
    
    def get_all_styles(self) -> List[TalkingStyle]:
        """Get all available talking styles"""
        return list(self.talking_styles.values())
    
    def add_style(self, key: str, style: TalkingStyle) -> None:
        """Add a new talking style to the collection"""
        self.talking_styles[key] = style
    
    def get_current_style(self) -> Optional[TalkingStyle]:
        """Get the currently active talking style"""
        return self.current_style
    
    def get_style_description(self) -> str:
        """Get a description of the current style"""
        if not self.current_style:
            return "No style selected"
        
        style = self.current_style
        return (
            f"Style: {style.name}\n"
            f"Tone: {style.tone}\n"
            f"Formality: {style.formality}\n"
            f"Pace: {style.pace}\n"
            f"Verbosity: {style.verbosity}\n"
            f"Traits: {', '.join(style.personality_traits)}"
        )
