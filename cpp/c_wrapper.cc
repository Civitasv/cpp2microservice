#include "algorithm.h"

extern "C" {
int c_add(int a, int b) { return add(a, b); }
int c_call_method_in_A() { return A::TestAlgorithmInCXX(); }

// for Person class
void *create_person(const char *name, int age) {
  Person *person = new Person();
  person->name = name;
  person->age = age;

  return reinterpret_cast<void *>(person);
}

void delete_person(void *person) { delete reinterpret_cast<Person *>(person); }

const char *get_person_name(void *person) {
  return reinterpret_cast<Person *>(person)->name.c_str();
}

int get_person_age(void *person) {
  return reinterpret_cast<Person *>(person)->age;
}
}
