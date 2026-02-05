#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Agent Skills - 角色切换完整指南
展示所有切换角色的方式
"""

from skills.agent_illness import DynamicAgent


def print_section(title):
    """打印分隔符和标题"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)


def method_1_random_switch():
    """方法1: 随机切换角色 (最简单!)"""
    print_section("方法1: 随机切换角色 (change_persona)")
    
    agent = DynamicAgent()
    
    # 初始化第一个角色
    agent.initialize_persona()
    persona1 = agent.get_current_persona()
    print(f"\n▶ 第一个角色:")
    print(f"   名字: {persona1['agent_name']}")
    print(f"   角色: {persona1['role']}")
    print(f"   风格: {persona1['tone']}")
    
    # 切换到随机新角色 (这是最常用的!)
    print(f"\n⟳ 调用 agent.change_persona() 切换角色...")
    agent.change_persona()
    persona2 = agent.get_current_persona()
    
    print(f"\n▶ 第二个角色 (随机!):")
    print(f"   名字: {persona2['agent_name']}")
    print(f"   角色: {persona2['role']}")
    print(f"   风格: {persona2['tone']}")
    
    # 继续切换
    print(f"\n⟳ 再次切换...")
    agent.change_persona()
    persona3 = agent.get_current_persona()
    
    print(f"\n▶ 第三个角色:")
    print(f"   名字: {persona3['agent_name']}")
    print(f"   角色: {persona3['role']}")


def method_2_specific_profile():
    """方法2: 切换到特定的角色 (角色 + 随机风格)"""
    print_section("方法2: 切换到特定角色 (initialize_persona_with_profile)")
    
    agent = DynamicAgent()
    
    profiles = ['researcher', 'educator', 'mentor', 'innovator', 'analyst', 'strategist']
    
    for i, profile in enumerate(profiles[:3], 1):
        agent.initialize_persona_with_profile(profile)
        persona = agent.get_current_persona()
        
        print(f"\n▶ 角色 {i}: {profile}")
        print(f"   名字: {persona['agent_name']}")
        print(f"   角色: {persona['role']}")
        print(f"   风格: {persona['tone']} (随机)")


def method_3_specific_style():
    """方法3: 切换到特定的说话风格 (随机角色 + 特定风格)"""
    print_section("方法3: 切换说话风格 (initialize_persona_with_style)")
    
    agent = DynamicAgent()
    
    styles = ['professional', 'friendly', 'enthusiastic', 'analytical']
    
    for i, style in enumerate(styles, 1):
        agent.initialize_persona_with_style(style)
        persona = agent.get_current_persona()
        
        print(f"\n▶ 风格 {i}: {style}")
        print(f"   名字: {persona['agent_name']} (随机)")
        print(f"   风格: {persona['tone']}")
        print(f"   正式程度: {persona['formality']}")


def method_4_custom_switch():
    """方法4: 自定义切换 (指定角色 + 指定风格)"""
    print_section("方法4: 完全自定义切换 (initialize_persona_custom)")
    
    agent = DynamicAgent()
    
    combinations = [
        ('educator', 'professional'),
        ('mentor', 'nurturing'),
        ('analyst', 'analytical'),
        ('innovator', 'enthusiastic'),
        ('researcher', 'professional'),
    ]
    
    for i, (profile, style) in enumerate(combinations, 1):
        agent.initialize_persona_custom(profile, style)
        persona = agent.get_current_persona()
        
        print(f"\n▶ 组合 {i}: {profile} + {style}")
        print(f"   名字: {persona['agent_name']}")
        print(f"   角色: {persona['role']}")
        print(f"   风格: {persona['tone']}")


