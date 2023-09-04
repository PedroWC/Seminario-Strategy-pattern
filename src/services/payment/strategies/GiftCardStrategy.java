package services.payment.strategies;

import services.payment.PaymentStrategy;

public class GiftCardStrategy implements PaymentStrategy {
    private final String giftCardCode;

    public GiftCardStrategy(String giftCardCode) {
        this.giftCardCode = giftCardCode;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento via Gift Card aqui

        System.out.println("Pagamento de $" + amount + " processado com código de vale-presente: " + giftCardCode);
    }
}
