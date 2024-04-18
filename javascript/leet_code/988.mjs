/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string}
 */
const dfs = function (node, path) {
    if (!node) return '';

    path += String.fromCharCode(node.val + 97);
    if (!node.left && !node.right) {
        return path.split('').reverse().join('');
    }
    const left = dfs(node.left, path);
    const right = dfs(node.right, path);
    return left < right ? left : right;
};

const smallestFromLeaf = function (root) {
    const dfs = (node, path) => {
        if (!node) return '';
        path += String.fromCharCode(node.val + 97);
        if (!node.left && !node.right) {
            return path.split('').reverse().join('');
        }
        const left = dfs(node.left, path);
        const right = dfs(node.right, path);
        return left < right ? left : right;
    };

    return dfs(root, '');
};
