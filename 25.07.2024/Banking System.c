#include <stdio.h>
#include <string.h>
struct BankAccount {
    char name[50];
    int accountNumber;
    double balance;
};
struct BankAccount createAccount(char name[], int accountNumber, double initialBalance) {
    struct BankAccount account;
    strcpy(account.name, name);
    account.accountNumber = accountNumber;
    account.balance = initialBalance;
    return account;
}
void withdraw(struct BankAccount *account, double amount) {
    if (account->balance >= amount) {
        account->balance -= amount;
        printf("%s has withdrawn %.2lf\n", account->name, amount);
        printf("Balance after withdrawal: %.2lf\n", account->balance);
    } else {
        printf("%s cannot withdraw %.2lf\n", account->name, amount);
        printf("Your balance is: %.2lf\n", account->balance);
    }
}
void deposit(struct BankAccount *account, double amount) {
    account->balance += amount;
    printf("%s has deposited %.2lf\n", account->name, amount);
    printf("Balance after deposit: %.2lf\n", account->balance);
}
void transfer(struct BankAccount *from, struct BankAccount *to, double amount) {
    if (from->balance >= amount) {
        from->balance -= amount;
        to->balance += amount;
        printf("Transferred %.2lf from %s to %s\n", amount, from->name, to->name);
    } else {
        printf("%s does not have sufficient balance for the transfer\n", from->name);
    }
}
int main() {
    struct BankAccount account1 = createAccount("Alice", 1001, 500.0);
    struct BankAccount account2 = createAccount("Bob", 1002, 300.0);
    withdraw(&account1, 200.0);
    deposit(&account2, 100.0);
    transfer(&account1, &account2, 50.0);
    return 0;
}
