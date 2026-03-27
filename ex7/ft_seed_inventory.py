def ft_seed_inventory(vgb, count, packet):
    if packet == "packets":
        print(vgb, "seeds:", count, "packets available")
    if packet == "grams":
        print(vgb, "seeds:", count, "grams total")
    if packet == "area":
        print(vgb, "seeds:", "covers", count, "square meters")


ft_seed_inventory("carrot", 8, "grams")
