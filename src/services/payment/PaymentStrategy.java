package services.payment;

public interface PaymentStrategy {
    // Método para processar o pagamento
    void processPayment(double amount);

}