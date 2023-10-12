# 挑戦2 ダーツゲーム
# ダーツゲームはダーツ板にダーツを3回投げてその点数の合計で実力を競うゲームで、皆が簡単に楽しめる。
# ダーツゲームの点数計算ロジックは以下の通りである。

# 1. ダーツゲームは計3回のチャンスで構成される
# 2. 各機会ごとに得られる点数は0点から10点までだ。
# 3. 点数と共にSingle(S)、Double(D)、Triple(T)領域が存在し、各領域当選時に点数で1乗、2乗、3乗(\^1、\^2、\^3)で計算される。
# 4. オプションで、スター賞(*)、アチャ賞(#)が存在し、スター賞(*)当選時に該当点数と直前に得た点数を2倍にする。 峨嵯賞当選時、該当点数はマイナスになる。
# 5. スター賞は1回目のチャンスでも出ることが。 この場合は最初の点数のみ2倍にする
# 6. スター賞の効果は、以前のスター賞の効果と重なることができる。 この場合は重畳したスター像は4倍になる。
# 7. スター像の効果は、峨嵯像の効果と重なることができる。 この場合は重畳した峨嵯像は-2 倍になる。
# 8. Single(S)、Double(D)、Triple(T)は点数ごとに一つずつ存在する。
# 9. スター賞、アチャ賞は点数ごとに二つのうち一つだけ存在することができ、存在しないこともある。

# 0~10の整数と文字S、D、T、*、#で構成された文字列が入力された時、総点数を返す関数を作成せよ。

# 入力形式
# "スコア|ボーナス|[オプション]"で構成される文字列3セット
# 例）1S2D*3T

# 点数は0から10の間の整数である。
# ボーナスはS、D、Tのいずれかである。
# オプションは*か#のいずれかであり、ない場合もある。

# 出力形式
# 3 回の機会で得られた点数の合計に相当する整数値を出力する。


# 入出力例
# |例題 | dartResult | answer | 説明 |
# | -------------------------------------- | -------- | ---------------------------------- | -------------------------- |
# |1 | 1S2D*3T |37 | 1^1 * 2 + 2^2 * 2 + 3^3|
# |2 |1D2S#10S |9  |1^2 + 2^1 * (-1) + 10^1|
# |3 |1D2S0T |3  |1^2 + 2^1 + 0^3|
# |4 |1S*2T*3S |23 | 1^1 * 2 * 2 + 2^3 * 2 + 3^1|
# |5 |1D#2S3S |5 | 1^2 * (-1) + 2^1 + 3^1|
# |6 |1T2D3D# |-4 | 1^3 + 2^2 + 3^2 * (-1)|
# |7 |1D2S3T* |59 | 1^2 + 2^1 * 2 + 3^3 * 2|


# 解決方法
# 1. 与えられた文字列から、1番目2番目3番目の情報を取得する。
# 2. 点数計算方法に従い、点数の計算を行う。
# 4. 結果を出力する。

# コード作成

def solution(dartResult):
    first = ""
    second = ""
    third = ""
    first_score = 0
    second_score = 0
    third_score = 0
    index = 0
    group = 1
    score = 0
    multiple = ""
    special = ""
    for s in dartResult:
        if group == 1:
            first = first + dartResult[index]
        elif group == 2:
            second = second + dartResult[index]
        elif group == 3:
            third = third + dartResult[index]
        if dartResult[index] in "SDT":
            if len(dartResult) > index+1 and dartResult[index+1] in "*#":
                if group == 1:
                    first = first + dartResult[index+1]
                elif group == 2:
                    second = second + dartResult[index+1]
                elif group == 3:
                    third = third + dartResult[index+1]
                index = index + 1
            group = group + 1
        if group == 4:
            break
        index = index + 1
    if len(first) == 4:
        score = int(first[0:2])
        multiple = first[2]
        special = first[3]
    elif len(first) == 3:
        if first[2] in "*#":
            score = int(first[0])
            multiple = first[1]
            special = first[2]
        else:
            score = int(first[0:2])
            multiple = first[2]
    else:
        score = int(first[0])
        multiple = first[1]
        special = ""
    if multiple == "S":
        score = score ** 1
    elif multiple == "D":
        score = score ** 2
    elif multiple == "T":
        score = score ** 3
    if special == "*":
        score = score * 2
    elif special == "#":
        score = score * -1
    first_score = score

    score = 0
    multiple = ""
    special = ""
    if len(second) == 4:
        score = int(second[0:2])
        multiple = second[2]
        special = second[3]
    elif len(second) == 3:
        if second[2] in "*#":
            score = int(second[0])
            multiple = second[1]
            special = second[2]
        else:
            score = int(second[0:2])
            multiple = second[2]
    else:
        score = int(second[0])
        multiple = second[1]
        special = ""
    if multiple == "S":
        score = score ** 1
    elif multiple == "D":
        score = score ** 2
    elif multiple == "T":
        score = score ** 3
    if special == "*":
        score = score * 2
        first_score = first_score * 2
    elif special == "#":
        score = score * -1
    second_score = score

    score = 0
    multiple = ""
    special = ""
    if len(third) == 4:
        score = int(third[0:2])
        multiple = third[2]
        special = third[3]
    elif len(third) == 3:
        if third[2] in "*#":
            score = int(third[0])
            multiple = third[1]
            special = third[2]
        else:
            score = int(third[0:2])
            multiple = third[2]
    else:
        score = int(third[0])
        multiple = third[1]
        special = ""
    if multiple == "S":
        score = score ** 1
    elif multiple == "D":
        score = score ** 2
    elif multiple == "T":
        score = score ** 3
    if special == "*":
        score = score * 2
        second_score = second_score * 2
    elif special == "#":
        score = score * -1
    third_score = score
    print(first_score + second_score + third_score)
