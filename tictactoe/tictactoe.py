area = ["1.1", "1.2", "1.3", "2.1", "2.2", "2.3", "3.1", "3.2", "3.3"]
a = f"| {area[0]} | {area[1]} | {area[2]} |" \
    f"\n| {area[3]} | {area[4]} | {area[5]} |" \
    f"\n| {area[6]} | {area[7]} | {area[8]} |"
print(a)
life = 0
while True:

    coordinates_x = area.index(str(input("Enter coordinates X\n>")))
    area[coordinates_x] = " X "
    a = f"| {area[0]} | {area[1]} | {area[2]} |" \
        f"\n| {area[3]} | {area[4]} | {area[5]} |" \
        f"\n| {area[6]} | {area[7]} | {area[8]} |"
    print(a)

    coordinates_o = area.index(str(input("Enter coordinates 0\n>")))
    area[coordinates_o] = " 0 "
    a = f"| {area[0]} | {area[1]} | {area[2]} |" \
        f"\n| {area[3]} | {area[4]} | {area[5]} |" \
        f"\n| {area[6]} | {area[7]} | {area[8]} |"
    print(a)
