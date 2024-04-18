#include <stdlib.h>  // for free and strdup
#include <string.h>  // for strcmp

/**
 * Reverses a string in place.
 *
 * @param s The string to be reversed.
 * @param len The length of the string.
 */
void reverseInPlace(char *s, const int len) {
    int i = 0, j = len - 1;
    while (i < j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;
        j--;
    }
}

/**
 * Recursive function to find the smallest lexicographical string from leaf to root in a binary tree.
 *
 * @param root The root of the binary tree.
 * @param path The current path from root to leaf.
 * @param depth The current depth in the tree.
 * @param smallest The smallest lexicographical string found so far.
 */
void Finder(struct TreeNode *root, char *path, int depth, char **smallest) {
    if (root == NULL) {
        return;
    }
    path[depth] = root->val + 'a';

    if (!root->left && !root->right) {
        path[depth + 1] = '\0';
        reverseInPlace(path, depth + 1);
        if (*smallest == NULL || strcmp(path, *smallest) < 0) {
            if (*smallest != NULL) {
                free(*smallest);
            }
            *smallest = strdup(path);
        }
        reverseInPlace(path, depth + 1);
    }
    Finder(root->left, path, depth + 1, smallest);
    Finder(root->right, path, depth + 1, smallest);
}

/**
 * Returns the smallest lexicographical string from leaf to root in a binary tree.
 *
 * @param root The root of the binary tree.
 * @return The smallest lexicographical string from leaf to root.
 */
char *smallestFromLeaf(struct TreeNode *root) {
    char *smallest = NULL;
    char path[1000];

    Finder(root, path, 0, &smallest);

    return smallest;
}
