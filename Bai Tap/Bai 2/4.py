def in_nghich_dao(a, b):
    print(f"Nghịch đảo các số tự nhiên trong khoảng ({a}, {b}):")
    for i in range(a + 1, b):
        nghich_dao = 1 / i
        print(nghich_dao)

in_nghich_dao(2, 6)
