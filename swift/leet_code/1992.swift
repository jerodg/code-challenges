class Solution {
    func findFarmland(_ land: [[Int]]) -> [[Int]] {
        let (rows, cols) = (land.count, land[0].count)
        var land = land, result = [[Int]]()
        for y in 0 ..< rows {
            for x in 0 ..< cols where land[y][x] == 1 {
                var (right, bottom) = (x, y)
                while right < cols - 1, land[y][right + 1] == 1 {
                    right += 1
                }
                while bottom < rows - 1, land[bottom + 1][x] == 1 {
                    bottom += 1
                }
                for j in y ... bottom {
                    for i in x ... right {
                        land[j][i] = 0
                    }
                }
                result.append([y, x, bottom, right])
            }
        }
        return result
    }
}
