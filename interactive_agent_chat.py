#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Agent Skills 互动式对话演示
使用不同的 Agent 角色进行交流，每句话后自动切换角色
"""

from skills.agent_illness import DynamicAgent
from typing import List, Tuple


def show_agent_banner(agent: DynamicAgent):
    """显示当前 Agent 的信息横幅"""
    persona = agent.get_current_persona()
    system_prompt = agent.get_system_prompt()
    
    print("\n" + "="*90)
    print(f"  🤖 当前 Agent")
    print("="*90)
    print(f"  👤 名字: {persona['agent_name']}")
    print(f"  🎭 角色: {persona['role']}")
    print(f"  💬 说话风格: {persona['tone']}")
    print(f"  📊 正式程度: {persona['formality']}")
    print(f"  ✨ 性格特征: {persona['personality_traits']}")
    print("-"*90)


def simulate_response(agent: DynamicAgent, user_input: str) -> str:
    """
    模拟 Agent 的响应
    根据系统提示、角色特征、说话风格生成一句话
    这展示了如果使用 LLM 时会如何表现
    """
    persona = agent.get_current_persona()
    
    # 根据不同角色生成不同风格的响应
    responses = {
        'Research Expert': f"根据研究数据显示，关于『{user_input}』，我的学术分析是：这个问题涉及多个维度的考量，通过实证研究我们可以得出...",
        'Educator': f"很好的问题！关于『{user_input}』，让我用通俗的方式为你解释：首先，我们需要理解基本概念，然后深入探讨...",
        'Career Mentor': f"你的这个想法很不错。就『{user_input}』而言，从职业发展角度，我建议你：第一，要制定清晰的目标；第二，持续学习...",
        'Innovation Specialist': f"哇！『{user_input}』这个话题很有创意的角度！我的想法是打破常规思维，我们可以尝试创新方案，比如...",
        'Data Analyst': f"让我用数据驱动的方式分析『{user_input}』：根据统计学原理，我们可以看到趋势是...数据清楚地表明...",
        'Strategic Advisor': f"从战略规划的角度看『{user_input}』，我的建议是：长期来看，我们需要制定明确的路线图，关键步骤包括...",
    }
    
    # 获取对应的响应
    role = persona['role']
    response = responses.get(role, f"作为{role}，我对『{user_input}』的看法是...")
    
    return response


def interactive_chat():
    """交互式对话演示"""
    agent = DynamicAgent()
    
    print("\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " Agent Skills - 互动式对话演示（自动切换角色）".center(88) + "║")
    print("║" + " "*88 + "║")
    print("║" + " 每输入一个问题，Agent 会用不同的角色来回答，然后自动切换到下一个角色".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘")
    
    print("""
