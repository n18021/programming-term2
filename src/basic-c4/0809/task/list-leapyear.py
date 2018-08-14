year = [
    "アホ" if i % 3==0 else "アホ"
           if i // 10==3 else str(i)
    for i in range(1, 41)]
print("\n".join(year))

