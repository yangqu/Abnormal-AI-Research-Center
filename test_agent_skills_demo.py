#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Agent Skills 测试演示脚本
测试和展示Agent Skills包的各项功能
"""

from skills.agent_illness import DynamicAgent, SystemPromptSkill
from skills.agent_illness.config import AgentConfig, PRESET_AGENTS


def print_section(title):
    """打印分隔符和标题"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def test_1_random_persona():
    """测试1: 随机生成Agent角色"""
    print_section("测试 1: 随机生成 Agent 角色")
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona()
    persona = agent.get_current_persona()
    
    print(f"\n✓ Agent 名字: {persona['agent_name']}")
    print(f"✓ Agent 角色: {persona['role']}")
    print(f"✓ 说话风格: {persona['tone']}")
    print(f"✓ 正式程度: {persona['formality']}")
    print(f"✓ 性格特征: {persona['personality_traits']}")
    print(f"\n✓ 生成的系统提示长度: {len(system_prompt)} 字符")
    print(f"\n✓ 系统提示预览:")
    print("-" * 70)
    print(system_prompt[:300] + "...")


def test_2_specific_profile():
    """测试2: 使用特定的Agent角色 + 随机说话风格"""
    print_section("测试 2: 特定角色 (教育者) + 随机风格")
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_with_profile('educator')
    persona = agent.get_current_persona()
    
    print(f"\n✓ Agent 名字: {persona['agent_name']}")
    print(f"✓ Agent 角色: {persona['role']}")
    print(f"✓ 说话风格: {persona['tone']}")
    print(f"✓ 正式程度: {persona['formality']}")
    print(f"✓ 性格特征: {', '.join(persona['personality_traits'].split(', ')[:3])}...")


def test_3_specific_style():
    """测试3: 随机角色 + 特定的说话风格"""
    print_section("测试 3: 随机角色 + 专业风格")
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_with_style('professional')
    persona = agent.get_current_persona()
    
    print(f"\n✓ Agent 名字: {persona['agent_name']}")
    print(f"✓ Agent 角色: {persona['role']}")
    print(f"✓ 说话风格: {persona['tone']}")
    print(f"✓ 正式程度: {persona['formality']}")


def test_4_custom_combination():
    """测试4: 特定角色 + 特定风格"""
    print_section("测试 4: 自定义组合 (导师 + 温暖风格)")
    
    agent = DynamicAgent()
    system_prompt = agent.initialize_persona_custom('mentor', 'nurturing')
    persona = agent.get_current_persona()
    
    print(f"\n✓ Agent 名字: {persona['agent_name']}")
    print(f"✓ Agent 角色: {persona['role']}")
    print(f"✓ 说话风格: {persona['tone']}")
    print(f"✓ 说话速度: 慢速 (耐心)")
    print(f"✓ 性格特征: 关心, 耐心, 鼓励")


def test_5_persona_switching():
    """测试5: 中途切换Agent角色"""
    print_section("测试 5: 中途切换 Agent 角色")
    
    agent = DynamicAgent()
    
    # 第一个角色
    agent.initialize_persona()
    persona1 = agent.get_current_persona()
    print(f"\n▶ 第一个 Agent:")
    print(f"   名字: {persona1['agent_name']}")
    print(f"   角色: {persona1['role']}")
    print(f"   风格: {persona1['tone']}")
    
    # 切换角色
    print(f"\n⟳ 切换角色...")
    agent.change_persona()
    persona2 = agent.get_current_persona()
    print(f"\n▶ 第二个 Agent:")
    print(f"   名字: {persona2['agent_name']}")
    print(f"   角色: {persona2['role']}")
    print(f"   风格: {persona2['tone']}")


def test_6_conversation_tracking():
    """测试6: 对话历史记录"""
    print_section("测试 6: 对话历史记录")
    
    agent = DynamicAgent()
    agent.initialize_persona()
    persona = agent.get_current_persona()
    
    print(f"\n▶ Agent: {persona['agent_name']}")
    
    # 模拟对话
    conversations = [
        ("user", "你好! 你能帮我什么?"),
        ("assistant", "很高兴认识你! 我是一个AI助手。"),
        ("user", "你有什么专业技能?"),
        ("assistant", "我拥有多个领域的专业知识..."),
    ]
    
    for role, message in conversations:
        agent.add_to_history(role, message)
    
    print(f"\n✓ 记录的对话数: {len(agent.get_conversation_history())}")
    print(f"\n对话记录:")
    print("-" * 70)
    for i, msg in enumerate(agent.get_conversation_history(), 1):
        print(f"{i}. [{msg['role'].upper()}]: {msg['content']}")


