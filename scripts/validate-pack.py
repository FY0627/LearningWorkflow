import os
import sys
import json

# Ensure stdout uses utf-8 encoding on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def validate_skill_pack(agents_root):
    print("🔍 开始校验 Frank Agentic Skill Package...")
    
    pack_json_path = os.path.join(agents_root, "skill-pack.json")
    if not os.path.exists(pack_json_path):
        print("❌ [错误] 缺少 skill-pack.json 文件")
        return False
        
    with open(pack_json_path, 'r', encoding='utf-8') as f:
        pack_data = json.load(f)
        
    skills_dir = os.path.join(agents_root, "skills")
    if not os.path.exists(skills_dir):
        print("❌ [错误] 缺少 skills 目录")
        return False
        
    declared_skills = pack_data.get("skills", [])
    valid_count = 0
    
    for skill_name in declared_skills:
        skill_md_path = os.path.join(skills_dir, skill_name, "SKILL.md")
        if not os.path.exists(skill_md_path):
            print(f"⚠️ [警告] 声明的 Skill {skill_name} 缺少 SKILL.md 文件: {skill_md_path}")
            continue
            
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.startswith("---"):
            print(f"❌ [错误] {skill_name}/SKILL.md 缺少 Frontmatter (--- 开头)")
            continue
            
        if "name:" not in content or "description:" not in content:
            print(f"❌ [错误] {skill_name}/SKILL.md Frontmatter 缺少 name 或 description")
            continue
            
        valid_count += 1
        print(f"  ✓ {skill_name} 校验通过")
        
    print(f"\n🎉 校验完成！成功通过 {valid_count}/{len(declared_skills)} 个 Skill。")
    return True

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    validate_skill_pack(root_dir)
