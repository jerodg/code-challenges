// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")

// Including necessary libraries.
#include <array>
#include <bitset>
#include <fstream>
#include <ios>
#include <iostream>
#include <vector>

// Booster function to speed up cin and cout.
static const bool booster = []() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();

// Directions for DFS.
constexpr int d[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

// Grid to store the map and visited to keep track of visited cells.
static std::array<std::bitset<300>, 300> grid;
static std::array<std::bitset<300>, 300> visited;

// Variables to store the number of rows and columns in the grid.
static int rows;
static int cols;

/**
 * Parses the input data string and populates the grid and visited arrays.
 *
 * @param s The input data string.
 */
void parse_input_data_string(const std::string &s) {
    const int n = s.size();
    rows = 0;
    cols = 0;

    int col = 0;
    for (int i = 1; i < n - 1; ++i) {
        switch (s[i]) {
            case '[':
                col = 0;
                break;
            case ']':
                cols = col;
                ++rows;
                break;
            case '0':
                grid[rows].reset(col);
                ++col;
                break;
            case '1':
                grid[rows].set(col);
                ++col;
                break;
            default: ;
        }
    }
    for (int i = 0; i < rows; ++i) {
        visited[i].reset();
    }
}

/**
 * Visits an island using DFS.
 *
 * @param i The row index of the current cell.
 * @param j The column index of the current cell.
 */
void visit_island(const int i, const int j) {
    if (grid[i][j] == 0 || visited[i][j] == 1) {
        return;
    }
    visited[i][j] = true;
    for (int k = 0; k < 4; ++k) {
        const int in = i + d[k][1];
        if (const int jn = j + d[k][0]; in >= 0 && in < rows && jn >= 0 && jn < cols) {
            visit_island(in, jn);
        }
    }
}

/**
 * Counts the number of islands in the grid.
 *
 * @return The number of islands.
 */
int num_islands() {
    int res = 0;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 0 || visited[i][j] == 1) {
                continue;
            }
            visit_island(i, j);
            res++;
        }
    }
    return res;
}

// Solving the problem and writing the output to a file.
bool solve = []() {
    std::ofstream out("user.out");
    for (std::string s; std::getline(std::cin, s);) {
        parse_input_data_string(s);
        out << num_islands() << "\n";
    }
    out.flush();
    exit(0);
    return true;
}();

/**
 * Solution class for the problem.
 */
class Solution {
public:
    /**
     * Counts the number of islands in the given grid.
     *
     * @param grid The grid of cells.
     * @return The number of islands.
     */
    static int numIslands(std::vector<std::vector<char> > &grid) {
        return 0;
    }
};
