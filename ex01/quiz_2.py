import random
import datetime

def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題 : " + qa["q"])
    return qa["a"]

def kaitou(ams_lst):
    st = datetime.datetime.now()
    ans = input("答えるんだ : ")
    ed = datetime.datetime.now()
    if ans in ans_lst:
        print("せいかーーーーい")
    else:
        print("ぶぶー")
    
    print("解答機関: + (ed-st)秒" )

if __name__ == "__main__":
    qa_lst =[
        {"q" : "さざえのだんなさんは？","a":["マスオ","ますお"]},
        {"q" : "かつおのいもうとは?","a":["ワカメ","わかめ"]},
        {"q":"たらおとかつおはなに","a":["おい","甥","甥っ子","おいっこ"]}
    ]
    ans_lst = shutudai(qa_lst)
    kaitou(ans_lst)