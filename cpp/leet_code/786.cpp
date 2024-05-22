/**
 * @file 786.cpp
 * @brief This file contains the implementation of a solution for a problem related to finding the Kth smallest prime fraction.
 * @details The fractions are represented as a 2D vector. Each row in the vector represents a fraction and the goal is to find the Kth smallest fraction.
 * The solution uses a binary search approach to find the Kth smallest fraction.
 */

#include <vector>

/**
 * @class Solution
 * @brief This class encapsulates the solution for the problem.
 */
class Solution {
public:

    /**
     * @brief This function calculates the Kth smallest prime fraction.
     * @param arr A reference to the vector representing the fractions.
     * @param k The index of the fraction to find.
     * @return The Kth smallest prime fraction.
     */
    static std::vector<int> kthSmallestPrimeFraction(std::vector<int>& arr, int k) {
        double low=0.0; // The lower bound for the binary search.
        double high=1.0; // The upper bound for the binary search.
        std::vector<int>ans; // The vector to store the result.
        while(low<=high){
            const double mid=low+(high-low)/2; // The middle value for the binary search.
            int num=0,den=0; // The numerator and denominator of the current fraction.
            int j=1; // The index for the inner loop.
            const int n=arr.size(); // The size of the array.
            int frac=0; // The number of fractions less than the middle value.
            double maxfrac=0; // The maximum fraction less than the middle value.
            for(int i=0;i<n;i++){
                while(j<n && arr[i]>=arr[j]*mid){
                    j++;
                }
                frac+=(n-j);
                if(j<n && maxfrac<(arr[i]*1.0)/arr[j]){
                    maxfrac=(arr[i]*1.0)/arr[j];
                    num=i;
                    den=j;
                }
            }

            // If the number of fractions less than the middle value is equal to k, return the maximum fraction.
            if(frac==k){
                return {arr[num],arr[den]};
            }
            // If the number of fractions less than the middle value is greater than k, update the upper bound.
            else if(frac>k){
                high=mid;
            }
            // If the number of fractions less than the middle value is less than k, update the lower bound.
            else{
                low=mid;
            }
        }
        return {};
    }
};
