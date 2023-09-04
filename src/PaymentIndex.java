import services.payment.PaymentProcessor;
import services.payment.PaymentStrategy;
import services.payment.strategies.*;

public class PaymentIndex {
    public static void main(String[] args) {
        // Exemplo de uso com diferentes estratégias

        // Estratégia PayPal
        PaymentStrategy paypalStrategy = new PayPalStrategy("seu_email@exemplo.com");
        PaymentProcessor paypalProcessor = new PaymentProcessor(paypalStrategy);
        paypalProcessor.processPayment(100.0);

        // Estratégia Stripe
        PaymentStrategy stripeStrategy = new StripeStrategy("chave_de_api_stripe");
        PaymentProcessor stripeProcessor = new PaymentProcessor(stripeStrategy);
        stripeProcessor.processPayment(75.0);

        // Estratégia de Transferência Bancária
        PaymentStrategy bankTransferStrategy = new BankTransferStrategy("banco", "conta");
        PaymentProcessor bankTransferProcessor = new PaymentProcessor(bankTransferStrategy);
        bankTransferProcessor.processPayment(200.0);

        // Estratégia de Cartão de Crédito
        PaymentStrategy creditCardStrategy = new CreditCardStrategy("1234-5678-9012-3456", "Titular do Cartão", "12/25", "123");
        PaymentProcessor creditCardProcessor = new PaymentProcessor(creditCardStrategy);
        creditCardProcessor.processPayment(50.0);

        // Estratégia de Vale-Presente
        PaymentStrategy giftCardStrategy = new GiftCardStrategy("GIFT-12345");
        PaymentProcessor giftCardProcessor = new PaymentProcessor(giftCardStrategy);
        giftCardProcessor.processPayment(30.0);

        // Estratégia de Carteira Digital
        PaymentStrategy digitalWalletStrategy = new DigitalWalletStrategy("Apple Pay");
        PaymentProcessor digitalWalletProcessor = new PaymentProcessor(digitalWalletStrategy);
        digitalWalletProcessor.processPayment(15.0);

        // Estratégia de Pagamento com Criptomoeda
        PaymentStrategy cryptoPaymentStrategy = new CryptoPaymentStrategy("Endereco_Carteira_Cripto", "Bitcoin");
        PaymentProcessor cryptoPaymentProcessor = new PaymentProcessor(cryptoPaymentStrategy);
        cryptoPaymentProcessor.processPayment(0.005);
    }
}
