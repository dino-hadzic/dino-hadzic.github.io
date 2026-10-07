#include <iostream>
constexpr int N = 16;
int is_working[N] = {0};  // whether a job has been assigned
int tm[N][N];             // time needed to complete a job
int cost_time_total_min;  // minimum total time for the n jobs

// i is the index of the person, count is the total cost of the jobs
void work(int i, int count, int n) {
  // If i exceeds the maximum number of jobs that can be assigned, the assignment is complete; if count
  // is smaller than the current cost_time_total_min, update cost_time_total_min
  if (i > n && count < cost_time_total_min) {
    cost_time_total_min = count;
    return;
  }
  // backtracking idea
  if (count < cost_time_total_min) {
    // j is the index of the job
    for (int j = 1; j <= n; j++) {
      // if the job is not assigned, is_working = 0
      if (is_working[j] == 0) {
        // assign the job, is_working = 1
        is_working[j] = 1;
        // hand the work over to person i + 1
        work(i + 1, count + tm[i][j], n);
        // after one round of iteration, return to the previous person and reassign this job
        // reset is_working[j] to 0
        is_working[j] = 0;
      }
    }
  }
}

using std::cin;
using std::cout;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> tm[i][j];
    }
    cost_time_total_min += tm[i][i];
  }
  work(1, 0, n);
  cout << cost_time_total_min << '\n';
  return 0;
}
