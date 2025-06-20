from abc import ABC, abstractmethod
import json


class ProcesadorPago(ABC):

    @abstractmethod
    def procesar_pago(self, json_data: str):
        pass


class PagoModerno(ProcesadorPago):
    def procesar_pago(self, json_data):
        try:
            json_dict = json.loads(json_data)
            print(f"[MODERNO] Procesando pago de {json_dict['amount']:.2f} {json_dict['currency']} para usuario {json_dict['user_id']}")
        except json.JSONDecodeError:
            print("No se pudo procesar el JSON enviado")
        except KeyError:
            print("El formato del JSON no se corresponde con el esperado")
        

class ServicioPagoLegacy(ProcesadorPago):

    def procesar_pago(self, json_data):
        try:
            json_dict = json.loads(json_data)
            print(f"[LEGACY] Procesando pago de {json_dict['monto_total']:.2f} {json_dict['moneda']} para usuario {json_dict['cliente']}")
        except json.JSONDecodeError:
            print("No se pudo procesar el JSON enviado")
        except KeyError:
            print("El formato del JSON no se corresponde con el esperado")


# Adaptador para la nueva interfaz de datos JSON
class PagoAdapter(ProcesadorPago):

    def __init__(self, servicio_pago_legacy: ServicioPagoLegacy):
        self.servicio_pago_legacy = servicio_pago_legacy

    def procesar_pago(self, json_data):
        # parse the current JSON (modern) to the old format
        print(f"[JSON moderno recibido] {json_data}")
        modern_json = json.loads(json_data)
        old_json = json.dumps({
            'monto_total': modern_json['amount'],
            'cliente': modern_json['user_id'],
            'moneda': modern_json['currency'],
        }) 
        print(f"[Adaptado a legacy] {old_json}")

        self.servicio_pago_legacy.procesar_pago(old_json)


if __name__ == '__main__':
    json_input = json.dumps({
        "user_id": "u123",
        "amount": 250.0,
        "currency": "USD",
    })
    
    print('\n--- Uso de clase moderna ---')
    moderno = PagoModerno()
    moderno.procesar_pago(json_input)

    print('\n--- Uso de clase legacy con adaptador ---')
    legacy = ServicioPagoLegacy()
    adaptador = PagoAdapter(legacy)
    adaptador.procesar_pago(json_input)
