class Bank {
    private int totalBalance = 100; 
    void withdraw(String name, int withdrawalAmount) {
        if (totalBalance >= withdrawalAmount) {
            System.out.println(name + " has withdrawn " + withdrawalAmount);
            totalBalance -= withdrawalAmount;
            System.out.println("Balance after withdrawal: " + totalBalance);
        } else {
            System.out.println(name + " cannot withdraw " + withdrawalAmount);
            System.out.println("Your balance is: " + totalBalance);
        }
    }
    void deposit(String name, int depositAmount) {
        System.out.println(name + " has deposited " + depositAmount);
        totalBalance += depositAmount;
        System.out.println("Balance after deposit: " + totalBalance);
    }
}
public class BankingSystemExample {
    public static void main(String[] args) {
        Bank bank = new Bank();
        bank.withdraw("Arnab", 20);
        bank.withdraw("Monodwip", 40);
        bank.deposit("Mukta", 35);
        bank.withdraw("Rinkel", 80);
        bank.withdraw("Shubham", 40);
    }
}
