import sys
import os
import folder_paths
from datetime import datetime
import uuid
import platform
 
custom_nodes_path = os.path.join(folder_paths.base_path, "custom_nodes")
onebuttonprompt_path = os.path.join(custom_nodes_path, "OneButtonPrompt")

sys.path.append(onebuttonprompt_path)

from build_dynamic_prompt import *
from csv_reader import *

from one_button_presets import OneButtonPresets
OBPresets = OneButtonPresets()
allpresets = [OBPresets.RANDOM_PRESET_OBP] + list(OBPresets.opb_presets.keys())

artists = ["all", "all (wild)", "none", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", "cinema", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
artifyartists = ["all", "all (wild)", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", "cinema", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
imagetypes = ["all", "all - force multiple",  "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime key visual", "only other types", "only templates mode", "dynamic templates mode", "art blaster mode", "quality vomit mode", "color cannon mode", "unique art mode", "massive madness mode", "photo fantasy mode", "subject only mode", "fixed styles mode", "the tokinator"]
subjects =["all", "object", "animal", "humanoid", "landscape", "concept"]
genders = ["all", "male", "female"]
emojis = [False, True]

models = ["SD1.5", "SDXL", "Stable Cascade"]
prompt_enhancers = ["none", "superprompt-v1"]
#subjectsubtypesobject = ["all", "generic objects", "vehicles", "food", "buildings", "space", "flora"]
#subjectsubtypeshumanoid = ["all", "generic humans", "generic human relations", "celebrities e.a.", "fictional characters", "humanoids", "based on job or title", "based on first name"]
#subjectsubtypesconcept = ["all", "event", "the X of Y concepts", "lines from poems", "lines from songs"]

amountofflufflist = ["none", "dynamic", "short", "medium", "long"]
fluff_reverse_polarity = [False,True]

artifymodeslist = ["standard", "remix", "super remix turbo"]
artifyamountofartistslist = ["random", "0", "1", "2", "3", "4", "5"]

# 创建中文显示名列表
artists_display = ["全部", "全部 (狂野)", "无", "流行", "greg 模式", "3D", "抽象", "棱角", "动漫", "建筑", "艺术新潮", "装饰艺术", "巴洛克", "包豪斯", "卡通", "角色", "儿童插画", "城市景观", "电影", "干净", "云景", "拼贴", "多彩", "漫画书", "立体派", "黑暗", "详细", "数字", "表现主义", "奇幻", "时尚", "野兽派", "具象主义", "血腥", "涂鸦", "平面设计", "高对比", "恐怖", "印象派", "装置", "风景", "明亮", "线条画", "低对比", "光感主义", "魔幻现实主义", "漫画", "黑色素", "凌乱", "单色", "自然", "裸体", "摄影", "波普艺术", "肖像", "原始主义", "迷幻", "现实主义", "文艺复兴", "浪漫主义", "场景", "科幻", "雕塑", "海景", "太空", "彩色玻璃", "静物", "童话现实主义", "街头艺术", "街景", "超现实主义", "象征主义", "纺织", "浮世绘", "鲜艳", "水彩", "奇幻"]

imagetypes_display = ["全部", "全部 - 强制多重", "照片", "八角渲染", "数字艺术", "概念艺术", "绘画", "肖像", "动漫关键视觉", "仅其他类型", "仅模板模式", "动态模板模式", "艺术冲击模式", "质量喷涌模式", "色彩炮模式", "独特艺术模式", "大规模疯狂模式", "照片幻想模式", "仅主体模式", "固定风格模式", "代币生成器"]

subjects_display = ["全部", "物体", "动物", "人形", "风景", "概念"]

genders_display = ["全部", "男性", "女性"]

prompt_enhancers_display = ["无", "超级提示-v1"]

amountofflufflist_display = ["无", "动态", "短", "中", "长"]

artifyartists_display = ["全部", "全部 (狂野)", "流行", "greg 模式", "3D", "抽象", "棱角", "动漫", "建筑", "艺术新潮", "装饰艺术", "巴洛克", "包豪斯", "卡通", "角色", "儿童插画", "城市景观", "电影", "干净", "云景", "拼贴", "多彩", "漫画书", "立体派", "黑暗", "详细", "数字", "表现主义", "奇幻", "时尚", "野兽派", "具象主义", "血腥", "涂鸦", "平面设计", "高对比", "恐怖", "印象派", "装置", "风景", "明亮", "线条画", "低对比", "光感主义", "魔幻现实主义", "漫画", "黑色素", "凌乱", "单色", "自然", "裸体", "摄影", "波普艺术", "肖像", "原始主义", "迷幻", "现实主义", "文艺复兴", "浪漫主义", "场景", "科幻", "雕塑", "海景", "太空", "彩色玻璃", "静物", "童话现实主义", "街头艺术", "街景", "超现实主义", "象征主义", "纺织", "浮世绘", "鲜艳", "水彩", "奇幻"]

artifymodeslist_display = ["标准", "混音", "超级混音涡轮"]

artifyamountofartistslist_display = ["随机", "0", "1", "2", "3", "4", "5"]

# 子类型中文显示列表
subjectsubtypesobject_display = ["全部", "通用物体", "交通工具", "食物", "建筑", "太空", "植物"]
subjectsubtypeshumanoid_display = ["全部", "通用人类", "人类关系", "名人等", "虚构角色", "人形生物", "基于职业或头衔", "基于名字", "多个人类"]
subjectsubtypesconcept_display = ["全部", "事件", "X的Y概念", "诗歌句子", "歌曲句子", "卡牌游戏名称", "电视剧集标题", "概念混合器"]

# 创建从中文显示名到英文值的映射字典
artists_map = {
    "全部": "all",
    "全部 (狂野)": "all (wild)",
    "无": "none",
    "流行": "popular",
    "greg 模式": "greg mode",
    "3D": "3D",
    "抽象": "abstract",
    "棱角": "angular",
    "动漫": "anime",
    "建筑": "architecture",
    "艺术新潮": "art nouveau",
    "装饰艺术": "art deco",
    "巴洛克": "baroque",
    "包豪斯": "bauhaus",
    "卡通": "cartoon",
    "角色": "character",
    "儿童插画": "children's illustration",
    "城市景观": "cityscape",
    "电影": "cinema",
    "干净": "clean",
    "云景": "cloudscape",
    "拼贴": "collage",
    "多彩": "colorful",
    "漫画书": "comics",
    "立体派": "cubism",
    "黑暗": "dark",
    "详细": "detailed",
    "数字": "digital",
    "表现主义": "expressionism",
    "奇幻": "fantasy",
    "时尚": "fashion",
    "野兽派": "fauvism",
    "具象主义": "figurativism",
    "血腥": "gore",
    "涂鸦": "graffiti",
    "平面设计": "graphic design",
    "高对比": "high contrast",
    "恐怖": "horror",
    "印象派": "impressionism",
    "装置": "installation",
    "风景": "landscape",
    "明亮": "light",
    "线条画": "line drawing",
    "低对比": "low contrast",
    "光感主义": "luminism",
    "魔幻现实主义": "magical realism",
    "漫画": "manga",
    "黑色素": "melanin",
    "凌乱": "messy",
    "单色": "monochromatic",
    "自然": "nature",
    "裸体": "nudity",
    "摄影": "photography",
    "波普艺术": "pop art",
    "肖像": "portrait",
    "原始主义": "primitivism",
    "迷幻": "psychedelic",
    "现实主义": "realism",
    "文艺复兴": "renaissance",
    "浪漫主义": "romanticism",
    "场景": "scene",
    "科幻": "sci-fi",
    "雕塑": "sculpture",
    "海景": "seascape",
    "太空": "space",
    "彩色玻璃": "stained glass",
    "静物": "still life",
    "童话现实主义": "storybook realism",
    "街头艺术": "street art",
    "街景": "streetscape",
    "超现实主义": "surrealism",
    "象征主义": "symbolism",
    "纺织": "textile",
    "浮世绘": "ukiyo-e",
    "鲜艳": "vibrant",
    "水彩": "watercolor",
    "奇幻": "whimsical"
}

imagetypes_map = {
    "全部": "all",
    "全部 - 强制多重": "all - force multiple",
    "照片": "photograph",
    "八角渲染": "octane render",
    "数字艺术": "digital art",
    "概念艺术": "concept art",
    "绘画": "painting",
    "肖像": "portrait",
    "动漫关键视觉": "anime key visual",
    "仅其他类型": "only other types",
    "仅模板模式": "only templates mode",
    "动态模板模式": "dynamic templates mode",
    "艺术冲击模式": "art blaster mode",
    "质量喷涌模式": "quality vomit mode",
    "色彩炮模式": "color cannon mode",
    "独特艺术模式": "unique art mode",
    "大规模疯狂模式": "massive madness mode",
    "照片幻想模式": "photo fantasy mode",
    "仅主体模式": "subject only mode",
    "固定风格模式": "fixed styles mode",
    "代币生成器": "the tokinator"
}

subjects_map = {
    "全部": "all",
    "物体": "object",
    "动物": "animal",
    "人形": "humanoid",
    "风景": "landscape",
    "概念": "concept"
}

genders_map = {
    "全部": "all",
    "男性": "male",
    "女性": "female"
}

prompt_enhancers_map = {
    "无": "none",
    "超级提示-v1": "superprompt-v1"
}

amountofflufflist_map = {
    "无": "none",
    "动态": "dynamic",
    "短": "short",
    "中": "medium",
    "长": "long"
}

artifymodeslist_map = {
    "标准": "standard",
    "混音": "remix",
    "超级混音涡轮": "super remix turbo"
}

artifyamountofartistslist_map = {
    "随机": "random",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5"
}

# 子类型映射字典
subjectsubtypesobject_map = {
    "全部": "all",
    "通用物体": "generic objects",
    "交通工具": "vehicles",
    "食物": "food",
    "建筑": "buildings",
    "太空": "space",
    "植物": "flora"
}

subjectsubtypeshumanoid_map = {
    "全部": "all",
    "通用人类": "generic humans",
    "人类关系": "generic human relations",
    "名人等": "celebrities e.a.",
    "虚构角色": "fictional characters",
    "人形生物": "humanoids",
    "基于职业或头衔": "based on job or title",
    "基于名字": "based on first name",
    "多个人类": "multiple humans"
}

subjectsubtypesconcept_map = {
    "全部": "all",
    "事件": "event",
    "X的Y概念": "the X of Y concepts",
    "诗歌句子": "lines from poems",
    "歌曲句子": "lines from songs",
    "卡牌游戏名称": "names from card based games",
    "电视剧集标题": "episode titles from tv shows",
    "概念混合器": "concept mixer"
}
superprompterstyleslist = csv_to_list("superprompter_styles")


# Load up stuff for personal artists list, if any
# find all artist files starting with personal_artits in userfiles
script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
userfilesfolder = os.path.join(script_dir, "./userfiles/" )
for filename in os.listdir(userfilesfolder):
    if(filename.endswith(".csv") and filename.startswith("personal_artists") and filename != "personal_artists_sample.csv"):
        name = os.path.splitext(filename)[0]
        name = name.replace("_"," ",-1).lower()
        # directly insert into the artists list
        artists.insert(2, name)

# on startup, check if we have a config file, or else create it
config = load_config_csv()  


# load subjects stuff from config
generatevehicle = True
generateobject = True
generatefood = True
generatebuilding = True
generatespace = True
generateflora = True
generateanimal = True
generatemanwoman = True
generatemanwomanrelation = True
generatemanwomanmultiple = True
generatefictionalcharacter = True
generatenonfictionalcharacter = True
generatehumanoids = True
generatejob = True
generatefirstnames = True
generatelandscape = True
generateevent = True
generateconcepts = True
generatepoemline = True
generatesongline = True
generatecardname = True
generateepisodetitle = True
generateconceptmixer = True


for item in config:
        # objects
        if item[0] == 'subject_vehicle' and item[1] != 'on':
            generatevehicle = False
        if item[0] == 'subject_object' and item[1] != 'on':
            generateobject = False
        if item[0] == 'subject_food' and item[1] != 'on':
            generatefood = False
        if item[0] == 'subject_building' and item[1] != 'on':
            generatebuilding = False
        if item[0] == 'subject_space' and item[1] != 'on':
            generatespace = False
        if item[0] == 'subject_flora' and item[1] != 'on':
            generateflora = False
        # animals
        if item[0] == 'subject_animal' and item[1] != 'on':
            generateanimal = False
        # humanoids
        if item[0] == 'subject_manwoman' and item[1] != 'on':
            generatemanwoman = False
        if item[0] == 'subject_manwomanrelation' and item[1] != 'on':
            generatemanwomanrelation = False
        if item[0] == 'subject_manwomanmultiple' and item[1] != 'on':
            generatemanwomanmultiple = False
        if item[0] == 'subject_fictional' and item[1] != 'on':
            generatefictionalcharacter = False
        if item[0] == 'subject_nonfictional' and item[1] != 'on':
            generatenonfictionalcharacter = False
        if item[0] == 'subject_humanoid' and item[1] != 'on':
            generatehumanoids = False
        if item[0] == 'subject_job' and item[1] != 'on':
            generatejob = False
        if item[0] == 'subject_firstnames' and item[1] != 'on':
            generatefirstnames = False
        # landscape
        if item[0] == 'subject_landscape' and item[1] != 'on':
            generatelandscape = False
        # concept
        if item[0] == 'subject_event' and item[1] != 'on':
            generateevent = False
        if item[0] == 'subject_concept' and item[1] != 'on':
            generateconcepts = False
        if item[0] == 'subject_poemline' and item[1] != 'on':
            generatepoemline = False
        if item[0] == 'subject_songline' and item[1] != 'on':
            generatesongline = False
        if item[0] == 'subject_cardname' and item[1] != 'on':
            generatecardname = False
        if item[0] == 'subject_episodetitle' and item[1] != 'on':
            generateepisodetitle = False
        if item[0] == 'subject_conceptmixer' and item[1] != 'on':
            generateconceptmixer = False

# build up all subjects we can choose based on the loaded config file
if(generatevehicle or generateobject or generatefood or generatebuilding or generatespace):
     subjects.append("object")
if(generateanimal):
     subjects.append("animal")
if(generatemanwoman or generatemanwomanrelation or generatefictionalcharacter or generatenonfictionalcharacter or generatehumanoids or generatejob or generatemanwomanmultiple):
     subjects.append("humanoid")
if(generatelandscape):
     subjects.append("landscape")
if(generateevent or generateconcepts or generatepoemline or generatesongline or generatecardname or generateepisodetitle or generateconceptmixer):
     subjects.append("concept")


# do the same for the subtype subjects
subjectsubtypesobject = ["all"]
subjectsubtypeshumanoid = ["all"]
subjectsubtypesconcept = ["all"]

# objects first
if(generateobject):
     subjectsubtypesobject.append("generic objects")
if(generatevehicle):
     subjectsubtypesobject.append("vehicles")
if(generatefood):
     subjectsubtypesobject.append("food")
if(generatebuilding):
     subjectsubtypesobject.append("buildings")
if(generatespace):
     subjectsubtypesobject.append("space")
if(generateflora):
     subjectsubtypesobject.append("flora")

# humanoids (should I review descriptions??)
if(generatemanwoman):
     subjectsubtypeshumanoid.append("generic humans")
if(generatemanwomanrelation):
     subjectsubtypeshumanoid.append("generic human relations")
if(generatenonfictionalcharacter):
     subjectsubtypeshumanoid.append("celebrities e.a.")
if(generatefictionalcharacter):
     subjectsubtypeshumanoid.append("fictional characters")
if(generatehumanoids):
     subjectsubtypeshumanoid.append("humanoids")
if(generatejob):
     subjectsubtypeshumanoid.append("based on job or title")
if(generatefirstnames):
     subjectsubtypeshumanoid.append("based on first name")
if(generatemanwomanmultiple):
     subjectsubtypeshumanoid.append("multiple humans")

# concepts
if(generateevent):
     subjectsubtypesconcept.append("event")
if(generateconcepts):
     subjectsubtypesconcept.append("the X of Y concepts")
if(generatepoemline):
     subjectsubtypesconcept.append("lines from poems")
if(generatesongline):
     subjectsubtypesconcept.append("lines from songs")
if(generatecardname):
     subjectsubtypesconcept.append("names from card based games")
if(generateepisodetitle):
     subjectsubtypesconcept.append("episode titles from tv shows")
if(generateconceptmixer):
     subjectsubtypesconcept.append("concept mixer")
     

class OneButtonPrompt:


    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "疯狂等级": ("INT", {
                    "default": 5,
                    "min": 1, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                },
            "optional": {
                "艺术家": (artists_display, {"default": "全部"}),
                "图像类型": (imagetypes_display, {"default": "全部"}),
                "图像模式几率": ("INT", {
                    "default": 20,
                    "min": 1, #Minimum value
                    "max": 100, #Maximum value
                    "step": 1 #Slider's step
                }),
                "主体": (subjects_display, {"default": "全部"}),
                "自定义主题": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": ""
                }),
                "自定义服装": ("STRING", {
                    "multiline": False, # This is the overwrite for an outfit, super nice
                    "default": ""
                }),
                "物体子类型": (subjectsubtypesobject_display, {"default": "全部"}),
                "人物子类型": (subjectsubtypeshumanoid_display, {"default": "全部"}),
                "性别": (genders_display, {"default": "全部"}),
                "概念子类型": (subjectsubtypesconcept_display, {"default": "全部"}),
                "表情符号":(emojis, {"default": False}),
                "基础模型":(models, {"default": "SDXL"}),
                "提示增强器":(prompt_enhancers_display, {"default": "无"}),
                
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING","STRING", "STRING")
    RETURN_NAMES = ("prompt","prompt_g", "prompt_l")

    FUNCTION = "Comfy_OBP"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP(self, 疯狂等级, 自定义主题, 随机种子, 艺术家, 图像类型, 主体, 图像模式几率, 性别, 物体子类型, 人物子类型, 概念子类型, 表情符号, 自定义服装, 基础模型, 提示增强器):
        # 将中文显示名映射回英文值
        艺术家 = artists_map.get(艺术家, 艺术家)
        图像类型 = imagetypes_map.get(图像类型, 图像类型)
        主体 = subjects_map.get(主体, 主体)
        性别 = genders_map.get(性别, 性别)
        提示增强器 = prompt_enhancers_map.get(提示增强器, 提示增强器)
        物体子类型 = subjectsubtypesobject_map.get(物体子类型, 物体子类型)
        人物子类型 = subjectsubtypeshumanoid_map.get(人物子类型, 人物子类型)
        概念子类型 = subjectsubtypesconcept_map.get(概念子类型, 概念子类型)
        
        generatedpromptlist = build_dynamic_prompt(疯狂等级, 主体, 艺术家, 图像类型, False, "", "", "", 1, "", 自定义主题, True, "", 图像模式几率, 性别, 物体子类型, 人物子类型, 概念子类型, False, 表情符号, 随机种子, 自定义服装, True, 基础模型, "", 提示增强器)
        #print(generatedprompt)
        generatedprompt = generatedpromptlist[0]
        prompt_g = generatedpromptlist[1]
        prompt_l = generatedpromptlist[2]

        return (generatedprompt, prompt_g, prompt_l)


class CreatePromptVariant:


    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "原始提示": ("STRING", {"default": '', "multiline": True}),
            },
            "optional": {
                "疯狂等级": ("INT", {
                    "default": 5,
                    "min": 1, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "Comfy_OBP_PromptVariant"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP_PromptVariant(self, 原始提示, 疯狂等级, 随机种子):
        generatedprompt = createpromptvariant(原始提示, 疯狂等级)
        
        print("生成的提示词变体: " + generatedprompt)
        
        return (generatedprompt,)

# Let us create our own prompt saver. Not everyone has WAS installed
class SavePromptToFile:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "文件名前缀": ("STRING", {"default": "Prompt"}),
                "正向提示": ("STRING",{"multiline": True}),
                "负向提示": ("STRING",{"multiline": True}),
            },
            "optional": {
                "提示_g": ("STRING",{"multiline": True}),
                "提示_l": ("STRING",{"multiline": True}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = "saveprompttofile"

    CATEGORY = "一键提示"

    def saveprompttofile(self, 正向提示, 提示_g, 提示_l, 负向提示, 文件名前缀):
        # Some stuff for the prefix
        文件名前缀 += self.prefix_append

        # turns out there is some hardcoded stuff on saveimage we have to kind of repeat here
        # Find the %date:yyyy-M-d% pattern using regular expression
        pattern = r'%date:([^\%]+)%'
        match = re.search(pattern, 文件名前缀)

        if match:
            # Extract the date format from the match
            date_format = match.group(1)

            # Get the current date
            current_date = datetime.now()

            # convert the ComfyUI standard into Python standard format.
            # What a crazy way of doing this
            # first lol, I got to make sure it doesn't overlap things
            date_format = date_format.replace('M', 'X')
            date_format = date_format.replace('m', 'Z')
            
            # This is so bad

            # lets make it even worse, it work differently on windows than in Linux
            if(platform.system() == 'Windows'):

                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%#y')
                date_format = date_format.replace('X', '%#m')
                date_format = date_format.replace('d', '%#d')
                date_format = date_format.replace('h', '%#H')
                date_format = date_format.replace('Z', '%#M')
                date_format = date_format.replace('s', '%#S')
            else:
                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%-y')
                date_format = date_format.replace('X', '%-m')
                date_format = date_format.replace('d', '%-d')
                date_format = date_format.replace('h', '%-H')
                date_format = date_format.replace('Z', '%-M')
                date_format = date_format.replace('s', '%-S')


            # Format the date using the extracted format
            formatted_date = current_date.strftime(date_format)

            # Replace the matched pattern with the formatted date
            文件名前缀 = re.sub(pattern, formatted_date, 文件名前缀)
            

           

        full_output_folder, filename_short, counter, subfolder, 文件名前缀 = folder_paths.get_save_image_path(文件名前缀, self.output_dir)

        # make the filename, from from a to the first comma
        # find the index of the first comma after "of a" or end of the prompt
        if(正向提示.find("of a ") != -1):
            start_index = 正向提示.find("of a ") + len("of a ")
            end_index = 正向提示.find(",", start_index)
            if(end_index == -1):
                end_index=len(正向提示)
        else:
            start_index = 0
            end_index = 128
  
        # extract the desired substring using slicing
        filename = 正向提示[start_index:end_index]

        # cleanup some unsafe things in the filename
        filename = filename.replace("\"", "")
        filename = filename.replace("[", "")
        filename = filename.replace("|", "")
        filename = filename.replace("]", "")
        filename = filename.replace("<", "")
        filename = filename.replace(">", "")
        filename = filename.replace(":", "_")
        filename = filename.replace(".", "")
        filename = re.sub(r'[0-9]+', '', filename)

        safe_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")

        # Use regular expression to filter out any characters not in the whitelist
        filename = re.sub(r"[^{}]+".format(re.escape(''.join(safe_characters))), '', filename)
        

        if(filename==""):
            filename = str(uuid.uuid4())
        
        if(文件名前缀 == ""):
        # create a datetime object for the current date and time
        # if there is no prefix
            now = datetime.now()
            filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip() + ".txt"
        
        else:
            # lol since we insert a file, the counter of the image goes up by 1.
            # So we add 1 here, so the prompt file matches the image file
            formatted_counter = str(counter + 1).zfill(5)
            filenamecomplete = filename_short + "_" + formatted_counter + "_" + filename.replace(" ", "_").strip() + ".txt"
    
        
        directoryandfilename = os.path.abspath(os.path.join(full_output_folder, filenamecomplete))
        

        with open(directoryandfilename, 'w', encoding="utf-8") as file:
            file.write("prompt: " + 正向提示 + "\n")
            
            if(len(提示_g) > 0):
                file.write("prompt_g: " + 提示_g + "\n")
            if(len(提示_l) > 0):
                file.write("prompt_l: " + 提示_l + "\n")
            
            file.write("negative prompt: " + 负向提示 + "\n")



        return ("done")

class OneButtonPreset:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "预设": (allpresets, {"default": "Standard"}),
            },
            "optional": {
                "基础模型":(models, {"default": "SDXL"}),
                "提示增强器":(prompt_enhancers_display, {"default": "无"}),   
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }


    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "Comfy_OBP_OneButtonPreset"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP_OneButtonPreset(self, 预设, 随机种子, 基础模型, 提示增强器):
        # 将中文显示名映射回英文值
        提示增强器 = prompt_enhancers_map.get(提示增强器, 提示增强器)
        
        # load the stuff
        if(预设 == OBPresets.RANDOM_PRESET_OBP):
            selected_opb_preset = OBPresets.get_obp_preset("Standard")
        else:
            selected_opb_preset = OBPresets.get_obp_preset(预设)
        
        insanitylevel=selected_opb_preset["insanitylevel"]
        subject=selected_opb_preset["subject"]
        artist=selected_opb_preset["artist"]
        chosensubjectsubtypeobject=selected_opb_preset["chosensubjectsubtypeobject"]
        chosensubjectsubtypehumanoid=selected_opb_preset["chosensubjectsubtypehumanoid"]
        chosensubjectsubtypeconcept=selected_opb_preset["chosensubjectsubtypeconcept"]
        chosengender=selected_opb_preset["chosengender"]
        imagetype=selected_opb_preset["imagetype"]
        imagemodechance=selected_opb_preset["imagemodechance"]
        givensubject=selected_opb_preset["givensubject"]
        smartsubject=selected_opb_preset["smartsubject"]
        givenoutfit=selected_opb_preset["givenoutfit"]
        prefixprompt=selected_opb_preset["prefixprompt"]
        suffixprompt=selected_opb_preset["suffixprompt"]
        giventypeofimage=selected_opb_preset["giventypeofimage"]
        antistring=selected_opb_preset["antistring"]
        
        generatedprompt = build_dynamic_prompt(insanitylevel=insanitylevel,
                                               forcesubject=subject,
                                               artists=artist,
                                               subtypeobject=chosensubjectsubtypeobject,
                                               subtypehumanoid=chosensubjectsubtypehumanoid,
                                               subtypeconcept=chosensubjectsubtypeconcept,
                                               gender=chosengender,
                                               imagetype=imagetype,
                                               imagemodechance=imagemodechance,
                                               givensubject=givensubject,
                                               smartsubject=smartsubject,
                                               overrideoutfit=givenoutfit,
                                               prefixprompt=prefixprompt,
                                               suffixprompt=suffixprompt,
                                               giventypeofimage=giventypeofimage,
                                               antivalues=antistring,
                                               advancedprompting=False,
                                               hardturnoffemojis=True,
                                               seed=随机种子,
                                               base_model=基础模型,
                                               OBP_preset=OneButtonPreset,
                                               prompt_enhancer=提示增强器,
                                               )
        
        
        return (generatedprompt,)

class AutoNegativePrompt:


    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "正向提示": ("STRING", {"default": '', "multiline": True}),
            },
            "optional": {
                "基础负向词": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "text, watermark"
                }),
                "增强负向": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 1, #Maximum value
                    "step": 1, #Slider's step
                }),
                "疯狂等级": ("INT", {
                    "default": 0,
                    "min": 0, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                "基础模型":(models, {"default": "SDXL"}),
                
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)

    FUNCTION = "Comfy_OBP_AutoNegativePrompt"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP_AutoNegativePrompt(self, 正向提示, 疯狂等级, 增强负向, 基础负向词, 随机种子, 基础模型):
        generatedprompt = build_dynamic_negative(正向提示, 疯狂等级, 增强负向, 基础负向词, base_model=基础模型)
        
        print("生成的负向提示词: " + generatedprompt)
        
        return (generatedprompt,)
    
class OneButtonArtify:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "提示": ("STRING", {"default": '', "multiline": True}),
                "艺术家": (artifyartists_display, {"default": "全部"}),
                "艺术家数量": (artifyamountofartistslist_display, {"default": "1"}),
                "美化模式": (artifymodeslist_display, {"default": "标准"})
            },
            "optional": {                
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("artified_prompt",)

    FUNCTION = "Comfy_OBP_Artify"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP_Artify(self, 提示, 艺术家, 艺术家数量, 美化模式, 随机种子):
        # 将中文显示名映射回英文值
        艺术家 = artists_map.get(艺术家, 艺术家)
        艺术家数量 = artifyamountofartistslist_map.get(艺术家数量, 艺术家数量)
        美化模式 = artifymodeslist_map.get(美化模式, 美化模式)

        # artify here
        artified_prompt = artify_prompt(prompt=提示, artists=艺术家, amountofartists=艺术家数量, mode=美化模式, seed=随机种子)
        
        print("美化后的提示词: " + artified_prompt)
        
        return (artified_prompt,)

class OneButtonFlufferize:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "提示": ("STRING", {"default": '', "multiline": True}),
                "软化量": (amountofflufflist_display, {"default": "动态"}),
                "反向极性": (fluff_reverse_polarity, {"default": False}),
            },
            "optional": {                
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fluffed_prompt",)

    FUNCTION = "Comfy_OBP_Flufferize"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP_Flufferize(self, 提示, 软化量, 反向极性, 随机种子):
        # 将中文显示名映射回英文值
        软化量 = amountofflufflist_map.get(软化量, 软化量)
        # artify here
        fluffed_prompt = flufferizer(prompt=提示, amountoffluff=软化量, reverse_polarity=反向极性, seed=随机种子)
        
        print("润色后的提示词: " + fluffed_prompt)
        
        return (fluffed_prompt,)

class OneButtonSuperPrompt:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "提示": ("STRING", {"default": '', "multiline": True}),
                "疯狂等级": ("INT", {
                    "default": 5,
                    "min": 1, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                "超提示风格": (superprompterstyleslist, {"default": "all"}),
            },
            "optional": {                
                "随机种子": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("super_prompt",)

    FUNCTION = "Comfy_OBP_SuperPrompt"

    #OUTPUT_NODE = False

    CATEGORY = "一键提示"
    
    def Comfy_OBP_SuperPrompt(self, 疯狂等级, 提示, 超提示风格, 随机种子):

        OBPsuperprompt = one_button_superprompt(insanitylevel=疯狂等级, prompt=提示, seed=随机种子, superpromptstyle=超提示风格)
        
        print("超级提示词: " + OBPsuperprompt)
        
        return (OBPsuperprompt,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OneButtonPrompt": OneButtonPrompt,
    "OneButtonPreset": OneButtonPreset,
    "OneButtonArtify": OneButtonArtify,
    "CreatePromptVariant": CreatePromptVariant,
    "SavePromptToFile": SavePromptToFile,
    "AutoNegativePrompt": AutoNegativePrompt,
    "OneButtonFlufferize": OneButtonFlufferize,
    "OneButtonSuperPrompt": OneButtonSuperPrompt,
    
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OneButtonPrompt": "一键提示生成",
    "OneButtonPreset": "一键预设",
    "OneButtonArtify": "一键美化",
    "CreatePromptVariant": "生成提示变体",
    "SavePromptToFile": "保存提示到文件",
    "AutoNegativePrompt": "自动负向提示",
    "OneButtonFlufferize": "一键润色提示",
    "OneButtonSuperPrompt": "一键超级提示",
}