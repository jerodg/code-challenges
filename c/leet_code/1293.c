#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// todo: fix heap-buffer-overflow

typedef struct {
    int x;
    int y;
} Point;

typedef struct QueueNode {
    Point point;
    struct QueueNode* next;
} QueueNode;

typedef struct {
    QueueNode* front;
    QueueNode* rear;
} Queue;

QueueNode* newQueueNode(const int x, const int y) {
    QueueNode* temp = (QueueNode*)malloc(sizeof(QueueNode));
    temp->point.x = x;
    temp->point.y = y;
    temp->next = NULL;
    return temp;
}

Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

void enqueue(Queue* q, const int x, const int y) {
    QueueNode* temp = newQueueNode(x, y);
    if (q->rear == NULL) {
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
}

Point dequeue(Queue* q) {
    if (q->front == NULL) {
        Point p = {-1, -1};
        return p;
    }
    QueueNode* temp = q->front;
    Point item = temp->point;
    q->front = temp->next;
    if (q->front == NULL)
        q->rear = NULL;
    free(temp);
    return item;
}

bool isEmpty(Queue* q) {
    return (q->rear == NULL);
}

int shortestPath(int** grid, int m, int n, int k) {
    bool** visited = (bool**)malloc(m * sizeof(bool*));
    for (int i = 0; i < m; i++) {
        visited[i] = (bool*)malloc(n * sizeof(bool));
        memset(visited[i], false, n * sizeof(bool));
    }
    int** obstacles = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        obstacles[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            obstacles[i][j] = INT_MAX;
        }
    }
    Queue* q = createQueue();
    int step = 0;
    enqueue(q, 0, 0);
    obstacles[0][0] = 0;
    int breadth = 1;

    while (!isEmpty(q)) {
        Point p = dequeue(q);
        int x = p.x;
        int y = p.y;
        if (x == m - 1 && y == n - 1) {
            // Free the memory allocated for the queue
            while (!isEmpty(q)) {
                dequeue(q);
            }
            free(q);

            // Free the memory allocated for the 2D arrays
            for (int i = 0; i < m; i++) {
                free(visited[i]);
                free(obstacles[i]);
            }
            free(visited);
            free(obstacles);

            return step;
        }
        int dx[] = {1, -1, 0, 0};
        int dy[] = {0, 0, 1, -1};
        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (new_x < 0 || new_x >= m || new_y < 0 || new_y >= n)
                continue;
            int new_obs = obstacles[x][y] + grid[new_x][new_y];
            if (new_obs >= obstacles[new_x][new_y])
                continue;
            if (new_obs <= k) {
                enqueue(q, new_x, new_y);
                obstacles[new_x][new_y] = new_obs;
            }
        }
        visited[x][y] = true;
        breadth--;
        if (breadth == 0) {
            step++;
            breadth = q->rear == NULL ? 0 : 1;
        }
    }

    // Free the memory allocated for the queue
    while (!isEmpty(q)) {
        dequeue(q);
    }
    free(q);

    // Free the memory allocated for the 2D arrays
    for (int i = 0; i < m; i++) {
        free(visited[i]);
        free(obstacles[i]);
    }
    free(visited);
    free(obstacles);

    return -1;
}
