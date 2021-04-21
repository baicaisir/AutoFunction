# log文件夹路径
logdirpath = 'D:/02_project/AutoFunction/log/'

# all游戏关卡打点信息匹配规则
pattern = r'level_complete level_id:\d*|level_enter level_id:\d*|reward_btn_.* ad_ready:\d*|question_id:\d+|scene:scene_.*|level_complete level_id:\d*|revive_opportunity.*|revive level_id:'

#进入关卡
level_enter = 'level_enter level_id:'
# 关口结算
level_complete = 'level_complete level_id:'
# 问题关卡
question_id = 'question_id:'
# 激励广告是否展示：0/1
reward_btn_show = 'reward_btn_show ad_ready:'
# 复活机会
revive_opportunity = 'revive_opportunity level_id:'
# 复活
revive = 'revive level_id:'

# 激励打点
# 激励按钮展示--0/1
reward_btn_show = 'reward_btn_show ad_ready:'
# 激励按钮点击
reward_btn_click = 'reward_btn_click ad_ready:'
# 激励广告展示
reward_ad_show = 'reward_ad_show'

# 插屏/banner需要展示时
int_opportunity = 'int_opportunity'

# 提示
scene = ['scene:scene_hint','scene:scene_skip','scene:scene_special_level_unlock']


