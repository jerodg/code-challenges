/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
    const sMap = new Map();
    const tMap = new Map();
    for (let i = 0; i < s.length; i++) {
        if (sMap.has(s[i]) && sMap.get(s[i]) !== t[i]) {
            return false;
        }
        if (tMap.has(t[i]) && tMap.get(t[i]) !== s[i]) {
            return false;
        }
        sMap.set(s[i], t[i]);
        tMap.set(t[i], s[i]);
    }
    return true;
};
