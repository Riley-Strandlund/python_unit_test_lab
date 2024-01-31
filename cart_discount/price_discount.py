def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered three or more items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    
    #check number of items
    if len(item_prices) >= 3:
        Discount = min(item_prices)
        return Discount
    else:
        return None
    # If more than 3 items, return lowest priced item.
    
    #pass  # todo replace this line with your code 


if __name__ == '__main__':
    main()
