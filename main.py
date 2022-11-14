def format_table(benchmarks, algos, results):
    table = [["Benchmark"] + benchmarks]
    for i in range(len(algos)):
        table.append([algos[i]])
        for j in range(len(benchmarks)):
            table[i+1] += [results[j][i]]
    strs = (len(benchmarks)+1)*["|"]
    for j in range(len(algos)+1):
        for i in range(len(benchmarks)+1):
            strs[i] += f" {table[j][i]: <{max([len(str(el)) for el in table[j]])}} |"
    print("\n"+strs[0])
    print(f"|{(len(strs[0])-2)*'-'}|")
    for i in range(1, len(strs)):
        print(strs[i])


if __name__ == '__main__':
    format_table(["best case", "worst case"],
                 ["quick sort", "merge sort", "bubble sort"],
                 [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    format_table(["best case", "the worst case"],
                 ["quick sort", "merge sort", "bubble sort"],
                 [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