def test_7_available_options():
    """测试7: 列出所有可用的角色和风格"""
    print_section("测试 7: 可用的角色和风格")
    
    skill = SystemPromptSkill()
    
    profiles = skill.list_available_profiles()
    print(f"\n✓ 可用的 Agent 角色 ({len(profiles)} 个):")
    for role, name in profiles.items():
        print(f"   - {role}: {name}")
    
    styles = skill.list_available_styles()
    print(f"\n✓ 可用的说话风格 ({len(styles)} 个):")
    for style_name, tone in list(styles.items())[:6]:
        print(f"   - {style_name}: {tone}")


def test_8_preset_agents():
    """测试8: 预设的Agent配置"""
    print_section("测试 8: 预设 Agent 配置")
    
    config = AgentConfig()
    presets = config.list_preset_agents()
    
    print(f"\n✓ 预设的 Agent 配置 ({len(presets)} 个):")
    for preset_name in presets:
        preset = config.get_preset_agent(preset_name)
        print(f"\n   [{preset_name}]")
        print(f"   - 角色: {preset['profile']}")
        print(f"   - 风格: {preset['style']}")
        print(f"   - 描述: {preset['description']}")


def test_9_agent_info():
    """测试9: 获取完整的Agent信息"""
    print_section("测试 9: 完整的 Agent 信息")
    
    agent = DynamicAgent()
    agent.initialize_persona_custom('analyst', 'analytical')
    
    # 添加几条对话
    agent.add_to_history('user', '分析一下这个数据')
    agent.add_to_history('assistant', '根据数据显示...')
    
    info = agent.get_agent_info()
    
    print(f"\n✓ 当前 Persona 信息:")
    print(f"   - 名字: {info['persona']['agent_name']}")
    print(f"   - 角色: {info['persona']['role']}")
    print(f"   - 风格: {info['persona']['tone']}")
    
    print(f"\n✓ 系统提示长度: {len(info['system_prompt'])} 字符")
    print(f"\n✓ 对话历史: {info['history_length']} 条消息")
    
    print(f"\n✓ 可用的角色: {len(info['available_profiles'])} 个")
    print(f"\n✓ 可用的风格: {len(info['available_styles'])} 个")


def test_10_multi_perspective():
    """测试10: 多角度分析 (不同的Agent给出不同观点)"""
    print_section("测试 10: 多角度分析")
    
    topic = "什么是人工智能?"
    perspectives = [
        ('researcher', 'professional'),
        ('educator', 'friendly'),
        ('analyst', 'analytical'),
    ]
    
    print(f"\n话题: {topic}\n")
    
    for profile, style in perspectives:
        agent = DynamicAgent()
        agent.initialize_persona_custom(profile, style)
        persona = agent.get_current_persona()
        
        print(f"▶ {persona['agent_name']} ({persona['role']})")
        print(f"   - 说话风格: {persona['tone']}")
        print(f"   - 正式程度: {persona['formality']}")
        print(f"   - 特征: {persona['personality_traits']}\n")


def main():
    """运行所有测试"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + " Agent Skills 包 - 完整功能测试演示".center(68) + "║")
    print("║" + " "*68 + "║")
    print("└" + "="*68 + "┘")
    
    try:
        test_1_random_persona()
        test_2_specific_profile()
        test_3_specific_style()
        test_4_custom_combination()
        test_5_persona_switching()
        test_6_conversation_tracking()
        test_7_available_options()
        test_8_preset_agents()
        test_9_agent_info()
        test_10_multi_perspective()
        
        print_section("✅ 所有测试完成!")
        print("\n🎉 Agent Skills 包工作正常！")
        print("\n📚 更多信息请查看:")
        print("   - skills/README.md")
        print("   - skills/QUICKSTART.md")
        print("   - skills/agent_illness/examples.py")
        print()
        
    except Exception as e:
        print(f"\n❌ 测试出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
