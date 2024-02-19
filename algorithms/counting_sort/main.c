#include <stdio.h>

void countingSort(int *arr, int n) {
  int min = arr[0], max = arr[0];
  for (int i = 1; i < n; i++) {
    if (arr[i] < min) {
      min = arr[i];
    } else if (arr[i] > max) {
      max = arr[i];
    }
  }

  int count[max - min + 1];
  for (int i = 0; i < max - min + 1; i++) {
    count[i] = 0;
  }

  for (int i = 0; i < n; i++) {
    count[arr[i] - min]+=1;
  }
  // arr[i] - min -> номер элемента

  int i = 0, j = 0;
  while (i < max - min + 1) {
    while (count[i] > 0) {
      arr[j++] = i + min;
      count[i]--;
    }
    i++;
  }
}

int main() {
  int arr[] = {1, 2, 3, 4, 2, 1, 2, 2, 3, 4};
  int n = sizeof(arr) / sizeof(arr[0]);

  countingSort(arr, n);

  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }

  return 0;
}
