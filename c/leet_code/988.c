void reverseInPlace(char *s, int len) {
    int i = 0, j = len - 1;
    while (i < j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;
        j--;
    }
}

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

char *smallestFromLeaf(struct TreeNode *root) {
    char *smallest = NULL;
    char path[1000];

    Finder(root, path, 0, &smallest);

    return smallest;
}
