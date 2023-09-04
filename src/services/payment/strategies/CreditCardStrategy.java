package services.payment.strategies;

import services.payment.PaymentStrategy;

public class CreditCardStrategy implements PaymentStrategy {
    private final String cardNumber;
    private final String cardHolderName;
    private final String expirationDate;
    private final String cvv;

    public CreditCardStrategy(String cardNumber, String cardHolderName, String expirationDate, String cvv) {
        this.cardNumber = cardNumber;
        this.cardHolderName = cardHolderName;
        this.expirationDate = expirationDate;
        this.cvv = cvv;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento com cartão de crédito aqui

        System.out.println("Pagamento de $" + amount + " processado com cartão de crédito: " + cardNumber
                + ", Nome do titular: " + cardHolderName + ", Data de validade: " + expirationDate + ", CVV: " + cvv);
    }
}
