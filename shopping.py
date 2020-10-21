# Brittany Sundberg
# CS 325 HW 3 Fall 2020


infile = open('shopping.txt', 'r')
with open('results.txt', 'w') as outfile:
    num_tests = int(infile.readline())
    for i in range(num_tests):
        test_case_num = i+1
        num_items = int(infile.readline())
        Prices = [0] * num_items
        Weight = [0] * num_items
        for j in range(0, num_items):
            line = infile.readline().strip()
            list = line.split()
            for k in range(0, len(list)):
                list[k] = int(list[k])
            Prices[j] = list[0]
            Weight[j] = list[1]
        num_people = int(infile.readline())
        total_for_family = 0
        People = [0] * num_people
        for l in range(0, num_people):
            cap = int(infile.readline())
            People[l] = cap
        print("Test Case # ", test_case_num)
        string_out = "Test Case # "
        string_out += str(test_case_num)
        outfile.write(string_out)
        outfile.write('\n')
        print("Number of Items Available = ", num_items)
        print("Prices of the items are ", Prices)
        print("Weights of the items are ", Weight)
        print("Number of People in the Family= ", num_people)
        print("Weights that each person in the family can carry = ", People)

        for x in range(0, len(People)):
            table = [[0] * (num_items+1) for _ in range(People[x]+1)]
            for p in range(1, num_items+1):
                for w in range(1, People[x]+1):
                    if Weight[p-1] <= w:  #if it’s not too heavy for us to take
                        if Prices[p-1] + table[w-Weight[p-1]][p-1] > table[w][p-1]:
                            table[w][p] = Prices[p-1] + table[w-Weight[p-1]][p-1]
                        else:
                            table[w][p] = table[w][p-1]
                    else:  #if it is too heavy for us to take
                        table[w][p] = table[w][p-1]

            total_price = table[People[x]][num_items]
            total_for_family += total_price
            used_items = []
            n = num_items
            c = People[x]
            while c > 0 and n > 0:
                while n > 0 and table[c][n] == table[c][n-1]: #means current item n is not included in bag
                    n -= 1
                #when the while loop stops, we’re at an item that was included in the bag. We know item n was used, so add it to used_items array (but +1 because indexing begins at 0). Then use n to find weight in Weight array and subtract from capacity to continue backtracking.
                if n != 0:
                    used_items.append(n)
                n -= 1
                c -= Weight[n-1]
            print("items for person ", x+1, " to take = ", used_items)
            string_out = "Items for person "
            string_out += str(x+1)
            string_out += " to take = "
            for element in used_items:
                string_out += str(element)
                string_out += " "
            outfile.write(string_out)
            outfile.write('\n')
        print("Total Price for All Family Members = ", total_for_family)
        string_out = "Total Price for all Family Members' Items = "
        string_out += str(total_for_family)
        outfile.write(string_out)
        outfile.write('\n')
        outfile.write('------------------------------------')
        outfile.write('\n')


