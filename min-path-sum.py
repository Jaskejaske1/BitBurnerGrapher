triangle = [
           [8],
          [1,7],
         [3,1,4],
        [5,3,3,9],
       [7,8,5,7,3],
      [5,7,4,8,8,2],
     [5,8,6,2,6,1,6],
    [2,9,2,3,6,8,8,3],
   [2,3,1,2,9,6,9,8,2],
  [5,6,2,1,2,8,1,8,5,4]
]

def min_path_sum(triangle: list[list[int]]) -> int:
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current cell with the minimum path sum
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element now contains the minimum path sum
    return triangle[0][0]

# Example usage
if __name__ == "__main__":
    result = min_path_sum(triangle)
    print(f"The minimum path sum is: {result}")