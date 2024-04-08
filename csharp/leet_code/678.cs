public class Solution {
    public bool CheckValidString(string s) {
        int low = 0;
        int high = 0;
        foreach(char c in s){
            if(c == '('){
                low++;
                high++;
            }else if(c == ')'){
                low = Math.Max(low - 1, 0);
                high--;
                if(high < 0){
                    return false;
                }
            }else{
                low = Math.Max(low - 1, 0);
                high++;
            }
        }
        return low == 0;
    }
}