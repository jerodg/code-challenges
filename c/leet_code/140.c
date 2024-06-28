/**
* Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see SSPL.
 */

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#define MAX_WORD_LENGTH 10
#define MAX_SENTENCES 1000
#define MAX_SENTENCE_LENGTH 1000

/**
 * @file 140.c
 * @brief This file contains the implementation of the word breaking problem.
 */

/**
 * @brief This array stores the final answers.
 */
char ans[MAX_SENTENCES][MAX_SENTENCE_LENGTH];

/**
 * @brief This function checks if a word exists in the dictionary or not.
 *
 * @param word The word to check.
 * @param word_dict The dictionary of words.
 * @param word_dict_size The size of the dictionary.
 * @return true if the word exists in the dictionary, false otherwise.
 */
bool does_exist(const char* word, char** word_dict, const int word_dict_size) {
    for (int i = 0; i < word_dict_size; i++) {
        if (strcmp(word, word_dict[i]) == 0) {
            return true;
        }
    }
    return false;
}

/**
 * @brief This function is a recursive function that constructs all possible sentences from the given string.
 *
 * @param i The current index in the given string.
 * @param sentence The current sentence being constructed.
 * @param given_string The string from which sentences are to be constructed.
 * @param word_dict The dictionary of words.
 * @param word_dict_size The size of the dictionary.
 *
 * This function does not return a value, but modifies the ans array to hold all possible sentences.
 */
void solve(const int i, char* sentence, char* given_string, char** word_dict, const int word_dict_size) {
    if (i >= strlen(given_string)) {
        strcpy(ans[i], sentence);
        return;
    }

    for (int j = i + 1; j <= i + MAX_WORD_LENGTH && j <= strlen(given_string); j++) {
        char word[MAX_WORD_LENGTH + 1];
        strncpy(word, &given_string[i], j - i);
        word[j - i] = '\0';

        if (does_exist(word, word_dict, word_dict_size)) {
            char* old_sentence = strdup(sentence);
            if (strlen(sentence) == 0) {
                strcpy(sentence, word);
            } else {
                strcat(sentence, " ");
                strcat(sentence, word);
            }
            solve(j, sentence, given_string, word_dict, word_dict_size);
            strcpy(sentence, old_sentence);
            free(old_sentence);
        }
    }
}

/**
 * @brief This function returns all possible sentences that can be formed from the given string using the words in the dictionary.
 *
 * @param s The string from which sentences are to be constructed.
 * @param wordDict The dictionary of words.
 * @param wordDictSize The size of the dictionary.
 * @return A pointer to the array of all possible sentences.
 *
 * This function uses the solve function to construct all possible sentences.
 */
char (*wordBreak(char* s, char** wordDict, int wordDictSize))[MAX_SENTENCE_LENGTH] {
    char sentence[MAX_SENTENCE_LENGTH] = "";
    solve(0, sentence, s, wordDict, wordDictSize);
    return ans;
}
