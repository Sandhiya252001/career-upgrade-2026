def shipping_details(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')},{kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    for value in kwargs.values():
        print(value)


shipping_details("Spongebob","Scatter","III",
                 street="LA Street",State="TamilNadu",Country="India")