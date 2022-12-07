import multiprocessing
import time
import joblib



def grep(args):
    data_set, pattern = args
    res = []
    for data in data_set:
        data = data.lower()
        if data[0] in pattern:
            res.append(data)
    return res


def getGrepSet(data_set, pattern, num=6):
    pool = multiprocessing.Pool(num)

    new_data_set = split_arr(data_set, num)
    args = []
    for datas in new_data_set:
        args.append((datas, pattern))
    all_data = pool.map(grep, args)
    return all_data


def split_arr(arr, size):
    res = []
    internel = len(arr) // size
    for i in range(size - 1):
        tmp = arr[i * internel:(i + 1) * internel]
        res.append(tmp)
    res.append(arr[(size - 1) * internel:])

    return res

def word_count(data_set):
    dic = {}
    for datas in data_set:
        for data in datas:
            if data in dic:
                dic[data] += 1
            else:
                dic[data] = 0

    return dic


arr = ["Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs",
       "Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs",
       "Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs",
       "Agads", "adfadf", "jldalf", "dcdcs", "Agads", "adfadf", "jldalf", "dcdcs"]



pattern = "da"
split_grep_data = getGrepSet(arr, "da", 3)

save_path = pattern +'.pkl'
joblib.dump(split_grep_data, save_path)
start = time.clock()
deal_data = joblib.load(save_path)
print(word_count(split_grep_data))
time.sleep(1)
end = time.clock()

print('运行时间为：{}秒'.format(end - start))
print('运行时间为：{}毫秒'.format((end - start) * 1000))
