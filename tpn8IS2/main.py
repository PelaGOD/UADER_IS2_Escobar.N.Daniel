from payment_processor import PaymentSystem

def main():
    system = PaymentSystem()

    for i in range(1, 6):
        try:
            pago = system.request_payment(i, 500)
            print(f"✔️ Pago procesado: {pago}")
        except Exception as e:
            print(f"❌ Error al procesar pedido #{i}: {e}")

    print("\n📋 Listado de pagos realizados:")
    for pago in system.list_payments():
        print(pago)


if __name__ == "__main__":
    main()
