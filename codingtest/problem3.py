# 挑戦3 Jaccard類似度係数
# Jaccard類似度係数は集合間の類似度を検査する様々な方法の一つとして知られている。
# 二つの集合A、Bの間のジャカード類似度J(A、B)は、二つの集合の交集合サイズを二つの集合の和集合サイズで割った値と定義される。 
# 例えば、集合A={1,2,3}、集合B={2,3,4}とするとき、交集合AB={2,3}、和集合AB={1,2,3,4}となるので、集合A、B間のJaccard類似度係数J(A、B)=2/4=0.5となる。 集合A と集合B が共集合の場合には割り算が定義されないので、別にJ(A,B) = 1 と定義する。
# Jaccard類似度係数は元素の重複を許容する多重集合に対して拡張できる。 多重集合Aは元素"1"を3つ持っていて、多重集合Bは元素"1"を5つ持っているとしよう。
# この多重集合の交集合ABは元素"1"をmin(3,5)の3つ、和集合ABは元素"1"をmax(3,5)の5つ持つことになる。 
# 多重集合 A = {1,1,2,2,3}、多重集合 B = {1,1,2,4,5} とすると、交集合 A B = {1、2、2、3、4、5} となるので、Jaccard類似度係数J(A，B) = 3/7，約0.42 となる。 これを利用して文字列間の類似度を計算するのに利用できる。 
# 文字列"FRANCE"と"FRENCH"が与えられたとき、これを2文字ずつ切って多重集合を作ることができる。 
# それぞれ{FR，RA，AN，NC，CE}，{FR，RE，EN，NC､CH}となり、交集合は{FR,NC}、和集合は{FR,RA,AN,NC,CE,RE,EN,CH}となるので、二つの文字列間のJaccard類似度係数J（"FRANCE"、"FRENCH"）=2/8=0.25となる。

# 入力形式

# 入力ではstr1とstr2の2文字列が入る。 各文字列の長さは2 以上、1000 以下である。
# 入力として入ってきた文字列は2文字ずつ切って多重集合の元素にする。 
# この時、英字の文字対だけが有効で、その他の空白や数字、特殊文字が入っている場合はその文字対を捨てる。 
# 例えば、ab+が入力で入ってくると"ab"だけを多重集合の元素とし、"b+"は捨てる。
# 多重集合元素の間を比較するとき、大文字と小文字の違いは無視する。
#  「AB」と「Ab」、「ab」は同じ元素として扱う。
 
# 出力形式
# 入力で入ってきた二つの文字列のJaccard類似度係数を出力する。 
# 類似度係数の値は 0 から 1 までの実数であるため、これを扱いやすいように65536 を掛けた上で小数点以下を捨て整数部のみ出力する。

# 入出力例
# |例題 | str1 | str2 | answer |
# | -------------------------------------- | -------- | ---------------------------------- | -------------------------- |
# |1 | FRANCE |french | 16384|
# |2 |handshake |shake hands  |65536|
# |3 |aa1+aa2 |AAAA12  |43690|
# |4 |E=M*c^2 |e=m*c^2 | 65536|


# 解決方法
# 1. 与えられた文字列から、1番目2番目3番目の情報を取得する。
# 2. 点数計算方法に従い、点数の計算を行う。
# 4. 結果を出力する。

# コード作成

def solution(str1, str2):
    answer = 0
    list1 = []
    list2 = []
    intersection = []
    union = []
    for index in range(len(str1)):
        if str1[index:index+2].isalpha() and len(str1[index:index+2]) == 2:
            list1.append(str1[index:index+2].lower())

    dup_list1 = list(list1)
    for index in range(len(str2)):
        if str2[index:index+2].isalpha() and len(str2[index:index+2]) == 2:
            list2.append(str2[index:index+2].lower())
    if len(list1) == 0 and len(list2) == 0:
        answer = 1 * 65536
        print(answer)
        return
    for source in list1:
        if source in list2:
            intersection.append(source)
            list2.remove(source)

    for index in range(len(list1)):
        if dup_list1[index] in intersection:
            list1.remove(dup_list1[index])

    for source in list1:
        union.append(source)

    for source in list2:
        union.append(source)

    for source in intersection:
        union.append(source)

    answer = int(len(intersection) / len(union) * 65536)
    print(answer)
