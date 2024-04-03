#include <vector>
#include <string>
#include <algorithm>

std::vector<int> digitize(unsigned long num) {
    // Convert the number to a string
    std::string numStr = std::to_string(num);

    // Create an empty vector
    std::vector<int> digitList;

    // Iterate over the string in reverse order
    for (auto it = numStr.rbegin(); it != numStr.rend(); ++it) {
        // Convert each character to an integer and append to the list
        digitList.push_back(*it - '0');
    }

    return digitList;
}