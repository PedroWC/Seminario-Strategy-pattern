package services.payment.strategies;

import services.payment.PaymentStrategy;

public class DigitalWalletStrategy implements PaymentStrategy {
    private final String walletType;

    public DigitalWalletStrategy(String walletType) {
        this.walletType = walletType;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento com carteira digital aqui
        
        System.out.println("Pagamento de $" + amount + " processado com carteira digital: " + walletType);
    }
}
