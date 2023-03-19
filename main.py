# python3
import heapq

def parallel_processing(n, m, data):
    izvade = []
    brivie = [(0, i) for i in range(n)]
    heapq.heapify(brivie)
    beigu_laiks = [0] * m
    for i in range(m):
        t_sakuma_laiks, index = heapq.heappop(brivie)
        darba_ilgums = data[i]
        sakuma_laiks = max(t_sakuma_laiks, beigu_laiks[i-1])
        beigu_laiks = sakuma_laiks + darba_ilgums
        izvade.append((index, sakuma_laiks))
        beigu_laiks[i] = beigu_laiks
        heapq.heappush(brivie, (beigu_laiks, index))
    return izvade


def main():
    n, m = map(int, input().split())
    dati = list(map(int, input().split()))
    rezultati = parallel_processing(n, m, dati)
    for index, sakuma_laiks in rezultati:
        print(index, sakuma_laiks)

if __name__ == "__main__":
    main()
