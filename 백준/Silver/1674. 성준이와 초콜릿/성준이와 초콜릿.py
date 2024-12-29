import sys

def process_input():
    events = []
    input = sys.stdin.read
    lines = input().splitlines()  # 한 번에 입력 처리
    for line in lines:
        parts = line.split()
        cmd, t = parts[0], int(parts[1])
        if cmd == "Query":
            events.append((t, "Query", 0))
        elif cmd == "Chocolate" and len(parts) == 3:
            events.append((t, "Chocolate", float(parts[2])))
        elif cmd == "Coffee" and len(parts) == 3:
            events.append((t, "Coffee", float(parts[2])))
    return sorted(events)  # 시간 기준으로 정렬

def binary_search(data, T):
    """T 이하의 최대 인덱스를 찾음"""
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][0] <= T:
            low = mid + 1
        else:
            high = mid - 1
    return high

def calculate_safe_distance(events):
    queries = []
    chocolates = []
    coffees = []
    results = []

    # 이벤트 분리
    for t, event_type, value in events:
        if event_type == "Query":
            queries.append((t, len(queries)))
        elif event_type == "Chocolate":
            chocolates.append((t, value))
        elif event_type == "Coffee":
            coffees.append((t, value))

    # Query 처리
    for T, order in queries:
        safe_distance = 0.0

        # 초콜릿 효과 계산
        chocolate_idx = binary_search(chocolates, T)
        if chocolate_idx >= 0:
            for i in range(chocolate_idx + 1):
                t, n = chocolates[i]
                safe_distance += max(0, 8 * n - (T - t) / 12)

        # 커피 효과 계산
        coffee_idx = binary_search(coffees, T)
        if coffee_idx >= 0:
            for i in range(coffee_idx + 1):
                t, n = coffees[i]
                safe_distance += max(0, 2 * n - (T - t) ** 2 / 79)

        # 최소 안전 거리 적용
        safe_distance = max(1.0, round(safe_distance, 1))
        results.append((T, safe_distance, order))

    return sorted(results, key=lambda x: x[2])

# 메인 실행
events = process_input()
results = calculate_safe_distance(events)
for T, R, _ in results:
    print(f"{T} {R:.1f}")