import os


# AutoFunction根目录
class Model:
    basepath, _ = os.getcwd().split('AutoFunction')

    # 日志截图位置
    logscreen = basepath + 'AutoFunction/report/assets/'

    # log文件夹路径
    logdirpath = basepath + 'AutoFunction/resource/logs/'
    firebaselog = logdirpath + 'firebase.log'
    proxypath = basepath + 'AutoFunction/resource/adproxy.py'
    # all游戏关卡打点信息匹配规则
    pattern = r'level_complete level_id:\d*|level_enter level_id:\d*|reward_btn_.* ad_ready:\d*|question_id:\d+|scene:scene_.*|level_complete level_id:\d*|revive_opportunity.*|revive level_id:'

    # 进入关卡
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
    # reward_btn_show = 'reward_btn_show ad_ready:'
    # 激励按钮点击
    reward_btn_click = 'reward_btn_click ad_ready:'
    # 激励广告展示
    reward_ad_show = 'reward_ad_show'

    # 插屏/banner需要展示时
    int_opportunity = 'int_opportunity'

    # 提示
    scene = ['scene:scene_hint', 'scene:scene_skip', 'scene:scene_special_level_unlock']

    '''
    firebase打点信息正则匹配规则
    '''
    firebasebannerpattern = r'Event:nox_sdk_request parameters:{[\d\D]*?"mediation_name" = Noxmobi[\d\D]*?"placement_type" = 4[\d\D]*?}'

    # nox_sdk_waterfall_request瀑布流打点
    banner_nox_sdk_waterfall_request = r'vent:nox_sdk_waterfall_request parameters:{[\d\D]*?placement_type" = 4[\d\D]*?}'
    int_nox_sdk_waterfall_request = r'vent:nox_sdk_waterfall_request parameters:{[\d\D]*?placement_type" = 5[\d\D]*?}'
    reward_nox_sdk_waterfall_request = r'vent:nox_sdk_waterfall_request parameters:{[\d\D]*?placement_type" = 3[\d\D]*?}'

    # nox展示打点
    banner_nox_sdk_show = r'Event:nox_sdk_show parameters:{[\d\D]*?"placement_type" = 4[\d\D]*?}'
    int_nox_sdk_show = r'Event:nox_sdk_show parameters:{[\d\D]*?"placement_type" = 5[\d\D]*?}'
    reward_nox_sdk_show = r'Event:nox_sdk_show parameters:{[\d\D]*?"placement_type" = 3[\d\D]*?}'

    # nox_sdk_request 请求打点
    banner_nox_sdk_request = r'Event:nox_sdk_request parameters:{[\d\D]*?mediation_name" = Noxmobi[\d\D]*?placement_type" = 4[\d\D]*?}'
    int_nox_sdk_request = r'Event:nox_sdk_request parameters:{[\d\D]*?mediation_name" = Noxmobi[\d\D]*?placement_type" = 5[\d\D]*?}'
    reward_nox_sdk_request = r'Event:nox_sdk_request parameters:{[\d\D]*?mediation_name" = Noxmobi[\d\D]*?placement_type" = 3[\d\D]*?}'

    # nox_sdk_click 点击跳转打点
    banner_nox_sdk_click = r'Event:nox_sdk_click parameters:{[\d\D]*?placement_type" = 4[\d\D]*?}'
    int_nox_sdk_click = r'Event:nox_sdk_click parameters:{[\d\D]*?placement_type" = 5[\d\D]*?}'
    reward_nox_sdk_click = r'Event:nox_sdk_click parameters:{[\d\D]*?placement_type" = 3[\d\D]*?}'

    # nox_sdk_third_ad_info  从三方获取的广告
    banner_nox_sdk_third_ad_info = r'Event:nox_sdk_third_ad_info parameters:{[\d\D]*?ad_format" = 4[\d\D]*?}'
    int_nox_sdk_third_ad_info = r'Event:nox_sdk_third_ad_info parameters:{[\d\D]*?ad_format" = 5[\d\D]*?}'
    reward_nox_sdk_third_ad_info = r'Event:nox_sdk_third_ad_info parameters:{[\d\D]*?ad_format" = 3[\d\D]*?}'

    # third mediation firebase 打点
    # 请求配置
    banner_nox_sdk_request_config = r'Event:nox_sdk_request_config parameters:{[\d\D]*?placement_type" = 4[\d\D]*?}'
    int_nox_sdk_request_config = r'Event:nox_sdk_request_config parameters:{[\d\D]*?placement_type" = 5[\d\D]*?}'
    reward_nox_sdk_request_config = r'Event:nox_sdk_request_config parameters:{[\d\D]*?placement_type" = 3[\d\D]*?}'

    # sdk发起的一次广告请求
    banner_third_mediation_request = r'Event:third_mediation_request parameters:{[\d\D]*?ad_sdk_placement_type" = 4[\d\D]*?}'
    int_third_mediation_request = r'Event:third_mediation_request parameters:{[\d\D]*?ad_sdk_placement_type" = 5[\d\D]*?}'
    reward_third_mediation_request = r'Event:third_mediation_request parameters:{[\d\D]*?ad_sdk_placement_type" = 3[\d\D]*?}'

    # third_mediation_show 广告展示
    banner_third_mediation_show = r'Event:third_mediation_show parameters:{[\d\D]*?ad_sdk_placement_type" = 4[\d\D]*?}'
    int_third_mediation_show = r'Event:third_mediation_show parameters:{[\d\D]*?ad_sdk_placement_type" = 5[\d\D]*?}'
    reward_third_mediation_show = r'Event:third_mediation_show parameters:{[\d\D]*?ad_sdk_placement_type" = 3[\d\D]*?}'

    # third_mediation_click  广告点击
    banner_third_mediation_click = r'Event:third_mediation_click parameters:{[\d\D]*?ad_sdk_placement_type" = 4[\d\D]*?}'
    int_third_mediation_click = r'Event:third_mediation_click parameters:{[\d\D]*?ad_sdk_placement_type" = 5[\d\D]*?}'
    reward_third_mediation_click = r'Event:third_mediation_click parameters:{[\d\D]*?ad_sdk_placement_type" = 3[\d\D]*?}'

    # third_mediation_close 广告关闭打点
    banner_third_mediation_close = r'Event:third_mediation_close parameters:{[\d\D]*?ad_sdk_placement_type" = 4[\d\D]*?}'
    int_third_mediation_close = r'Event:third_mediation_close parameters:{[\d\D]*?ad_sdk_placement_type" = 5[\d\D]*?}'
    reward_third_mediation_close = r'Event:third_mediation_close parameters:{[\d\D]*?ad_sdk_placement_type" = 3[\d\D]*?}'

    # third_mediation_banner_auto_refresh Max banner自动刷新时打点
    third_mediation_banner_auto_refresh = r'Event:third_mediation_banner_auto_refresh parameters:{[\d\D]*?ad_sdk_placement_type" = 4[\d\D]*?}'

    #展示失败信息
    nox_sdk_request_config_failed = r'config_req_fail_msg.*'
    nox_sdk_waterfall_request_failed = r'mediation_req_err_msg.*'