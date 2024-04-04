class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        var sMap = [Character: Character]()
        var tMap = [Character: Character]()

        for (sChar, tChar) in zip(s, t) {
            if let sValue = sMap[sChar], sValue != tChar {
                return false
            }
            if let tValue = tMap[tChar], tValue != sChar {
                return false
            }
            sMap[sChar] = tChar
            tMap[tChar] = sChar
        }

        return true
    }
}