# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

for i in range(len(Prices)):
    row_sum = 0

    for j in range(len(Prices[0])):          # Loop through each element in the current row
        row_sum += Prices[i][j] * Array2[j]  # Calculate the product of the price and the corresponding quantity 
    Ans.append(row_sum)                      # Append the calculated sum for the current row to the results list  

print(Ans) 
