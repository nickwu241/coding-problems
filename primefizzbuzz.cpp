// g++ primefizzbuzz.cpp -o primefizzbuzz
#include <iostream>

#define START_NUM 1
#define MAX_NUM 100

// returns true if the number is prime, false otherwise
bool prime(int n)
{
  if (n <= 2 || n % 2 == 0)
    return false;

  for (int i=3; i < n; i += 2)
  {
    if (n % i == 0) 
      return false;
  }

  return true;
}

int main()
{
  bool primebuzz = false;
  for (int n=START_NUM; n <= MAX_NUM; n++)
  {
    primebuzz = false;

    if (prime(n))
    {
      std::cout << "Prime";
      primebuzz = true;
    }

    if (n % 3 == 0)
    {
      std::cout << "Fizz";
      primebuzz = true;
    }

    if (n % 5 == 0)
    {
      std::cout << "Buzz";
      primebuzz = true;
    }

    if (!primebuzz)
    {
      std::cout << n;
    }

    std::cout << '\n';
  }

  return 0;
}
