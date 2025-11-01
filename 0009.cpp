# include <bits/stdc++.h>
using namespace std;
bool isPalindrome(int x);
int main() {
    cout << isPalindrome(121) << endl;
}

bool isPalindrome(int x) {
    if (x < 0) return false;
    long temp = x, rev = 0;
    while (temp > 0) {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    if (x == rev) return true;
    return false;
}