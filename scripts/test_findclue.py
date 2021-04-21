from aw import common
from model import Model
import pytest

# 从lo文件中匹配关键字
wordlist = common.logKeywordExist(Model.pattern, '%siphone.log'%Model.logdirpath)

# level_complete关卡  --需要根据实际通关关卡来设定相关参数
testlist = common.keywordLogZip(wordlist,Model.level_enter,5)+\
           common.keywordLogZip(wordlist,Model.level_complete,3)+\
           common.keywordLogZip(wordlist,Model.question_id,6)+\
           common.keywordLogZip(wordlist,Model.reward_btn_show,2,0)+\
           common.keywordLogZip(wordlist,Model.reward_btn_click,2,0)+\
           common.keywordListLogZip(wordlist,Model.scene)


@pytest.mark.parametrize('wordlist,keyword',testlist)
def test_findclue(wordlist,keyword):
    # 游戏level打点信息
    assert keyword in wordlist

