#!/usr/bin/env python3
# 测试中文汉化后的代码

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 模拟 folder_paths 模块
class MockFolderPaths:
    @staticmethod
    def get_output_directory():
        return "/tmp/output"

    @staticmethod
    def get_save_image_path(prefix, output_dir):
        return "/tmp/full_output", "filename_short", 1, "subfolder", prefix

sys.modules['folder_paths'] = MockFolderPaths()

# 模拟其他导入
import types
mock_csv_reader = types.ModuleType('csv_reader')
def mock_csv_to_list(filename):
    if filename == "superprompter_styles":
        return ["artful", "adorable", "alluring"]
    return []
mock_csv_reader.csv_to_list = mock_csv_to_list
sys.modules['csv_reader'] = mock_csv_reader

# 模拟 build_dynamic_prompt 模块
mock_build_dynamic_prompt = types.ModuleType('build_dynamic_prompt')
def mock_build_dynamic_prompt_func(*args, **kwargs):
    return ["测试提示词", "测试提示词_g", "测试提示词_l"]
mock_build_dynamic_prompt.build_dynamic_prompt = mock_build_dynamic_prompt_func
mock_build_dynamic_prompt.createpromptvariant = lambda x, y: "变体提示词"
mock_build_dynamic_prompt.build_dynamic_negative = lambda x, y, z, w, **kwargs: "负向提示词"
mock_build_dynamic_prompt.artify_prompt = lambda **kwargs: "美化提示词"
mock_build_dynamic_prompt.flufferizer = lambda **kwargs: "润色提示词"
mock_build_dynamic_prompt.one_button_superprompt = lambda **kwargs: "超级提示词"
sys.modules['build_dynamic_prompt'] = mock_build_dynamic_prompt

# 模拟 one_button_presets 模块
mock_one_button_presets = types.ModuleType('one_button_presets')
class MockOneButtonPresets:
    RANDOM_PRESET_OBP = "随机预设"
    opb_presets = {"标准": {"insanitylevel": 5}}
    def get_obp_preset(self, name):
        return self.opb_presets.get(name, {})
mock_one_button_presets.OneButtonPresets = MockOneButtonPresets
sys.modules['one_button_presets'] = mock_one_button_presets

# 模拟 load_config_csv 函数
def mock_load_config_csv():
    return []
sys.modules['__main__'].load_config_csv = mock_load_config_csv

try:
    # 导入汉化后的模块
    import OneButtonPromptNodes as obp

    print("✅ 模块导入成功！")
    print(f"✅ 节点类别映射: {obp.NODE_CLASS_MAPPINGS.keys()}")
    print(f"✅ 节点显示名称映射: {obp.NODE_DISPLAY_NAME_MAPPINGS}")

    # 测试中文显示列表
    print(f"\n✅ 艺术家中文显示列表长度: {len(obp.artists_display)}")
    print(f"✅ 图像类型中文显示列表长度: {len(obp.imagetypes_display)}")
    print(f"✅ 主体中文显示列表长度: {len(obp.subjects_display)}")

    # 测试映射字典
    print(f"\n✅ 艺术家映射字典大小: {len(obp.artists_map)}")
    print(f"✅ 图像类型映射字典大小: {len(obp.imagetypes_map)}")
    print(f"✅ 主体映射字典大小: {len(obp.subjects_map)}")

    # 测试映射功能
    test_chinese = "全部"
    test_english = obp.artists_map.get(test_chinese, test_chinese)
    print(f"\n✅ 映射测试: '{test_chinese}' -> '{test_english}'")

    print("\n🎉 所有测试通过！汉化代码编译成功且基本功能正常。")

except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)