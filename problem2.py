def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    l = 0 #探索区間の左端
    r = len(sorted_array) #探索区間の右端

    flag = 0 #sorted_array内にtarget_numberが含まれている時に立つフラグ
    while (l <= r): #l > rとなった時に探索終了
        m = int((l+r)/2) #探索区間中間のインデックス

        if sorted_array[m] == target_number: #mが求めるインデックスであり、探索終了
            target_index = m
            flag = 1
            break
        elif sorted_array[m] < target_number: #target_numberが存在するならばそのインデックスはmより大きい
            l = m+1 #区間を[m+1,r]に縮小
        else: #target_numberが存在するならばそのインデックスはmより小さい
            r = m-1 #区間を[l,m-1]縮小

        if l == r: #l==rの場合、sorted_array[l]がtarget_numberならlが求めるインデックスであり、そうでないならsorted_arrayにtarget_numberは含まれない
            if sorted_array[l] == target_number:
                target_index = l
                flag = 1
                break
            else: 
                break
    
    if flag==1:
        return target_index
    #ここまでを記述

    # 探索対象が存在しない場合、-1を返却
    return -1
    

if __name__ == '__main__':
    main()