def conversation_with_switching():
    """实际应用: 在对话中中途切换角色"""
    print_section("实际应用: 对话中切换角色")
    
    agent = DynamicAgent()
    
    # 第一个角色 - 研究员
    print("\n📚 场景1: 用研究员角色分析问题")
    print("-" * 80)
    agent.initialize_persona_with_profile('researcher')
    persona1 = agent.get_current_persona()
    print(f"当前专家: {persona1['agent_name']} ({persona1['role']})")
    print(f"说话风格: {persona1['tone']}")
    
    agent.add_to_history('user', '什么是机器学习?')
    agent.add_to_history('assistant', '从数据科学的角度来看，机器学习是...')
    print(f"✓ 已记录对话")
    
    # 切换角色 - 教育者
    print("\n\n👨‍🏫 场景2: 切换到教育者角色，用更简单的方式解释")
    print("-" * 80)
    agent.initialize_persona_with_profile('educator')
    persona2 = agent.get_current_persona()
    print(f"当前专家: {persona2['agent_name']} ({persona2['role']})")
    print(f"说话风格: {persona2['tone']}")
    print(f"⚠️  注意: 初始化新角色会清空对话历史")
    
    # 如果要保持对话历史，使用另一种方式
    print("\n\n💡 技巧: 如果要保持对话继续，应该这样做:")
    print("-" * 80)
    
    agent = DynamicAgent()
    
    # 初始化第一个角色
    agent.initialize_persona_with_profile('analyst')
    persona = agent.get_current_persona()
    print(f"\n▶ 当前角色: {persona['agent_name']}")
    
    # 添加对话
    agent.add_to_history('user', '分析这个数据')
    agent.add_to_history('assistant', '根据分析...')
    print(f"✓ 对话消息数: {len(agent.get_conversation_history())}")
    
    # 方式A: 直接切换 (会清空历史)
    print(f"\n方式A: agent.initialize_persona_with_profile('educator')")
    print(f"       → 会清空对话历史")
    
    # 方式B: 保持历史继续对话 (推荐!)
    print(f"\n方式B: agent.change_persona() 然后重新添加消息")
    agent.change_persona()
    persona_new = agent.get_current_persona()
    print(f"✓ 现在是: {persona_new['agent_name']}")


def switching_scenarios():
    """切换角色的实际场景"""
    print_section("实际场景: 多角度问题分析")
    
    question = "AI对社会的影响"
    
    perspectives = [
        ('researcher', 'professional', '学术研究视角'),
        ('educator', 'friendly', '教育角度'),
        ('analyst', 'analytical', '数据分析角度'),
        ('mentor', 'nurturing', '职业指导角度'),
    ]
    
    print(f"\n问题: {question}\n")
    
    for profile, style, description in perspectives:
        agent = DynamicAgent()
        agent.initialize_persona_custom(profile, style)
        persona = agent.get_current_persona()
        
        print(f"\n{'='*80}")
        print(f"视角: {description}")
        print(f"专家: {persona['agent_name']} ({persona['role']})")
        print(f"风格: {persona['tone']}")
        print(f"特征: {persona['personality_traits']}")
        print(f"系统提示长度: {len(agent.get_system_prompt())} 字符")


def available_profiles_and_styles():
    """显示所有可用的角色和风格"""
    print_section("可用的角色和风格列表")
    
    agent = DynamicAgent()
    info = agent.get_agent_info()
    
    profiles = info['available_profiles']
    styles = info['available_styles']
    
    print("\n▶ 可用的角色 (6个):")
    print("-" * 80)
    for profile_key, profile_name in profiles.items():
        print(f"   '{profile_key}' → {profile_name}")
    
    print("\n▶ 可用的风格 (6个):")
    print("-" * 80)
    for style_key, style_tone in styles.items():
        print(f"   '{style_key}' → {style_tone}")


