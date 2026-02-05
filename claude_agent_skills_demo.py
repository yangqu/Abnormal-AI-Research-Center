#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Claude + Agent Skills 对话演示
展示 Claude 模型集成 Agent Skills，实现每句话自动切换角色的对话
"""

from skills.agent_illness import DynamicAgent
import time


def print_separator(width: int = 90):
    """打印分隔线"""
    print("─" * width)


def demonstrate_agent_conversation():
    """演示 Agent 不同角色的对话"""
    
    print("\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " Claude + Agent Skills - 角色切换对话演示".center(88) + "║")
    print("║" + " 实时展示同一个问题用不同角色回答的差异".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘\n")
    
    # 演示场景：用户提出一个问题，6个不同角色的Agent来回答
    question = "我想创建一个成功的创业公司，应该怎么做？"
    
    print(f"📌 用户问题：{question}\n")
    print("="*90)
    print("同一个问题，6个不同角色的Agent如何用各自的角度回答：")
    print("="*90)
    
    # 6个不同角色的回答（展示风格差异）
    responses = [
        {
            'profile': 'researcher',
            'style': 'professional',
            'short_response': '根据创业研究数据，成功企业的共同因素包括：明确的市场定位、强大的团队、充足的资金和持续的创新。我建议先进行深入的市场调研，分析竞争格局。'
        },
        {
            'profile': 'educator', 
            'style': 'friendly',
            'short_response': '很好的想法！让我用简单的步骤来帮你理解：首先，找到你热爱且擅长的领域；其次，了解市场需求；最后，找到志同道合的伙伴一起努力。过程很关键！'
        },
        {
            'profile': 'mentor',
            'style': 'nurturing', 
            'short_response': '我为你的梦想感到高兴！我的建议：第一，磨练你的领导力；第二，建立一个信任的团队；第三，保持学习心态。记住，人比商业计划更重要。'
        },
        {
            'profile': 'analyst',
            'style': 'analytical',
            'short_response': '从数据看，创业成功率约30%。成功的关键驱动因子：融资能力(35%)、团队执行(40%)、市场机遇(25%)。建议制定详细的财务预测和市场分析。'
        },
        {
            'profile': 'innovator',
            'style': 'enthusiastic',
            'short_response': '太令人兴奋了！关键是找到市场中的痛点，用创新的方式解决它！打破传统思维，敢于尝试别人没做过的东西，这才是创业的精髓！'
        },
        {
            'profile': 'strategist',
            'style': 'professional',
            'short_response': '从战略角度，成功的创业需要：明确的愿景、清晰的路线图、合理的资源配置、风险管理策略。前三年是关键，需要保持专注和灵活性的平衡。'
        },
    ]
    
    for idx, response_info in enumerate(responses, 1):
        # 初始化该角色的Agent
        agent = DynamicAgent()
        agent.initialize_persona_custom(response_info['profile'], response_info['style'])
        
        persona = agent.get_current_persona()
        
        # 显示Agent信息
        print(f"\n🔄 角色 {idx}: {persona['agent_name']} ({persona['role']})")
        print_separator()
        print(f"   👤 身份: {persona['agent_name']}")
        print(f"   🎭 角色: {persona['role']}")
        print(f"   💬 说话风格: {persona['tone']}")
        print(f"   ✨ 性格特征: {persona['personality_traits']}")
        print_separator()
        
        # 显示系统提示的关键部分
        system_prompt = agent.get_system_prompt()
        lines = system_prompt.split('\n')
        
        print(f"   📜 系统提示 (前800字符):")
        print(f"   ")
        print("   " + "\n   ".join(lines[:15]))
        print(f"   ... (共 {len(lines)} 行)")
        
        print_separator()
        
        # 显示该角色的回答
        print(f"   🎯 回答:")
        print(f"   ")
        response_text = response_info['short_response']
        # 换行显示，每行添加缩进
        for line in response_text.split('\n'):
            print(f"      {line}")
        
        # 添加到历史记录
        agent.add_to_history('user', question)
        agent.add_to_history('assistant', response_text)
        
        time.sleep(0.5)  # 短暂延迟，给用户阅读时间


def demonstrate_conversation_flow():
    """演示信息流转过程"""
    
    print("\n\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " 实时对话流展示 - 每轮切换新角色".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘\n")
    
    # 模拟一个多轮对话
    conversation_turns = [
        {
            'turn': 1,
            'user': '你好，我对 AI 很感兴趣',
            'profile': 'educator',
            'style': 'friendly'
        },
        {
            'turn': 2,
            'user': 'AI 的未来发展方向是什么？',
            'profile': 'analyst',
            'style': 'analytical'
        },
        {
            'turn': 3,
            'user': '如何应用 AI 到我的业务中？',
            'profile': 'strategist',
            'style': 'professional'
        },
        {
            'turn': 4,
            'user': '有没有创新的想法？',
            'profile': 'innovator',
            'style': 'enthusiastic'
        },
    ]
    
    print("模拟一个完整的对话过程，每条回复自动切换不同角色：\n")
    print("="*90)
    
    for turn_info in conversation_turns:
        turn = turn_info['turn']
        user_msg = turn_info['user']
        
        # 初始化新角色
        agent = DynamicAgent()
        agent.initialize_persona_custom(turn_info['profile'], turn_info['style'])
        persona = agent.get_current_persona()
        
        # 显示对话轮次
        print(f"\n【对话轮次 {turn}】")
        print("─"*90)
        print(f"👤 用户: {user_msg}")
        print()
        
        # 生成回答
        agent.add_to_history('user', user_msg)
        
        # 根据不同角色生成不同回答
        if turn == 1:
            response = f"你好！我叫{persona['agent_name']}，很高兴认识你！作为{persona['role']}，我可以用生动的方式为你讲解AI的奥妙。AI技术正在改变世界，我们一起探索吧！"
        elif turn == 2:
            response = f"很好的问题。根据当前数据分析，AI的发展方向主要有三个：1) 自然语言处理(占35%)，2) 视觉识别(30%)，3) 决策系统(35%)。预计未来五年这三个领域会深度融合。"
        elif turn == 3:
            response = f"从战略角度看，你可以在三个方面应用AI：数据分析、自动化流程、客户体验优化。首先评估你的核心业务痛点，然后有针对性地导入AI解决方案。"
        else:
            response = f"哇！创新的想法真的太棒了！我建议你考虑AI+X的模式，比如AI+教育、AI+医疗、AI+制造。找到你所在行业的痛点，然后用颠覆性的AI方案来解决！"
        
        agent.add_to_history('assistant', response)
        
        # 显示Agent信息和回答
        print(f"🤖 {persona['agent_name']} ({persona['role']}, {persona['tone']})")
        print(f"   {response}")
        
        # 显示对话历史长度
        history = agent.get_conversation_history()
        print(f"\n   📊 对话历史记录: {len(history)} 条消息")
        print("─"*90)
        
        time.sleep(0.3)
    
    print("\n✅ 对话演示完毕！")


def show_system_prompt_differences():
    """展示系统提示的差异"""
    
    print("\n\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " 系统提示对比 - 同角色不同风格的提示差异".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘\n")
    
    print("同一个「研究员」角色，不同说话风格的系统提示对比：\n")
    
    # 对比两种风格的提示
    profiles = [
        ('researcher', 'professional', 'Professional - 正式专业'),
        ('researcher', 'friendly', 'Friendly - 友好亲和')
    ]
    
    for profile, style, label in profiles:
        agent = DynamicAgent()
        agent.initialize_persona_custom(profile, style)
        persona = agent.get_current_persona()
        system_prompt = agent.get_system_prompt()
        
        print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"📋 {label} 的 System Prompt")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\n😊 Agent: {persona['agent_name']}")
        print(f"🎯 Tone: {persona['tone']}")
        print(f"💫 Traits: {persona['personality_traits']}\n")
        
        # 截取前600个字符
        truncated = system_prompt[:600] + "..." if len(system_prompt) > 600 else system_prompt
        print(truncated)
        print()


def main():
    """主演示程序"""
    
    print("\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " Agent Skills 完整对话演示系统".center(88) + "║")
    print("║" + " 展示 Claude 集成 Agent Skills 进行角色切换".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘\n")
    
    print("""
