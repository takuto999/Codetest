def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]

    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    l = 0 #先頭からの探索のインデックス
    r = len(array)-1 #末端からの探索のインデックス

    while (l <= r): #l > rとなる時に探索終了
        while (array[l] < pivot and l < len(array)-1): #配列arrayにおいてpivot以上の値を持つインデックスの値を保存
            l += 1
        while (array[r] >= pivot and l <= r): #配列arrayにおいてpivot未満の値を持つインデックスの値を保存
            r -= 1
        if l <= r:
            array[l] , array[r] = array[r] , array[l] #arrayにおけるインデックスlとrの値を交換
    
    if r < 0: #r < 0 が成り立つ時、1)array[0]が最小値である、もしくは2)arrayが昇順に並んでいる
        return array[:1] + sort(array[1:])
    else:
        return sort(array[:l]) + sort(array[l:])
    # ここまで記述

if __name__ == '__main__':
    main()