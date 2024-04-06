#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRING_LENGTH 6

// fixme: The code is not working as expected. The output is not as expected.

struct package {
  char *id;
  int weight;
};

typedef struct package package;

struct post_office {
  int min_weight;
  int max_weight;
  package *packages;
  int packages_count;
};

typedef struct post_office post_office;

struct town {
  char *name;
  post_office *offices;
  int offices_count;
};

typedef struct town town;

void print_all_packages(town t) {
  printf("%s:\n", t.name);
  for (int i = 0; i < t.offices_count; i++) {
    printf("\t%d:\n", i);
    for (int j = 0; j < t.offices[i].packages_count; j++) {
      printf("\t\t%s\n", t.offices[i].packages[j].id);
    }
  }
}

void send_all_acceptable_packages(town *source, int source_office_index,
                                  town *target, int target_office_index) {
  post_office *source_office = &source->offices[source_office_index];
  post_office *target_office = &target->offices[target_office_index];
  int target_min_weight = target_office->min_weight;
  int target_max_weight = target_office->max_weight;
  int num_packages_to_send = 0;
  for (int i = 0; i < source_office->packages_count; i++) {
    if (source_office->packages[i].weight >= target_min_weight &&
        source_office->packages[i].weight <= target_max_weight) {
      num_packages_to_send++;
    }
  }
  package *new_packages = malloc(
      sizeof(package) * (target_office->packages_count + num_packages_to_send));
  for (int i = 0; i < target_office->packages_count; i++) {
    new_packages[i] = target_office->packages[i];
  }
  int new_package_index = target_office->packages_count;
  for (int i = 0; i < source_office->packages_count; i++) {
    if (source_office->packages[i].weight >= target_min_weight &&
        source_office->packages[i].weight <= target_max_weight) {
      new_packages[new_package_index] = source_office->packages[i];
      new_package_index++;
    }
  }
  free(target_office->packages);
  target_office->packages = new_packages;
  target_office->packages_count += num_packages_to_send;
  source_office->packages_count -= num_packages_to_send;
  package *new_source_packages =
      malloc(sizeof(package) * (source_office->packages_count));
  int new_source_package_index = 0;
  for (int i = 0; i < source_office->packages_count + num_packages_to_send;
       i++) {
    if (source_office->packages[i].weight < target_min_weight ||
        source_office->packages[i].weight > target_max_weight) {
      new_source_packages[new_source_package_index] =
          source_office->packages[i];
      new_source_package_index++;
    }
  }
  free(source_office->packages);
  source_office->packages = new_source_packages;
  free(new_packages);
  free(new_source_packages);
}

int number_of_packages(town t) {
  int count = 0;
  for (int i = 0; i < t.offices_count; i++) {
    count += t.offices[i].packages_count;
  }
  return count;
}

int number_of_packages_in_office(post_office p) { return p.packages_count; }

town town_with_most_packages(town *towns, int towns_count) {
  town most_packages_town = towns[0];
  for (int i = 1; i < towns_count; i++) {
    if (number_of_packages(towns[i]) > number_of_packages(most_packages_town)) {
      most_packages_town = towns[i];
    }
  }
  return most_packages_town;
}

town *find_town(town *towns, int towns_count, char *name) {
  for (int i = 0; i < towns_count; i++) {
    if (strcmp(towns[i].name, name) == 0) {
      return &towns[i];
    }
  }
  return NULL;
}

int main() {
  int towns_count;
  scanf("%d", &towns_count);
  town *towns = malloc(sizeof(town) * towns_count);
  for (int i = 0; i < towns_count; i++) {
    towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
    scanf("%s", towns[i].name);
    scanf("%d", &towns[i].offices_count);
    towns[i].offices = malloc(sizeof(post_office) * towns[i].offices_count);
    for (int j = 0; j < towns[i].offices_count; j++) {
      scanf("%d%d%d", &towns[i].offices[j].packages_count,
            &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
      towns[i].offices[j].packages =
          malloc(sizeof(package) * towns[i].offices[j].packages_count);
      for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
        towns[i].offices[j].packages[k].id =
            malloc(sizeof(char) * MAX_STRING_LENGTH);
        scanf("%s", towns[i].offices[j].packages[k].id);
        scanf("%d", &towns[i].offices[j].packages[k].weight);
      }
    }
  }
  int queries;
  scanf("%d", &queries);
  char town_name[MAX_STRING_LENGTH];
  while (queries--) {
    int type;
    scanf("%d", &type);
    switch (type) {
    case 1:
      scanf("%s", town_name);
      town *t = find_town(towns, towns_count, town_name);
      print_all_packages(*t);
      break;
    case 2:
      scanf("%s", town_name);
      town *source = find_town(towns, towns_count, town_name);
      int source_index;
      scanf("%d", &source_index);
      scanf("%s", town_name);
      town *target = find_town(towns, towns_count, town_name);
      int target_index;
      scanf("%d", &target_index);
      send_all_acceptable_packages(source, source_index, target, target_index);
      break;
    case 3:
      printf("Town with the most number of packages is %s\n",
             town_with_most_packages(towns, towns_count).name);
      break;
    }
  }
  return 0;
}