🎬 本演示包含以下内容：

1️⃣  【角色回答对比】
    同一个问题，6个不同角色用各自的角度和风格回答
    ✓ 展示不同角色的思维方式
    ✓ 展示系统提示的内容
    ✓ 展示说话风格的差异

2️⃣  【真实对话流】  
    模拟一个完整的多轮对话过程
    ✓ 每一轮使用不同的角色
    ✓ 展示对话历史的记录
    ✓ 展示动态角色切换

3️⃣  【系统提示对比】
    展示同角色不同风格的系统提示内容
    ✓ 理解提示词是如何影响回答的
    ✓ 理解风格标签的实际作用

════════════════════════════════════════════════════════════════════════════════
    """)
    
    try:
        # 执行所有演示
        demonstrate_agent_conversation()
        time.sleep(1)
        
        demonstrate_conversation_flow()
        time.sleep(1)
        
        show_system_prompt_differences()
        
        # 最后总结
        print("\n\n" + "╔" + "="*88 + "╗")
        print("║" + " "*88 + "║")
        print("║" + " ✅ 演示完成！".center(88) + "║")
        print("║" + " "*88 + "║")
        print("└" + "="*88 + "┘\n")
        
        print("""
📊 演示总结：

✨ 演示成功展示了以下功能：

1. 【动态角色切换】
   ✓ 每次初始化时 Agent 可选择任意角色组合
   ✓ 支持 6 种角色 × 6 种风格 = 36 种组合
   ✓ 系统提示根据角色和风格动态生成

2. 【对话历史管理】
   ✓ 自动记录用户和 Agent 的对话
   ✓ 支持查询对话历史长度和内容
   ✓ 便于后续分析和上下文理解

3. 【系统提示生成】
   ✓ 对不同角色自动生成个性化的系统提示
   ✓ 系统提示包含身份、expertise、说话风格、行为准则
   ✓ 充分影响 LLM 的回答内容和形式

4. 【实际应用价值】
   ✓ 可用于教育场景：多角度学习
   ✓ 可用于决策场景：收集多方观点
   ✓ 可用于内容创作：自动生成多风格文案
   ✓ 可用于角色扮演：动态人设演绎

════════════════════════════════════════════════════════════════════════════════

💡 下一步建议：

1. 将 Agent Skills 集成到你的应用中
2. 使用 initialize_persona_custom() 创建指定角色
3. 使用 get_system_prompt() 获取系统提示
4. 将系统提示传给 LLM 模型（Claude/GPT等）
5. 用 add_to_history() 记录对话过程

════════════════════════════════════════════════════════════════════════════════
        """)
        
    except Exception as e:
        print(f"\n❌ 演示过程中发生错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 演示已中断，再见！")
