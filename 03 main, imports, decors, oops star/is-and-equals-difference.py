
lst1 = [1,2]
lst2 = [1,2]
lst3 = lst2

if __name__ == "__main__":
    print lst1 == lst2 #true
    print lst1 is lst2 #false
    print lst3 == lst2 #true
    print lst2 is lst3 #true