def quick_reference():
    """快速参考"""
    print_section("快速参考表")
    
    print("""
┌─────────────────────────────────────────────────────────────────────────────┐
│                           角色切换方法汇总                                   │
├────────────────────────────────┬──────────────┬─────────────────────────────┤
│ 方法                           │ 语法         │ 说明                        │
├────────────────────────────────┼──────────────┼─────────────────────────────┤
│ 1. 随机切换                    │ change_      │ 生成随机新角色              │
│    (最常用!)                   │ persona()    │ 会清空对话历史              │
│                                │              │                             │
│ 2. 特定角色+随机风格           │ initialize_  │ 指定角色，随机风格          │
│                                │ persona_with │ 会清空对话历史              │
│                                │ _profile()   │                             │
│                                │              │                             │
│ 3. 随机角色+特定风格           │ initialize_  │ 随机角色，指定风格          │
│                                │ persona_with │ 会清空对话历史              │
│                                │ _style()     │                             │
│                                │              │                             │
│ 4. 完全自定义                  │ initialize_  │ 同时指定角色和风格          │
│    (角色+风格)                 │ persona_     │ 会清空对话历史              │
│                                │ custom()     │ 最灵活的选择!              │
│                                │              │                             │
│ 5. 获取当前信息                │ get_current_ │ 不改变角色                  │
│                                │ persona()    │ 只是查看当前信息            │
└────────────────────────────────┴──────────────┴─────────────────────────────┘

重要提示:
  ✓ 所有 initialize_* 方法都会清空对话历史
  ✓ change_persona() 本质上是调用 initialize_persona()
  ✓ 如果要保持对话，需要手动重新添加消息到历史中
  ✓ get_current_persona() 可以查看当前角色信息，不会改变角色
""")


def code_examples():
    """完整代码示例"""
    print_section("完整代码示例")
    
    examples = """
【例子1】最简单的角色切换:
────────────────────────────────
from skills.agent_illness import DynamicAgent

agent = DynamicAgent()
agent.initialize_persona()  # 初始化角色

print(agent.get_current_persona())  # 查看当前角色

agent.change_persona()  # 切换到新角色!

print(agent.get_current_persona())  # 查看新角色


【例子2】在对话中切换不同角色给出建议:
────────────────────────────────
agent = DynamicAgent()

# 第一种专业意见
agent.initialize_persona_with_profile('analyst')
# 获取分析师的建议...

# 切换到另一种专业意见
agent.initialize_persona_with_profile('mentor')
# 获取导师的建议...

# 切换到第三种专业意见
agent.initialize_persona_with_profile('educator')
# 获取教育者的建议...


【例子3】自定义组合切换:
────────────────────────────────
agent = DynamicAgent()

# 严肃的研究员
agent.initialize_persona_custom('researcher', 'professional')
# ...

# 友好的教育者
agent.initialize_persona_custom('educator', 'friendly')
# ...

# 热情的创新者
agent.initialize_persona_custom('innovator', 'enthusiastic')
# ...


【例子4】循环切换多个角色:
────────────────────────────────
profiles = ['researcher', 'educator', 'mentor', 'analyst']

for profile in profiles:
    agent.initialize_persona_with_profile(profile)
    persona = agent.get_current_persona()
    
    print(f"现在是: {persona['agent_name']}")
    # 在这个角色下做某些工作...
    # ...


【例子5】保留对话历史切换角色的技巧:
────────────────────────────────
agent = DynamicAgent()

# 初始化第一个角色并添加对话
agent.initialize_persona_with_profile('analyst')
agent.add_to_history('user', '分析问题')
agent.add_to_history('assistant', '分析结果...')

# 保存当前历史
history = agent.get_conversation_history()

# 切换角色 (会清空历史)
agent.initialize_persona_with_profile('mentor')

# 恢复历史
for msg in history:
    agent.add_to_history(msg['role'], msg['content'])

# 继续使用新角色，但保留之前的对话上下文
"""
    print(examples)


def main():
    """运行所有演示"""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + " Agent Skills - 角色切换完整指南".center(78) + "║")
    print("║" + " "*78 + "║")
    print("└" + "="*78 + "┘")
    
    # 运行所有演示
    method_1_random_switch()
    method_2_specific_profile()
    method_3_specific_style()
    method_4_custom_switch()
    available_profiles_and_styles()
    conversation_with_switching()
    switching_scenarios()
    quick_reference()
    code_examples()
    
    print("\n" + "="*80)
    print("  ✅ 所有演示完成!")
    print("="*80)
    print("""
推荐阅读:
  - skills/README.md - 完整API文档
  - skills/QUICKSTART.md - 快速入门
  - skills/agent_illness/examples.py - 更多示例
""")


if __name__ == '__main__':
    main()
