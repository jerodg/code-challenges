#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

char *kth_word_in_mth_sentence_of_nth_paragraph(char ****document, int k, int m,
                                                int n) {
    return *(*(*(document + --n) + --m) + --k);
}

char **kth_sentence_in_mth_paragraph(char ****document, int k, int m) {
    return *(*(document + --m) + --k);
}

char ***kth_paragraph(char ****document, int k) { return *(document + --k); }

char **split(char *s, char delim, int *count) {
    char **split_s = NULL;
    char *part = NULL;
    unsigned int idx_split_s = 0;
    unsigned int idx_part = 0;

    char c = '\0';
    for (unsigned int i = 0; *(s + i) != '\0'; i++) {
        c = *(s + i);

        if (c == delim && idx_part != 0) {
            // mark the end of part string
            part = realloc(part, sizeof(char *) * (idx_part + 1));
            *(part + idx_part) = '\0';

            // append part to split_s
            split_s = realloc(split_s, sizeof(char **) * (idx_split_s + 1));
            *(split_s + idx_split_s) = part;
            idx_split_s++;

            // clear part string values
            part = NULL;
            idx_part = 0;
        } else {
            // append character to part
            part = realloc(part, sizeof(char *) * (idx_part + 1));
            *(part + idx_part) = c;
            idx_part++;
        }
    }

    // append last part to split_s
    if (idx_part != 0) {
        // mark the end of part string
        part = realloc(part, sizeof(char *) * (idx_part + 1));
        *(part + idx_part) = '\0';

        // append part to split_s
        split_s = realloc(split_s, sizeof(char **) * (idx_split_s + 1));
        *(split_s + idx_split_s) = part;
        idx_split_s++;
    }

    *count = idx_split_s;

    return split_s;
}

char ****get_document(char *text) {
    int *len_paragraphs = calloc(1, sizeof(int));
    int *len_sentences = calloc(1, sizeof(int));
    int *len_words = calloc(1, sizeof(int));

    // split into paragraphs and store temporarily
    char **paragraphs_temp = split(text, '\n', len_paragraphs);

    // allocate space for paragraphs in document
    char ****document = malloc(*len_paragraphs * sizeof(char ***));

    char *s = NULL;
    for (int i = 0; i < *len_paragraphs; i++) {
        s = *(paragraphs_temp + i); // get current paragraph

        // split into sentences and store temporarily
        char **sentences_temp = split(s, '.', len_sentences);

        // allocate space for sentences in each paragraph
        *(document + i) = malloc(*len_sentences * sizeof(char **));

        for (int j = 0; j < *len_sentences; j++) {
            s = *(sentences_temp + j); // get crrent sentence

            // split into words and store temporarily
            char **words_temp = split(s, ' ', len_words);

            // allocate space for words in each sentence
            *(*(document + i) + j) = malloc(*len_words * sizeof(char *));

            for (int k = 0; k < *len_words; k++) {
                s = *(words_temp + k); // get current word
                *(*(*(document + i) + j) + k) = s;
            } // end of len_words loop
        }   // end of len_sentences loop
    }     // end of len_paragraphs loop

    // free stuff in heap
    free(len_words);
    free(len_sentences);
    free(len_paragraphs);

    return document;
}

char *get_input_text() {
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char *returnDoc = (char *) malloc((strlen(doc) + 1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

void print_word(char *word) { printf("%s", word); }

void print_sentence(char **sentence) {
    int word_count;
    scanf("%d", &word_count);
    for (int i = 0; i < word_count; i++) {
        printf("%s", sentence[i]);
        if (i != word_count - 1)
            printf(" ");
    }
}

void print_paragraph(char ***paragraph) {
    int sentence_count;
    scanf("%d", &sentence_count);
    for (int i = 0; i < sentence_count; i++) {
        print_sentence(*(paragraph + i));
        printf(".");
    }
}

int main() {
    char *text = get_input_text();
    char ****document = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3) {
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            char *word = kth_word_in_mth_sentence_of_nth_paragraph(document, k, m, n);
            print_word(word);
        } else if (type == 2) {
            int k, m;
            scanf("%d %d", &k, &m);
            char **sentence = kth_sentence_in_mth_paragraph(document, k, m);
            print_sentence(sentence);
        } else {
            int k;
            scanf("%d", &k);
            char ***paragraph = kth_paragraph(document, k);
            print_paragraph(paragraph);
        }
        printf("\n");
    }
}
