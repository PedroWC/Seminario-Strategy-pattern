package services.payment.strategies;

import services.payment.PaymentStrategy;

public class CryptoPaymentStrategy implements PaymentStrategy {
    private final String cryptoWalletAddress;
    private final String cryptoCurrency;

    public CryptoPaymentStrategy(String cryptoWalletAddress, String cryptoCurrency) {
        this.cryptoWalletAddress = cryptoWalletAddress;
        this.cryptoCurrency = cryptoCurrency;
    }

    @Override
    public void processPayment(double amount) {

        // Implementação da lógica de pagamento com criptomoeda aqui
        
        System.out.println("Pagamento de $" + amount + " processado com criptomoeda: " + cryptoCurrency +
                ", para o endereço da carteira: " + cryptoWalletAddress);
    }
}
