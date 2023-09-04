package services.payment.strategies;

import services.payment.PaymentStrategy;

public class StripeStrategy implements PaymentStrategy {
    private final String apiKey;

    public StripeStrategy(String apiKey) {
        this.apiKey = apiKey;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento com Stripe aqui
        
        System.out.println("Pagamento de $" + amount + " processado via Stripe com API Key: " + apiKey);
    }
}
