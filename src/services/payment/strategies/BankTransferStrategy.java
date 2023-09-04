package services.payment.strategies;

import services.payment.PaymentStrategy;

public class BankTransferStrategy implements PaymentStrategy {
    private final String bankName;
    private final String accountNumber;

    public BankTransferStrategy(String bankName, String accountNumber) {
        this.bankName = bankName;
        this.accountNumber = accountNumber;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento por transferência bancária aqui

        System.out.println("Pagamento de $" + amount + " via transferência bancária para o banco: " + bankName
                + ", conta: " + accountNumber);
    }
}
