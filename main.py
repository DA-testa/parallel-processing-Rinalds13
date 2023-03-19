# python3

def parallel_processing(n, m, data):
    izvade = [(0, k) for k in range(n)]
    rez = []
    for t in data:
        min_beigu_laiks = float('inf')
        izvades_index = None
        for k, (beigu_laiks, index) in enumerate(izvade):
            if beigu_laiks < min_beigu_laiks:
                min_beigu_laiks = beigu_laiks
                izvades_index = k
        rez.append((izvades_index, min_beigu_laiks))
        izvade[izvades_index] = (min_beigu_laiks + t, izvades_index)
    return rez

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    rez = parallel_processing(n, m, data)
    
    for k in range(m):
        print(rez[k][0], rez[k][1])

if __name__ == "__main__":
    main()
