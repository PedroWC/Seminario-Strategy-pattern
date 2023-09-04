package services.payment.strategies;

import services.payment.PaymentStrategy;

public class PayPalStrategy implements PaymentStrategy {
    private final String email;

    public PayPalStrategy(String email) {
        this.email = email;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento com PayPal aqui
        
        System.out.println("Pagamento de $" + amount + " processado via PayPal para o email: " + email);
    }
}
