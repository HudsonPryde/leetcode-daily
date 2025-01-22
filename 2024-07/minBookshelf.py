from typing import List


def minHeightShelvesTopDown(books: List[List[int]], shelfWidth: int) -> int:
    # book: [width, height]
    n = len(books)
    dp = [[0 for _ in range(shelfWidth+1)] for _ in range(n)]
    def placeBook(i, height, width):
        book = books[i]
        max_height = max(height, book[1])
        if i == n-1:
            if width >= book[0]:
                return max_height
            else:
                return height + book[1]
        if dp[i][width] != 0:
            return dp[i][width]
        new_shelf = height + placeBook(i+1, book[1], shelfWidth-book[0])
        if width >= book[0]:
            same_shelf = placeBook(i+1, max_height, width-book[0])
            dp[i][width] = min(new_shelf, same_shelf)
            return dp[i][width]
        dp[i][width] = new_shelf
        return dp[i][width]
    return placeBook(0, 0, shelfWidth)

# bottom up
def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
    # book: [width, height]
    n = len(books)
    dp = [0]*(n+1)
    dp[1] = books[0][1]
    for i in range(2, n+1):
        width = shelfWidth - books[i-1][0]
        max_height = books[i-1][1]
        dp[i] = books[i-1][1] + dp[i-1]
        j = i-1
        while j > 0 and width - books[j-1][0] >= 0:
            max_height = max(max_height, books[j-1][1])
            width -= books[j-1][0]
            
            j-=1
        dp[i] = min(dp[i], max_height+dp[j])
    return dp[-1]

print(minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
print(minHeightShelves([[1,3],[2,4],[3,2]], 6))
print(minHeightShelves([[7,3],[8,7],[2,7],[2,5]], 10))
        
        