📝 使用说明:
   - 输入你的问题或话题
   - 系统会自动生成一个随机角色
   - 该角色会用其特有的风格回答你
   - 然后自动切换到下一个角色
   - 输入 'quit' 或 'exit' 来退出
   - 输入 'list' 来查看所有可用角色
    """)
    
    # 示例问题列表
    example_questions = [
        "如何有效地管理时间?",
        "什么是人工智能?",
        "如何应对工作压力?",
        "如何提高创新能力?",
        "怎样才能成功?",
    ]
    
    conversation_history = []
    turn = 1
    
    while True:
        try:
            # 获取用户输入
            if turn == 1:
                print("\n💡 示例问题:")
                for i, q in enumerate(example_questions, 1):
                    print(f"   {i}. {q}")
            
            user_input = input("\n🗣️  请输入你的问题或话题 (输入'quit'退出): ").strip()
            
            # 处理特殊命令
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 感谢使用 Agent Skills，再见！")
                break
            
            if user_input.lower() == 'list':
                agent.initialize_persona()  # 初始化一个 Agent
                info = agent.get_agent_info()
                print("\n🎭 可用的角色:")
                for role, name in info['available_profiles'].items():
                    print(f"   - {name}")
                continue
            
            if not user_input:
                print("⚠️  请输入有效的问题")
                continue
            
            # 初始化 Agent（随机角色）
            agent.initialize_persona()
            
            # 显示 Agent 信息
            show_agent_banner(agent)
            
            # 添加用户输入到历史
            agent.add_to_history('user', user_input)
            print(f"\n👤 你的问题: {user_input}")
            
            # 生成 Agent 响应
            response = simulate_response(agent, user_input)
            agent.add_to_history('assistant', response)
            
            print(f"\n🤖 {agent.get_current_persona()['agent_name']} 的回答:")
            print(f"   {response}")
            
            # 显示统计信息
            turn += 1
            print(f"\n📊 对话统计:")
            print(f"   - 轮次: {turn}")
            print(f"   - 对话消息总数: {len(agent.get_conversation_history())}")
            print(f"   - 系统提示字符数: {len(agent.get_system_prompt())}")
            print(f"\n🔄 下一轮会自动切换到其他角色...")
            
        except KeyboardInterrupt:
            print("\n\n👋 对话已中断，再见！")
            break
        except Exception as e:
            print(f"\n❌ 出错了: {e}")
            continue


def demo_multi_perspectives(topic: str = "AI对未来的影响"):
    """多角度分析演示"""
    print("\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + f" Agent Skills - 多角度分析演示：'{topic}'".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘")
    
    # 创建多个 Agent，每个都用不同的角色
    agents_config = [
        ('researcher', 'professional', '学术研究视角'),
        ('educator', 'friendly', '教育传播视角'),
        ('analyst', 'analytical', '数据分析视角'),
        ('mentor', 'nurturing', '职业发展视角'),
        ('innovator', 'enthusiastic', '创新创意视角'),
        ('strategist', 'professional', '战略规划视角'),
    ]
    
    print(f"\n📌 话题：{topic}\n")
    print("现在让 6 个不同角色的 Agent 来分析这个话题：\n")
    
    for i, (profile, style, description) in enumerate(agents_config, 1):
        agent = DynamicAgent()
        agent.initialize_persona_custom(profile, style)
        persona = agent.get_current_persona()
        
        print("─"*90)
        print(f"观点 {i}: {description}")
        print("─"*90)
        print(f"👤 专家: {persona['agent_name']} ({persona['role']})")
        print(f"💬 风格: {persona['tone']}")
        print(f"✨ 特征: {persona['personality_traits']}\n")
        
        # 生成该角色的回答
        response = simulate_response(agent, topic)
        print(f"📖 观点:\n   {response}\n")
        
        # 显示片段系统提示
        system_prompt = agent.get_system_prompt()
        print(f"📋 系统提示预览 (前200字符):")
        print(f"   {system_prompt[:200]}...")
        print()


def demo_role_switching_conversation():
    """角色切换对话演示"""
    print("\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " Agent Skills - 发表演讲场景（每句话切换角色）".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘")
    
    topic = "如何在职业中取得成功"
    
    # 模拟一个发言稿，每句话由不同角色说出
    print(f"\n🎤 话题：{topic}\n")
    print("由6位不同背景的专家轮流发表意见：\n")
    print("="*90)
    
    speeches = [
        {
            'profile': 'researcher',
            'style': 'professional',
            'input': '从实证研究角度看成功',
            'response': '根据大量研究数据，成功的人具有明确的目标设定、持续的学习能力和强大的抗挫折能力。'
        },
        {
            'profile': 'educator',
            'style': 'friendly',
            'input': '让我用简单的方式解释成功',
            'response': '成功其实很简单，就是把复杂的目标分解成小的、可管理的步骤，然后坚持执行！'
        },
        {
            'profile': 'mentor',
            'style': 'nurturing',
            'input': '职业发展建议',
            'response': '我的建议是：第一，要有职业规划；第二，持续投资自己；第三，建立良好的人脉网络。'
        },
        {
            'profile': 'analyst',
            'style': 'analytical',
            'input': '数据驱动的成功要素',
            'response': '统计数据显示，成功的核心要素是：40%的能力，35%的坚持，25%的运气和人脉。'
        },
        {
            'profile': 'innovator',
            'style': 'enthusiastic',
            'input': '创新是成功的关键',
            'response': '打破常规思维！不要做别人做过的事，要找到独特的解决方案，这才是真正的成功！'
        },
        {
            'profile': 'strategist',
            'style': 'professional',
            'input': '战略规划观点',
            'response': '从战略高度看，成功需要明确的愿景、可行的计划、充分的资源配置和持续的执行力。'
        },
    ]
    
    for i, speech in enumerate(speeches, 1):
        agent = DynamicAgent()
        agent.initialize_persona_custom(speech['profile'], speech['style'])
        persona = agent.get_current_persona()
        
        print(f"\n🎤 发言 {i}: {persona['agent_name']} ({persona['role']})")
        print(f"   风格: {persona['tone']}")
        print(f"   ───────────────────────────────────────────────────────────────────────────────")
        print(f"   💬 \"{speech['response']}\"")
        print()
    
    print("="*90)
    print("\n✅ 演讲完毕！6位不同背景的专家共同阐述了职业成功的多个维度。")


def main():
    """主程序"""
    print("\n" + "╔" + "="*88 + "╗")
    print("║" + " "*88 + "║")
    print("║" + " Agent Skills - 完整演示系统".center(88) + "║")
    print("║" + " "*88 + "║")
    print("└" + "="*88 + "┘")
    
    while True:
        print("""
🎯 选择演示模式:

1️⃣  【互动对话】 - 与不同角色的 Agent 进行交互式对话（最有趣！）
2️⃣  【多角度分析】- 用6个不同角色分析同一个话题
3️⃣  【发表演讲】- 6位专家轮流发表演讲，每句话切换角色
4️⃣  【退出】

────────────────────────────────────────────────────────────────────────────────
        """)
        
        choice = input("请选择 (1/2/3/4): ").strip()
        
        if choice == '1':
            interactive_chat()
        elif choice == '2':
            demo_multi_perspectives()
        elif choice == '3':
            demo_role_switching_conversation()
        elif choice == '4':
            print("\n👋 再见！")
            break
        else:
            print("⚠️  请输入有效的选项 (1/2/3/4)")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 程序已退出，再见！")
    except Exception as e:
        print(f"\n❌ 出错: {e}")
        import traceback
        traceback.print_exc()
